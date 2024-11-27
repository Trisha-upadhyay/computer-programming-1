password = "P@ssw0rd123"
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
print(has_upper and has_lower) 
# Output: True
