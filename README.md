# Fast-API
<h1>Creating API using FastApi framework</h1>

For a full step by step tutorial visit: https://www.youtube.com/watch?v=0sOvCWFmrtA&t=2315s&ab_channel=freeCodeCamp.org

FastAPI documentation: https://fastapi.tiangolo.com/ 

<h2>Getting Started</h2>

1. Create repository with `.gitignore and license`

2. Create a virtual environment with `py -3 -m venv venv`

3. Turn on virtual environment with `. venv/Scripts/activate`

4. Install fastapi with `pip install fastapi[all]` 
- [all] this will install all dependencies related to fastapi
- when installing dependencies, make sure the virtual environment is on by checking ther terminal and looking for (venv) or the name that has been given for the virtual environment 
<hr>

`Postman` is a good tool to be able to test the environments of the api for the HTTP requests 

`What is a api?` - a way to automate request, how a computer communicates to another when requesting data, only a way to see and get data but not change it otherwise this will corrupt the code or cause data breaches

`What is a virtual environment?` - an area that yo can code freely without having the installed packages affect your computer. Ensuring that the code you have built with the packages/dependicies will run on someone elses computer just like it did with your own. 

`Why install Flask?` - flask is a premade package that someone else has already made to help make creating the API process faster otherwise you would write the code from scratch which is time consuming. <hr>


<h2>4 major calls in api/HTTP method called CRUD:</h2>

-    `C post` - create a record <br> 
-   `R get`- retrieve a record <br>
-   `U put` - modify/update record <br>
-   `D delete` - deletes a record <br>
<hr>


<h2>Databases</h2>

- Databases is collection of organized data that can easily be accessed and managed <br>
Normally the will be a database management system aka <strong>DBMS</strong> that a user will send requests to, then DBMS will preform the operation to the database and send the result back to the user so technically a user will never directly work with the database <br><br>

Most commonly used language to communicate with DBMS is Structured Query Language aka <strong>SQL</strong><br>

`PostgreSQL`, also known as <strong>Postgres</strong>, is a free and open-source relational database management system emphasizing extensibility and SQL compliance.<br>

- Download the latest version of Postgres from: https://www.postgresql.org

- `pgadmin` will be the Graphical User Interface aka <strong>GUI</strong> tool that you use to manage your database

- Databases holds data like a table and they have datatypes just like a normal programming language

- Each row in the table will have a primary key to identify the data that is listed in the row. Keep in mind that you cannot have duplicate keys. These keys can be numbers, emails, phone numbers, username, etc. To make sure that the user complies, multiple conditions/constraint can be preformed to make sure that the keys are unique.

- Install <strong>PSYCOPG</strong> by typing <strong><em>pip install "psycopg2"</em></strong> into the terminal<br>
    - Note that I am using psycopg2 version 2.9.5 for this api
    - Installing psycopg will help connect your code to the SQL server<br>
<hr>

<h2>Object Relational Mapper(ORM)</h2>

- This is another way to interact with database but instead of using raw SQL code, we can use python languae itself that will translate to SQL. FastAPI <---> ORM <---> SQL<br>

- The most popular python ORMs is `Sqlalchemy`. It is a standalone library and has no association with FastAPI. It can be user with any other pthin web frameworks or any python based application

- `pip install sqlalchemy` to download sqlalchemy. I am currently using version 1.4.46
   - Sqlalchemy does not know how to communicate to a database so you will need a database driver. We've already been using postgres database and had psycopg2 installed but as for refrence if you are installing Sqlalchemy first, you will need a database driver so that Sqlalchemy can communicate with the database

- Here is also the link to help setup Sqlalchemy: https://fastapi.tiangolo.com/tutorial/sql-databases/

- Sqlalchemy and Pydantic work together to help manage schemas and database. Here is a link to understand the difference between pydantic and sqlalchemy: https://www.youtube.com/watch?v=Yn174prreT8&ab_channel=SanjeevThiyagarajan
<hr>

<h2>JWT Tokens</h2>

- A JWT Token is something the API gives to the user once they login with their credentials. <strong><em>A Token is not the same as an encryption</em></strong><br>
- A JWT Token consists of 3 parts: 
    - Header: Algorithum and token type/metadata about the token

    - Payload: data entered by the user, most common things to be embed in the payload is id, username, or role. Best to keep this simple otherwise the more information that is is the payload, the bigger the packet. <strong><em>Still keep in mind that this is not an encryption so having passwords, secrets, or orther private information is not recommened</em></strong>

    - Verify Signature: this is considered a secret meaning that there is a special password that is kept on API. This is something that the user would not know and it is the most important piece of this token meaning it should never be released to public view. This is another form of validation ensuring that no one is able to change/tamper the token data. 
<hr>

<h2>Environment Variable</h2>

- Is a varible that is configured on a computer. Some of the things on this code has been hard coded such as our sql connection that has our login information or our JWT token with containing the secret key. These should never be hard coded because once our code is push into github/gitlab, it will be visible to the public which can cause a potenial hack if someone reviews our code. 

- Depneding on the project, you could have multiple Env variables and the most common case that can happen is forgetting to add a env variable. The best way to cover this is to create a validation method to check and make sure all the properties is there otherwise the application may crash. 

- You can add the env variables onto your local machine but it is a large amount of work to preform and it's not the most optimal way to create and store them
<hr>

<h2>Database Migrations</h2>

- Developers can track changes to code and rollback code easily with GIT. Why can't we do the same for database models/tables?

- Database Migrations will allow us to incrementally track changes to database schema and rollback chagnes to any point in time

- We will use a tool called Alembic to make cahnges to our database
 
- Alembic can also automatically pull database models from Sqlalchemy and generate the proper tables