a,b=map(str,input().split())
c=list(map(str,input().split()))
for i in c:
      if i in b:
            print('Yes')
            break
else:
      print('No')
