from flask import Flask, render_template, request
from datetime import datetime
import psycopg2
import psycopg2.extras


app = Flask(__name__)
def getConn():
	connStr = ("dbname='studentdb' user='dbuser' password='dbPassword' ")
	conn = psycopg2.connect(connStr)
	
	return conn


@app.route('/')
def home():
    return render_template('home.html')
	

@app.route('/addCustomer', methods=['POST'])
def addCust():
try:

	customerID = int(request.form['CustomerID']
	name  = request.form['Name']
	email = request.form['Email']
	
	conn  = None
	conn  = getConn()
	cur   = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	cur.execute('SET search_path TO AssignmentDatabase')
	
	cur.execute('INSERT INTO Customer VALUES(%s, %s, %s)',\
		[customerID, name, email])
	Conn.commit()
		
	return render_template('home.html', msg1 = 'Customer added')
except Exception as e
	return render_template('home.html', msg1 = 'Customer NOT added', error1 = e)
	
finally:
	if conn:
		conn.close()


@app.route('/addTicket', methods=['GET', 'POST'])
def addTicket():
try:

	TicketID = int(request.form['TicketID']
	Problem = request.form['Problem']
	Status = request.form['Status']
	Priority = int(request.form['Priority']
	CustomerID = int(request.form['Status'])
	ProductID =  int(request.form['ProductID']
	
	conn = None
	conn = getConn()
	cur   = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	cur.execute('SET search_path TO AssignmentDatabase')
	msg=''
	
	cur.execute('INSERT INTO Ticket VALUES(%s, %s, %s, %s, CURRENT_TIMESTAMP %s, %s)'\
		[TicketID, Problem, Status, Priority, LoggedTime, CustomerID, ProductID])
	Conn.commit()
	
	return render_template('home.html', msg2 = 'Ticket Logged')
except Exception as e
	return render_template('home.html', msg2 = 'Ticket FAILED to log', error2 = e)
	
finally:
	if conn:
		conn.close()
	
	
		

if __name__ == '__main__':
    app.run(debug=True)
