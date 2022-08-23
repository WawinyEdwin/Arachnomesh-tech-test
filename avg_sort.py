# Initialize a sample array
arr = [1, 4, 3, 2]

# Sort the array for easy manipulation
sortarr = sorted(arr)

# Initialize the vars for re-usability.
small_num = sortarr[0] 
large_num  = sortarr[len(sortarr) -1 ]

# Find Avg.
avg = (small_num  + large_num ) / 2

# Output the computed average.
print(avg)