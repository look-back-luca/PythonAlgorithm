#객체 정렬(익명함수 lambda를 사용하여)
#cmd + d -> 같은 단어 하나씩 차례로 선택하여 수정
#cmd + shift + l -> 같은 단어 동시에 모두 선택하여 수정 

class Participant:
    def __init__(self, test1, test2, test3):
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3

#객체 리스트 생성 
participants = [
    Participant(90, 85, 90), 
    Participant(90, 85, 80), 
    Participant(80, 30, 60), 
    Participant(80, 10, 50), 
    Participant(70, 20, 10), 
]

#sort 함수에 key 인자로 lambda 함수를 작성하였을 때, x인자에 들어오는 값이 하나의 객체다.
#reverse 함수 대신에 x 객체에 - 붙이면 내림차순 정렬이 가능하다.
participants.sort(key=lambda x: (x.test1, x.test2, x.test3), reverse = True) 

for (i, participant) in enumerate (participants):
    print(f'{i + 1}: {participant.test1}, {participant.test2}, {participant.test3}')

