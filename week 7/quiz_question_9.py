recipt = {}
recipt["side salad"] = 6
recipt["chicken par,"] = 12
recipt["cookie"] = 3

def get_total_cost(recipt):
    total_cost = 0
    for each_item in recipt:
        cost = recipt[each_item]
        total_cost += cost
    return total_cost
