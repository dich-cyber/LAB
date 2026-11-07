# l=[]
# n = int(input())
# for j in range(n):
#     x = int(input())
#     l.append(x)
# avr = sum(l)/n
# print(avr)


# l=[]
# n = int(input())
# for j in range(n):
#     x = int(input())
#     l.append(x)
# for u in l:
#     ca = l.index((max(l)))
#     ci = l.index((min(l)))
# l[ca],l[ci] = l[ci],l[ca]
# print(l)
#

# n = int(input())
# l= []
# for j in range(n):
#      x = int(input())
#      l.append(x)
# d = l[1] - l[0]
# for i in range(1,n-1):
#     if l[i+1] - l[i] != d:
#         print('false')
#         break
# print('true')


# l=[]
#
# n = int(input())
# a= []
# for j in range(n):
#      x = int(input())
#      a.append(x)
#
# b = []
# m = int(input())
# for j in range(m):
#      x = int(input())
#      b.append(x)
#
# for x in a:
#     l.append(x)
# for x in b:
#     l.append(x)
# print(list(set(l)))


n= int(input())
# a = list(map(int, input().split()))
a= []
for j in range(n):
     x = int(input())
     a.append(x)
mx=0
mix=0
for i in range(n):
        for j in range(n):
            if a[i] > a[j]:
                mx = i
            if a[i] < a[j]:
                mix = i
t = a[mx]
a[mx]=a[mix]
a[mix] = t
print(a)




