import sys  

def input_score() :
    student = {}
    student['name'] = input('이름: ')
    student['kor'] = int(input('국어: '))
    student['eng']= int(input('영어: '))
    student['mat']= int(input('수학: '))
    student['tot'] = student['kor']+student['eng']+student['mat']
    student['avg'] = student['tot']/3

    if student['avg'] >=90 and student['avg']<=100:
        student['grade'] = 'A'
    elif student['avg'] >=80 and student['avg']<90:
        student['grade'] = 'B'
    elif student['avg'] >=70 and student['avg']<80:
        student['grade'] = 'C'
    elif student['avg'] >=60 and student['avg']<70:
        student['grade'] = 'D'
    elif student['avg'] <60:
        student['grade'] = 'F'
    # 리스트에 저장
    students.append(student)

def output_score() :
    print('------------------------------------------------------')
    print('{:3}\t{:3}\t{:3}\t{:3}\t{:3}\t{:4}\t{:2}'\
          .format('이름', '국어', '영어', '수학', '총점', '평균', '학점'))
    print('------------------------------------------------------')
    for s in students:
        str1 = '{name:3}\t{kor:3}\t\t{eng:3}\t\t{mat:3}\t\t{tot:3}\t\t{avg:4.1f}\t{grade:2}'.format(**s)
        print(str1)
    print('------------------------------------------------------')

def file_save()  :
    with open('score11.csv', 'w', encoding='utf-8') as f:
        for s in students:
            data = '{name},{kor},{eng},{mat},{tot},{avg:.1f},{grade}\n'\
                   .format(**s)
            f.write(data)
        print('파일 저장 성공')


def file_read() :
    with open('score11.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
        # 리스트 내용 비우기
        
        
        for line in lines:
            line = line.replace('\n', '')
            line = line.split(',')
            
            s = {}
            s['name'] = line[0]
            s['kor'] = int(line[1])
            s['eng'] = int(line[2])
            s['mat'] = int(line[3])
            s['tot'] = int(line[4])
            s['avg'] = float(line[5])
            s['grade'] = line[6]            
            # 리스트에 저장
            students.append(s)
        print('파일 읽기 성공')

def end_pgm() :
    is_save = input("파일에 저장하겠습니까(저장: y)? ")
    if is_save == 'y' :
        file_save();
        
    print('프로그램을 종료합니다.')
    sys.exit(0)


# contoller
students = []
file_read() # 시작시 파일읽기
print()

while True:
    print("""\
*****************
  1. 성적입력
  2. 성적출력
  3. 파일저장
  4. 파일읽기
  5. 종료
*****************""")
    num = int(input('   메뉴 번호: '))
    print()

    if num == 1 : input_score()
    elif num == 2 : output_score()
    elif num == 3 : file_save()
    elif num == 4 : file_read()
    elif num == 5 : end_pgm()
    
    print()
    
    
    
    
