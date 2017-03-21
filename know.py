from bs4 import BeautifulSoup #for analyzing htmls
import os #for speech in mac

def openKnowledge(k='k.html'): #the function for almost all the work. No special reason for making this function
	with open(k, 'r+') as k: #open the html file
		c = k.read() 
	bs = BeautifulSoup(c, 'html.parser') #BS it!
	os.system('say your file is loaded. What do you want to know') 
	while True: #let's do it forever
		answer = input()
		target = bs.find(attrs={'name':answer}) #it will search by the name attributed defined in the html file.
		for i in target.attrs:
			print(i,':', target.attrs[i]) #listing all the attributes
		print(target['name'], "is under", target.parent.name, target.parent['name'], ". \nIt includes:") #intro of parent, and children
		for i in target.children: #Listing the level, string
			if i != '\n':
				level = i.name
				string = i.string
				try:
					print(level,i['name'],':',string)
				except KeyError:
					print(level,':',string)
		os.system('say what else would you like to search?')
    
os.system("say open which one")
#answer = input()
openKnowledge() #add 'answer' in the bracket


