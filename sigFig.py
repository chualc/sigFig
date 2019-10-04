import math

#https://github.com/chualc/sigFig
def round_sfig(num, sfig):
    if num == 0:
        return 0
    else:
        # https://en.wikipedia.org/wiki/Significant_figures
        r_loc = int(math.floor(math.log10(abs(num))) + 1 - sfig)
        answer = round(num, -r_loc)
        
        # EX: 
        # if answer is 312.0 and int(answer) is 312, return int(answer)
        # if answer is 31.2 and int(answer) is 31, return answer
        
        if answer == int(answer):
            return int(answer)
        
        return answer

