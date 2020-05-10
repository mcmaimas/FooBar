
def solution(x, y):
    big = max(int(x),int(y))
    little = min(int(x),int(y))
    log_level = 0
    error_string = 'impossible'
    if ((big % 2 == 0) and (little % 2 == 0)) or big == 0 or little == 0:
        return error_string
    while little > 1:
        if (big == little): 
            return error_string
        log_level = log_level + int(big/little)
        new_little = big % little
        big = little 
        little = new_little
        if (little < 1):
            return error_string
        log_level = log_level + (big - little)
    return str(log_level)
