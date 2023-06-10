import json

# Load the cat fact from the JSON file
with open('cat_fact.json') as f:
    data = json.load(f)

# Print the cat fact
print(data['fact'])
