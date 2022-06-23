# LinkedList에서 사용할 노드를 정의한다.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# linkedList의 처음 부분을 정의한다.
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
    # LinkedList의 데이터를 삽입한다.
    def insert(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
    # linkedList의 해당 index값을 가져온다.
    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            count += 1
            node = node.next

        return node
    # linkedList의 해당 index값을 삭제한다.
    def delete_Node(self, index):
        if index == 0:
            del_node = self.head.data
            self.head = self.head.next
            return del_node
        node = self.get_node(index - 1)
        del_node = node.next.data
        node.next = node.next.next
        return del_node

N, K = map(int, input().split()) # n과 k를 입력받는다.
Link = LinkedList(1) # LinkedList 자료구조에 첫 값을 1로 넣어준다.
# 그 뒤 2~n까지 수들을 n에 넣어준다.
for i in range(2, N + 1):
    Link.insert(i)
answer = [] # 정답을 기록하기 위한 answer 변수를 생성한다.
idx = K-1 # idx=k-1(초기 위치를 k-1)로 설정한다.
# LinkedList가 비어있지 않다면 무한 반복한다.
while Link.head is not None:
    idx %= N # 남아있는 사람의 수로 나눈 나머지 값으로 설정한다.
    answer.append(Link.delete_Node(idx)) # answer에 LinkedList의 idx번째 노드를 값을 넣고 LinkedList의 idx번째 노드를 삭제한다.
    idx += (K-1) # idx+=(k-1)로 설정한다(오른쪽으로 3번 이동)
    N -= 1 # 남아있는 사람의 수-=1이다.
# 문제에 맞게 출력
print('<', end='')
for i in range(len(answer) - 1):
    print(answer[i], end=', ')
print(answer[len(answer) - 1], end='')
print('>')