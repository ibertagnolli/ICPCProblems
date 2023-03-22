# Python implementation of Binary Indexed Tree

# Returns sum of arr[0..index]. This function assumes
# that the array is preprocessed and partial sums of
# array elements are stored in BITree[].
def getsum(BITree,i):
	s = 0 #initialize all to 0

	# index in BITree[] is 1 more than the index in arr[]
	i = i+1

	# Traverse tree
	while i > 0:

		# Add current element of BITree to sum
		s += BITree[i]

		# Move index to parent node in getSum View
		i -= i & (-i)
	return s

# Updates a node in Binary Index Tree (BITree) at given index
# in BITree. The given value 'val' is added to BITree[i] and
# all of its ancestors in tree.
def updatebit(BITree , n , i ,v):

	# index in BITree[] is 1 more than the index in arr[]
	i += 1

	# Traverse all ancestors and add 'val'
	while i <= n:

		# Add 'val' to current node of BI Tree
		BITree[i] += v

		# Update index to that of parent in update View
		i += i & (-i)


# Constructs and returns a Binary Indexed Tree for given
# array of size n.
def construct(arr, n):

	# Create and initialize BITree[] as 0
	BITree = [0]*(n+1)

	# Store the actual values in BITree[] using update()
	for i in range(n):
		updatebit(BITree, n, i, arr[i])

	# Uncomment below lines to see contents of BITree[]
	#for i in range(1,n+1):
	#	 print BITTree[i],
	return BITree

def query(BITree, a):
        for i in range(a):
            total =  sum(BITree, i), sum(BITree, a)
        print(total)
        return total

def get_input():
        inputLine = input().split(" ")
        n = int(inputLine[0])
        q = int(inputLine[1])
        freq =  [item for item in range(0, n+1)]
        bIT = construct(freq, n)
        for i in range(q):
            line = [x for x in input().split(' ')]
            print(line)
            if len(line) > 2:
                #call update 
                updatebit(bIT, n, int(line[1]), int(line[2]))
            else:
                #call query
                query(bIT, int(line[1]))
		

if __name__ == "__main__":
         get_input()


