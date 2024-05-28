"""
para cada par debo checar si su string ya esta 

si ya esta agarro su ultimo tiempo, si es mayor a val + 10, regresar true
"""

class Logger:

    def __init__(self):
        self.dicc = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        #never seen
        if message not in self.dicc:
            self.dicc[message] = timestamp
            return True
        else:
            #only register the valid ones
            if (timestamp - self.dicc[message]) >= 10:
                self.dicc[message] = timestamp
                return True
            else:
                #anything that is not valid does not need to be registered
                return False
        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)