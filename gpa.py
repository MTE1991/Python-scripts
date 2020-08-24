class Student:
	def __init__(self,year,exam):
		self.year = int(year)
		self.exam = exam
		self.subjects = ["Mathematics","Physics","Chemistry","Biology",
		"English","Bangla","ICT"]
		self.marks = [] # marks & gpa to be appended later
		self.gpa = []

	def get_marks(self):
		for i in range(0,7):
			print(i+1, self.subjects[i])
			n = int(input(">> "))
			self.marks.append(n)

			if n >= 33 and n <= 39:
				self.gpa.append(1.00)
			elif n >= 40 and n <= 49:
				self.gpa.append(2.00)
			elif n >= 50 and n <= 59:
				self.gpa.append(3.00)
			elif n >= 60 and n <= 69:
				self.gpa.append(3.50)
			elif n >= 70 and n <= 79:
				self.gpa.append(4.00)
			elif n >= 80:
				self.gpa.append(5.00)
			
			#Error handling:	
			elif n < 33:
				raise ValueError("Fail.")
			elif n > 100:
				raise ValueError("Marks can't exceed 100.")
			
	def show_marks(self):
		print(self.marks)
		print(self.gpa)
	
	def result(self):
		total = sum(self.marks)
		gpa = sum(self.gpa)/7

		print("Total marks = ", total)
		print("GPA", gpa)

s1 = Student(2020,"HSC")
s1.get_marks()
s1.show_marks()
s1.result()
