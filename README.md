# kanboard2trello

### How to use

- Export your board from your Kanboars instance
- Save the file as `data.csv`
- Get a Trello app key from [https://trello.com/app-key]("")
- Run `importer.py`
- Copy the printed URL into your browser and sign in with your Trello account
- Copy the token on the webpage into the importer
- Go to your Trello board and grab the **bold** part of the URL: trello.com/b/**B4a35kpF**/proj
- Copy the board ID into the importer
- The importer will print all of the lists in the board, Select the **'id'** from the dictionary dump corresponding to the list you want to import into


[
	{u'idBoard': u'150a433e249d4167af50b3275423116e', u'subscribed': False, u'pos': 163839, u'closed': False, u'id': u'56a8a895b0b89907469cfd32', u'name': u'Done'}, {u'idBoard': u'**150a433e249d4167af50b3275423116e**', u'subscribed': False, u'pos': 229375, u'closed': False, u'id': u'dfasdggfdg43345235', u'name': u'Ready'},
	{u'idBoard': u'150a433e249d4167af50b3275423116e', u'subscribed': False, u'pos': 294911, u'closed': False, u'id': u'**dfasdggfdg43345256**', u'name': u'TODO'},
	{u'idBoard': u'150a433e249d4167af50b3275423116e', u'subscribed': False, u'pos': 360447, u'closed': False, u'id': u'**dfasdggfdg43345270**', u'name': u'In-Progress'}
]

- Type in the name of the Kanboard Board you want to import
- It will now import your data