#aList = [0, 1, 2, 3]
#friends = ["dog", "dog 2", "dog 3", "myself"]
#print(friends)

#print(len(aList))

a = ["apple", "pen", "pinapple", "pen"]

#indexing list: choosing one element of all of them
print(a[1], a[2], a[0], a[4])
print(a)

    #if theyre next to each other
#print(a[0,2])
    # bc it stops before the last number (2)

    #to start at the end towrds front, use negative numbers
    #last item on list would be -1, not 0
#print(a[-1, -3])

# use indexing to skip towards things

#print(pen in a)

#iterated
#if you dont care about position
numbers = [1, 2, 3, 2, 1]
for num in numbers:
    print(num)

#runner

    #if you care about position in list
for i in range(len(number)):
    print(numbers[i])
