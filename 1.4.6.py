  #break
print('break.....')
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')


#continue
print('continue.....')
for num in range(2,10):
    if(num %2 ==0):
        continue
    print(num)

#pass
def funcname(parameter_list):
    pass
 
class classname(object):
    pass
a = 1
if a==0:
    pass
else:
    pass