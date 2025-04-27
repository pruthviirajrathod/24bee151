file1_path = 'file1.txt'
file2_path = 'file2.txt'
output_file_path = 'merged_file.txt'


with open(file1_path, 'r', encoding='utf-8') as file1, \
     open(file2_path, 'r', encoding='utf-8') as file2, \
     open(output_file_path, 'w', encoding='utf-8') as outfile:
    
   
    lines1 = file1.readlines()
    lines2 = file2.readlines()


    max_len = max(len(lines1), len(lines2))


    for i in range(max_len):
        if i < len(lines1):
            outfile.write(lines1[i].rstrip('\n') + '\n')
        if i < len(lines2):
            outfile.write(lines2[i].rstrip('\n') + '\n')

print(f"Files '{file1_path}' and '{file2_path}' merged successfully into '{output_file_path}'!")
