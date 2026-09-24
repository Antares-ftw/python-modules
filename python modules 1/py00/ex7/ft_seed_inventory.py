def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:

    if unit == "packets":
        print(f"{seed_type} seeds: {quantity}  packets available")
    elif unit == "grams":
        print(f"{seed_type} seeds: {quantity}  grams total")
    elif unit == "area":
        print(f"{seed_type} seeds: covers {quantity} quare meters")
    else:
        ("Unknown unit type")
