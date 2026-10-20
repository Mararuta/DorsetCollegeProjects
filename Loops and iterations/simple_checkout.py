PRICES_IN_CENTS = {
    "apple": 60,
    "orange": 25
}

def calculate_total_total(items: list[str]) -> int:

    total = 0
    for item in items:
        normalized_item = item.strip().lower()
        if normalized_item in PRICES_IN_CENTS:
            total += PRICES_IN_CENTS[normalized_item]
        else:
            print(f"Unknown item ignored: {item}")
    return total

def format_euros(cents: int) -> str:
    euros, remaining_cents = divmod(cents, 100)
    return f"€{euros}.{remaining_cents:02d}"


def run() -> None:
    items = ["Apple", "Apple", "Orange", "Apple"]
    total_cost_in_cents = calculate_total_total(items)

    print ("Simple chekcout system")
    print (f"Scanned items:  {', '.join(items)}")
    print (f"Total cost:  {format_euros(total_cost_in_cents)}")
    

if __name__ == "__main__":
    run()