'''
    적성일 : 2023년 10월 11일
    작성자 : 202195057 손패택
    설면: def
'''
print("def 예약어를 이용하여 함수 작성하고 호출하기")

def address() :
    print("부산시 사상구")
    print("괘법동 산 1-1번지")
    print("신라대학교 국제교육관 552호")
    
address()
address()

print()

'''
    함수에 값을 넘겨주고 일을 시킨다.
    인자와 매개변수
'''
print("인자와 매개변수")


def welcome(name) :  
    print(name,"님 안녕하세요.")
    print(f"{name}님 안녕하세요.")
    print("{}님 안녕하세요." .format(name))

   
welcome("손패택")
welcome("손패택")