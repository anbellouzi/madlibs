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
        print("One of the "+ read(0) +" and most gripping scenes of the movie was when " + read(1) +
        ",an " + read(2) + " athlete, and Carl Ludwing Long, jumper from " + read(3) +
        ",were competing up to their celebration. This particular scene stood out to "+
         "all of us because it was one of the most " + read(4) +  " scene in the movie.")

def test():
    create(user_input("Enter an adjective: "))
    create(user_input("Enter an actor/actress: "))
    create(user_input("Enter an race: "))
    create(user_input("Enter an country: "))
    create(user_input("Enter an verb: "))

    print_to_screen()

test()
