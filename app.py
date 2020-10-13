from flask import Flask, request
from flask_restful import Resource, Api
from models import ProgrammingLanguages, Related, Users
from flask_httpauth import HTTPBasicAuth
import hashlib 

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

@auth.verify_password
def verify(login, password):
    if not(login, password):
        return False
    hash_password = hashlib.md5(password.encode('utf-8'))
    return Users.query.filter_by(login=login, password=hash_password.hexdigest()).first()

class Responses():
    def responses_with_text_parm(self, id, text):
        try:
            responses = [
                {
                    "status"    : "error",
                    "message"   : "There is no programming language registered with name '{}'." .format(text),
                    "id"        : 0
                },
                {
                    "status"    : "sucess",
                    "message"   : "Programming language '{}' has been deleted." .format(text),
                    "id"        : 1
                },
                {
                    "status"    : "error",
                    "message"   : "The programming language '{}' already exists." .format(text),
                    "id"        : 2
                },
                {
                    "status"    : "error",
                    "message"   : "There is no '{}' as related with any programming language." .format(text),
                    "id"        : 3
                },
                {
                    "status"    : "error",
                    "message"   : "There is no programming language registered with id '{}'." .format(text),
                    "id"        : 4
                },
                {
                    "status"    : "error",
                    "message"   : "The data '{}' must be a string." .format(text),
                    "id"        : 5
                },
                {
                    "status"    : "error",
                    "message"   : "The data related '{}' already exists." .format(text),
                    "id"        : 6
                },
                {
                    "status"    : "error",
                    "message"   : "There is no programming language with initial letter as '{}'." .format(text),
                    "id"        : 7
                },
                {
                    "status"    : "error",
                    "message"   : "There is no related with initial letter as '{}'." .format(text),
                    "id"        : 8
                }
            ]
            return responses[id]
        except IndexError:
            return {
                "status"    : "error",
                "message"   : "List index out of range in 'responses_with_text_parm' with parameter 'id' {}." .format(id)
            }

    def responses_without_text_parm(self, id):
        try:
            responses = [
                {
                    "status"    : "error",
                    "message"   : "There is no column 'name' in body json.",
                    "id"        : 0
                },
                {
                    "status"    : "error",
                    "message"   : "There is no column 'language' in body json.",
                    "id"        : 1
                },
                {
                    "status"    : "error",
                    "message"   : "There is no column 'related' in body json.",
                    "id"        : 2
                },
                {
                    "status"    : "error",
                    "message"   : "There is no column 'language' in body json.",
                    "id"        : 3
                },
                {
                    "status"    : "error",
                    "message"   : "There is no column 'initial' in body json.",
                    "id"        : 4
                }
            ]
        except IndexError:
            return {
                "status"    : "error",
                "message"   : "List index out of range in 'responses_with_text_parm' with parameter 'id' {}." .format(id)
            }
        return responses[id]

class ProgrammingLanguage(Resource):

    def __init__(self):
        self.responses = Responses()

    def get(self):
        data = request.json
        if 'name' in data:
            programmingLanguage = ProgrammingLanguages.query.filter_by(name=data['name'].lower()).first()
            try:
                response = {
                    "id"    : programmingLanguage.id,
                    "name"  : programmingLanguage.name
                }
            except AttributeError:
                response = self.responses.responses_with_text_parm(0, data['name'])
        else:
            response = self.responses.responses_without_text_parm(0)
        return response

class PutOrDeleteProgrammingLanguage(Resource):
    def __init__(self):
        self.responses = Responses()

    @auth.login_required
    def put(self):
        data = request.json
        if 'language' in data:
            if 'name' in data:
                programmingLanguage = ProgrammingLanguages.query.filter_by(name=data['language'].lower()).first()
                if programmingLanguage:
                    programmingLanguage.name = data['name'].lower()
                    programmingLanguage.save()
                    response = {
                        "id"        : programmingLanguage.id,
                        "name"      : programmingLanguage.name
                    }
                else:
                    response = self.responses.responses_with_text_parm(0, data['language'])
            else:
                response = self.responses.responses_without_text_parm(0)
        else:
            response = self.responses.responses_without_text_parm(3)
        return response

    @auth.login_required
    def delete(self):
        data = request.json
        if 'name' in data:
            programmingLanguage = ProgrammingLanguages.query.filter_by(name=data['name'].lower()).first()
            if programmingLanguage:
                programmingLanguage.delete()
                response = self.responses.responses_with_text_parm(1, data['name'])
            else:
                response = self.responses.responses_with_text_parm(0, data['name'])
        else:
            response = self.responses.responses_without_text_parm(0)
        return response

