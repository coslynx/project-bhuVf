# third_party_integration.py (Python)

# Import necessary packages
import requests

class ThirdPartyIntegration:
    def __init__(self, api_key):
        self.api_key = api_key

    def connect_to_service(self, service_url):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        response = requests.get(service_url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return None

    def send_data_to_service(self, service_url, data):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        response = requests.post(service_url, headers=headers, json=data)

        if response.status_code == 200:
            return True
        else:
            return False

# End of third_party_integration.py