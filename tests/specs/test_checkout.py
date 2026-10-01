import pytest
from guara.application import Application

from tests.settings import STANDARD_PASSWORD, STANDARD_USERNAME
from tests.transactions.app_transactions import (
    AddProductToCart,
    FinishPurchase,
    OpenCart,
    OpenSauceDemo,
    StartCheckout,
    SubmitLogin,
    SubmitShippingInformation,
)


@pytest.mark.smoke
def test_compra_produto_com_sucesso(app: Application) -> None:
    app.at(OpenSauceDemo)
    app.at(
        SubmitLogin,
        username=STANDARD_USERNAME,
        password=STANDARD_PASSWORD,
    )
    assert "inventory.html" in app.result

    app.at(AddProductToCart, product_id="sauce-labs-backpack")
    app.at(OpenCart)
    assert "cart.html" in app.result

    app.at(StartCheckout)
    assert "checkout-step-one.html" in app.result

    app.at(
        SubmitShippingInformation,
        first_name="Douglas",
        last_name="Teste",
        postal_code="12345",
    )
    assert "checkout-step-two.html" in app.result

    app.at(FinishPurchase)
    assert "Thank you" in app.result