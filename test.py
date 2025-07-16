stack = []
closeToOpen = {")":"(","]":"[","}":"{"}
s = "([{}])"
def isValid(s:str)->bool:
    for c in s:

        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                return True
            else:
                return True
        else:
            stack.append(c)

    return True if not stack else False

isValid("([{}])")