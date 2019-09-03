# One of the ________ and most gripping scenes of the movie was when ____________,
# an _______________ athlete, and Carl Ludwing Long, jumper from _____________,
# were competing up to their celebration. This particular scene stood out to
#  all of us because it was one of the most ________ scene in the movie.
words = list()
# 1. Adjective
# 2. Actor/Actress
# 3. Race
# 4. Country
# 5. Verb

# CREATE
def create(word):
    words.append(word)

def read(index):
    return words[index]

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input



def print_to_screen():
        print("One of the \033[0;32m"+ read(0) +"\033[0m and most gripping scenes of the movie was when \033[33;0;33m" + read(1) +
        "\033[0m,an \033[35;5;35m" + read(2) + "\033[0m athlete, and Carl Ludwing Long, jumper from \033[37;4;37m" + read(3) +
        "\033[0m,were competing up to their celebration. This particular scene stood out to "+
         "all of us because it was one of the most \033[36;6;36m" + read(4) +  "\033[0m scene in the movie.")

# print("\033[0;32mGREEN TEXT\033[0m")
# print "\033[5;41;32mGREEN TEXT\033[0m"


def test():
    adjective = user_input("Enter an adjective: ")
    actor = user_input("Enter an actor/actress: ")
    race = user_input("Enter an race: ")
    country = user_input("Enter an country: ")
    verb = user_input("Enter an verb: ")

    if adjective:
        create(adjective)
    else:
        create("best")

    if actor:
        create(actor)
    else:
        create("Michael Cane")

    if race:
        create(race)
    else:
        create("American")

    if country:
        create(country)
    else:
        create("Italy")

    if verb:
        create(verb)
    else:
        create("gripping")

    print_to_screen()

test()
