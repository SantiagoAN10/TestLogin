import requests

class DoLogin:
    """Ejecuta la acción de login en el servicio."""
    

    URL = "https://castlemockdemo.subocol.com/castlemock/mock/rest/project/NpJ1A9/application/eu72DD/login"

    @staticmethod
    def perform(login_data):
        response = requests.post(DoLogin.URL, json=login_data)
        return response.json()
    
