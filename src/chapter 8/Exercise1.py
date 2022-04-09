lst_of_letters = ['a', 'b', 'c', 'd', 'e']
def chop(list_name):  # the function chop removes the first and last letters in the list
    del list_name[0]
    del list_name[-1]
    return None  # it returns noting when called
chop(lst_of_letters)

lst_of_letters = ['a', 'b', 'c', 'd', 'e']
def middle(list_name):
    del list_name[0]
    del list_name[-1]
    return list_name
Q = middle(lst_of_letters)
print(Q)