import sqlite3

new = sqlite3.connect("./domain.db")
'''
#new.execute("CREATE TABLE documents (id PRIMARY KEY, text,document);")

new.execute("insert into documents (id,text,document) values (?,?,?)",(1,"sharma","i love food"))
new.commit()
new.close()



'''
cursor = new.execute("SELECT id, text from documents")

for row in cursor:
    print(row)

new.close()
