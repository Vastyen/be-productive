import sysOpFunctions

# Read the config
'''
The config is a .txt file that saves the parameters to work with
'''

class Config:
    # Atributes
    def __init__(self):
        # A list that stores the names of the programs in each space
        self.programsToClose = sysOpFunctions.readTextFile("programs.txt").split("\n")
        
    # Methods
        