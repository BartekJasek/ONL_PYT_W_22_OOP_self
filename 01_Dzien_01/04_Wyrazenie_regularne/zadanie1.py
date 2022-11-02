import re


def check_dice(dice):
    if re.match(r"^\d*D\d+[+-]*\d*$", dice):
        return True
    else:
        return False


print(check_dice('1D10-10'))
