class Citizen:
  """주민 클래스"""
  drinking_age = 19

  def __init__(self, name, age, resident_id):
    """이름, 나이, 주민번호"""
    self.name = name
    self._age = age #__는 클래스밖에서 접근금지
    self._resident_id = resident_id
  
  def authenticate(self, id_field):
    """본인확인"""
    return self._resident_id == id_field
  
  def can_drink(self):
    """음주가능 나이 확인"""
    return self._age >= Citizen.drinking_age

  def __str__(self):
    """주민번호를 문자열로"""
    return self.name + "씨는" + str(self._age) + "살입니다."

  """접근할수있는메소드"""
  @property
  def age(self):
    print("나이를 리턴한다")
    return self._age
  
  @age.setter
  def age(self, value):
    print("나이 설정")
    if value < 0:
      print("나이는 0이하가 될수없음. 기본값 0으로설정")
      self._age = 0
    else:
      self._age = value

"""def get_age(self):
    #숨겨놓은 변수 __age의 값을 받는 메소드
    return self._age
  
  def set_age(self, value)
  #숨겨놓은 변수 __age의 값을 설정하는 메소드
    if value < 0:
      print("나이가 0보다 커야함. 기본값 0으로 설정함")
      self._age = 0
    else:
      self._age = value"""

taylor = Citizen("Taylor", -10, "1234567")
taylor.age = 19
print(taylor.age)