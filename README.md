<div align="center">

# Holberton web back end

</div>

---

In this repository, there be saved different projects and exercises made during the second year of fullstack training with Holbertonschool.

---

<div align="center">

**[Caching](README.md#caching) - [Personal data](README.md#personal-data) - [Basic authentication](README.md#basic-authentication) - [Session authentication](README.md#session-authentication) - [Unittests and integration tests](README.md#unittests-and-integration-tests) - [i18n](README.md#i18n)**

---

![Back end dev](./asset/back%20end.jpeg)

</div>

---

## Caching

The objective of this project is to implement different caching algorithms and gain an understanding of how caching systems work. Caching involves storing copies of frequently accessed data in a faster but smaller memory space to improve access times.

### Tasks

0. Basic dictionary
1. FIFO caching
2. LIFO Caching
3. LRU Caching
4. MRU Caching

## Personal data

This project aims to implement secure practices for managing personal data, particularly Personally Identifiable Information (PII). The objectives are to understand PII, apply log filtering to obfuscate PII fields, securely encrypt passwords, and authenticate to a database using environment variables.

### Tasks

0. Regex-ing
1. Log formatter
2. Create logger
3. Connect to secure database
4. Read and filter data
5. Encrypting passwords
6. Check valid password

## Basic authentication

This project seeks to give practical experience in comprehending and implementing Basic Authentication in a straightforward API.

### Tasks

0. Simple-basic-API
1. Error handler: Unauthorized
2. Error handler: Forbidden
3. Auth class
4. Define which routes don't need authentication
5. Request validation!
6. Basic auth
7. Basic - Base64 part
8. Basic - Base64 decode
9. Basic - User credentials
10. Basic - User object
11. Basic - Overload current_user - and BOOM!

## Session authentication

This project is designed to offer practical experience in implementing Session Authentication, a widely-used method for authenticating users in web applications. Instead of utilizing established modules or frameworks like Flask-HTTPAuth, the focus is on grasping the underlying principles and processes involved in Session Authentication by constructing it from zero.

### Tasks

0. Et moi et moi et moi!
1. Empty session
2. Create a session
3. User ID for Session ID
4. Session cookie
5. Before request
6. Use Session ID for identifying a User
7. New view for Session Authentication
8. Logout

## User authentication service

In this project, you will create a user authentication service using Flask, focusing on cookie handling, form data retrieval, API routes, and HTTP status codes. While it is advisable to use established modules or frameworks for authentication (such as Flask-User) in real-world applications, this project is intended for educational purposes. By building a custom authentication system from scratch, you will gain a step-by-step understanding of the underlying mechanisms.

### Tasks

0. User model
1. create user
2. Find user
3. update user
4. Hash password
5. Register user
6. Basic Flask app
7. Register user
8. Credentials validation
9. Generate UUIDs
10. Get session ID
11. Log in
12. Find user by session ID
13. Destroy session
14. Log out
15. User profile
16. Generate reset password token
17. Get reset password token
18. Update password
19. Update password end-point


## Unittests and integration tests

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests with

`$ python -m unittest path/to/test_file.py`

### Tasks

0. Parameterize a unit test
1. Parameterize a unit test
2. Mock HTTP calls
3. Parameterize and patch
4. Parameterize and patch as decorators
5. Mocking a property
6. More patching
7. Parameterize
8. Integration test: fixtures

## i18n

This project will integrate internationalization capabilities (i18n) into a Flask web application. The main objectives are to configure Flask templates for displaying multilingual content, to identify the correct localization based on URL parameters, user parameters or query headers, and to adjust timestamps according to the localized context.

### Tasks

0. Basic Flask app
1. Basic Babel setup
2. Get locale from request
3. Parametrize templates
4. Force locale with URL parameter
5. Mock logging in
6. Use user locale
7. Infer appropriate time zone
