# API

---
API documentation for

- [/api/auth/login/](#post-apiauthlogin)
- [/api/auth/register/](#post-apiauthregister)
- [/api/auth/refresh/](#post-apiauthrefresh)
- [/api/auth/verify/](#post-apiauthverify)


- [/api/account/](#post-apitoken)
- [/api/account/notes/](#post-apitoken)

---

- [/api/users/](#post-apitoken) ----------------- DEBUG
- [/api/users/(user_id)](#post-apitoken) ----- DEBUG
- [/api/notes/](#post-apitoken) ----------------- DEBUG
- [/api/notes/(note_id)](#post-apitoken) ----- DEBUG

###### NOTE: DEBUG can be accessed only by users who have is_staff == TRUE (for development purposes)

###### CREATE STAFF-USER BY POST: /api/users/ A USER DATA WITH is_staff: true (for development purposes)

# JSON WEB TOKEN AUTHORIZATION

---

JWT is a universal cross-platform authorization technique.

It is used in **anynote** server authentication system.

It allows users to be authenticated without a use of sessions or another ip-driven auth.

POST: /api/auth/login/
---
**Request Body:**

```json
{
  "username": "<username>",
  "password": "<user's password>"
}
```

Send user's username and password to get the JWT. The JWT is responsible for authorization.
Server will know what user sends requests only by the token.

In order to work with the API you must firstly authorize and get your token.
Then set your Request **Authorization** **header** to this: **Authorization: Bearer** _access_token_you_got_

_(terminal example using **curl**)_

```shell
curl --location --request POST 'http://localhost:8000/api/some_api_endpoint/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyMjY0NjA0LCJpYXQiOjE3MjIyNjEwMDQsImp0aSI6IjkyNWUzY2FkMDAyOTQxZjI5OTQ5ZDQ5M2EzODRmOTNlIiwidXNlcl9pZCI6MX0.kJ8AeSSLKExmFUokIgC2NvQUKylM0xEaDXtostGmJv0' \
--header 'Content-Type: application/json' \
# other data of your request 
# for example this is data you send to get your JW token
--data '{
    "username": "testUser",
    "password": "testPassword"
}
```

**Answer Body (valid account data):**

```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

**Answer Body (invalid account data):**

```json
{
  "detail": "No active account found with the given credentials"
}
```

# _access_ token

Authorization header token. It allows server to identify, who is the request sender.

Must be provided in every user request to API

###### (except for the POST: api/token/, because it is a endpoint to acquire the token).

**Has lifetime** _(currently 1 hour)_

Answer body if access token is not valid:

```shell
{
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is invalid or expired"
        }
    ]
}
```

# _refresh_ token

Token for getting a new access token, instead of your expired one.

**POST: /api/auth/register/**
---
**Request Body:**

```json
{
  "username": "<username>",
  "password": "<password>",
  ...
}
```

###### Additional data besides username and password for now are not needed. Further in the development it will be required

**Answer Body:**

```json
{
  "id": 26,
  "last_login": null,
  "date_joined": "2024-07-30T13:37:13.466766Z",
  "is_superuser": false,
  "username": "test9",
  "first_name": "",
  "last_name": "",
  "email": "",
  "is_staff": false,
  "is_active": true,
  "groups": [],
  "user_permissions": []
}
```

---

```css
IMPORTANT NOTE!
```

This endpoint _**does not require Authorization header**_. DO NOT provide Authorization header

**Answer Body IF EXPIRED ACCESS TOKEN PROVIDED:**

```json
{
  "detail": "Given token not valid for any token type",
  "code": "token_not_valid",
  "messages": [
    {
      "token_class": "AccessToken",
      "token_type": "access",
      "message": "Token is invalid or expired"
    }
  ]
}
```

---

**POST: /api/auth/refresh/**
---
**Request Body:**

```json
{
  "refresh": "<refresh_token>"
}
```

Send a refresh token to the server and receives a new acces token

**Answer Body (valid refresh token):**

```json
{
  "access": "<access_token>"
}
```

**Answer Body (invalid refresh token):**

```json
{
  "detail": "Token is invalid or expired",
  "code": "token_not_valid"
}
```

**POST: /api/auth/verify/**
---
**Request Body:**

```json
{
  "token": "<refresh_token>"
}
```

Send a token to get an information of it expirency

**Answer Body (expired token):**

```json
{
  "detail": "Token is invalid or expired",
  "code": "token_not_valid"
}
```

**Answer Body (valid token):**

```json
{}
``` 

# /api/auth/account/

## **GET: /api/auth/account/**

Send a token to get an information of it expirency

**Answer Body:**

```json
{
  "id": 26,
  "last_login": null,
  "date_joined": "2024-07-30T13:37:13.466766Z",
  "is_superuser": false,
  "username": "test9",
  "first_name": "",
  "last_name": "",
  "email": "",
  "is_staff": false,
  "is_active": true,
  "groups": [],
  "user_permissions": []
}
```

## PATCH: /api/auth/account/

Modify some data of the user

**Request Body**

```shell
{
  "username": "test9",
  "first_name": "",
  "last_name": "",
  "email": "",
  "is_staff": false,
}
```

```css
!!!WARNING!!!
```

Password change by PATCH request is not implemented yet. **DO NOT PATCH PASSWORD VALUE**

# /api/auth/account/notes

## GET: /api/auth/account/notes

Get all user's notes

**Answer Body:**

```json
[
  {
    "id": 5,
    "content": {},
    "hash": "test",
    "user": 26
  }
]
```


## POST: /api/auth/account/notes/

Create new note

**Request Body**

```json
{
  "content": {},
  "hash": "test"
}
```

**Answer Body**

```json
{
  "id": 5,
  "content": {},
  "hash": "test",
  "user": 26
}
```

## PATCH: /api/auth/account/notes/(note_id)

```css
!!!WARNING!!!
```
_**For now [HATEOAS](https://habr.com/ru/articles/483328/) is not implemented yet and you must set `note_id` in url**_

```json
{
  "id": 5,
  "content": {},
  "hash": "test",
  "user": 26
}
```





