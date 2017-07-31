response_map = {'"I like it this way"' : 0,
		'"I expect it this way"' : 1,
		'"I am neutral"' : 2,
		'"I can live with it this way"' : 3,
		'"I dislike it this way"' : 4}

kanotypes = {'m' : "Must-have",
		'l' : "Linear", 
		'e' : "Exciter", 
		'r' : "Reverse", 
		'q' : "Questionable", 
		'i' : "Inverse"}

questions = ["The solution allows you to still communicate with others",
		"The solution provides you smarter information about your phone's battery performance",
		"The solution provides options to charge your phone wherever you are",
		"The solution is convenient and helps you maintain your productivity",
		"The solution doesn't upset the design aesthetic of the actual phone",
		"The solution makes you feel safe"]

def main():
	resultmap = []
 	with open("survey.csv") as f:
		questions = f.readline()
		count_questions = len(questions.split(","))
		for q in range(count_questions/2): # each question has a two sub-questions
			responses = [0] * len(kanotypes)
			resultmap.append(responses)
		for l in f:
			answers = l.split(",")
			i = 0
			while i < count_questions-1:
				k = kanotype(response_map[answers[i]], response_map[answers[i+1].strip('\n')])
				resultmap[i/2][k] += 1 # i/2 beacuse there are two sub-questions per question	
				i+=2
	return resultmap

def output(resultmap):
	with open("results.csv", "w") as f:
		f.write("" + "," + kanotypes['m']+ ","+ kanotypes['l']+ ","+ kanotypes['e']+ ","+ kanotypes['r']+ ","+ kanotypes['q']+ ","+ kanotypes['i']+"\n")
		i = 0
		for q in resultmap:
			line = []
			line.append(questions[i]+",")
			i+=1
			for r in q:
				line.append(str(r)+",")
			f.write("".join(line)+"\n")
			
def kanotype(satisfied, unsatisfied):
	''' 
	Determines one of six kano categories for each survey response.
	The categories are m (must-have), l (linear), e (exciter), r (reverse), q (questionable), i (indifferent).
	'''
	su = (satisfied, unsatisfied)
	if(su==(0,4)):
		return 1 #l
	if(su==(0,0) or su==(4,4)):
		return 4 #q
	if(satisfied==0 and unsatisfied in range(1,4)):
		return 2 #e
	if(unsatisfied==4 and satisfied in range(1,4)):
		return 0 #m
	if((unsatisfied==4 and satisfied in range(1,5)) or (satisfied==4 and unsatisfied in range(0,4))):
		return 3 #r
	return 5 #i


if __name__ == "__main__":
	output(main())
