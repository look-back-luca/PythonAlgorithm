#class를 이용한 객체 정렬
#cmd + d -> 같은 단어 하나씩 차례로 수정하기
#cmd + shift + l -> 같은 단어를 동시에 모두 수정하기

class Candidate:
    def __init__(self, test1, test2, test3):
        self.test1, self.test2, self.test3 = test1, test2, test3
    
#객체 리스트 생성 
candidates = [
    Candidate(100, 85, 90),
    Candidate(90, 85, 80),
    Candidate(90, 85, 60),
    Candidate(60, 10, 50),
    Candidate(70, 20, 10)
]

#익명 함수 lambda 이용하기(간단한 정렬 기준인 경우, 사용 가능)
#key = lambda x: x 에서 x인자에 들어오는 값은 "하나의 객체"이다. 
candidates.sort(key=lambda x: (x.test1, x.test2, x.test3), reverse=True)

for i, candidate in enumerate (candidates):
    print(f'{i + 1}: {candidate.test1}, {candidate.test2}, {candidate.test3}')