students = [{"name":"홍길동", "kor":90, "eng":80, "mat":70},
	        {"name":"김철수", "kor":80, "eng":70, "mat":60}]
print(students)
print('-' * 20)

# 딕셔너리로 구성된 리스트를 csv 파일로 저장하기
with open('score.csv', 'w', encoding='utf-8') as f :
    for s in students :
        data = "{name},{kor},{eng},{mat}\n".format(**s)
        f.write(data)
    print("파일 저장")
    
print('-' * 20)

# csv 파일을 딕셔너리로 구성된 리스트로 저장하기
ss = []
with open('score.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()  # 리스트로 읽어오기
    print(lines)
print('-' * 20)
    
for line in lines :
    # '\n' 삭제
    line = line.replace("\n", "") 
    # 콤마 기준으로 분리하기
    line = line.split(',')
    print(line)
    # 딕셔너리에 저장하기
    s = {}
    s['name'] = line[0]
    s['kor'] = int(line[1])
    s['eng'] = int(line[2])
    s['mat'] = int(line[3])
    
    ss.append(s)
    
print(ss)



