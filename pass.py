import bcrypt
# Declaring our password
password = input("Enter your password: ").encode('utf-8')
open('pass.txt', 'wb').write(password)

# Adding the salt to password
salt = bcrypt.gensalt()
open('pass.txt', 'wb').write(salt)
# Hashing the password
hashed = bcrypt.hashpw(password, salt)
open('pass.txt', 'wb').write(hashed)

# printing the salt
print("Salt :")
print(salt)

# printing the hashed
print("Hashed")
print(hashed)
