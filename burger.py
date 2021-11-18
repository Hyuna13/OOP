#상속
#부모클래스
class Employee:
  """직원 클래스"""
  company_name = "버거"
  raise_percentage = 1.03

  def __init__(self, name, wage):
      """인스턴스 변수"""
      self.name = name
      self.wage = wage
  
  def raise_pay(self):
      """시급 인상 메소드"""
      self.wage *= self.raise_percentage
  
  def __str__(self):
      """직원정보 문자열 메소드"""
      return Employee.company_name + "직원: " + self.name


#자식클래스
class Cashier(Employee):
  """오버라이딩"""
  raise_percentage = 1.05
  burger_price = 4000

  def __init__(self, name, wage, number_sold):
    super().__init__(name, wage)
    self.number_sold = number_sold #판매된 버거 개수
  
  def take_order(self, money_received):
    if Cashier.burger_price > money_received:
      print("돈이 충분하지않음. 다시 계산 해주세요.")
      return money_received
    else:
      self.number_sold += 1
      change = money_received - Cashier.burger_price
      return change

  def __str__(self):
      return Cashier.company_name + "계산대 직원: " + self.name
      

class DeliveryMan(Employee):
   def __init__(self, name, wage, on_standby):
       super().__init__(name, wage)
       self.on_standby = on_standby
   def deliber_to(self, address):
       if self.on_standby:
         print(address + "로 배달 나감")
         self.on_standby = False
       else:
         print("이미 배달 나감")

   def back(self):
       """배달 복귀"""
       self.on_standby = True     

taylor = Cashier("Taylor", 8900, 0)




