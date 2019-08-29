# One of the ________ and most gripping scenes of the movie was when ____________,
# an _______________ athlete, and Carl Ludwing Long, jumper from _____________,
# were competing up to their celebration. This particular scene stood out to
#  all of us because it was one of the most ________ scene in the movie.

# 1. Adjective
# 2. Actor/Actress
# 3. Race
# 4. Country
# 5. Verb





noun = list()

# CREATE
# def create(type, item):
#     type.append(item)
#
# # # READ
# def read(type, index):
#     return type[index]

# # UPDATE
# def update(index, item):
#     checklist[index] = item
#
# # DESTROY
# def destroy(index):
#     checklist.pop(index)
#
# # READ ALL
# def list_all_items():
#     index = 0
#     for list_item in checklist:
#         print("{} {}".format(index, list_item))
#         index += 1
#
# def mark_completed(index):
#     checklist[index] = "√"+checklist[index]
#
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
#
# def select(function_code):
#     # Create item
#
#     if function_code.capitalize() == "noun":
#         #Create item in checklist here
#         item = user_input("Add a noun: ")
#         create(noun, item)
#
#
#     elif function_code.capitalize() == "R":
#         # Read item in checklist here
#         index = user_input("Index of item you want to read: ")
#         print(read(int(index)))
#
#     # elif function_code.capitalize() == "P":
#     #     # Print all items here
#     #     list_all_items()
#
#     elif function_code.capitalize() == "Q":
#         # This is where we want to stop our loop
#         return False
#     else:
#         #Catch all
#         print("Unknown Option")
#     return True
#
# #
# running = True
# while running:
#
#     selection = user_input(
#         "Press C to add to list, R to Read from list and P to display list: ")
#     running = select(selection)

#
# def test():
#     # Your testing code here
#
#     user_value = user_input("Please Enter a value:")
#     print(user_value)
#
#     # ...
#     # Call your new function with the appropriate value
#     select("C")
#     # View the results
#     list_all_items()
#     # Call function with new value
#     select("R")
#     # View results
#     list_all_items()
#     # Continue until all code is run
#
# # test()
