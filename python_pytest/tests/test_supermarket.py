
import pytest

from model_objects import Product, SpecialOfferType, ProductUnit
from shopping_cart import ShoppingCart
from teller import Teller
from tests.fake_catalog import FakeCatalog


def checkout_with_offer(offer_type, quantity, argument, unit_price=10.0):
    catalog = FakeCatalog()
    product = Product("test_product", ProductUnit.EACH)
    catalog.add_product(product, unit_price)

    teller = Teller(catalog)
    teller.add_special_offer(offer_type, product, argument)

    cart = ShoppingCart()
    cart.add_item_quantity(product, quantity)

    return teller.checks_out_articles_from(cart)


def test_product_without_matching_offer():
    catalog = FakeCatalog()
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    catalog.add_product(toothbrush, 0.99)
    apples = Product("apples", ProductUnit.KILO)
    catalog.add_product(apples, 1.99)

    teller = Teller(catalog)
    teller.add_special_offer(
        SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0
    )

    cart = ShoppingCart()
    cart.add_item_quantity(apples, 2.5)

    receipt = teller.checks_out_articles_from(cart)

    assert 4.975 == pytest.approx(receipt.total_price(), 0.01)
    assert [] == receipt.discounts
    assert len(receipt.items) == 1
    assert apples == receipt.items[0].product
    assert 1.99 == receipt.items[0].price
    assert 2.5 == receipt.items[0].quantity


def test_ten_percent_discount():
    receipt = checkout_with_offer(
        SpecialOfferType.TEN_PERCENT_DISCOUNT, 2, 10.0
    )

    assert 18.0 == pytest.approx(receipt.total_price())
    assert len(receipt.discounts) == 1
    assert -2.0 == pytest.approx(receipt.discounts[0].discount_amount)


def test_three_for_two_offer():
    receipt = checkout_with_offer(
        SpecialOfferType.THREE_FOR_TWO, 3, 0
    )

    assert 20.0 == pytest.approx(receipt.total_price())
    assert len(receipt.discounts) == 1
    assert -10.0 == pytest.approx(receipt.discounts[0].discount_amount)


def test_two_for_amount_offer():
    receipt = checkout_with_offer(
        SpecialOfferType.TWO_FOR_AMOUNT, 2, 15.0
    )

    assert 15.0 == pytest.approx(receipt.total_price())
    assert len(receipt.discounts) == 1
    assert -5.0 == pytest.approx(receipt.discounts[0].discount_amount)


def test_five_for_amount_offer():
    receipt = checkout_with_offer(
        SpecialOfferType.FIVE_FOR_AMOUNT, 5, 40.0
    )

    assert 40.0 == pytest.approx(receipt.total_price())
    assert len(receipt.discounts) == 1
    assert -10.0 == pytest.approx(receipt.discounts[0].discount_amount)