from guara.transaction import AbstractTransaction

from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage
from tests.pages.confirmation_page import ConfirmationPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.login_page import LoginPage
from tests.pages.selenium_form_page import SeleniumFormPage
from tests.settings import BASE_URL, SELENIUM_FORM_URL


class OpenSauceDemo(AbstractTransaction):
    def do(self) -> str:
        return LoginPage(self._driver).open(BASE_URL)


class SubmitLogin(AbstractTransaction):
    def do(self, username: str, password: str) -> str:
        return LoginPage(self._driver).login(username, password)


class AddProductToCart(AbstractTransaction):
    def do(self, product_id: str) -> str:
        InventoryPage(self._driver).add_product(product_id)
        return product_id


class OpenCart(AbstractTransaction):
    def do(self) -> str:
        return InventoryPage(self._driver).open_cart()


class StartCheckout(AbstractTransaction):
    def do(self) -> str:
        return CartPage(self._driver).start_checkout()


class SubmitShippingInformation(AbstractTransaction):
    def do(self, first_name: str, last_name: str, postal_code: str) -> str:
        return CheckoutPage(self._driver).submit_shipping_information(
            first_name, last_name, postal_code
        )


class FinishPurchase(AbstractTransaction):
    def do(self) -> str:
        CheckoutPage(self._driver).finish_purchase()
        return ConfirmationPage(self._driver).message()


class OpenSeleniumForm(AbstractTransaction):
    def do(self) -> str:
        return SeleniumFormPage(self._driver).open(SELENIUM_FORM_URL)


class SubmitSeleniumForm(AbstractTransaction):
    def do(self, text: str) -> str:
        return SeleniumFormPage(self._driver).submit_text(text)