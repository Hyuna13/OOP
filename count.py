#class변수 : 모두가 공유하는 속성
class User:
  #유저 수 세기
  count = 0

  def __init__(self, name, email, pw):
    self.name = name
    self.email = email
    self.pw = pw

    User.count += 1

user1 = User("Maria", "maria@codeit.kr", "1234")
user2 = User("Sarah", "sarah@codeit.kr", "1234")
user3 = User("Alex", "aelex@codeit.kr", "1234")

print(User.count)

#decorating
def add_print_to(original):
  def wrapper():
    print("start")
    original()
    print("end")
  return wrapper

@add_print_to
def print_hello():
  print("Hello")

print_hello()