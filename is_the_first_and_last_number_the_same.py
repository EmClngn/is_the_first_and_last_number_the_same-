# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# pseudo code

# ask user for number of elements they want in the list
desired_number_of_list = int(input("How many numbers of elements do you want in the list? "))
list = []

# make user input said elements
for i in range(desired_number_of_list):
    elements = input("Input your element: ")
    list.append(elements)


# write the program to identify whether or not the first and last number of the list is the same
def first_and_second_number_identifier (list):
    first_number = list [0]
    second_number = list [-1]

    if first_number == second_number:
        return True
    else:
        return False
    
print("Your given list is ", list)
print("\n""...And the result is",first_and_second_number_identifier(list))