import pandas as pd
from datetime import datetime, timedelta
from app import get_asteroids_by_date

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')

def preprocess_data(data):
    if 'near_earth_objects' not in data:
        raise KeyError("Key 'near_earth_objects' not found in the data")
    
    neos = data['near_earth_objects']
    
    records = []
    for date, objects in neos.items():
        for obj in objects:
            record = {
                'id': obj.get('id'),
                'name': obj.get('name'),
                'is_potentially_hazardous_asteroid': obj.get('is_potentially_hazardous_asteroid'),
                'absolute_magnitude_h': obj.get('absolute_magnitude_h'),
                'diameter_min_km': obj.get('estimated_diameter', {}).get('kilometers', {}).get('estimated_diameter_min'),
                'diameter_max_km': obj.get('estimated_diameter', {}).get('kilometers', {}).get('estimated_diameter_max'),
                'velocity_km_s': obj.get('close_approach_data', [{}])[0].get('relative_velocity', {}).get('kilometers_per_second'),
                'miss_distance_km': obj.get('close_approach_data', [{}])[0].get('miss_distance', {}).get('kilometers')
            }
            records.append(record)
    
    df = pd.DataFrame(records)
    
    df['diameter_min_km'] = pd.to_numeric(df['diameter_min_km'], errors='coerce')
    df['diameter_max_km'] = pd.to_numeric(df['diameter_max_km'], errors='coerce')
    df['velocity_km_s'] = pd.to_numeric(df['velocity_km_s'], errors='coerce')
    df['miss_distance_km'] = pd.to_numeric(df['miss_distance_km'], errors='coerce')

    return df

def get_data_for_range(start_date, end_date, api_key):
    # Initialize list to hold data
    all_data = []
    
    # Convert start_date and end_date to datetime objects
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    
    # Loop through the date range in 7-day chunks
    while start <= end:
        chunk_end = start + timedelta(days=6)
        if chunk_end > end:
            chunk_end = end
        
        print(f"Fetching data from {start.strftime('%Y-%m-%d')} to {chunk_end.strftime('%Y-%m-%d')}")
        
        # Fetch data for the current chunk
        data = get_asteroids_by_date(start.strftime('%Y-%m-%d'), chunk_end.strftime('%Y-%m-%d'), api_key)
        
        if data:
            all_data.append(data)
        
        # Move to the next chunk
        start = chunk_end + timedelta(days=1)
    
    # Combine all data
    combined_data = {}
    for data in all_data:
        if 'near_earth_objects' in data:
            for date, objects in data['near_earth_objects'].items():
                if date not in combined_data:
                    combined_data[date] = []
                combined_data[date].extend(objects)
    
    # Preprocess combined data
    df = preprocess_data({'near_earth_objects': combined_data})
    return df

# Assuming you have a function that retrieves data
# start_date = '2015-01-01'
# end_date = '2024-08-30'

# df = get_data_for_range(start_date, end_date, api_key)
# df.to_csv('data.csv', index=False)