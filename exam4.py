# 파일 쓰기
with open('test4.txt', 'w') as f :
    for i in range(1, 6) :
        data = str(i) + "번째 줄입니다.\n"
        f.write(data)
    print('저장 완료')        
print('-' * 20)    

# 파일 읽기
with open('test4.txt', 'r') as f :
    text = f.read()
    print(text)
