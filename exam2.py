# 방법1 : 문자열 통째로
f = open('test1.txt', 'r') 
text = f.read()
f.close()

print(text)
print('-' * 20)

# 방법2 : 한줄씩
f = open('test1.txt', 'r') 
while True :
    line = f.readline()
    #print(bool(line), line)
    if not line : break
    print(line, end="")

f.close()
print('-' * 20)

# 방법3 : 1줄씩 리스트로 읽기
f = open('test1.txt', 'r') 
lines = f.readlines()
f.close()

print(lines)
print('-' * 20)






