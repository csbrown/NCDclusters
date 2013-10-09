#from svm import *
import sys
import os
import zlib
import NCD
from homeworkmap import buildMap
NCD.COMPRESSIONLEVEL = 6

class StudentPair:
	def __init__(self, studentx, studenty, distance):
		self.studentx = studentx
		self.studenty = studenty
		self.distance = distance

def compareStudents(homeworkpath):
	studenthomeworkmap = buildMap(homeworkpath)
	students = studenthomeworkmap.keys()
	#Initialize biggest5 to nothing in particular
	biggest5 = []
	for i in range(5):
		biggest5.append(StudentPair(None, None, 1))

	for i in range(len(students)-1):
		studentxhomeworkfile = open(studenthomeworkmap[students[i]], 'r')
		studentxhomework = studentxhomeworkfile.read()
		studentxhomeworkfile.close()

		for j in range(len(students[i+1:])):
			j += i + 1
			studentyhomeworkfile = open(studenthomeworkmap[students[j]], 'r')
			studentyhomework = studentyhomeworkfile.read()
			studentyhomeworkfile.close()

			xydistance = NCD.NCDkernel(studentxhomework, studentyhomework)
			
			bigenough = False
			k = 0
			while k< len(biggest5) and not bigenough:
				if xydistance < biggest5[k].distance:
					biggest5[k] = StudentPair(students[i], students[j], xydistance)
					bigenough = True
				k+=1

	return biggest5					
		

biggest5 = compareStudents(sys.argv[1])

for pair in biggest5:
	print pair.studentx
	print pair.studenty
	print pair.distance
	print '-------------'


      
    
