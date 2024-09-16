import requests
import random
import time
from datetime import datetime

def generate_measurement_data():
    return {
        'heart_rate': random.randint(60, 100),
        'spo2': round(random.uniform(95.0, 100.0), 1),
        'timestamp': datetime.now().isoformat()
    }

def send_data_to_server(patient_id, url):
    while True:
        data = generate_measurement_data()
        try:
            response = requests.post(f"{url}/patient/{patient_id}/measurements/", json=data)
            print(f"Data sent: {data} - Status: {response.status_code}")
        except requests.RequestException as e:
            print(f"Failed to send data: {e}")
        
        time.sleep(5)  # Adjust the interval as needed

if __name__ == "__main__":
    server_url = 'http://localhost:8000'  # Replace with your Django server URL
    patient_id = 1  # Replace with your patient ID
    send_data_to_server(patient_id, server_url)
