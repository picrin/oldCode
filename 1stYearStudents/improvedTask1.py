res = open("Responses.txt.txt","r")
que = open("QuestionInfo.txt.txt","r")
response = res.readlines()
questions = que.readlines()
response = [[int(element) for element in stri.split(" ")] for stri in response]
questions = [[int(element) for element in stri.split(" ")] for stri in questions]
res.close()
que.close()

def dictFromResponses(response):
    dictResp = {}
    for questionNumber in response:
        if questionNumber[0] in dictResp:
            dictResp[questionNumber[0]].append(questionNumber[1:])
        else:
            dictResp[questionNumber[0]] = [questionNumber[1:]]
    return dictResp

#creats a dict with studentID as keys and the most recent answer as a value
def countAnswers(studentsAnswers):
    studentID = {}
    for element in studentsAnswers:
        studentID[element[0]] = element[1]
    return studentID

#creates a new dictionary from a given range
def newDictFromRange(responN, lowerBound = 1):
    questionR = range(lowerBound, responN +1)
    returned = {}
    for element in questionR:
        returned[element] = 0
    return returned
#increments the answers dict using a dictionary with student answers
def putAnswersToDict(answers, dictIDAns):
    for stID in dictIDAns:
        answers[dictIDAns[stID]] += 1

def printQuestion(resultDict, correctAnswer, questionNumber):
    returned = "Question" + str(questionNumber) + "\n"
    for questionNumber in resultDict:
        if questionNumber == correctAnswer:
            returned += "**"
        returned += str(questionNumber) + ":" + str(resultDict[questionNumber])
        if questionNumber == correctAnswer:
           returned += "**"
        returned += " "
    return returned

def parseQuestion(numberOfAnswers, studentAnswers, lowerBound = 1):
    QuestionAnswers = newDictFromRange(numberOfAnswers, lowerBound)
    dictionaryStudentIDAnswer = countAnswers(studentAnswers)
    putAnswersToDict(QuestionAnswers, dictionaryStudentIDAnswer)
    return QuestionAnswers

def mainProcess(response, question, questionNumber, lowerBound = 1):
    numberOfAnswers = questions[questionNumber][1]
    correctAnswer = questions[questionNumber][0]
    qNumber = questionNumber + 1
    resultDict = parseQuestion(numberOfAnswers, dictFromResponses(response)[qNumber], lowerBound)
    print printQuestion(resultDict, correctAnswer, qNumber)

def main(response, questions):
    for questionNumber in range(len(questions)):
        if questionNumber != 3:
            mainProcess(response, questions, questionNumber)
        else:
            mainProcess(response, questions, questionNumber, 0)
main(response, questions)


