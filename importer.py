import csv
from trello import TrelloApi

with open('data.csv', 'rb') as csvfile:
	tapi = raw_input("What is your trello app key? - ")
	trello = TrelloApi(tapi) # get API key from https://trello.com/app-key
	print trello.get_token_url('Kanboard Importer', expires='30days', write_access=True)
	key = raw_input("What is the token? - ")

	trello.set_token(key)

	board = raw_input("What is the board ID - ")
	tboard = trello.boards.get(board)

	print trello.boards.get_list(board)
	listid = raw_input("What is the list ID - ") # Don't use idBoard, use id

	projectname = raw_input("What is the name of the Kanboard Project? - ")

	csvreader = csv.reader(csvfile, delimiter=',')
	for row in csvreader:
		Project = row[1]
		Swimlane = row[4]
		Name = row[13]
		if Project == projectname:
			print Name
			trello.cards.new(Name, listid)