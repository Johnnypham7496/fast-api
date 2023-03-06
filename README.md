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

-   `C post` - create a record <br> 
-   `R get`- retrieve a record <br>
-   `U put` - modify/update record <br>
-   `D delete` - deletes a record <br>
<hr>


<h2>Databases</h2>

- `Postgres Tutorial`: https://www.postgresqltutorial.com/

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

- This is another way to interact with database but instead of using raw SQL code, we can use python language itself that will translate to SQL. FastAPI <---> ORM <---> SQL<br>

- The most popular python ORMs is `Sqlalchemy`. It is a standalone library and has no association with FastAPI. It can be used with any python web frameworks or any python based application

- `pip install sqlalchemy` to download sqlalchemy. I am currently using version 1.4.46
   - Sqlalchemy does not know how to communicate to a database so you will need a database driver. We've already been using postgres database and had psycopg2 installed but as for refrence if you are installing Sqlalchemy first, you will need a database driver so that Sqlalchemy can communicate with the database

- Here is also the link to help setup Sqlalchemy: https://fastapi.tiangolo.com/tutorial/sql-databases/

- Sqlalchemy and Pydantic work together to help manage schemas and database. Here is a link to understand the difference between pydantic and sqlalchemy: https://www.youtube.com/watch?v=Yn174prreT8&ab_channel=SanjeevThiyagarajan
<hr>

<h2>JWT Tokens</h2>

- A `JWT Token` is something the API gives to the user once they login with their credentials. <strong><em>A Token is not the same as an encryption</em></strong><br>
- A JWT Token consists of 3 parts: 
    - Header: Algorithum and token type/metadata about the token

    - Payload: data entered by the user, most common things to be embed in the payload is id, username, or role. Best to keep this simple otherwise the more information that is is the payload, the bigger the packet. <strong><em>Still keep in mind that this is not an encryption so having passwords, secrets, or orther private information is not recommened</em></strong>

    - Verify Signature: this is considered a secret meaning that there is a special password that is kept on API. This is something that the user would not know and it is the most important piece of this token meaning it should never be released to public view. This is another form of validation ensuring that no one is able to change/tamper the token data. 
<hr>

<h2>Environment Variable</h2>

- Is a varible that is configured on a computer. Some of the things on this code has been hard coded such as our sql connection that has our login information or our JWT token with containing the secret key. These should never be hard coded because once our code is push into github/gitlab, it will be visible to the public which can cause a potenial hack if someone reviews our code. 

- Depneding on the project, you could have multiple `Env variables` and the most common case that can happen is forgetting to add a env variable. The best way to cover this is to create a validation method to check and make sure all the properties is there otherwise the application may crash. 

- You can add `env variables` onto your local machine but it is a large amount of work to preform and it's not the most optimal way to create and store them
<hr>

<h2>Database Migrations</h2>

- `Alembic Documentation`: https://alembic.sqlalchemy.org/en/latest/tutorial.html

- Developers can track changes to code and rollback code easily with GIT. Why can't we do the same for database models/tables?

- Database Migrations will allow us to incrementally track changes to database schema and rollback chagnes to any point in time

- We will use a tool called `Alembic` to make cahnges to our database
 
- `Alembic` can also automatically pull database models from Sqlalchemy and generate the proper tables
<hr>

<h2>CORS</h2>

-   Cross Origin Resouce Sharing`(CORS)` allows you to make requests from the web browser on one domain to a server on a different domain

- By default our API will only allow webbrowsers running on the same domain as our server to make requests to it
<hr>

<h2>Git</h2>

- `Git tutorial`: https://git-scm.com/docs/gittutorial

- Git is a distributed version control system that tracks changes in any set of computer files, usually used for coordinating work among programmers collaboratively developing source code during software development. Its goals include speed, data integrity, and support for distributed, non-linear workflows

- The most important part of Git is to have a `.gitignore`. There are files and folders that we <strong>DO NOT</strong> want to check into git because this will be in public view. It is <strong>CRUCIAL</strong> that everything is added to .gitignore before commiting otherwise it will be very difficult to remove from github/gitlab

- It is standard to never include the virtual environment when checking into git. Instead it is best practice to use a `requirements.txt`. This file will show the user a list of dependencies and versions that was being used when creating this repository/project. 
<hr>

<h2>Heroku</h2>

- `Herkou Tutorial`: https://devcenter.heroku.com/articles/getting-started-with-python

- `Connecting Heroku to Postgres`: https://devcenter.heroku.com/categories/heroku-postgres

