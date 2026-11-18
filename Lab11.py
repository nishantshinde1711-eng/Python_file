def welcome_message():
   print("===================================")
   print(" Indian Railways Reservation ")
   print("===================================")
   print("Welcome to Railway Reservation System")

welcome_message()

def book_ticket(passenger_name, train_name):
   print("Passenger Name     :", passenger_name)
   print("Train Name         :", train_name)
   print("Reservation Status : Confirmed")

book_ticket(
   "Rahul Sharma",
   "Rajdhani Express")

def calculate_fare(ticket_price, passengers):
   total_amount = ticket_price*passengers
   return total_amount

final_fare = calculate_fare(2450,2)
print("Final Fare : ", final_fare)