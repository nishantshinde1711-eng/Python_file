total_seats = 5
while total_seats > 0:
    print("Seats Booked Succesfully")
    print("Reamainig Seats :",total_seats - 1)
    total_seats -= 1
print("All Seats are Filled")

print("Available Seat Number:")

for seat in range(1,11):
    print("Seat Number :", seat)

total_seats = 5

for booking in range(1, 10):

    if booking > total_seats:
        print("No Seats Available")
        break

    if booking == 3:
        print("Checking Special Reservation")
        continue

    pass

    print("Seat", booking, "Booked Successfully")