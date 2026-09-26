tuples = [(6,5,4),(8,6),(4,),(3,5,7,9),(4,0,6,5,2),(6,0)]
largest = max(tuples,key=len)
print("list of elements :",tuples)
print("tuple with more elements :",largest)
print("number of elements :",len(largest))