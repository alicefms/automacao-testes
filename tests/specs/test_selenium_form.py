import pytest
from guara.application import Application

from tests.transactions.app_transactions import OpenSeleniumForm, SubmitSeleniumForm


@pytest.mark.integration
def test_envio_de_formulario_selenium(app: Application) -> None:
    app.at(OpenSeleniumForm)
    app.at(SubmitSeleniumForm, text="foo")

    assert "selenium.dev" in app.result