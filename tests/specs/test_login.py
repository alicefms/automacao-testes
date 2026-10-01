import pytest
from guara.application import Application

from tests.settings import STANDARD_PASSWORD, STANDARD_USERNAME
from tests.transactions.app_transactions import OpenSauceDemo, SubmitLogin


@pytest.mark.smoke
def test_login_com_sucesso(app: Application) -> None:
    app.at(OpenSauceDemo)
    app.at(
        SubmitLogin,
        username=STANDARD_USERNAME,
        password=STANDARD_PASSWORD,
    )

    assert "inventory.html" in app.result


@pytest.mark.smoke
@pytest.mark.parametrize(
    ("username", "password", "expected_error"),
    [
        (
            "usuario_invalido",
            "senha_invalida",
            "Username and password do not match",
        ),
        (
            "locked_out_user",
            STANDARD_PASSWORD,
            "Sorry, this user has been locked out",
        ),
    ],
)
def test_login_com_credenciais_rejeitadas(
    app: Application,
    username: str,
    password: str,
    expected_error: str,
) -> None:
    app.at(OpenSauceDemo)
    app.at(SubmitLogin, username=username, password=password)

    assert expected_error in app.result