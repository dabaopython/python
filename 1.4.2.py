
    #for 
print('for 测试.....')
words = ['cat', 'window', 'defenestrate']
for word in words:
    print(word,len(word))

    #利用切片复制列表   代码通过切片操作得到了words的一个拷贝
print('利用切片复制列表.....')
for word in words[:]:
    if len(word)>6:
        words.insert(0,word)
print(words)