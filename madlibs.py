# One of the ________ and most gripping scenes of the movie was when ____________,
# an _______________ athlete, and Carl Ludwing Long, jumper from _____________,
# were competing up to their celebration. This particular scene stood out to
#  all of us because it was one of the most ________ scene in the movie.

# 1. Adjective
# 2. Actor/Actress
# 3. Race
# 4. Country
# 5. Verb


def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input



def test():
    adjective = user_input("Enter an adjective: ")
    actor = user_input("Enter an actor/actress: ")
    race = user_input("Enter an race: ")
    country = user_input("Enter an country: ")
    verb = user_input("Enter an verb: ")

    print("One of the "+ adjective +" and most gripping scenes of the movie was when " + actor +
    ",an " + race + " athlete, and Carl Ludwing Long, jumper from " + country +
    ",were competing up to their celebration. This particular scene stood out to "+
     "all of us because it was one of the most" + verb +  "scene in the movie.")

test()
