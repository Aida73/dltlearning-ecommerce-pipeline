from faker import Faker
import random

fake = Faker()


def generate_orders(n=100):
    """Génère n commandes fictives avec données imbriquées."""
    products = ["laptop", "phone", "tablet", "headphones", "keyboard"]
    statuses = ["completed", "pending", "cancelled"]

    orders = []
    for i in range(n):
        quantity = random.randint(1, 5)
        unit_price = round(random.uniform(50, 1500), 2)

        orders.append({
            "order_id": f"ORD-{i+1:04d}",
            "customer_id": f"CUST-{random.randint(1, 30):03d}",
            "product": random.choice(products),
            "quantity": quantity,
            "unit_price": unit_price,
            "total_amount": round(quantity * unit_price, 2),
            "country": fake.country(),
            "status": random.choice(statuses),
            "created_at": fake.date_time_this_year().isoformat(),
            "shipping": {
                "address": fake.street_address(),
                "city": fake.city(),
                "zip": fake.postcode()
            }
        })
    return orders