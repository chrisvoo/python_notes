while True:
  try:
    age = int(input("Your age? "))
    print(f'Your age is: {age}')
    if (age < 18):
      raise Exception("You're not old enough")
  except ValueError as e:
    print(f'Not an integer number: {e}')
  except (ZeroDivisionError, KeyboardInterrupt):
    # just an example of how to catch multiple errors
    pass  
  else:
    print("*" * 15)
    break
  finally:
    print("Done")