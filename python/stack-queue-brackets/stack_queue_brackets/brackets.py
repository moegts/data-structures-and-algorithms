def validateBrackets(str):
    newArray, checker= [char for char in str], []
    for character in newArray:
        if (character == '(' or character == '{' or character == '['): checker.append(character)
        elif (character == ')'):
            if (checker[-1] == '('): checker.pop()
            else: return False
        elif (character == '}'):
            if (checker[-1] == '{'): checker.pop()
            else: return False
        elif (character == ']'):
            if (checker[-1] == '['): checker.pop()
            else: return False
    return True