# Read input as sepcified in the question
# Print output as specified in the question

## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
##      print(val1, " ", val2)
start = int(input())
end = int(input())
step = int(input())

curr_temp = start

while curr_temp <= end:
    c = 5/9 * (curr_temp-32)
    print(curr_temp, " ", int(c))
    curr_temp = curr_temp+step
