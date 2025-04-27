source_file = 'source.txt'
destination_file = 'destination.txt'


with open(source_file, 'r', encoding='utf-8') as src:
    content = src.read()

content_upper = content.upper()

with open(destination_file, 'w', encoding='utf-8') as dest:
    dest.write(content_upper)

print(f"Contents copied from '{source_file}' to '{destination_file}' with all lowercase letters converted to uppercase!")
