from checkout_models import Checkout, Product, SimplePriceCalculator
from simple_checkout import format_euros

def run () -> None:
    print("Object-Oriented checkout system")

    apple = Product("Apple", "Fruit", 60)
    orange = Product("Orange", "Fruit", 25)

    price_calculator = SimplePriceCalculator()
    checkout = Checkout(price_calculator)

    items_to_scan = [apple, apple, orange, apple]

    for item in items_to_scan:
        checkout.scan(item)

    total_in_cents = checkout.get_total_price_in_cents()
    names = ", ".join(str(item) for item in checkout.get_scanned_items())

    print(f"Scanned items : {names}")
    print(f"Total cost: {format_euros(total_in_cents)}")

    