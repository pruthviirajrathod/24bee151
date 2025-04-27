import csv
# Ask user for contact details
full_name = input("Enter full name: ")
phone_number = input("Enter phone number: ")
email = input("Enter email address: ")
address = input("Enter address: ")

# Build the vCard content
vcard_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{full_name}
TEL;TYPE=CELL:{phone_number}
EMAIL:{email}
ADR;TYPE=HOME:;;{address}
END:VCARD
"""

# File name (you can change if needed)
filename = "contact.vcf"

# Write the vCard to a file
with open(filename, 'w', encoding='utf-8') as file:
    file.write(vcard_content)

print(f"vCard '{filename}' created successfully!")
