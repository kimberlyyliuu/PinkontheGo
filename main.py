''' calculate cost of ride'''
def cost(distance):
  total_charge=0
  #$2.50 per mile  
  distance_charge= (distance * 2.50)
  total_charge += distance_charge
  #fees
  fees= distance*0.1 
  total_charge+=fees
  #tip
  percent_tip= int(input("What percent would you like to tip? "))
  total_charge*= 1+(percent_tip/100) 
  total_charge = round(total_charge, 2)
  return("Your total charge is " + str(total_charge) )



'''return details of driver'''
rating=0 #global variable
def driver_details(name, ratings): 
  global rating
  rating=ratings
  return "Your driver is "+ name + " They have a rating of "+ str(rating) + " stars."

'''create account taking inputs of name, email, phone number, 
 credit card''' 
#global variables
name=""
emailAddress=""
phoneNumber=0
creditCard=0

def create_account():
   global name
   global emailAddress
   global phoneNumber
   global creditCard
   name = input("Enter Your Full Name: ")
   emailAddress = input("Enter Your Email Address: ")
   phoneNumber = input("Enter Your Phone Number (leave out the dashes):")
   creditCard = input("Enter Your Credit Card Information (leave out the dashes): ")

  

'''rate driver'''
def rateDriver():
  yourRating = int(input("How many stars would you rate you driver: 1-5? "))
  takeAgain = input("Would you ride with this driver again? Please enter either 'yes', 'no', or 'maybe'? ")
  global rating
  numRatings = 0
  rating+=yourRating
  numRatings += 1
  rating = (rating) / numRatings
  
  if takeAgain == "Yes":
    print("You would ride with the driver again.")
  elif takeAgain == "No":
    print("You would not ride with this driver again.")
  else:
    print("You might ride with this driver again")
    
  print( "Your driver received " + str(yourRating) + " stars")
  print( "The driver's average rating is now " + str(rating) )
      

  
'''safety button'''
def safety_button():
  danger=False
  while danger is False:
    safety_check=input("Are you in danger? Yes or No? ")
    if safety_check=="Yes":
      danger=True
      print("We are alerting the authorities.")
    elif safety_check=="No":
      danger=False
      print("The authorities were not alerted.")
# if danger=True, our system takes note of this and authorities is alerted 


