# Add api_key in key.py file in the same directory 
import key
import requests
import sys

# Check command-line arguments
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# Convert to float
try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line is not a number")

# Get data from coincap api
try:
    response = requests.get(
        f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={key.api_key}").json()
except requests.RequestException:
    sys.exit("Couldn't get data")

# Extract current price
current_price = float(response["data"]["priceUsd"])

# Print bitcoins values
print(f"${current_price * bitcoins:,.4f}")
