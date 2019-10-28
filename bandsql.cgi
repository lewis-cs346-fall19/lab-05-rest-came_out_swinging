#! /usr/bin/python3

import cgi
import cgitb
cgitb.enable()
import MySQLdb
import passwords
import os


#print('Content-Type: text/html')
#print('Status: 200 OK')
#print()

#print('Content-Type: application/json')
#print('Status: 200 OK')
#print()

form = cgi.FieldStorage()

if 'band' in form:
	x=form['band'].value
else:
	x=''
if 'Shows' in form:
	y=form['Shows'].value
else:
	y=''
if 'date' in form:
	d=form['date'].value
else:
	d=''

try:
	test = os.environ['PATH_INFO']
except:
	test= ''


#x = "'" + x + "'"
#y = "'" + y + "'"
#d = "'" + d + "'"

#print(x)
#print(y)
#print(d)

if(x != '' and y != '' and d != ''):
	conn = MySQLdb.connect(host = passwords.SQL_HOST,user = passwords.SQL_USER,passwd = passwords.SQL_PASSWD,db = 'kirchdata')

	cursor = conn.cursor()

	cursor.execute('INSERT INTO bands(Name,Shows,ShowDate) VALUES (%s,%s,%s);',(x,y,d))

	m = cursor.lastrowid

	cursor.close()

	conn.commit()
	conn.close()

	#m = cursor.lastrowid
	print('Content-Type: text/html')
	print('Status: 302 Redirect')
	print('Location:/cgi-bin/bandsql.cgi/' + str(m)+ "/")
	#print('Status: 200 OK')
	print()


	#print("""
	#<html>
	#<body>
	
	#<p>""" +str(m) + """</p>

	#</body>
	#</html>""")	

else:
	conn = MySQLdb.connect(host = passwords.SQL_HOST,user = passwords.SQL_USER,passwd = passwords.SQL_PASSWD,db = 'kirchdata')

	cursor = conn.cursor()

	if (test == '' or test == '/'):
		cursor.execute('SELECT * FROM kirchdata.bands;')
	else:
		#cursor.execute('SELECT * FROM kirchdata.bands;')
		cursor.execute('SELECT * FROM kirchdata.bands WHERE id LIKE %ls;', (int(test[-3:-1]),))
		#cursor.execute('SELECT * FROM kirchdata.bands WHERE id LIKE 43;')
		#print('SELECT * FROM kirchdata.bands WHERE id LIKE %s;', ('43'))
	
	results = cursor.fetchall()


	cursor.close()

	conn.commit()
	conn.close()

#for rec in results:
#        print("""<tr>""")
#        for ele in rec:
#                print("""<td>""" + str(ele) + """</td>""")
#        print("""</tr>""")
#print("""</table>""")
	
	print('Content-Type: application/json')
	print('Status: 200 OK')
	print()

	n=0
	print("""[""")
	#print(test[-2:])
	#print('INSERT INTO bands(Name,Shows,ShowDate) VALUES (%s,%s,%s);',(x,y,d))
	#print('SELECT * FROM kirchdata.bands WHERE id LIKE %s;', 43)
	for rec in results:
		print("""{"id":""" + str(rec[0]) + """,""")
		print(""" "Name": \"""" + str(rec[1]) + """\",""")
		print(""" "Shows":""" + str(rec[2]) + """,""")
		print(""" "ShowDate": \"""" + str(rec[3]) + """\"""")
		n = n + 1
		if n < len(results):
			print("""},""")
		else:
			print("""}""")
		#n = n + 1
	print("""]""")	
