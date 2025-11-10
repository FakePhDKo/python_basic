milk_orders = {'101': {'milk':1, 'yogurt': 5},
               '102': {'milk':2},
               '103': {'milk': 1, 'yogurt': 10},
               '104': {'yogurt': 15}}
for number, info in milk_orders.items():
    milk = info.get('milk')
    print(f"{number} 필요한 milk: {milk} ")