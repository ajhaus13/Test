from datetime import datetime


def age_over_twenty(age):
    if age > 20:
        message = "You are getting pretty old..."
    else:
        message = "You still have a good few years!"
    return message


def main():

    name = input("What is your name? ")
    age = int(input("How old are you? "))
    birth = input("Where are you from? ")
    color = input("What is your favorite color? ").lower()

    now = datetime.now()

    print("Your name is {name}. You are {age} years old and are from {birth}. Your favorite color is {color}.".format(name=name, age=age, birth=birth, color=color))
    print(age_over_twenty(age))
    print("The current date is {}/{}/{}. The current time is {}:{}:{}".format(now.month, now.day, now.year, now.hour, now.minute, now.second))

    user_input = "{0},{1},{2},{3}".format(name, age, birth, color)

    with open('data.csv', 'a') as d:

        d.write("\n")
        d.write(user_input)


if __name__ == "__main__":
    main()