class GetProgrammingLanguages(Resource):
    def get(self):
        languages = ProgrammingLanguages.query.all()
        response = [
            {
                "id"    : i.id,
                "name"  : i.name 
            }
            for i in languages
        ]
        response.sort(key = lambda i: i['name'])
        return response

class GetProgrammingLanguageByInitialLetter(Resource):
    def __init__(self):
        self.responses = Responses()

    def get(self):
        data = request.json
        if 'initial' in data:
            programmingLanguages = ProgrammingLanguages.query.filter(ProgrammingLanguages.name.like('{}%' .format(data['initial'])))

            response = [
                {
                    "name": i.name
                }
                for i in programmingLanguages
            ]

            if len(response) == 0:
                response = self.responses.responses_with_text_parm(7, data['initial'])
        else:
            response = self.responses.responses_without_text_parm(4)
        return response

class PostProgrammingLanguage(Resource):
    def __init__(self):
        self.responses = Responses()

    @auth.login_required
    def post(self):
        data = request.json
        if 'name' in data:
            programmingLanguage = ProgrammingLanguages.query.filter_by(name=data['name'].lower()).first()
            if programmingLanguage:
                response = self.responses.responses_with_text_parm(2, data['name'])
            else:
                programmingLanguage = ProgrammingLanguages(name=data['name'].lower())
                programmingLanguage.save()
                response = {
                    "id"    : programmingLanguage.id,
                    "name"  : programmingLanguage.name 
                }
        else:
            response = self.responses.responses_without_text_parm(0)
        return response

class GetRelated(Resource):
    def __init__(self):
        self.responses = Responses()

    def get(self):
        data = request.json
        if 'related' in data:
            related = Related.query.filter_by(name=data['related'].lower()).first()
            if related:
                programmingLanguage = ProgrammingLanguages.query.filter_by(id=related.programming_id).first()
                if programmingLanguage:
                    response = {
                        "name"              : related.name,
                        "language"          : programmingLanguage.name
                    }
                else:
                    response = self.responses.responses_with_text_parm(4, related.programming_id) 
            else:
                response = self.responses.responses_with_text_parm(3, data['related'])
        else:
            response = self.responses.responses_without_text_parm(2)
        return response

class GetRelatedWithInitialLetter(Resource):
    def __init__(self):
        self.responses = Responses()
    
    def get(self):
        data = request.json
        if 'initial' in data:
            related = Related.query.filter(Related.name.like('{}%' .format(data['initial'])))

            response = [
                {
                    "name"                  : i.name,
                    "language"              : ProgrammingLanguages.query.filter_by(id=i.programming_id).first().name
                }
                for i in related
            ]
            if len(response) == 0:
                response = self.responses.responses_with_text_parm(8, data['initial'])
        else:
            resposne = self.responses.responses_without_text_parm(4)
        return response


class PostRelated(Resource):
    def __init__(self):
        self.responses = Responses()

    @auth.login_required
    def post(self):
        data = request.json
        if 'language' in data:
            if isinstance(data['language'], str):
                programmingLanguage = ProgrammingLanguages.query.filter_by(name=data['language'].lower()).first()
                if programmingLanguage:
                    programmingLanguageId = programmingLanguage.id
                else:
                    response = self.responses.responses_with_text_parm(0, data['language'])
            else:
                response = self.responses.responses_with_text_parm(5, data['language'])

            if 'related' in data:
                if Related.query.filter_by(name=data['related'].lower()).first():
                    response = self.responses.responses_with_text_parm(6, data['related'])
                else:
                    if isinstance(data['related'], str):
                        related = Related(name=data['related'].lower(), programming_id=programmingLanguageId)
                        related.save()
                        response = {
                            "id"                    : related.id,
                            "name"                  : related.name,
                            "language"              : ProgrammingLanguages.query.filter_by(id=related.programming_id).first().name
                        }
                    else:
                        response = self.responses.responses_with_text_parm(5, data['related'])
            else:
                response = self.responses.responses_without_text_parm(2)
        else:
            response = self.responses.responses_without_text_parm(1)
        return response

