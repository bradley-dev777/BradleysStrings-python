def insert(mainstr,pos,insertstr):
    mainstr1 = mainstr[:pos]
    mainstr2 = mainstr[pos:]
    return mainstr1 + insertstr + mainstr2
def splitatpos(str,pos):
    return [str[:pos],str[pos:]]