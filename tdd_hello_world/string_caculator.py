def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def run(s_num):

    result = 0
    temp = ""
    for i in range(len(s_num)):
        if is_integer(s_num[i]):
            temp+=s_num[i]
        else:
            if len(temp):
                result+=int(temp)
                temp = ""
    if len(temp):
        result+=int(temp)
    return result
