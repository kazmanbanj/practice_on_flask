def who_do_you_know():
    people = input("Enter the name of people you know, seperated by commas: ")
    people_without_spaces = [person.strip() for person in people.split(",")]

    return people_without_spaces

def ask_user():
    person = input("Enter a name of someone you know: ")
    if person in who_do_you_know():
        print("You know {}!".format(person))
    else:
        print("You dont know {}!".format(person))

ask_user()