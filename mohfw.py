import requests
import json
import pandas as pd

url = 'https://www.mohfw.gov.in/data/datanew.json'
res = requests.get(url)

# Load the JSON data
data = res.json()

# Save the JSON data to a file
with open("data.json", "w") as f:
    json.dump(data, f)

# Convert JSON to DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv("data.csv", index=False)