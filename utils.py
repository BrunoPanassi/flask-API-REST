from models import ProgrammingLanguages, Related, Users
import hashlib

def insertProgrammingLanguage(name):
    if ProgrammingLanguages.query.filter_by(id=name.lower()).first():
        print('Error: The programming language {} already exists.' .format(name))
    else:
        programmingLanguage = ProgrammingLanguages(name=name)
        programmingLanguage.save()

def insertRelated(name, programmingLanguageId):
    if not ProgrammingLanguages.query.filter_by(id=programmingLanguageId).first():
        print('Error: There is no programming language with id {}' .format(programmingLanguageId))
    elif ProgrammingLanguages.query.filter_by(id=programmingLanguageId).first():
        print('Error: The name {} already exists.' .format(programmingLanguageId))
    else:
        related = Related(name=name, programming_id=programmingLanguageId)
        related.save()

def insertUser(login, password):
    if Users.query.filter_by(login=login).first():
        print('Error: The users {} already exists.' .format(login))
    else:
        hash_password = hashlib.md5(password.encode('utf-8'))
        user = Users(login=login, password=hash_password.hexdigest())
        user.save()


if __name__ == "__main__":
    # insertProgrammingLanguage('php')
    # insertRelated('laravel', 2)
    insertUser('guest', 'verifymypassword')