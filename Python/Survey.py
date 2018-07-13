# # name = ["What is your name? "]
# # number = ["What is your age?"]
# #
# # responseA = input(name[0])
# # responseB = input(number[0])
# # responseB.isnumeric
# #
# # #ages.update(response)
# #
# # print(responseA)
# # print(responseB)
# #
# # question = dict(zip(responseA, responseB))
# #
# # print(question)
#
# #-------------------------
#
# question = {"name": "What is your name?", "age": "What is your age?"}
#
# response = input(question[0])
#
# for key in response:
#     answers[key] = response
#
# print(answers)
#--------------------------

questions = ["What is your name?", "What is your age?", "What is your favorite color?", "What is your favorite food?" ]
answers = {}

for i in range(4):
    response = input(questions[i])
    answers[i] = response
    print(answers)
