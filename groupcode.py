def technician_menu():
    while True:
        print("\n--- Technician Menu ---")
        print("1. Upcoming movie schedules")
        print("2. Equipments under maintenance")
        print("3. Back to main menu")

        try:
            techchoice = int(input("Enter your choice: "))
            if techchoice == 1:
                print("Displaying upcoming movie schedules...")
            elif techchoice == 2:
                print("Checking equipments under maintenance...")
            elif techchoice == 3:
                break  # Go back to main menu
            else:
                print("Invalid choice. Please enter a number from 1-3.")
        except ValueError:
            print("Invalid input! Enter a valid number.")
def customerdetials():
  
  if option == 2:
    print("Please fill in your personal account details below:")
    name = ("Enter your full name:")
    birthday = int(input("Enter the year you were born:"))
    email = input("Enter your email:")
    print("Insert your occupation: \n -Student \n -Working")
    occupation = input(">>")
    print("Which movie would you like to watch?")
    print("1 - Zootopia 2")
    print("2 - Wicked: For Good")
    print("3 - Spongebob")
    print("4 - Arcane")
    print("5 - Sherlock Holmes")
    print("6 - Barbie")
    movie = int(input(">>"))
    if movie == 1 or movie == 2 or movie == 3:
        print("When would you like to watch the movie? \n (Enter the day of the week)")
        print("Friday (3/10)")
        print("Sunday (4/10)")
        print("Tuesday (7/10)")
        print("Thursday (9/10)")
        day = input(">>")
    elif movie == 4 or movie == 5 or movie == 6:
        print("When would you like to watch the movie? \n (Enter the day of the week)")
        print("Saturdary (4/10)")
        print("Monday (6/10)")
        print("Wednesday (8/10)")
        day = input(">>")
def ticketing():
#find way to make text file for movie and apply
#make customer choose the movie and then pay
#make 2 version of movie description. 1 for show screen which will be short and in rectantage 
#

    movie={
      "Zootopia 2":{"time": "10 am",
                    "seats":50 ,
                    "price": 10 ,
                   "story":"\nDetectives Judy Hopps and Nick Wilde find themselves on the twisting trail of a mysterious reptile who turns the mammal metropolis of Zootopia upside down. Testing their growing partnership like never before, they go under cover in new parts of town to crack the case."
                   "\n"},
      "Wicked: For Good":{"time":"2:30 pm",
                          "seats":50 ,
                          "price":15, 
                          "story":"\nhis article is about the musical. For the Broadway cast recording, see Wicked (musical album). For the two-part film adaptation, see Wicked (film franchise). For the novel that inspired the musical, see Wicked (Maguire novel)."
                          "\n"},
      "Spongebob": {"time":"6:30 pm",
                    "seats":50 ,
                    "price":20, 
                    "story":"\nThe series follows SpongeBob SquarePants, an energetic and optimistic sea sponge who lives in a submerged pineapple, and his aquatic friends. SpongeBob has a childlike enthusiasm for life, which carries over to his job as a fry cook at a fast food restaurant"
                    "\n"} 
    }

    def showing_Movie ():
      print ("=========Available Movies========\n")
      for name,info in movie.items():
        print(f"{name} ---> Time: {info['time']}, Seats: {info['seats']}, Price: RM{info['price']}, Story:{info['story']}")

    def print_receipt(customer_name,movie_name,seats, price,total,paid,balance):
      reciept_text= (
        "\n" + "="*30 +"\n" + #decorlartion
        "   MOVIE TICKET RECEIPT\n"+
        "="*30+ "\n"+
        f"customer Name:{customer_name}\n"+
        f"Movie: {movie_name} \n"+
        f"seats booked:  {seats}\n"+
        f"Price for 1 seat:  RM {price}\n"+
        f"total amount :RM {total}\n"+
        f"Amount paid :RM {paid}\n"+
        f"Balance :RM {balance}\n"+
        "="*30 +"\n"+
        "    thanks you & enjoy your movie!\n"+
        "="*30 +"\n\n"
      )
      print(reciept_text) #make variable called revieot text to add it to

      with open ("reciepts.txt", "a") as file:
         file.write(reciept_text)


    def book_ticket():
      showing_Movie()
      choice=input("Enter movie name you want to book:")
      if choice in movie:
        selected_movie =movie[choice]
        customer_name =input("enter your name:")
        seats=int(input(f"how many seats do you want? (Available :{selected_movie['seats']}): "))
      
        if seats<= selected_movie["seats"]:
            total =seats*selected_movie["price"]
            selected_movie["seats"]-=seats
            #ask for payment
            paid= float(input(f"Enter payment amount (Total= RM{total}):"))
            if paid>=total:
              balance=paid-total
              print_receipt(customer_name, choice, seats, selected_movie["price"],total, paid,balance)
            else:
              print ("not enough money! Transaction cancelled")
        else:
              print("not enough seats availavle!")
      else:
        print("movie not found!")


    while True:
      print("\n1,show movie list\n2. book ticket\n3.Exit")
      option= input("choose an option:")
      if option=="1":
        showing_Movie()
      elif option=="2":
        book_ticket()
      elif option=="3":
        print("goodbye!")
        break
      else:
        print("invalid choice, try again.")


def main_menu():
    while True:
        print("\n=== Cinema Ticket Booking Management System ===")
        print("1. Ticketing Clerk")
        print("2. Cinema Manager")
        print("3. Technician")
        print("4. Customer")
        print("5. Exit")

        try:
            choice_of_role = int(input("Enter your choice (1-5): "))
            if choice_of_role == 1:
                print("You selected Ticketing Clerk!")
                ticketing()
                # You can add clerk_menu() here
            elif choice_of_role == 2:
                print("You selected Cinema Manager!")
                # You can add manager_menu() here
            elif choice_of_role == 3:
                print("You selected Technician.")
                technician_menu()
            elif choice_of_role == 4:
                print("You selected Customer!")
                customerdetials()
                # You can add customer_menu() here
            elif choice_of_role == 5:
                print("Exiting system... Goodbye!")
                break
            else:
                print("Invalid choice! Choose a number from 1 to 5.")
        except ValueError:
            print("Invalid input. Enter a valid number.")


# Start the application
main_menu()
