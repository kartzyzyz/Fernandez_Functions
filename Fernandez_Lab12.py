def showmenu(menu):
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: P{price:.2f}")

def order(menu):
    while True:
        order = input("Enter your order here: ").strip()
        if order in menu:
            return order, menu[order]
        else:
            print("Please choose an item available from the menu.")

def payment_method(total):
    while True:
        try:
            payment = float(input(f"Total cost is P{total:.2f}. Please enter Payment: P"))
            if payment >= total:
                return payment
            else:
                print("Payment is not enough. Provide exact or greater amount.")
        except ValueError:
            print("Invalid input.")

def calculate_change(payment, total):
    return payment - total

def main():
    menu = {
        "Siomai Rice": 50.00,
        "Chicken Pastil": 40.00,
        "Gulaman": 15.00,
        "Pares": 100.00,
        "Lomi": 80.00,
    }

    showmenu(menu)
    order_item, order_price = order(menu)
    total = order_price

    payment = payment_method(total)
    change = calculate_change(payment, total)

    print(f"\nYou ordered: {order_item}")
    print(f"Total cost: P{total:.2f}")
    print(f"Amount received: P{payment:.2f}")
    print(f"Change: P{change:.2f}")

if __name__ == "__main__":
    main()