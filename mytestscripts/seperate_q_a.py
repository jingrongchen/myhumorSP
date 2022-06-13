# file1=open('../dataset/groundtruth','r')
# file2=open('question.txt','w')
# file3=open('answer.txt','w')
# content_list=file1.readlines()
#
# for row in content_list:
#     if 'User:' in row:
#         file2.write(row)
#     if 'Humorous reply:' in row:
#         file3.write(row)



##########locate the answer###################

# question=open('question.txt','r')
# qs=question.readlines()
# gpthumor=open('../dataset/gptj_result.txt','w')
# # input=open('../dataset/test_user_result.txt', "r")
#
# for InputText in qs:
#     # print(InputText)
# # InputText='User: "I’m sorry” and “I apologize” mean the same thing...'
#     with open('../dataset/test_user_result_v1.txt', "r") as input:
#         for line in input:
#             if InputText in line:
#                 # print(line, end='')
#                 gpthumor.write(next(input))
#                 # print(next(input), end='')


##########de humorous reply###################
file2=open('./gptanswerclear.txt','w')
file1=open('../dataset/gptj_result.txt','r')
lines=file1.readlines()
for line in lines:
    reply=line.split('Humorous reply: ')[1]
    file2.write(reply)