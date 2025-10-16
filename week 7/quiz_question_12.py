def items_purchased(store,wallet):
    affordable = []
    for item in store:
        price = store[item]
        if price <= wallet:
            affordable.append(item)
    return affordable