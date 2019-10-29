#! /usr/bin/python3

import cgi
import cgitb
cgitb.enable()
import MySQLdb
import os
import json


form = cgi.FieldStorage()

try:
	test = os.environ['PATH_INFO']
except:
	test= ''

if(test == '/found_me'):
	print('Content-Type: text/html')
	print('Status: 200 OK')
	print()
	print("""
	<html>
	<body>

	<h1>Damn You! </h1>

	<p>You found me, congrats</p>

	</body>
	</html>""")
elif(test == '/Jboy'):
	print('Content-Type: text/html')
	print('Status: 302 Redirect')
	print('Location:/cgi-bin/jboy.cgi')
	print()
	#print("""
	#<html>
	#<body>

	#<h1>Damn You Jboy! </h1>""")

	#x= ['Some','Stuff','Is',42,'Complex',{'meaning':'life'}]
	#xj = json.dumps(x)

	#print(xj)	


	#print("""<p>You found me, congrats</p>

	#</body>
	#</html>""")
else:
	print('Content-Type: text/html')
	print('Status: 302 Redirect')
	print('Location:../../loser.html')
	print()
	#print("""
	#<html>
	#<body>

	#<h1>Hehehehe! </h1>

	#<p>Didn’t find it yet….</p>

	#</body>
	#</html>""")
