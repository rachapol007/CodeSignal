def addBorder(picture):
    output = []
    border = ""
    for i in range(0,len(picture[0])+2):
        border += "*"
    output.append(border)
    for i in range(0,len(picture)):
        output.append("*"+picture[i]+"*")
    
    output.append(border)
    
    return output
    
    
    '''
    Given a rectangular matrix of characters, add a border of asterisks(*) to it.

    Example:

    For picture = ["abc","ded"]
    the output should be addBorder(picture) = 
                      ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
    
    '''
