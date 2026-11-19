discount_fare = lambda fare: fare - 200
print("Discounted Fare :", discount_fare(2500))

updated_fares = list(

   map(
       lambda fare: fare + 100,
        ticket_fares))

print(updated_fares)

reservation_status = [
   "Confirmed",
   "Waiting",
   "Confirmed",
   "RAC"]

confirmed_tickets = list(
   filter(
       lambda status: status == "Confirmed",
       reservation_status))
print(confirmed_tickets)

passengers = [
   "Rahul Sharma",
   "Priya Singh",
   "Amit Verma"]

seats = [
   "B1-21",
   "B1-22",
   "B1-23"]

reservation_data = list(
   zip(passengers, seats))

print(reservation_data)

passenger_list = [
   "Rahul Sharma",
   "Priya Singh",
   "Amit Verma"]

for index, passenger in enumerate(passenger_list):
   print(index, passenger)

ticket_fares = [2500, 800, 3200, 600]

valid_fares = list(
   filter(
       lambda fare: fare > 1000,
       ticket_fares))

final_fares = list(
   map(
       lambda fare: fare + 100,
       valid_fares))

passengers = ["Rahul", "Priya", "Amit"]
seats = ["S1", "S2", "S3"]
fares = [2500, 1800, 3200]

reservation_data = list(
   zip(passengers, seats, fares))

print("===================================")
print(" Railway Reservation Report ")
print("===================================")

for index, data in enumerate(reservation_data):

   passenger, seat, fare = data

   final_fare = (lambda x: x - 100)(fare)

   print("Reservation ID :", index + 1)
   print("Passenger      :", passenger)
   print("Seat           :", seat)
   print("Final Fare     :", final_fare)
   print("-----------------------------------")