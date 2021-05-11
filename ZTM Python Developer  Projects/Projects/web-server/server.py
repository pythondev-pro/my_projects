from flask import Flask
from flask import render_template, url_for, request, redirect
import csv

app = Flask(__name__)
#print(__name__) --> __main__

@app.route('/')
def my_home():
	return render_template('index.html')
	
@app.route('/<string:page_name>')
def about(page_name):
	return render_template(page_name)

'''
def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email},{subject},{message}')
		return file
'''
				
def write_to_csv(data):
	with open('database.csv', mode='a', newline='') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])
						
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)  # or write_to_file(data)
			return redirect('/thankyou.html')
		except:
			return 'Did not save to database'
	else:
		return "Something went wrong. Try again"

	
app.run(use_reloader = False, debug=True)

