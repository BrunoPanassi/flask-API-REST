# Programming Languages REST API

![Python](https://img.shields.io/badge/Python-3.7.3-yellowgreen) ![PIP](https://img.shields.io/badge/pip-20.2.3-orange) ![Flask](https://img.shields.io/badge/flask-1.1.2-green) ![Flask-RESTful](https://img.shields.io/badge/flask--RESTful-0.3.8-blue) ![Flask-HTTPAuth](https://img.shields.io/badge/flask--HTTPAuth-4.1.0-red) ![SQL Alchemy](https://img.shields.io/badge/SQLAlchemy-1.3.19-yellow)

A REST API made with Flask, Flask-RESTful, Flask-HTTPAuth and SQLAlchemy to get information about Programming Languages names and relateds names. <br/>
A related name is a framework or something related to a programming language, like Flutter is to Dart and Laravel is to PHP.

## Why
This project was made to provide all possible information about names of programming languages at all. <br>
For latelly being useful in future projects that will need of this kind of information.

## Models, Utils and App
The *models.py* is responsible for the modeling of tables and the creation of it. <br/>
The *utils.py* is used to manipulate data without the use of the API, just through functions. <br/>
And the *app.py* it´s where is defined the requests and the authorization method using classes.

## URL
If you want to see the API without running locally, access the link bellow:
```url
https://api-programming-languages.herokuapp.com/
```
All the *Endpoints* it's described on the section **Endpoints**.  

## Requirements

First of all, to a better usage, create a virtual environment and then install the requirements.

```bash
pip install -r requirements.txt
```

## Database
To create the database that will serve to keep the information you must run the following command:
```bash
python .\models.py
```
And you will have on your folder a file with name *programming-languages.db* with three tables, **programminglanguages**, **related** and **users**.
You can use [SQLiteStudio](https://sqlitestudio.pl/) to a better view of the tables.

## Authorization
Some of the request methods needs an authorization, and the table *users* it´s the responsible for it, but first, you need to populate it.<br/>
In the *utils.py* you will get a method called *insertUser*, use it to insert a login and password.
<img src="/prints/insertUser.jpg"
     alt="insertUsers"
     style="float: left; margin-right: 10px;" 
/>

If you not be authorized you will receive a response code *401: Unauthorized*

## Run the Project
So you have created the tables and the authorization user, now to run and test the API you just need to run the following command:
```bash
python .\app.py
```
When 
<hr>

## Endpoints
#### Insert a new Programming Language

| Method        | URL                        | Content-Type      | 
| ------------- |:--------------------------:| -----------------:|
| POST          | /postProgrammingLanguage/  | application/json  |
##### Body JSON
```json
{
     "name": "Python"
}
```
##### Success Response
```json
{
     "id"    : 0,
     "name"  : "python"
}
```
##### Note
All data is stored in lower case.
<hr>

#### Get a Programming Language
| Method        | URL                             | Content-Type      | 
| ------------- |:-------------------------------:| -----------------:|
| GET           | /programmingLanguage/           | application/json  |

##### Body JSON
```json
{
     "name"  : "python"
}
```

##### Success Response
```json
{
     "id"    : 0,
     "name"  : "python"
}
```
<hr>

#### Get All Programming Languages
| Method        | URL                              | URL Params        | 
| ------------- |:--------------------------------:| -----------------:|
| GET           | /programmingLanguages/           | None.             |

##### Success Response
```json
[
  {
    "id": 4,
    "name": "c#"
  },
  {
    "id": 1,
    "name": "java"
  },
  {
    "id": 2,
    "name": "php"
  },
  {
    "id": 3,
    "name": "python"
  },
  {
    "id": 5,
    "name": "ruby"
  }
]
```
##### Note
The *JSON* returned is ordered by alphabetical order of the programming languages names.
<hr>

#### Get a Programming Language by initial letter
| Method        | URL                                            | Content-Type      | 
| ------------- |:----------------------------------------------:| -----------------:|
| GET           | /programmingLanguageByInitialLetter/           | application/json  |

##### Body JSON
```json
{
  "initial": "p"
}
```

##### Success Response
```json
[
  {
    "name": "php"
  },
  {
    "name": "python"
  }
]
```
<hr>

#### Update a Programming Language Name
| Method        | URL                                            | Content-Type      |
| ------------- |:----------------------------------------------:| -----------------:|
| PUT           | /modifyProgrammingLanguage/                    | application/json  |

##### Example
```Body JSON
{
  "language": "c#",
  "name": "csharp"
}
```
##### Success Response
```json
{
  "id": 4,
  "name": "csharp"
}
```
<hr>

#### Delete a Programming Language Name
| Method        | URL                                            | Content-Type      |
| ------------- |:----------------------------------------------:| -----------------:|
| PUT           | /modifyProgrammingLanguage/                    | application/json  |

##### Example
```Body JSON
{
  "name": "csharp"
}
```
##### Success Response
```json
{
  "status": "sucess",
  "message": "Programming language 'csharp' has been deleted.",
  "id": 1
}
```
<hr>

#### Insert a Related
| Method        | URL                            | Content-Type      |
| ------------- |:------------------------------:| -----------------:|
| POST          | /relatedProgrammingLanguage/   | application/json  |

##### Body JSON
```json
{
  "related" : "spring mvc",
  "language": "java"
}
```
##### Success Response
```json
{
  "id": 0,
  "name": "spring mvc",
  "language": "java"
}
```
<hr>

#### Get a Related
| Method        | URL                            | Content-Type      |
| ------------- |:------------------------------:| -----------------:|
| GET           | /relatedProgrammingLanguage/   | application/json  |

##### Body JSON
```json
{
  "related" : "spring mvc",
}
```
##### Success Response
```json
{
  "name": "spring mvc",
  "language": "java"
}
```
<hr>

#### Get all Relateds
| Method        | URL                            | URL Params     |
| ------------- |:------------------------------:| --------------:|
| GET           | /relatedProgrammingLanguages/  | None           |
##### Success Response
```json
[
  {
    "id": 1,
    "name": "spring rest",
    "language": "java"
  },
  {
    "id": 5,
    "name": "spring mvc",
    "language": "java"
  },
  {
    "id": 2,
    "name": "laravel",
    "language": "php"
  },
  {
    "id": 3,
    "name": "flask",
    "language": "python"
  },
  {
    "id": 4,
    "name": "ruby on rails",
    "language": "ruby"
  }
]
```
##### Note
The *JSON* returned is ordered by the language names.
<hr>

#### Get a Related by Initial Letter
| Method        | URL                                              | Content-Type     |
| ------------- |:------------------------------------------------:| ----------------:|
| GET           | /getRelatedProgrammingLanguageByInitialLetter/   | application/json |
##### Body JSON
```json
{
  "initial": "s"
}
```
##### Success Response
```json
[
  {
    "name": "spring rest",
    "language": "java"
  },
  {
    "name": "spring mvc",
    "language": "java"
  }
]
```
<hr>

#### Get a Related by Programming Language Name
| Method        | URL                                 | Content-Type     |
| ------------- |:-----------------------------------:| ----------------:|
| GET           | /getRelatedByProgrammingLanguage/   | application/json |
##### Body JSON
```json
{
  "language": "java"
}
```
##### Success Response
```json
[
  {
    "name": "spring rest",
    "language": "java"
  },
  {
    "name": "spring mvc",
    "language": "java"
  }
]
```
<hr>

#### Update a Related
| Method        | URL                                 | Content-Type     |
| ------------- |:-----------------------------------:| ----------------:|
| PUT           | /modifyRelatedProgrammingLanguage/  | application/json |
##### Body JSON
```json
{
  "related" : "spring_rest",
  "name"    : "spring rest"
}
```
##### Success Response
```json
{
  "id": 1,
  "related": "spring rest",
  "language": "java"
}
```
<hr>

#### Delete a Related
| Method        | URL                                 | Content-Type     |
| ------------- |:-----------------------------------:| ----------------:|
| DELETE        | /modifyRelatedProgrammingLanguage/  | application/json |
##### Body JSON
```json
{
  "related" : "spring mvc"
}
```
##### Success Response
```json
{
  "status": "sucess",
  "message": "Programming language 'spring mvc' has been deleted.",
  "id": 1
}
```
<hr>

## Responses
There two kinds of responses, those with params and those without params. <br/>
First, the responses with text params.
| ID | Status    | Message                                                       |
| -- |:---------:| -------------------------------------------------------------:|
| 0  | error     | There is no programming language registered with name '{}'.   |
| 1  | success   | Programming language '{}' has been deleted.                   |
| 2  | error     | The programming language '{}' already exists.                 |
| 3  | error     | There is no '{}' as related with any programming language.    |
| 4  | error     | There is no programming language registered with id '{}'.     |
| 5  | error     | The data '{}' must be a string.                               |
| 6  | error     | The data related '{}' already exists.                         |
| 7  | error     | There is no programming language with initial letter as '{}'. |
| 8  | error     | There is no related with initial letter as '{}'.              |
| 9  | success   | The related '{}' has been deleted                             |

Now, the responses without text params.
| ID | Status    | Message                                     |
| -- |:---------:| -------------------------------------------:|
| 0  | error     | There is no column 'name' in body json.     |
| 1  | error     | There is no column 'language' in body json. |
| 2  | error     | There is no column 'related' in body json.  |
| 3  | error     | There is no column 'initial' in body json.  |

## Notes
Feel free to open a *Pull Request* and comment about the project itself.
