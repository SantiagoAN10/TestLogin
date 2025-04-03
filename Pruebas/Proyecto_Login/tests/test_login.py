import pytest
from screenplay import Actor, LoginData, DoLogin

@pytest.mark.parametrize("test_case, expected", [
    ("login exitoso", True),
    ("login fallido", False)
])
def test_login(test_case, expected):      
    """Prueba el login exitoso y fallido."""
    user = Actor("TestUser")
    login_data = LoginData.from_json("data/login_data.json", test_case)
    response = user.attempts_to(DoLogin, login_data)

    print(f"\nRespuesta de la API para {test_case}: {response}")  # Debugging

    if expected:  # Login exitoso
        assert "result" in response, f"Fallo en {test_case}: {response}"
        assert response["result"].get("code") == 90700, f"Fallo en {test_case}: {response}"
    else:  # Login fallido
        assert "error" in response, f"Fallo en {test_case}: {response}"
        assert response["error"].get("code") == 90683, f"Fallo en {test_case}: {response}"
