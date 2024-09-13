# Seongeun Park / seongeup / 12-746 A1 / Homework 3-3
 
from datetime import datetime

class DateTimeFormatter: # object
    def __init__(self):
        self.current_time = datetime.now()

    def get_european_format(self): # method
        return self.current_time.strftime("%d %m %Y %H:%M:%S")

formatter = DateTimeFormatter()
european_time = formatter.get_european_format() 
print(f"European Time: {european_time}")