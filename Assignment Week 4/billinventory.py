def process_order(inventory, cart):

    total = 0
    print("---- Bill ----")

    for item in cart:

        if cart[item] <= inventory[item]["stock"]:

            cost = inventory[item]["price"] * cart[item]
            total = total + cost

            print(item, "x" + str(cart[item]), "= NPR", cost)

            inventory[item]["stock"] = inventory[item]["stock"] - cart[item]

        else:
            print("Sorry, not enough stock for", item)

    print("Grand Total: NPR", total)
    print("--------------")
    print("Updated stock:")

    for item in inventory:
        print(item, "=", inventory[item]["stock"])


inventory = {
    "rice": {"price": 120, "stock": 20},
    "milk": {"price": 90, "stock": 10},
    "bread": {"price": 60, "stock": 15},
    "eggs": {"price": 15, "stock": 30}
}

cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}

process_order(inventory, cart)