class PutOrDeleteRelated(Resource):
    def __init__(self):
        self.responses = Responses()

    @auth.login_required
    def put(self):
        data = request.json
        if 'related' in data:
            related = Related.query.filter_by(name=data['related']).first()
            if related:
                if isinstance(data['related'], str):
                    if isinstance(data['name'], str):

                        related.name = data['name']
                        programmingLanguageName = ProgrammingLanguages.query.filter_by(id=related.programming_id).first().name
                        related.save()
                        response = {
                            "id"                    : related.id,
                            "related"               : related.name,
                            "language"              : programmingLanguageName
                        }

                    else:
                        response = self.responses.responses_with_text_parm(5, data['programming-language'])
                else:
                    response = self.responses.responses_with_text_parm(5, data['related'])
            else:
                response = self.responses.responses_with_text_parm(3, data['related'])
        else:
            response = self.responses.responses_without_text_parm(2)
        return response

    @auth.login_required
    def delete(self):
        data = request.json
        if 'related' in data:
            related = Related.query.filter_by(name=data['related']).first()
            if related:
                related.delete()
                response = self.responses.responses_with_text_parm(1, data['related'])
            else:
                response = self.responses.responses_with_text_parm(3, data['related'])
        else:
            response = self.responses.responses_without_text_parm(2)
        return response

class GetRelateds(Resource):
    def get(self):
        relateds = Related.query.all()
        response = [
            {
                "id"                    : i.id,
                "name"                  : i.name,
                "language"  : ProgrammingLanguages.query.filter_by(id=i.programming_id).first().name 
            }
            for i in relateds
        ]
        response.sort(key = lambda i: i['language'])
        return response

class GetRelatedByProgrammingLanguage(Resource):
    def __init__(self):
        self.responses = Responses()

    def get(self):
        data = request.json
        if 'language' in data:
            programmingLanguage = ProgrammingLanguages.query.filter_by(name=data['language']).first()
            if programmingLanguage:

                relateds = Related.query.filter_by(programming_id=programmingLanguage.id)

                response = [
                    {
                        "name":                 i.name,
                        "programming-language": programmingLanguage.name
                    }
                    for i in relateds
                ]
            else:
                response = self.responses.responses_with_text_parm(0, data['language'])
        else:
            response = self.responses.responses_without_text_parm(1)
        return response

api.add_resource(ProgrammingLanguage,                   '/programmingLanguage/')
api.add_resource(GetProgrammingLanguages,               '/programmingLanguages/')
api.add_resource(PutOrDeleteProgrammingLanguage,        '/modifyProgrammingLanguage/')
api.add_resource(PostProgrammingLanguage,               '/postProgrammingLanguage/')
api.add_resource(GetProgrammingLanguageByInitialLetter, '/programmingLanguageByInitialLetter/')

api.add_resource(GetRelated,                            '/relatedProgrammingLanguage/')
api.add_resource(PostRelated,                           '/relatedProgrammingLanguage/')
api.add_resource(PutOrDeleteRelated,                    '/modifyRelatedProgrammingLanguage/')
api.add_resource(GetRelateds,                           '/relatedProgrammingLanguages/')
api.add_resource(GetRelatedWithInitialLetter,           '/getRelatedProgrammingLanguageByInitialLetter/')
api.add_resource(GetRelatedByProgrammingLanguage,       '/getRelatedByProgrammingLanguage/')

if __name__ == "__main__":
    app.run(debug=True)