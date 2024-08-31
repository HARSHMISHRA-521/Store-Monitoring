import pandas as pd
from .models import get_store_status_collection, get_business_hours_collection, get_store_timezone_collection

def load_csv_data():
    store_status_df = pd.read_csv('app/data/store_status.csv')
    business_hours_df = pd.read_csv('app/data/business_hours.csv')
    store_timezone_df = pd.read_csv('app/data/store_timezone.csv')

    store_status_collection = get_store_status_collection()
    business_hours_collection = get_business_hours_collection()
    store_timezone_collection = get_store_timezone_collection()

    # Populate StoreStatus collection
    store_status_collection.insert_many(store_status_df.to_dict('records'))

    # Populate BusinessHours collection
    business_hours_collection.insert_many(business_hours_df.to_dict('records'))

    # Populate StoreTimezone collection
    store_timezone_collection.insert_many(store_timezone_df.to_dict('records'))
