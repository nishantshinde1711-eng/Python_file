passenger_age = 25
ticket_confirmed = True

if passenger_age >= 18 and ticket_confirmed : 
    print("Passenger Eligibal For Travel")

confirmed_seat = False
rac_seat = True

if  confirmed_seat or rac_seat:
    print("Reservation Available")

ticket_cancelled = False

if not ticket_cancelled:
   print("Ticket is Active")

passenger_age = 65
payment_completed = True

if passenger_age >= 60  and payment_completed:
    print("Senior citizen Reservation Approved")

available_seats = 5
payment_status = True
if available_seats > 0 and payment_status:
    print("Ticket confirmed Successfully")
else:
    print("Reservation Faild")

valid_id_proof = True
booking_time_valid = True

if valid_id_proof and booking_time_valid:
    print("Tatkal Booking Allowed")
else:
    print("Tatkal Booking Denied")

## Task 7: Build Final Reservation Rule Validation Module
passenger_name = "Rahul Sharma"
passenger_age = 30
available_seats = 2
payment_completed = True
ticket_cancelled =False

if (
    passenger_age >= 18 and
    available_seats >0 and
    payment_completed and
    not ticket_cancelled
):
    print("====================================")
    print(" Indian Railways Reservation ")
    print("====================================")
    print("Passenger Name  :",passenger_name)
    print("Reservation Status  : Confirmed ")
    print("------------------------------------")
else:
    print("REservation Faild")