import json, requests

API_KEY = 'OylOqGPorg2UjpgDMgoGnVtRBKDhcNn7q6XF0rVb'

def get_votes_by_date(chamber, start_date, end_date):

	url = 'https://api.propublica.org/congress/v1/' + chamber + '/votes/' + start_date + '/' + end_date + '.json'
	response = requests.get(url, headers={"X-API-Key": API_KEY}).content

	data =json.loads(response)

	return data

	def format_nomination_votes(data):
		output = ['date', 'question', 'description', 'result', 'yes', 'no', 'present', 'not_voting']
	for vote in data['results']['votes']: 
    
			date = vote['date']


			question = vote['question']
			description = vote['description']

			result = vote['result']

			yes = vote['total: yes']

			no = vote['total: no']

			present = vote['total: present']

			not_voting = vote['total: not voting']

			output.append([date, question, description, result, yes, no, present, not_voting])

	return output
if __name__ == '__main__':
	votes = get_votes_by_date('senate', '2017-04-06', '2017-04-06')

	if votes == None:
		print "Looks like you haven't finished implementing the get_votes_by_date method ..."
		exit()
	elif type(votes) != dict:
		print "Something's wrong. You might still need to process the data using the json module."
		exit()
	elif type(votes) == dict:
		print 'Your data looks ok!'
		print votes

	formatted = format_nomination_votes(votes)

	if len(formatted) <= 1:
		print 'You only seem to have one item in your output. Did you append records for the others?'
		exit()

	print 'Output:'
	print formatted
