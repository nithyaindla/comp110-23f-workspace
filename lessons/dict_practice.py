"""Practice with Dictionary Syntax."""

# Create New Dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

# Adding Key,Value pair to a Dictionary
ice_cream["oreo"] = 3

# Removing Key,Value pair from Dictionary
ice_cream.pop("oreo")

# Accessing a Value
print(ice_cream["chocolate"])

# Modify a Value
ice_cream["vanilla"] = 10

# Length of Dictionary
print(len(ice_cream))  # returns number of key,value pairs

# Check if key is in dictionary
print("vanilla" in ice_cream)

if "mint" in ice_cream == True:
    print(ice_cream["mint"])
else: 
    print("No orders of mint")

# Loop through dictionary
    for flavor in ice_cream:
        print(flavor + " has " + str(ice_cream[flavor]) + " orders")  # using string concatentaion
        print(f"{flavor} has {ice_cream[flavor]} orders")  # using a f-string

print(ice_cream)