"""
example:
from util.styles import styles
string = "" + styles.red + "ERROR" + styles.clear +\
                 ": Max Recursion Depth Reached. Stopping instance"
"""
class styles:
    #text colors
    black = '\u001b[30m'
    red = '\u001b[31m'
    green = '\u001b[32m'
    yellow = '\u001b[33m'
    blue = '\u001b[34m'
    magenta = '\u001b[35m'
    cyan = '\u001b[36m'
    white = '\u001b[37m'

    #background colors
    blackBackground = '\u001b[40m'
    redBackground = '\u001b[41m'
    greenBackground = '\u001b[42m'
    yellowBackground = '\u001b[43m'
    blueBackground = '\u001b[44m'
    magentaBackground = '\u001b[45m'
    cyanBackground = '\u001b[46m'
    whiteBackground = '\u001b[47m'

    #extra
    bright = ';1m'
    clear = '\u001b[0m'
    bold = "\u001b[1m"
    underline = "\u001b[4m"
    revers = "\u001b[7m"