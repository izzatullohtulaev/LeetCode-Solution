def isValid(s: str):
    stack = []
    closeToOpen = {
        ')':'(',
        '}':'{',
        ']':'[',
        }
    print(stack)
    for c in s: # }
        if c in closeToOpen:
            if stack and stack[-1]==closeToOpen[c]:
                stack.pop()
                print(stack)
            else:
                return False
        else:
            stack.append(c)
            print(stack)
    return True if not stack else False
            