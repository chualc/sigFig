import math

def round_sfig(num, sfig):
    if num == 0:
        return 0
    else:
        # https://en.wikipedia.org/wiki/Significant_figures
        r_loc = int(math.floor(math.log10(abs(num))) + 1 - sfig)
        return round(num, -r_loc)
