# script: validating_emails.py

from validate_email import validate_email

email_address = input("Enter an Email to validate: ")
print(validate_email(f'{email_address}'))
