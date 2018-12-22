#1、实现用户输入用户名和密码，当用户名为 seven且密码为123时，显示登陆成功，否则登陆失败！

while True:
    user = input("请输入用户名:")
    password = input("请输入密码:")
    if user == 'seven' and password == '123':
        print('登录成功！')
        break
    else:
        print('登录失败!')



#2、使用while循环实现输出2-3+4-5+6.....+100的和
n = 2
sum = 0
while n <= 100:
    if n%2 == 0:
        sum += n
    else:
        sum += -n
    n +=1
print(sum)

