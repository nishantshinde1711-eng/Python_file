train = { 
    "Train_Number":12951,
    "Train_Name" :"Mumbai Rajdhani Express",
    "Source": "Mumbai",
    "Destination": "Delhi",
    "Available_Seats": 120
} 
print("Train Information:")
print(train)

print("\nTrain Number       :", train["Train_Number"])
print("Train Name         :",train["Train_Name"])
print("Source Station     :", train["Source"])
print("Destination Station:",train["Destination"])
print("Available Seats    :",train["Available_Seats"])

print("Train Name         :",train["Train_Name"])
print("Available Seats    :",train["Available_Seats"])
train['Available_Seats' ]= 95 
print(train)

train.update({"Platform No ":4})
print(train)

train.pop("Platform No ")
print(train)

print("\nUpdated Train Record:")
print(train)