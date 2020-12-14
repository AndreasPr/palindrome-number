def isPalindrome(inputNumber):
    if (inputNumber < 0 or (inputNumber % 10 == 0 and inputNumber != 0)):
        return False

    revertedNumber = 0
    while inputNumber > revertedNumber:
        revertedNumber = revertedNumber * 10 + inputNumber % 10
        inputNumber = inputNumber / 10

    return inputNumber == revertedNumber or inputNumber == revertedNumber / 10

inputNumber = 123
result = isPalindrome(inputNumber)
print("Output: ", result)
