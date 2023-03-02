from datetime import date

class coder:
    # constructor
    def __init__(self, name, location, course, graduation_date):
        self.name = name
        self.location = location
        self.course = course
        self.graduation_date = graduation_date
    
    def greeting(self, person):
        return f'Hello {person}, my name is {self.name}'
    
    def  alumni(self):
        date_today = date.today().strftime("%B %d, %Y").split()
        months = {'January': 1, "February": 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, "July": 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December' : 12}
        graduation_date =  self.graduation_date.split()
        
        if int(graduation_date[1]) < int(date_today[2]):
            return True
        elif int(graduation_date[1]) == int(date_today[2]) and months[graduation_date[0]] <= months[date_today[0]]:
            return True
        else:
            return False