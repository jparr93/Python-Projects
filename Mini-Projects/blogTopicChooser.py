# Import random library
import random

# User Import
blogging_Topic = ['AppServices','SQLServer', 'SQLPaaS', 'ServiceBus', 'IOT', 'FunctionApps', 'LogicApps',
'Monitoring', 'Synapse', 'DataFactory', 'Networking']

# Lets chose a takeaway

selected_blogging_Topic = random.choice(blogging_Topic)
print("Blog topic is: " + selected_blogging_Topic )

    