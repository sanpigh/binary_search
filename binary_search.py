def binary_search(array, x): #array is a list of growing objects
    a_size = len(array)
    i = a_size//2
    i_inf = 0
    i_max = a_size
    while i_inf<i_max:
        i = (i_inf+i_max)//2
        if array[i] < x: #binary_search(array[i+1,a_size], x)
            i_inf = i + 1
        elif array[i] > x: #binary_search(array[0,i], x)
            i_max = i
        else: return i
    print("{} not found".format(x))
    return None

print(binary_search([1,2,3,4,5,6,7,8,9], 3))
print(binary_search([1.4,2.5,3.6,4.7,5.6,6.7,7,8,99], 2.5))
print(binary_search([9,8,7,6,5,4,3,2,1], 3)) #Numbers are not growing, it won't work
