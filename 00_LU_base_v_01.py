

# function goes here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response =="n":
            response = "no"
            return response

        else:
            print("please answer yes /no")


def instructions():
    print("**** how to play ****")
    print()
    print("the rules of the game go here")
    print()
    return ""


def num_check(question, low, high):
    error = "please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is to low / to high give
            if low < response <= high:
                return  response

                # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# the main routine goes here...
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

# ask user how much they would like to play with...
how_much = num_check("how much would you like to play with? ", 0, 10)

print("you will be spending ${}".format(how_much))
