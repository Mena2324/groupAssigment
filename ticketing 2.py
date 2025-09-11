def ticketing():


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

ticketing()
