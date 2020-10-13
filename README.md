# Programming Languages REST API

![Build Status](https://img.shields.io/badge/Python-3.7.3-yellowgreen) ![Build Status](https://img.shields.io/badge/pip-20.2.3-orange) ![Build Status](https://img.shields.io/badge/flask-1.1.2-green) ![Build Status](https://img.shields.io/badge/flask--RESTful-0.3.8-blue) ![Build Status](https://img.shields.io/badge/flask--HTTPAuth-4.1.0-red) ![Build Status](https://img.shields.io/badge/SQLAlchemy-1.3.19-yellow) ![Build Status](https://img.shields.io/badge/build-success-success)

A REST API made with Flask, Flask-RESTful, Flask-HTTPAuth and SQLAlchemy to get information about Programming Languages names and relateds names. <br/>
A related name is a framework or something related to a programming language, like Flutter is to Dart and Laravel is to PHP.

## Requirements

First of all, to a better usage, create a virtual environment and then install the requirements.

```bash
pip install -r requirements.txt
```

## Database
To create the database that will serve to keep the information you must run the following command:
```bash
python models.py
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
<hr>

## Requests
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

