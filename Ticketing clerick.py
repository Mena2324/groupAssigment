def ticketClerick():
  

 movie={
   "Zootopia 2":{"time": "10 am","seats":50 , "price": 10},
   "Wicked: For Good":{"time":"2:30 pm","seats":50 ,"price":15},
   "Spongebob": {"time":"6:30 pm","seats":50 ,"price":20} 
   }
 
  def showing_Movie ():
    print ("Available Movies: ")
     for name,info in movie.items():
      print(f"{name} ---> Time: {info['time']}, Seats: {info['seats']}, Price: RM{info['price']}")

  def print_receipt(customer_name,movie_name,seats, price,total,paid,balance):
    print("\n" + "="*30) #decorlartion
    print("   MOVIE TICKET RECEIPT")
    print("="*30)
    print(f"customer Name:{customer_name}")
    print(f"Movie: {movie_name} ")
    print(f"seats booked:  {seats}")
    print(f"Price for 1 seat:  RM {price}")
    print(f"total amount :RM {total}")
    print(f"Amount paid :RM {paid}")
    print(f"Balance :RM {balance}" )
    print("="*30)
    print("    thanks you & enjoy your movie!")
    print("="*30 +"\n")





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




 

