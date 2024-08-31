from datetime import datetime
import pandas as pd
from .models import get_store_status_collection, get_business_hours_collection, get_store_timezone_collection
import json
import os

# Define a path to save the generated report
REPORTS_DIR = 'app/reports'
if not os.path.exists(REPORTS_DIR):
    os.makedirs(REPORTS_DIR)

def generate_report(report_id):
    # Fetch data from MongoDB
    store_status_collection = get_store_status_collection()
    business_hours_collection = get_business_hours_collection()
    store_timezone_collection = get_store_timezone_collection()

    store_status_df = pd.DataFrame(list(store_status_collection.find()))
    business_hours_df = pd.DataFrame(list(business_hours_collection.find()))
    store_timezone_df = pd.DataFrame(list(store_timezone_collection.find()))

    # Handles 'timestamp_utc' conversion with timezone handling
    store_status_df['timestamp_utc'] = pd.to_datetime(store_status_df['timestamp_utc'], errors='coerce')
    store_status_df['timestamp_utc'] = store_status_df['timestamp_utc'].dt.tz_localize(None)  # Remove timezone info if needed

    # Perform calculations or aggregations
    report_data = store_status_df.groupby('store_id').agg({
        'status': 'count',  # Count status occurrences
        'timestamp_utc': lambda x: (datetime.utcnow() - x.max()).total_seconds()  # Time since last status
    }).reset_index()
    report_data.columns = ['store_id', 'status_count', 'time_since_last_status']

    # Generate report as CSV
    report_file_path = os.path.join(REPORTS_DIR, f'{report_id}.csv')
    report_data.to_csv(report_file_path, index=False)

    # Save report status
    with open(os.path.join(REPORTS_DIR, f'{report_id}.json'), 'w') as f:
        json.dump({
            'status': 'Complete',
            'file': report_file_path
        }, f)

def check_report_status(report_id):
    # Check if the report file and status exist
    report_status_file = os.path.join(REPORTS_DIR, f'{report_id}.json')
    if os.path.exists(report_status_file):
        with open(report_status_file, 'r') as f:
            status_data = json.load(f)
            if status_data['status'] == 'Complete':
                return status_data['status'], status_data['file']
    return 'Running', None
