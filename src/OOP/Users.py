
class User():
  def __init__(self, email):
    self.email = email

  def sign_in(self):
    print(f"{self.__class__.__name__} logged in")


class Wizard(User):
  '''
  We inherit from User class by passing its type up here
  '''
  def __init__(self, name, power, email):
    # Using super() in place of User throws an error, as it is interpreted as Wizard, not User.
    User.__init__(self, email)
    self.name = name
    self.power = power

  def attack(self):
    print(f'Attacking with power {self.power}')

  def __str__(self):
    '''
    We redefine the dunder method, like toString in Java
    '''
    return f'{self.__class__.__name__} named {self.name} with power {self.power}' 


class Archer(User):
  def __init__(self, name, numOfArrows, email):
    # Using super() in place of User throws an error, as it is interpreted as Archer, not User.
    User.__init__(self, email)
    self.name = name
    self.numOfArrows = numOfArrows
    self.my_dict = {
        'name':'Yoyo',
        'has_pets': False,
    }

  def attack(self):
    print(f'Attacking with arrows {self.numOfArrows}')

  def __getitem__(self,i):
    '''
    Allows to use the index notation on an instance, like a list
    '''
    return self.my_dict[i]    

  def __str__(self):
    '''
    We redefine the dunder method, like toString in Java.
    https://docs.python.org/3/reference/datamodel.html#special-method-names
    '''
    return f'{self.__class__.__name__} named {self.name} with {self.numOfArrows} arrows left'      


class WizardArcher(Wizard, Archer):
  '''
  Multiple inheritance
  '''
  def __init__(self, name, power, arrows, email):
      Archer.__init__(self, name, arrows, email)
      Wizard.__init__(self, name, power, email)

  def __str__(self):
      return f'{self.__class__.__name__} named {self.name} with power {self.power} and {self.numOfArrows} arrows left' 


wizard = Wizard('Merlin', 50, "merlin@game.org")
archer = Archer('Robin', 100, "archer@game.org")

wizard.attack()
archer.sign_in()
print(isinstance(wizard, User))
print(issubclass(Wizard, User))
print(isinstance(User, object)) # base superclass from which every object inherits
print(wizard.email)
print(wizard)
print(archer['name'])

wizarcher = WizardArcher("Beastie", 100, 56, "beastie@gmail.com")
print(wizarcher)
# Since attack is used in both User's subclasses, Wizard, defined as first in the WizardArcher's constructor, overrides Archer's attack method.
# This is defined by MRO (Method Resolution Order)
# http://www.srikanthtechnologies.com/blog/python/mro.aspx
wizarcher.attack()
print(WizardArcher.mro())