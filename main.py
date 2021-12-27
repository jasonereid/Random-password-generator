import string
import random

S = random.randint(10,20)
ran = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits, k = S))
print("Your new password is: " + ran)