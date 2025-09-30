def loading_movie(filename):
    movie_date ={}
    with open (filename,"r") as file: #open the file in read mode
      for line in file: #read each line one by one
        key, value=line.strip().split(":",1)#key is name and value is name of movie,time,price
        movie_date [key.strip()] = value.strip()
    if "price"in movie_date:
      movie_date["price"]= float(movie_date["price"].replace("RM",""))
    if "seats"in movie_date:
     movie_date["seats"] = int (movie_date["seats"])
    return movie_date
def save_movie(filename,data):
   with open (filename,"w") as file:#open file in writing mode
       file.write(f"name:{data['name']}\n")
       file.write(f"time:{data['time']}\n")
       file.write(f"price:{data['price']}\n")
       file.write(f"seats:{data['seats']}\n")
       file.write(f"story:{data['story']}\n")




def ticketing():
 movie_file=["Zootopia2.txt" , "Wicked.txt" , "Spongebob.txt"]
 movie={}
 for filename in movie_file:
  data=loading_movie(filename)#call thhe function
  movie[data["name"]]= data


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