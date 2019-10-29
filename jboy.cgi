#! /usr/bin/python3

#import cgi
#import cgitb
#cgitb.enable()
#import MySQLdb
#import json

print('Content-Type: application/json')
print('Status: 200 OK')
print()
#print("""
#<html>
#<body>

#<h1>Damn You Jboy! </h1>""")

print("""[
	  {
	   "id": 1,
           "title": "My first post!",
            "body": "I don't have much to say",
            "date": "2017-06-01"},
          {   
            "id": 2,
            "title": "Still Bored",
            "body": "Should I post something someday?",
            "date": "2018-09-02"}]
	""")
#xj = json.dumps(x)

#print(xj)


#print("""<p>You found me, congrats</p>

#</body>
#</html>""")

