# 1. 파일 열기
f = open("test1.txt", "w")  # "wt" : 문자열 출력
# 2. 파일 입,출력
for i in range(1, 11) :
    data = str(i) + "번째 줄입니다.\n"
    f.write(data)

# 3. 파일 닫기
f.close()
print("쓰기 완료")
####################################

# 1. 파일 열기
f = open("test2.txt", "wb")  
# 2. 파일 입,출력
for i in range(1, 11) :
    data = (str(i) + "번째 줄입니다.\n").encode('utf-8')
    f.write(bytes(data))

# 3. 파일 닫기
f.close()
print("쓰기 완료")

