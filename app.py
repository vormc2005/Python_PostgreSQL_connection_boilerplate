from database import Database
from user import User

Database.initialize(user='postgres', password='Mysql#123', database='learning', host='localhost')
# loading from db

my_user = User.load_from_db_by_email('dvvip1@gmail.com')
print(my_user)

my_user = User('test@test.com', 'Jose', 'Smoze', None)
my_user.save_to_db()

# user_from_b = User.load_from_db_by_email('test@test.com')
# print(user_from_b)
