movies = {
    "Avengers": {"time": "7:00 PM", "seats": 50, "price": 10},
    "Inception": {"time": "9:00 PM", "seats": 30, "price": 12}
}
name= input("inter the name: ")
time= input("inter available time:")
seats= input("number of seats availables: ")
price=  input("the prise : ")
def add_movie(name, time, seats, price):
    movies[name] = input({"name": name,"time": time, "seats": seats,"price":price})

print(add_movie(name, time, seats, price ))