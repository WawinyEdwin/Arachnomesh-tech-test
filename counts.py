def count(array, array_length):

    # Find the sum  & avg of elements
    sum_of = sum(array)

    average = sum_of / array_length


    # Lets insert the array elements in a hash map
    hashmap = {}
    for i in range(0, array_length):
        hashmap[array[i]] = hashmap.get(array[i], 0) + 1

    # Init a set to hold unique elements
    unique_set = set()

    # We insert elements and the given count 
    for x in hashmap:
        unique_set.add((x, hashmap[x]))

    count = 0

    # We want to print count for given elements
    for x in sorted(unique_set):
        count += x[1]
        print(x[0], count)

    