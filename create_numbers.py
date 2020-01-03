import mysql.connector

mydb = mysql.connector.connect(
	host="127.0.0.1",
	user="root",
	passwd="intvou123",
	database="numbers"
)

mycursor = mydb.cursor()
mycursor.execute("delete from integers;")
mycursor.execute("ALTER TABLE integers AUTO_INCREMENT = 1;")

def insertInteger( creator, number, expresion):
	mycursor.execute("INSERT INTO integers (creator, number, expresion) VALUES (%s, %s, %s);", (creator,number,expresion))
	mydb.commit()

def insertPow ( n,pp):
	insertInteger(n**pp,cero,cero)
	for times in range(0,pp):
		insertArray(n**pp,n)
maxNumber = 1000
for creator in range(1,maxNumber):
	insertInteger(creator-1,creator,str(creator-1)+"+1")

	#iterate over all previous numbers including it self.
	for previous in range(2,creator+1):
		#multiply
		created = creator*previous
		if created >= maxNumber:
			created = None
		insertInteger(creator,created,str(creator)+"*"+str(previous))
		
		#pow
		created = creator**previous
		if created >= maxNumber:
			created = None
		insertInteger(creator,created,str(creator)+"**"+str(previous))

	# #pow
	# insertPow(number,number)
	# created = created + 1

	# #with previous
	# print("iteration: "+ str(number) +" prime: " +str(prime))
	# mycursor.execute("SELECT number FROM integers where number >1 and number < %s", (number,))
	# myresult = mycursor.fetchall()
	# print(myresult)
	# for previous in myresult:
	# 	newNumber = number * int(previous[0])
	# 	insertInteger(newNumber,cero,cero)
	# 	created = created + 1

	# 	#insert pows
	# 	insertPow(previous[0],number)
	# 	created = created + 1

	# if created > 0:
	# 	mycursor.execute("UPDATE integers set created = %s where number = %s", (created, number))
	# 	mydb.commit()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")