from database import Persons
from database import db_session

def CreatePerson():
    try:
        newPerson = Persons(name='Lucas', age=19)
        db_session.add(newPerson)
        db_session.commit()
    except Exception as error:
        print(error)
def listPerson():
    listPersons = Persons.query.all()

if __name__ == '__main__':
    # CreatePerson()
    listPerson()



