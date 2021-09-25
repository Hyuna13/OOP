class User:

  count = 0

  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.passwrod = password

    User.count += 1

  def say_hello(self):
    print("Hello, my name is {}".format(self.name))

  def __str__(self):
    return "user: {}, email {}, password ****".format(self.name, self.email)

  @classmethod #클래스 메소드
  def number_of_users(cls):
      print("Total: {}".format(cls.count))

user1 = User("Maria", "maria@codeit.kr", "1234")
user2 = User("Sarah", "sarah@codeit.kr", "1234")
user3 = User("Alex", "aelex@codeit.kr", "1234")

User.number_of_users() #클래스메소드로 호출
user1.number_of_users() #인스턴스 메소드로 호출