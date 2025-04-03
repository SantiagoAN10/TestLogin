import json

class LoginData:
    """Carga los datos de login desde un archivo JSON."""

    @staticmethod
    def from_json(file_path, test_case):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data.get(test_case)
