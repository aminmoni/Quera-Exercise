def game(number):
    A_list=[int (d) for d in str(number)]
    if A_list[0] > A_list[1]:
        return (A_list[0] - A_list[1])
    else:
        return (A_list[1] - A_list[0])

print(game(47))



