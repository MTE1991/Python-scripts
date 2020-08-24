class Student:
    def __init__(self,year,exam):
        self.year = int(year)
        self.exam = exam
        self.subjects = ["Mathematics","Physics","Chemistry","Biology",
        "English","Bangla","ICT"]
        self.marks = [] # marks to be appended later

    def getmarks(self):
        for i in range(0,6):
            print(i,self.subjects[i],"=")
            n = int(input())
            self.marks.append(n)
            
	def gpa(self):
		if self.marks >= 33 and self.marks <= 39:
			return 1.00
		elif self.marks >= 40 and self.marks <= 49:
			return 2.00
		elif self.marks >= 50 and self.marks <= 59:
			return 3.00
		elif self.marks >= 60 and self.marks <= 69:
			return 3.50
		elif self.marks >= 70 and self.marks <= 79:
			return 4.00
		elif self.marks >= 80:
			return 5.00
			
		#Error handling:	
		elif self.marks < 33:
			raise ValueError("Fail.")
		elif self.marks > 100:
			raise ValueError("Marks can't exceed 100.")

s1 = Student(2020,"HSC")
s1.getmarks()
s1.gpa()
