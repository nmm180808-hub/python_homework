import re

text = """INFO User 123 logged in ERROR User 456 authentication failed
WARNING User 123 changed password ERROR User 789 authentication failed
INFO User 456 logged in"""

all_users = re.findall(r'User (\d+)', text)
errors = re.findall(r'ERROR User \d+ authentication failed', text)
error_users = re.findall(r'ERROR User (\d+)', text)

print("Все пользователи:", all_users)
print("Ошибки:", errors)
print("Пользователи с ошибками:", error_users)