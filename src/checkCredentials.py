import getpass

username = input("username: ")
# this do not stream to stdout the password typed
password = getpass.getpass(prompt="password: ")

if username == "jayjay" and password == "secret":
  pLength = len(password)
  hiddenPass = pLength  * '*'
  print(f"Logged in as {username} with password {hiddenPass}")
else:
  print('Invalid credentials')
