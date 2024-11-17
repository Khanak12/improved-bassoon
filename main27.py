import random
import string

def generate_password(length=12):
  password = ''
  for _ in range(length):
    password += random.choice(string.ascii_letters + string.digits)
  return password

print(generate_password)