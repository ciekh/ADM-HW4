def counting_sort(A):
    # All elements must be less than a predetermined k value, I take the maximum of the array and I add 1
    k = max(A) + 1
    C= []
    #I create a vector C where for every val of A I save in C [val] how many times val is repeated in A
    for i in range(k):
        C.append(0)
    for val in A:
        C[val] += 1
    # now i sum each value with the previous, so in array C i will be in each cells C[i] the number of values that are
    # less than or equal to i.
    for i in range(len(C)):
        if i != 0:
            C[i] += C[i-1]
    y = len(A)-1
    B = []
    for i in range(len(A)):
        B.append(0)
    y = len(A)-1
    # i create an another array B
    while y >= 0:
        # now I take the values in A and every value in A is an index to access in C thus recovering the last index in which
        #I must go to save the value in B in fact then decrease the value in C
        B[C[A[y]]-1] = A[y]
        C[A[y]] -= 1
        y -= 1
    return B


def counting_sort_letters(A):
    #for each letter I associate an integer and unique id to transform the problem of ordering strings
    #into integers in such a way that the counting sort can be applied
    alphabet ='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    id_letters = {i:j+1 for j,i in enumerate(alphabet)}
    # for each element in A I take its associated integer and order them based on these
    list_id = [id_letters[val] for val in A]
    # All elements must be less than a predetermined k value, I take the maximum of the array and I add 1
    k = max(list_id) + 1
    C = []
    #I create a vector C where for every val of A I save in C[val] how many times val is repeated in A
    for i in range(k):
        C.append(0)
    for val in list_id:
        C[val] += 1
    # now i sum each value with the previous, so in array C i will be in each cells C[i] the number of values that are
    # less than or equal to i.
    for i in range(len(C)):
        if i != 0:
            C[i] += C[i-1]
    B = []
    for i in range(len(A)):
        B.append(0)
    y = len(A)-1
    # i create an another array B
    while y >= 0:
        # now I take the values in A and every value in A is an index to access in C thus recovering the last index in which
        #I must go to save the value in B in fact then decrease the value in C
        B[C[list_id[y]]-1] = A[y]
        C[list_id[y]] -= 1
        y -= 1
    return B


import itertools
def counting_sort_subroutine(A,j):
    #for each letter I associate an integer and unique id to transform the problem of ordering strings
    #into integers in this case I also insert the empty space and the dash as they can be present in the wordsin such a waythat the counting sort can be applied
    alphabet =' -AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    id_letters = {i:j+1 for j,i in enumerate(alphabet)}
    #for each element in A I take the character in position j and its associated integer and order them based on these
    p = []
    for i in range(len(A)):
        try:
            #I order the i-word with the j-th letter
            c = id_letters[A[i][j]]
            p.append(c)
        except Exception:
            # if the string is shorter than j I add a space at the end to communicate that the string should not be considered
            A[i] += ' '
    k = max(p) + 1
    C = []
    for i in range(k+1):
        C.append(0)
    #print(C)
    for val in A:
        C[id_letters[val[j]]-1] += 1
    for i in range(len(C)):
        if i != 0:
            C[i] += C[i-1]

    B = []
    for i in range(len(A)):
        B.append(0)
    y = len(A) - 1
    # i create an another array B
    while y >= 0:
        # now I take the values in A and every value in A is an index to access in C thus recovering the last index in which
        # I must go to save the value in B in fact then decrease the value in C
        B[C[id_letters[A[y][j]] - 1] - 1] = A[y]
        C[id_letters[A[y][j]] - 1] -= 1
        y -= 1
    # return a list of lists sorted according to the j-th letter
    return [list(g) for k, g in itertools.groupby(B, lambda x: x[j])]

def counting_sort_words(lst,j):
    lst4 = []
    if len(lst) == 1 or len(set(lst)) == 1:
        return lst
    else:
        # call the function on each sub-list
        lst1 = counting_sort_subroutine(lst,j+1)
        for x in lst1:
            P = counting_sort_words(x,j+1)
            lst4.append(P)
            # return the list in the desired format
            merged = list(itertools.chain(*lst4))
            merged1 = [x.rstrip() for x in merged]
        return merged1


