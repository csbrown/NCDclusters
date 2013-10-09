import os

#send this a homework directory!
def buildMap(homeworkpath):
	studentids = os.listdir(homeworkpath)
	studenthomeworkmap = {}
	for student in studentids:
		submissionspath = os.path.join(homeworkpath,student)
		
		submissions = None
		if os.path.isdir(submissionspath):
			submissions = os.listdir(submissionspath)
		
		if submissions:
			latest = max(submissions)
			latestpath = os.path.join(submissionspath,latest)
			submissionfoldercontents = os.listdir(latestpath)
			lastsubmission = None
			i = 0
			while i<len(submissionfoldercontents) and not lastsubmission:
				if os.path.splitext(submissionfoldercontents[i])[1] == '.py':
					lastsubmission = os.path.join(latestpath, submissionfoldercontents[i])
					studenthomeworkmap[student] = lastsubmission
				i += 1
	return studenthomeworkmap
