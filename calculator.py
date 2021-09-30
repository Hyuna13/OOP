#인스턴스변수나 클래스변수를 쓰지 않을때 정적 메소드사용
class Calculator:
  @staticmethod
  def add(first, second):
    return first + second

  @staticmethod
  def subtract(first, second):
    return first - second

  @staticmethod
  def multiply(first, second):
    return first * second

  @staticmethod
  def divide(first, second):
    return first / second

#인스턴스 생성
calculator = Calculator()

print(calculator.add(6, 3))
print(calculator.subtract(6, 3))
print(calculator.multiply(6, 3))
print(calculator.divide(6, 3))
