txt_file = open("../dataset/val/val.txt", "r")
file_content = txt_file.read()
print("The file content are: ", file_content)

content_list = file_content.split("<|endoftext|>")
file1=open('lstm.txt','w')
for row in content_list:
    text_in=row.split('Humorous reply:')[0].split('User: ')[1].split('\n')[0]
    text_out=row.split('Humorous reply: ')[1]
    file1.write(text_in)
    file1.write(' ')
    file1.write(text_out)
    file1.write('\n')