- For this project I am using Heroku to deploy the application so that anyone get access the API created here. Keep in mind that Heroku at the end of 2022 stop hosting apps for free as goes the same for other hosting services. You will need to at a credit card for verification purposes. The apps that are being deployed will be free up to a certain point. After that charges may apply. 

- https://devcenter.heroku.com/articles/getting-started-with-python - By following this link, the instructions will show you how to setup Heroku for python. There are also different instructions for different languages. 

- For the apps to run successfully in Heroku, you will need to push all changes to github/gitlab and create the request to push changes into the main branch. Once that process is complete, type `git push heroku main` into the terminal to have those changes push into Heroku. 

- Part of having the app to run on Heroku is to have a `Procfile` which is a file that will tell our host platform the commands that will run out app. When deploying apps, there needs to be a file with instructions to tell the platform the commands it needs to run our app

- Remember that when psuhing commit to git you will have to push to heroku as well after git. To add tables to the database(this implies if you are using alembic) you will need to run the following command into the termainal: `heroku run alembic upgrade head` 
    - Notice how alembic upgrade head is the same as when we were making updates to the local database but now you will need to let heroku know to run this code
<hr>

<h2>Ubuntu Server</h2>

- There is a section of the video of where Sanjeev explains how to deploy our app with Ubuntu Server which is `Linux` based. I did not spend too much time during this part but a lot of the configuration will come from the termainal. This is an alternative way of deployment beisdes using Heroku.
<hr>

<h2>Docker</h2>

- Docker documentation for python: https://hub.docker.com/_/python

- Another common platform that people use is `Docker`

- Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker’s methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production.
<hr>

<h2>Testing</h2>

- `Pytest documentation`: https://docs.pytest.org/en/7.2.x/

- Who better to test the code than the person who wrote the code?

- Currently using `pytest` to write and create fixtures for testing. `Pytest fixtures` are functions that can be used to manage our apps states and dependencies. Most importantly, they can provide data for testing and a wide range of value types when explicitly called by our testing software. You can use the mock data that fixtures create across multiple tests

- Fixtures can be configured to be dependant on another fixture "passing a fixture as an aruguement into another"

- DevOps Testing is the process of automating and smoothing out the entire delivery lifecycle of software. A lot of companies employ DevOps testing strategies by starting with the agile practice of Continuous Integration (CI)

- Start by adding `pip install pytest`. By entering `pytest` into the terminal, this will run any test functions that you have created. I created a separate folder that holds all of the test files and created routes that will test our code in files within the app directory. 

- Use `pytest -v -s` to give you more details from every test that is being conducted. Without running `-v -s` will give you green periods for passing and red periods for failing which is a more simply way of looking at the results it prefered.

- When conducting multiple tests, you can either run them all and check for which ones have failed or you can add `-x` to `pytest -v -s` to have the testing stop as soon as a test fails.

- When creating test for your code, there are some cases where you would need to add testing data to a database but never to the active database. Instead you would want to create a test database that will delete the data after testing is over. 

- For certain tests, the last slash "/users/" will matter. FastAPI can reroute the request to a test database but will give off a differnt status code causing the test to fail if the code requires a result of status code

- Fixtures have different `scopes`
    - Example on how to user scopes: `@pytest.fixture(scope="function")`
    - `function`: the default scope, the fixture is destroyed at the end of the test
    - `class`: the fixture is destroyed during teardown of the last test in the class
    - `module`: the fixture is destroyed during the teardown of the last test in the module
    - `package`: the fixture is destroyed during teardown of the last test in the package
    - `session`: the fixture is destroyed at the end of the test session

- Fixtures can rely on other fixtures but tests should not rely on other tests which is considered as bad practice

- Creating a conftest within the test folder will allow pytest to define fixtures and give access to all test file with in the folder but conftest is specific to the directory so you have multiple test folders than you would need separate conftests file within those folders
<hr>

<h2>CI/CD</h2>

- `Continuous Integration` - automated process to build, package and test applications

- `Continuous Delivery` - picks up where continuous integrations ends and automated the delivery of applications

- Manual Process: Make Changes -> Commit Changes -> Run Tests -> Build Image -> Deploy
- Automated CI/CD: Makes Changes -> Commit Changes ->
    Continuous Integration: Pull Source Code -> Install Dependencies -> Run Automated Tests -> Build Images(Docker)
    Continuous Delivery: Grab images/code -> Update Production

- Most common CI/CD pipeline: Jenkins, Travis CI, Circle CI, Github Actions