# Store Monitoring

## Overview

Store Monitoring is a Python-based application designed to manage and monitor the status of various stores. The application provides endpoints to trigger the generation of reports and to retrieve the status of those reports. It utilizes Flask for web development and includes functionalities for handling store data and generating status reports.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Author](#author)
- [Video Demonstration](#video-demonstration)

## Project Structure

The project follows the directory structure outlined below:

```
store-monitoring/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── services.py
│   ├── utils.py
│   ├── config.py
│   └── data/
│       ├── store_status.csv
│       ├── business_hours.csv
│       └── store_timezone.csv
├── .gitignore
├── README.md
├── requirements.txt
└── run.py


```

## Setup and Installation

1. **Clone the Repository**

   ```
   git clone <repository_url>
   cd store-monitoring
   ```
   
2.**Create and Activate a Virtual Environment**
```doctest
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```

3.**Install the Required Packages**
```
pip install -r requirements.txt
 
```

4.**Run the Application**
```
python run.py

```
The application will start and be accessible at http://127.0.0.1:5000.

## API Endpoints
**POST /trigger_report**

- Triggers the generation of a new report and returns a unique report_id.

**GET /get_report**

- Retrieves the status of a report using the provided report_id. Returns either "Running" or "Complete" with the 
associated data.

## Author

This project is maintained by **Harsh Mishra**. You can reach out to me via [LinkedIn](http://www.linkedin.com/in/mishraharsh-hmc) for any queries or feedback.

## Video Demonstration

[Video Demonstration of the Project](https://video.drift.com/v/abH8HvnZOTQSZK8aUhBHZeLUuujIUBu4OxTn441OFtO8/)

---


