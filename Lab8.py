passengers = ["Rahul Shrama","Priya Patel",'Amit Varma']
print("Passenger Reservation List:")
print(passengers)

print("\nFirst Passenger:",passengers[0])
print("Second Passenger:",passengers[1])
print("Third Passenger:",passengers[2])

passengers.append("Neha Joshi")
print(passengers)

passengers.remove("Amit Varma")
print(passengers)

passengers.insert(1,"Rohan Mehata")
print(passengers)

removed_passenger = passengers.pop(2)
print(passengers)

print("\nUpdated Reservation List : ")
print(passengers)