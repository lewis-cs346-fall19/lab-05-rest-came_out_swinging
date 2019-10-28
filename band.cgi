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

if(test[0:5] == '/band'):
       	
	if(len(test)<=5):
		print('Content-Type: text/html')
		print('Status: 302 Redirect')
		print('Location:/cgi-bin/bandsql.cgi')
		print()
	else:
		t = test[5:]
		print('Content-Type: text/html')
		print('Status: 302 Redirect')
		print('Location:/cgi-bin/bandsql.cgi' + t)
		print()
elif(test == ''):
        #print('Content-Type: text/html')
        #print('Status: 302 Redirect')
        #print('Location:/cgi-bin/jboy.cgi')
        #print()
	
	print('Content-Type: text/html')
        
	print('Status: 200 OK')
        
	print()
        
	print("""
        
	<html>
        
	<body>

        
	<h1>Bands! </h1>

       	
	<a href='/cgi-bin/bandsql.cgi/'>List Bands</p>

	<a href='/cgi-bin/bandform.cgi/'>Add Band</p>

       	
	</body>
        
	</html>""")
else:
        #print('Content-Type: text/html')
        #print('Status: 302 Redirect')
        #print('Location:../../loser.html')
        #print()
	print('Content-Type: text/html')
	print('Status: 200 OK')
	print()
	print("""
	<html>
	<body>""")
	
	print(test[0:4])
	print("""

	<h1>Bands!</h1>
	<p><b>UNRECOGNIZED PATH: """)
	
	print(test)
	
	print("""! </b></p>

       
	<a href='/cgi-bin/bandsql.cgi/'>List Bands</p>

	<a href='/cgi-bin/bandform.cgi/'>Add Band</p>       
	
	</body>
	</html>""")
