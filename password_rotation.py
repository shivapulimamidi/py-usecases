import subprocess
import string
import random

# Get current password from user input 
current_password = input("Enter the current MySQL root password: ")

# Generate a new secure password
new_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))

# Change MysQL password using subprocess
subprocess.run (['mysql', '-u' 'root', '-P' + current_password,'-e', f" ALTER USER ' root '@'localhost' IDENTIFIED BY 'new_password'"])ß

# Print and store new password in a file
print(f"The new MySQL password is: (new_password)")
with open('/home/nasi/Python_usecases/mysql_secret_password.txt', 'w') as f:
       f. write (new_password)
