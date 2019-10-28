#! /usr/bin/python3

import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()


print("Content-Type: text/html")
print("Status: 200 OK")
print()

print("""
<html>
<body>

<h1>FORM</h1>

<p> Band Name, Number of Shows, Date of Next Show </p>
</br>
<form action='/cgi-bin/bandsql.cgi' method='get'>
	<input type=text name=band>
	<input type=text name=Shows>
	<input type=date name=date>
	<input type=submit>
</form>



</body>
</html>""")
