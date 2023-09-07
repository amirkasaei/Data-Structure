data = []
train = []
tempTrain = []
trainStation = []
possible = True
n = int(input("Enter number of elements : "))
print("Please enter data (press enter after each element): ")
for i in range(n):
    x = int(input())
    data.append(x)
    train.append(i + 1)
    tempTrain.append(i + 1)


def check(index, pr):
    if index == n:
        return

    if data[index] in train:
        while True:
            if pr:
                print("push " + str(train[0]))
            trainStation.append(train[0])
            if train[0] == data[index]:
                train.pop(0)
                break
            train.pop(0)

        if pr:
            print("pop " + str(trainStation[-1]))
        trainStation.pop(-1)

    elif data[index] == trainStation[-1]:
        if pr:
            print("pop " + str(trainStation[-1]))
        trainStation.pop(-1)

    else:
        global possible
        possible = False
        return

    check(index + 1, pr)


check(0, False)
if possible:
    train = tempTrain
    check(0, True)
else:
    print("impossible")
