from model import Person
import view

def showAll():
    # get all users in the db
    people = Person.getAll()
    # calls view
    return view.showAllView(people)

def start():
    view.startView()
    input = raw_input()
    if input == 'y':
        return showAll()
    else:
        return view.endView()

if __name__ == '__main__':
    # running controller function
    start()
