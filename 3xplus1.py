
def create_or_count_number_sequences(number, just_Count=True):
    listOfTerms=[]
    count = 0
    while number != 1:
        count += 1
        if number % 2 == 0:
            number /= 2
        else:
            number = (number * 3) + 1
        if not just_Count:
            listOfTerms.append(number)
    return {"listOfTerms": listOfTerms, "count": count}

def print_table(loopCounts):
    maxLoopCount = max(loopCounts)
    indexesOfMaxLoopCounts = [i + fromThisNumber for i, counT in enumerate(loopCounts) if counT == maxLoopCount]

    header = ["Number", "Loop Count"]
    print(f"{header[0]:<7} {header[1]:<12}")
    print("-" * 20)
    for number in range(1, len(loopCounts) + 1):
        print(f"{number + fromThisNumber - 1:<7} {loopCounts[number - 1]:<12}")
    print(f"\nMax loop count: {maxLoopCount}")
    print(f"\nIf that number(s) are given:", end=" ")
    for i in range(0, len(indexesOfMaxLoopCounts)):
        if i < len(indexesOfMaxLoopCounts) - 1:
            print(f"{indexesOfMaxLoopCounts[i]}", end=" or ")
        else:
            print(f"{indexesOfMaxLoopCounts[i]}")
    return indexesOfMaxLoopCounts
def print_longest_sequences(indexesOfMaxLoopCounts):
    giveListOfLoopNumbers = False
    condition = True
    while condition:
        giveListOfLoopNumbers_ = input("Show the list of longest sequence(s)?  Y / N  : ")
        if giveListOfLoopNumbers_.upper() == "Y":
            giveListOfLoopNumbers = True
            condition = False
        elif giveListOfLoopNumbers_.upper() == "N":
            giveListOfLoopNumbers = False
            condition = False
        else:
            print("\nPlease enter a valid answer. [y] or [n]\n")

    if giveListOfLoopNumbers:
        for term in indexesOfMaxLoopCounts:
            terms = [term]
            print(terms + create_or_count_number_sequences(term, False)["listOfTerms"])


print("Enter the START and END as integers:")
fromThisNumber = int(input("Start:"))
toThisNumber = int(input("End:"))

loopCounts = []
for number in range(fromThisNumber, toThisNumber + 1):
    count=0
    loopCounts.append(create_or_count_number_sequences(number)["count"])

indexesOfMaxLoopCounts=print_table(loopCounts)

print_longest_sequences(indexesOfMaxLoopCounts)





