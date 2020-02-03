from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("Lingobird-new.sqlite")

#USER TABLE
db.execute("CREATE TABLE IF NOT EXISTS User(UserId integer primary key autoincrement, first_name text, last_name "
		   "text, user_name text, email_address text, password, payment_method text, date_of_birth text, city);")

first_name = "Lisa"
last_name = "Dünck-Kerst"
user_name = "Lisbeth123"
email_address = "lisa@email.de"
password = "schwerzumerken123"
payment_method = "VISA"
date_of_birth = "26121994"
city = "Düsseldorf"

db.execute(
	"INSERT INTO User(first_name, last_name, user_name, email_address, password, payment_method, date_of_birth text, "
	"city text) VALUES( ?, ?, ?, ?, ?, ?, ?, ?)",
	(first_name, last_name, user_name, email_address, password, payment_method, date_of_birth, city))

db.pretty_print("SELECT * FROM User")

# INSTRUCTOR TABLE
db.execute("CREATE TABLE IF NOT EXISTS Instructor(InstructorId integer primary key autoincrement, first_name text, last_name text, email_address text, city text);")

instructor_first_name = "Minerva"
instructor_last_name = "McGonnagall"
instructor_email_address = "minerva@email.de"
instructor_city = "Hogwarts"

db.execute(
	"INSERT INTO Instructor(first_name, last_name, email_address, city) "
	"VALUES( ?, ?, ?, ?)",
	(instructor_first_name, instructor_last_name, instructor_email_address, instructor_city))

db.pretty_print("SELECT * FROM Instructor")

# COURSES TABLE
db.execute("CREATE TABLE IF NOT EXISTS Course(CourseId integer primary key autoincrement, title text, language text, start_date text, end_date text, weekday text, place text, city text, price integer);")

title = "Dutch for Beginners"
language = "Dutch"
start_date = "03022020"
end_date = "05072020"
weekday = "Tuesday"
place = "Place_to_be"
city = "Düsseldorf"
price = 500

db.execute(
	"INSERT INTO Course(title, language, start_date, end_date, weekday, place, city, price) VALUES( ?, ?, ?, ?, ?, ?, ?, ?)",
	(title, language, start_date, end_date, weekday, place, city, price))

db.pretty_print("SELECT * FROM Course")
