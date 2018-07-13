import json
f = open("allTheResponses.json", 'r')
contents = json.load(f)
print(contents)
f.close()

f = open("allTheResponses.json", 'w')


questions = ["What is your name? ", "Where are you? ", "What is your age? "]

keys = ["name", "state", "age"]

everyone_ans = []

while True:
    answers = {}
    for i in range(3):
        print("The key you are on is", keys[i])
        response = input(questions[i])
        answers[keys[i]] = response

    everyone_ans.append(answers)

    finished = input("Do you want to exit? y/n ")

    if finished == 'y':
        break
print(everyone_ans)
json.dump(everyone_ans, f)
