# Import random library
import random

# User Import
takeaway_cost = input('How much do you want to spend (£=Cheap, ££=Medium or £££=Expensive? ')

# Decide your takeaway categories
cheapTakeaway = ['McDonalds','KFC','Pizza','Chip Shop']
mediumTakeaway = ['Subway', 'Burger King']
expensiveTakeaway = ['Chinese','Indian']

# Lets chose a takeaway
if takeaway_cost == "£":
    selected_takeaway = random.choice(cheapTakeaway)
    print("Selected takeaway: " + selected_takeaway )
elif takeaway_cost == "££":
    selected_takeaway = random.choice(mediumTakeaway)
    print("Selected takeaway: " + selected_takeaway )
elif takeaway_cost == '£££':
    selected_takeaway =  random.choice(expensiveTakeaway)
    print("Selected takeaway: " + selected_takeaway )
else:
    print('Choose a cost!')

    