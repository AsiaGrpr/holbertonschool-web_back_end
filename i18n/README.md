<div align="center">

# i18n

![image](../asset/i18n.jpeg)

</div>

## Resources

Read or watch:

- [Flask-Babel](https://python-babel.github.io/flask-babel/)
- [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
- [pytz](https://sourceforge.net/directory/software-development/mac/)
- [Flask-Script](https://pythonhosted.org/Flask-Script/)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, ***without the help of Google***:

### General

  - Learn how to parametrize Flask templates to display different languages
  - Learn how to infer the correct locale based on URL parameters, user settings or request headers
  - Learn how to localize timestamps

## Requirements

### General

  - All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
  - All your files should end with a new line
  - A `README.md` file, at the root of the folder of the project, is mandatory
  Your code should use the pycodestyle style (version 2.5)
  - The first line of all your files should be exactly `#!/usr/bin/env python3`
  - All your `*.py` files should be executable
  - All your modules should have a documentation (p`ython3 -c 'print(__import__("my_module").__doc__)'`)
  - All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
  - All your functions and methods should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and` python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
  - A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
  - All your functions and coroutines must be type-annotated.

## Tasks

### 0. Basic Flask app
First you will setup a basic Flask app in `0-app.py`. Create a single / route and an i`ndex.html` template that simply outputs “Welcome to Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).

### 1. Basic Babel setup
Install the Babel Flask extension:
```bash
$ pip3 install flask_babel
```
Then instantiate the `Babel` object in your app. Store it in a module-level variable named `babel`.

In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.

Use `Config` to set Babel’s default locale (`"en"`) and timezone (`"UTC"`).

Use that class as config for your Flask app.

### 2. Get locale from request
Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.

### 3. Parametrize templates
Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.

Create a `babel.cfg` file containing
```
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```
Then initialize your translations with
```bash
$ pybabel extract -F babel.cfg -o messages.pot .
```
and your two dictionaries with
```bash
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```
Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Use the following translations:

| msgid	| English | French |
|:---:|:---:|:---:|
| home_title | "Welcome to Holberton" | "Bienvenue chez Holberton" |
| home_header | "Hello world" | "Bonjour monde" |

Then compile your dictionaries with
```bash
$ pybabel compile -d translations
```
Reload the home page of your app and make sure that the correct messages show up.