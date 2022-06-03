file1 = open('../dataset/test_user.txt', 'r')
Lines = file1.readlines()
file2 = open('../dataset/test_user_result.txt','w')


count=0
for line in Lines:
    count += 1
    print(line.strip())
    file2.writelines('hsdhu humorous reply:')
    file2.writelines(line.strip())
    file2.writelines('\n')

