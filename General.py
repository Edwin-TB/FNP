# ask user the degree fibonacci sequence they want and create a variable for it
def ask_degree():
    degree = int(input("Fibonacci Sequence Degree: "))
    return degree


# ask user the number of terms they want and create a variable for it
def ask_term():
    term = int(input("Terms: "))
    return term


# create an array with degree terms, all of them being 0 except [-1]
def initial_array():
    sequence = [0] * (degree - 1)
    sequence.append(1)
    return sequence


# sums the last degree terms by adding the previous term that loops degree times
def sum_indices(degree):
    index = 0
    for x in range(degree):
        index = index + sequence[0 - (x + 1)]
    sequence.append(index)


# repeats sum and append term - 1 times (subtract 1 cause it starts at 0)
def repeat_indices():
    terms = int(input("How many terms would you like: "))
    for x in range(terms-1):
        sum_indices(degree)


degree = ask_degree()
sequence = initial_array()
print("Initial Sequence: ")
print(sequence)
repeat_indices()
print(sequence)
