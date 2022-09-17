# Module that operates with the operative system
import psutil

def readTextFile(name):
    # Function that reads a text file and returns the information inside on a String
    # Input: String name
    # Output: String file
    file = open(name, "r")
    output = ''
    for caracter in file:
        output += caracter
    file.close()
    return output

def detectProgram(nameExecutable):
    # Function that evaluates if the program is executing in the system
    return nameExecutable in (p.name() for p in psutil.process_iter())

def writeTextFile(name, content):
    # Function that create a text file with content
    file = open(name, "w")
    file.write(content)
    file.close()