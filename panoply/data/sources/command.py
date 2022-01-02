import os

def getOutput(cmd):
    output = os.popen(cmd).read()
    output = output.replace('\n', '')
    
    return output
