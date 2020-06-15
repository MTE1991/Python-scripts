class marks:
	
	def __init__(self, marks):
		self.marks = marks

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

# instances with user input function:		
phy = marks(float(input("phy=")))
ch = marks(float(input("ch=")))
bio = marks(float(input("bio=")))
math = marks(float(input("math=")))
ban = marks(float(input("Ban=")))
eng = marks(float(input("eng=")))
ict = marks(float(input("ict=")))

total = phy.gpa()+ch.gpa()+bio.gpa()+math.gpa()+ban.gpa()+eng.gpa()
avg = total/7

print("GPA =",round(avg,2))

