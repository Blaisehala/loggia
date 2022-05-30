# L O G G I A 

#### Author 

[Blaise Hala](https://github.com/Blaisehala)

## Description

Loggia is a photo gallery web application showcasing picture collections. 

- Users get can view photos uploaded by admin. 
- Users can see photos based on the location, by clicking on the listed locations in the menu. 
- They can also copy the link to a photo to paste at their discretion. 
- And finally also search for photos based on the categories.


## Pre-requisites 
The Loggia project requires a prerequisite understanding of the following:
- Django Framework
- Python Nirtual environment
- Python3.8
- Postgres Database


## Setup and installation

#### Clone the Repo
####  Activate virtual environment
Activate virtual environment using python3.8 as default handler
    `virtualenv -p /usr/bin/python3.8 venv && source venv/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE gallery;
####  .env file
Create .env file and paste paste the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DBNAME = 'gallery'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
#### Run initial Migration
    python3.8 manage.py makemigrations gallery
    python3.8 manage.py migrate

#### Run the app
    python3.8 manage.py runserver
    Open terminal on localhost:8000

#### Deployment 



## Support and contact details 

To make a contribution to the code used or any suggestions you can click on the contact link and email me your suggestions.

- Email: blaisehala@gmail.com 


## Licence

MIT License

Copyright (c) [2021] [Blaise Hala Odhiambo]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, but not to sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:


The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Authors Contact
TEL : +254714775125 Email: blaisehala@gmail.com


##### Authors Info 

LinkedIn- [Blaise Hala](https://www.linkedin.com/in/blaise-hala-682aa511a/)

Github - [Blaisehala](https://github.com/Blaisehala)
