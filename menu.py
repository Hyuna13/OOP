#Menu class
class Menu:
  def __init__(self, name, price):
    #__init__: 클래스의 모든 인스턴스 변수를 초기화
    self.name = name
    self.price = price

  def __str__(self):
    #__str__: 인스턴스의 정보를 문자열로 리턴
    return "{} price :{}".format(self.name, self.price)

burger = Menu("hamberger", 3500)
pizza = Menu("potato pizza", 15000)

print(burger)
print(pizza)
