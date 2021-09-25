class User:
  def initialize(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password

user1 = User()
user1.initialize("Taylor", "taylor@codeit.kr", "1234")

user2 = User()
user2.initialize("Sarah", "sarah@codeit.kr", "5678")

print(user1.name)
print(user1.email)

#특수 메소드, 코드 줄이기
#__init__ 특수메소드: 특정상황에서 자동으로 호출
class User:
  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password

user1 = User("Taylor", "taylor@codeit.kr", "1234")

user2 = User("Sarah", "sarah@codeit.kr", "5678")

print(user1.name)
print(user1.email)