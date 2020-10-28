class PlayerCharacter:
  # static attribute
  membership = True

  # Please note that Python doesn't have private/public modifiers. As a convetion, it's used
  # underscore to denote an attribute as private, but without any technical implication
  def __init__(self, name, age=0):
    """
    Magic method, constructor, automatically called when
    this is instanciated.
    """
    self.name = name # attribute dynamically initialized
    self.age = age

  def run(self):
    print('run')

  # decorators are functions that apply logic or change the behavior
  # of other functions.

  # It's basically a static method in which you have a reference
  # to the class type, so you can instantiate a new Player
  @classmethod
  def newPlayer(cls, num1, num2):
    return cls('Teddy', num1 + num2)

  # It's a static method without any reference to the class
  @staticmethod
  def sumAges(p1, p2):
    return p1.age + p2.age


player1 = PlayerCharacter('Chris')
player1.anotherProp = True
player1.run()

player2 = PlayerCharacter.newPlayer(21, 32)

print(player1.name)
print(player1.anotherProp)
print(player2.name)
print(PlayerCharacter.sumAges(player1, player2))