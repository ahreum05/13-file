f = open('test1.txt', 'a')
for i in range(11, 16) :
    data = str(i) + "번째 줄입니다.\n"
    f.write(data)
    
f.close()

