user1 = {
    'name': 'Sorna',
    'valid': True
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    if (args[0]['valid']):
      fn(*args, **kwargs)
    
  return wrapper

@authenticated
def message_friends(user):
  name = user['name']
  print(f'message has been sent for {name}')

message_friends(user1)
