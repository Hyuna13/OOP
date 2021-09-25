class User:
  def say_hello(self):
    #객체의 행동 = 메소드, 첫번째 파라미터는 꼭 self
     print("hi my name is {}".format(self.name))
  
  def login(self, my_email, my_password):
    #로그인 메소드
     if (self.email == my_email and self.password == my_password):
         print("SUCCESSFUL!")
     else:
         print("FAILED!")

  def check_sum(self, name):
    #파라미터로 받는 name이 유저의 이름과 같은지 불린으로 리턴하는 메소드
     return self.name == name

#서로 다른 인스턴스
user1 = User()
user2 = User()

#객체 속성추가
user1.name = "Claudia"
user1.email = "claudia@codeit.kr"
user1.password = "1234"

user2.name = "Taylor"
user2.email = "taylor@codeit.kr"
user2.password = "5678"

print(user1.email) #속성 출력
User.say_hello(user1) #클래스의 메소드 출력1
user1.say_hello()#인스턴스의 메소드 출력2

user1.login("hyuna@codeit.kr", "1234") #로그인 메소드 출력
print(user1.check_sum("Claudia")) #불린 리턴
print(user1.check_sum("Maria"))


class User:
  def __init__(self, name, email, pw):
    self.name = name
    self.email = email
    self.pw = pw

  def say_hello(self):
    print("Hi, my name is {}".format(self.name))
  
  #__str__메소드
  def __str__(self):
    return "user: {}, email {}, password ****".format(self.name, self.email)

user1 = User("Maria", "maria@codeit.kr", "1234") 
user2 = User("Sophia", "sophia@codeit.kr", "5678") 

print(user1)
print(user2)