# task 1

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Susan", "Tablet", 3)
]

def fulfill():
    print(f"New Order: {orders[0][0]} has ordered {orders[0][2]} {orders[0][1]}\nNew order: {orders[1][0]} has ordered {orders[1][2]} {orders[1][1]}\nNew Order: {orders[2][0]} has ordered {orders[2][2]} {orders[2][1]}")
    return

fulfill()