from peewee import *
from datetime import datetime 

db = SqliteDatabase('todo.db')


class User(Model):
    first_name =  CharField(max_length=50, unique=True, null=False)
    last_name = CharField(max_length=50, null= False)
    join_date = DateTimeField(formats='%Y-%m-%d %H:%M:%S', default=datetime.now)
    
    class Meta:
        database = db
        
        
class Task(Model):
    title = CharField(max_length=100, null=False, unique=True)
    description = TextField(null=True)
    due_date = DateField(formats='%Y-%m-%d')
    status = BooleanField(default=False)
    user_id = ForeignKeyField(User, )
    
    class Meta:
        database = db
        




def add_user(firstName, lastName):
    """ Add a new user to Database """
    User.create(first_name=firstName, last_name=lastName)
    print('User added successfully !')


def find_user():
    """ Search for a user """

def delete_user():
    """ Remove user from Database """
    

# Create a menu 
def menu():
    print("************** Command Line APP ************")
    print("a) ",add_user.__doc__)
    print("f) ", find_user.__doc__)
    print("d)", delete_user.__doc__)
    print("q) Quite the App")



        
# Entry point of our APP
if __name__ == '__main__':
    # db.connect()
    # db.create_tables([Task, User])
    # Launch the menu at app startapp
    
    
    while True: # always executed
        menu()
        choice = input('Enter your choice ')
        if choice.lower() == 'q':
            break # stop the App
        
        elif choice.lower() == 'a':
            firstName = input('Enter First name : ')
            lastName = input('Enter last name : ')
            add_user(firstName, lastName)
        
        

