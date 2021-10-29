# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
array = list(map(int, input().split()))
count = 0
if (len(array) == 0):
    count = 2
elif (len(array) == 1):
    count = 1
elif (len(array) == 2 and array[0] == array[1]):
    count = 1
elif (len(array) > 2):
    even = list()
    odd = list()
    for i in range(N):
        if i%2==0:
            even.append(array[i])
        else:
            odd.append(array[i])
    evendict=dict()
    odddict=dict()
    for i in range(N):
        try:
            evendict[even[i]]=evendict.get(even[i],0)+1
            odddict[odd[i]]=odddict.get(odd[i],0)+1
        except:
            pass
    e=max(list(evendict.values()))
    o=max(list(odddict.values()))
    count=(len(even)-e)+(len(odd)-o)
print(count)