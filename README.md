# API Advisor

```json
"baseURL": "https://rain-forecast-risk-alert.herokuapp.com/"
```
---
## Summary
- [Cities](#cities)
  - [All cities](#cities-all)
  - [Cities from state](#cities-from-state)
- [Forecast risk](#forecast-risk)
  - [Forecast risk request with missing keys](#forecast-risk-missing-keys)
  - [Forecast risk request with invalid keys](#forecast-risk-invalid-keys)
  - [Forecast risk request with invalid value types](#forecast-risk-invalid-types)
  - [Forecast risk request with invalid request type](#forecast-risk-invalid-request-type)
- [Messages](#messages)
  - [All messages](#messages-all)
- [Users](#users)
  - [Signup](#users-signup)
    - [Signup with duplicated email](#users-signup-duplicated-email)
    - [Signup with duplicated phone](#users-signup-duplicated-phone)
    - [Signup with missing keys](#users-signup-missing-keys)
    - [Signup with invalid keys](#users-signup-invalid-keys)
    - [Signup with invalid value types](#users-signup-invalid-types)
    - [Signup with invalid email format](#users-signup-invalid-email-format)
    - [Signup with invalid phone format](#users-signup-invalid-phone-format)
    - [Signup with invalid zip code format](#users-signup-invalid-zip-code-format)
    - [Signup with city out of coverage](#users-signup-city-out-of-coverage)
  - [Signin](#users-signin)
    - [Signin with invalid credentials](#users-signin-invalid-credentials)
    - [Signin with missing keys](#users-signin-missing-keys)
    - [Signin with invalid keys](#users-signin-invalid-keys)
    - [Signin with invalid value types](#users-signin-invalid-types)
- [Protected requests](#protected-requests)
  - [Users](#users-protected)
    - [Risk profile](#risk-profile)
      - [Risk profile without token](#risk-profile-without-token)
      - [Risk profile with invalid token](#risk-profile-invalid-token)
      - [Risk profile with user not found](#risk-profile-user-not-found)
      - [Risk profile with missing keys](#risk-profile-missing-keys)
      - [Risk profile with invalid keys](#risk-profile-invalid-keys)
      - [Risk profile with invalid value types](#risk-profile-invalid-types)
    - [Patch user info](#users-patch)
      - [Patch user without token](#users-patch-without-token)
      - [Patch user with invalid token](#users-patch-invalid-token)
      - [Patch a not found user](#users-patch-user-not-found)
      - [Patch user with invalid keys](#users-patch-invalid-keys)
      - [Patch user with invalid value types](#users-patch-invalid-value-types)
      - [Patch user with duplicated email](#users-patch-duplicated-email)
      - [Patch user with duplicated phone](#users-patch-duplicated-phone)
      - [Patch user with invalid zip code](#users-patch-invalid-zip-code)
      - [Patch user with city out of coverage](#users-patch-city-out-of-coverage)
      - [Patch user password](#users-patch-password)
        - [Patch user password without old password key](#users-patch-password-without-old-password)
        - [Patch user password without password key and with old password key](#users-patch-password-without-password-with-old-password)
    - [Delete user](#users-delete)
      - [Delete user without token](#users-delete-without-token)
      - [Delete user with invalid token](#users-delete-invalid-token)
      - [Delete a not found user](#users-delete-user-not-found)
---
## <center>**Cities** <a name="cities"></a></center>
---
### All cities <a name="cities-all"></a>
```
GET - /api/cities
```
Get all cities that our application currently cover.

Response:
```
HTTP/1.1: 200 - OK
```

```json
[
  {
    "state": "Bahia",
    "cities": [
      "Rio de Contas"
    ]
  },
  {
    "state": "Espírito Santo",
    "cities": [
      "Iconha",
      "Vitória"
    ]
  },
  {
    "state": "Minas Gerais",
    "cities": [
      "Coronel Fabriciano",
      "Ipatinga"
    ]
  },
  {
    "state": "Rio de Janeiro",
    "cities": [
      "Angra dos Reis",
      "Magé",
      "Nilópolis",
      "Niterói",
      "Nova Friburgo",
      "Petrópolis",
      "Rio de Janeiro"
    ]
  },
  {
    "state": "Santa Catarina",
    "cities": [
      "Jaraguá do Sul"
    ]
  },
  {
    "state": "São Paulo",
    "cities": [
      "Caraguatatuba",
      "São José do Rio Pardo",
      "São José dos Campos",
      "São Paulo"
    ]
  }
]
```
---
### Cities from state <a name="cities-from-state"></a>
```
GET - /api/cities/from-state/<state_name>
GET - /api/cities/from-state/<state_uf>
```
Get all cities from an specific state.  
The user can pass cities with any casing and with our withouth latin characters.  
**Example**: *sao paulo* evaluates to *São Paulo*.  
  
The requests below evaluate to the same response
```
GET EXAMPLE - /api/cities/from-state/São Paulo
GET EXAMPLE - /api/cities/from-state/sãO pAulO
GET EXAMPLE - /api/cities/from-state/SaO pAulO
GET EXAMPLE - /api/cities/from-state/sp
GET EXAMPLE - /api/cities/from-state/sP
```
Response:
```
HTTP/1.1: 200 - OK
```
```json
[
  {
    "state": "São Paulo",
    "cities": [
      "Caraguatatuba",
      "São José do Rio Pardo",
      "São José dos Campos",
      "São Paulo"
    ]
  }
]
```
---
## <center>**Forecast Risk** <a name="forecast-risk"></a></center>
---
```
POST - /api/forecast-risk
```

Send a list of cities, states and precipitation and returns a list of endangered cities along with a quantity of users in the cities. The precipitation values and which values correspond to a danger were defined in the code.

## Parameter  

**A list of these parameters:**
| **Field**     | **Type**         | **Description**                     |
| ------------- | ---------------- | ----------------------------------- |
| city          | string           | A city name                         |
| state         | string           | The city state                      |
| precipitation | integer or float | A precipitation integer value in mm |

**Body:**
```json
[
  {
    "city": "Petrópolis",
    "state": "Rio de Janeiro",
    "precipitation": 80
  },
  {
    "city": "São Paulo",
    "state": "São Paulo",
    "precipitation": 30
  }
]
```
Response:
```
HTTP/1.1: 200 - OK
```
```json
{
  "endangered_cities": [
    {
      "city": "Petrópolis",
      "state": "Rio de Janeiro",
      "users_warned": 2
    }
  ]
}
```
### Errors
<details>
<summary>Forecast risk request with missing keys</summary> <a name="forecast-risk-missing-keys"></a>

**Body:**
```json
[
  {
    "state": "Rio de Janeiro",
    "precipitation": 80
  },
  {
    "city": "São Paulo",
    "state": "São Paulo"
  }
]
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "missing keys",
  "expected_keys": ["city", "state", "precipitation"],
  "missing_keys": [
    {
      "request": {
        "state": "Rio de Janeiro",
        "precipitation": 80
      },
      "missing_keys": ["city"]
    },
    {
      "request": {
        "city": "São Paulo",
        "state": "São Paulo"
      },
      "missing_keys": ["precipitation"]
    }
  ]
}
```
</details>
<details>
<summary>Forecast risk request with invalid keys</summary> <a name="forecast-risk-invalid-keys"></a>

**Body:**

```json
[
  {
    "city": "Petrópolis",
    "state": "Rio de Janeiro",
    "precipitation": 80,
    "flood_risk": "high"
  },
  {
    "city": "São Paulo",
    "state": "São Paulo",
    "precipitation": 30
  }
]
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "invalid keys",
  "expected_keys": ["city", "state", "precipitation"],
  "invalid_keys": [
    {
      "request": {
        "city": "Petrópolis",
        "state": "Rio de Janeiro",
        "precipitation": 80,
        "flood_risk": "high"
      },
      "invalid_keys": ["flood_risk"]
    }
  ]
}
```
</details>
<details>
<summary>Forecast risk request with invalid value types</summary> <a name="forecast-risk-invalid-value-types"></a>

**Body:**

```json
[
  {
    "city": "Petrópolis",
    "state": "Rio de Janeiro",
    "precipitation": "high"
  },
  {
    "city": "São Paulo",
    "state": 23,
    "precipitation": { "mm": 80 }
  }
]
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "invalid type",
  "expected_type": {
    "city": "str",
    "state": "str",
    "precipitation": "int or float"
  },
  "received_type": [
    {
      "request": {
        "city": "Petrópolis",
        "state": "Rio de Janeiro",
        "precipitation": "high"
      },
      "invalid_types": {
        "precipitation": "str"
      }
    },
    {
      "request": {
        "city": "São Paulo",
        "state": 23,
        "precipitation": {
          "mm": 80
        }
      },
      "invalid_types": {
        "state": "int",
        "precipitation": "dict"
      }
    }
  ]
}
```
</details>
<details>
<summary>Forecast risk request with invalid request type</summary> <a name="forecast-risk-invalid-request-type"></a>

**Body:**

```json
{
  "city": "Petrópolis",
  "state": "Rio de Janeiro",
  "precipitation": 80
}
```

Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "invalid type",
  "expected_type": "type",
  "received_type": "dict"
}
```
</details>

---
## <center>**Messages** <a name="messages"></a></center>
---
### **All messages** <a name="messages-all"></a>
```
GET - /api/messages
```

Get a message log for all the messages our application has sended.

Success-Response:
```
HTTP/1.1: 200 OK
```
```json
[
  {
    "id": 1,
    "date": "Thu, 05 May 2022 18:11:52 GMT"
  },
  {
    "id": 2,
    "date": "Thu, 05 May 2022 18:11:52 GMT"
  },
  {
    "id": 3,
    "date": "Fri, 06 May 2022 11:54:38 GMT"
  }
]
```
---
## <center>**Users** <a name="users"></a></center>
---
### Signup <a name="users-signup"></a>
```
POST /api/users/signup
```
---
Register a new user.

## Parameter

| **Field** | **Type** | **Description**          |
| --------- | -------- | ------------------------ |
| name      | string   | User name                |
| email     | string   | User email               |
| phone     | string   | User phone number        |
| cep       | string   | User location cep number |
| password  | string   | User password            |

**Body:**

```json
{
	"name": "JOhN DOE",
	"email": "johndoe@mail.com",
	"phone": "(47) 9999-9999",
	"cep": "03478-070",
	"password": "1234"
}
```
Response:
```
HTTP/1.1: 201 - CREATED
```
```json
{
  "name": "John Doe",
  "email": "johndoe@mail.com",
  "phone": "(47) 9999-9999",
  "address": "03478-070",
  "city": "São Paulo",
  "state": "São Paulo"
}
```
### Errors
<details>
<summary>Signup with duplicated email</summary> <a name="users-signup-duplicated-email"></a>

**Body:**
```json
{
	"name": "JOhN Doe Jr",
	"email": "johndoe@mail.com",
	"phone": "(47) 88888-8888",
	"cep": "03478-070",
	"password": "1234"
}
```
Response:
```
HTTP/1.1: 409 - CONFLICT
```
```json
{
  "error": "unique email error"
}
```
</details>
<details>
<summary>Signup with duplicated phone</summary> <a name="users-signup-duplicated-phone"></a>

**Body:**
```json
{
	"name": "JOhN DOE jr",
	"email": "johndoejr@mail.com",
	"phone": "(47) 9999-9999",
	"cep": "03478-070",
	"password": "1234"
}
```
Response:
```
HTTP/1.1: 409 - CONFLICT
```
```json
{
  "error": "unique phone error"
}
```
</details>
<details>
<summary>Signup with missing keys</summary> <a name="users-signup-missing-keys"></a>

**Body:**
```json
{
	"name": "JOhN DOE",
	"email": "johndoe@mail.com",
	"phone": "(47) 9999-9999"
}
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "missing keys",
  "expected_keys": [
    "name",
    "phone",
    "email",
    "password",
    "cep"
  ],
  "missing_keys": [
    "password",
    "cep"
  ]
}
```
</details>
<details>
<summary>Signup with invalid keys</summary> <a name="users-signup-invalid-keys"></a>

**Body:**
```json
{
	"name": "JOhN DOE",
	"email": "johndoe@mail.com",
	"phone": "(47) 9999-9999",
	"cep": "03478-070",
	"password": "1234",
	"status": "fine"
}
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "invalid keys",
  "expected_keys": [
    "name",
    "phone",
    "email",
    "password",
    "cep"
  ],
  "invalid_keys": [
    "status"
  ]
}
```
</details>
<details>
<summary>Signup with invalid value types</summary> <a name="users-signup-invalid-types"></a>

**Body:**
```json
{
	"name": ["JOhN", "DOE"],
  "email": {"name":"johndoe", "domain": "mail.com"},
  "phone": 0099999999,
  "cep": 63478.070,
  "password": "1234"
}
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "invalid type",
  "expected_type": {
    "name": "str",
    "phone": "str",
    "email": "str",
    "password": "str",
    "cep": "str"
  },
  "received_type": {
    "name": "list",
    "email": "dict",
    "phone": "int",
    "cep": "float"
  }
}
```
</details>
<details>
<summary>Signup with invalid email format</summary> <a name="users-signup-invalid-email-format"></a>

**Body:**
```json
{
	"name": "JOhN DOE",
	"email": "johndoemailcom",
	"phone": "(00) 99999-9999",
	"cep": "03478-070",
	"password": "1234"
}
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "invalid email format",
  "expected_format": "name@email.com",
  "received_format": "johndoemailcom"
}
```
</details>
<details>
<summary>Signup with invalid phone format</summary> <a name="users-signup-invalid-phone-format"></a>

**Body:**
```json
{
	"name": "JOhN DOE",
	"email": "johndoe@mail.com",
	"phone": "00999999999",
	"cep": "00000-000",
	"password": "1234"
}
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "invalid phone format",
  "expected_format": "(xx) xxxxx-xxxx",
  "received_format": "00999999999"
}
```
</details>
<details>
<summary>Signup with invalid zip code format</summary> <a name="users-signup-invalid-zip-code-format"></a>

**Body:**
```json
{
	"name": "JOhN DOE",
	"email": "johndoe@mail.com",
	"phone": "(00) 99999-9999",
	"cep": "00000-000",
	"password": "1234"
}
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "zip code not found"
}
```
</details>
<details>
<summary>Signup with city out of coverage</summary> <a name="users-signup-city-out-of-coverage"></a>

**Body:**
```json
{
	"name": "JOhN DOE",
	"email": "johndoe@mail.com",
	"phone": "(00) 99999-9999",
  "cep": "06803-440",
  "password": "1234"
}
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "city out of coverage",
  "received_city": "Embu das Artes",
  "cities_coverage": [
    {
      "city": "Rio de Janeiro",
      "uf": "RJ"
    },
    {
      "city": "São Paulo",
      "uf": "SP"
    },
    {
      "city": "Petrópolis",
      "uf": "RJ"
    },
    {
      "city": "Rio de Contas",
      "uf": "BA"
    },
    {
      "city": "Nova Friburgo",
      "uf": "RJ"
    },
    {
      "city": "Iconha",
      "uf": "ES"
    },
    {
      "city": "Caraguatatuba",
      "uf": "SP"
    },
    {
      "city": "Angra dos Reis",
      "uf": "RJ"
    },
    {
      "city": "Coronel Fabriciano",
      "uf": "MG"
    },
    {
      "city": "Niterói",
      "uf": "RJ"
    },
    {
      "city": "Nilópolis",
      "uf": "RJ"
    },
    {
      "city": "Magé",
      "uf": "RJ"
    },
    {
      "city": "Jaraguá do Sul",
      "uf": "SC"
    },
    {
      "city": "Ipatinga",
      "uf": "MG"
    },
    {
      "city": "Vitória",
      "uf": "ES"
    },
    {
      "city": "São José do Rio Pardo",
      "uf": "SP"
    },
    {
      "city": "São José dos Campos",
      "uf": "SP"
    }
  ]
}
```
</details>

---
### Signin <a name="users-signin"></a>
```
POST /api/users/signin
```
---
Signin a user.

## Parameter

| **Field** | **Type** | **Description**          |
| --------- | -------- | ------------------------ |
| name      | string   | User name                |
| password  | string   | User password            |

**Body:**

```json
{
  "email": "johndoe@mail.com",
  "password": "1234"
}
```
Response:
```
HTTP/1.1: 200 - OK
```
```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1MTg1MTM1MywianRpIjoiNjZlOTc3NmMtOWIxNC00ODM2LWFhNzYtNWI1NTg4NTIyY2Q3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ODQ2LCJuYmYiOjE2NTE4NTEzNTMsImV4cCI6MTY1MTg1MjI1M30.0krUZf6hNRx8xsMz_S9330uRms0AYlPJQWv-k6l7XB4"
}
```
### Errors
<details>
<summary>Signin with invalid credentials</summary> <a name="users-signin-invalid-credentials"></a>

**Body:**
```json
{
  "email": "unexisting_email@kenzie.com",
  "password": "12345"
}
```
Response:
```
HTTP/1.1: 404 - NOT FOUND
```
```json
{
  "message": "Unauthorized"
}
```
</details>
<details>
<summary>Signin with missing keys</summary> <a name="users-signin-missing-keys"></a>

**Body:**
```json
{
  "email": "johndoe@mail.com"
}
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "missing keys",
  "expected_keys": [
    "email",
    "password"
  ],
  "missing_keys": [
    "password"
  ]
}
```
</details>
<details>
<summary>Signin with invalid keys</summary> <a name="users-signin-invalid-keys"></a>

**Body:**
```json
{
	"username": "johndoe",
  "email": "johndoe@mail.com",
  "password": "1234"
}
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "invalid keys",
  "expected_keys": [
    "email",
    "password"
  ],
  "invalid_keys": [
    "username"
  ]
}
```
</details>
<details>
<summary>Signin with invalid value types</summary> <a name="users-signin-invalid-types"></a>

**Body:**
```json
{
  "email": {"name":"johndoe", "domain" : "mail.com"},
  "password": 12345
}
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "invalid type",
  "expected_type": {
    "email": "str",
    "password": "str"
  },
  "received_type": {
    "email": "dict",
    "password": "int"
  }
}
```
</details>

---
## <center>**Protected requests** <a name="protected-requests"></a></center>
---

The following requests needs a **bearer token** at the authorization header.  

```json
headers: {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1MDgyNzQ4MywianRpIjoiYzE1Y2M4MjktYmU2Ni00Y2MxLTgzYmEtZDVmY2ZmZjc4YmY5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjVjMDRlYTI2LTNjMmEtNDUxMS05OGNkLTMyODRiNjRmZjcwMCIsIm5iZiI6MTY1MDgyNzQ4MywiZXhwIjoxNjUwODI4MzgzfQ.AJ9cO8nxDuCO4ws61zCs7ng32lJo2fZCoJXeml6VNcE"
}
```

---
## <center>**Users** <a name="users-protected"></a></center>
---
### Risk profile <a name="risk-profile"></a>
```
POST /api/user/risk-profile
```
---
Add a risk profile to a user

---
## Parameter

| **Field**               | **Type**    | **Description**                                        |
| ----------------------- | ----------- | ------------------------------------------------------ |
| live_nearby_river       | bool        | A boolean to check if the user lives nearby a river    |
| live_nearby_mountain    | bool        | A boolean to check if the user lives nearby a mountain |

**Body:**

```json
{
	"live_nearby_river": true,
	"live_nearby_mountain": false
}
```
Response:
```
HTTP/1.1: 201 - CREATED
```
```json
{
  "name": "John Doe",
  "phone": "(47) 9999-9999",
  "email": "johndoe@mail.com",
  "risks": [
    {
      "title": "FLOOD",
      "text": "FORTES CHUVAS: RISCO DE ALAGAMENTO, reúna pertences importantes (documentos e dinheiro) e dirija-se p/ o ponto de apoio da Defesa Civil mais próximo."
    }
  ]
}
```
### Errors
<details>
<summary>Risk profile without token</summary> <a name="risk-profile-without-token"></a>

**Body:**
```json
{
	"live_nearby_river": true,
	"live_nearby_mountain": false
}
```
Response:
```
HTTP/1.1: 401 - UNAUTHORIZED
```
```json
{
  "msg": "Missing Authorization Header"
}
```
</details>
<details>
<summary>Risk profile with invalid token</summary> <a name="risk-profile-invalid-token"></a>

**Body:**
```json
{
	"live_nearby_river": true,
	"live_nearby_mountain": false
}
```
Response:
```
HTTP/1.1: 422 - UNPROCESSABLE ENTITY
```
```json
{
  "msg": "Signature verification failed"
}
```
</details>
<details>
<summary>Risk profile with user not found</summary> <a name="risk-profile-user-not-found"></a>

**Body:**
```json
{
	"live_nearby_river": true,
	"live_nearby_mountain": false
}
```
Response:
```
HTTP/1.1: 404 - NOT FOUND
```
```json
{
  "error": "user not found"
}
```
</details>
<details>
<summary>Risk profile with missing keys</summary> <a name="risk-profile-missing-keys"></a>

**Body:**
```json
{
	"live_nearby_mountain": true
}
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "missing keys",
  "expected_keys": [
    "live_nearby_river",
    "live_nearby_mountain"
  ],
  "missing_keys": [
    "live_nearby_river"
  ]
}
```
</details>
<details>
<summary>Risk profile with invalid keys</summary> <a name="risk-profile-invalid-keys"></a>

**Body:**
```json
{
	"live_nearby_river": true,
	"live_nearby_mountain": true,
	"live_nearby_volcano": true
}
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "invalid keys",
  "expected_keys": [
    "live_nearby_river",
    "live_nearby_mountain"
  ],
  "invalid_keys": [
    "live_nearby_volcano"
  ]
}
```
</details>
<details>
<summary>Risk profile with invalid value types</summary> <a name="risk-profile-invalid-types"></a>

**Body:**
```json
{
	"live_nearby_river": 0,
	"live_nearby_mountain": "yes"
}
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "invalid type",
  "expected_type": {
    "live_nearby_river": "bool",
    "live_nearby_mountain": "bool"
  },
  "received_type": {
    "live_nearby_river": "int",
    "live_nearby_mountain": "str"
  }
}
```
</details>

---
### Patch user info <a name="users-patch"></a>
```
PATCH /api/user
```
---
Patch the user info

---
## Parameter

| **Field**     | **Type** | **Description**                            |
| ---------     | -------- | ------------------------------------------ |
| name          | string   | User name                                  |
| email         | string   | User email                                 |
| phone         | string   | User phone number                          |
| cep           | string   | User location cep number                   |

**Body:**

```json
{
	"name": "John doe Jr"
}
```
Response:
```
HTTP/1.1: 204 - NO CONTENT
```
### Errors
<details>
<summary>Patch user without token</summary><a name="users-patch-without-token"></a>

**Body:**
```json
{
	"name": "Little johnny"
}
```
Response:
```
HTTP/1.1: 401 - UNAUTHORIZED
```
```json
{
  "msg": "Missing Authorization Header"
}
```
</details>
<details>
<summary>Patch user with invalid token</summary><a name="users-patch-invalid-token"></a>

**Body:**
```json
{
	"name": "Little johnny"
}
```
Response:
```
HTTP/1.1: 422 - UNPROCESSABLE ENTITY
```
```json
{
  "msg": "Missing Authorization Header"
}
```
</details>
<details>
<summary>Patch a not found user</summary><a name="users-patch-user-not-found"></a>

**Body:**
```json
{
	"name": "Little johnny"
}
```
Response:
```
HTTP/1.1: 404 - NOT FOUND
```
```json
{
  "error": "user not found"
}
```
</details>
<details>
<summary>Patch user with invalid keys</summary><a name="users-patch-invalid-keys"></a>

**Body:**
```json
{
	"mother_name": "Olivia"
}
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "invalid keys",
  "expected_keys": [
    "name",
    "phone",
    "email",
    "password",
    "cep"
  ],
  "invalid_keys": [
    "mother_name"
  ]
}
```
</details>
<details>
<summary>Patch user with invalid value types</summary><a name="users-patch-invalid-value-types"></a>

**Body:**
```json
{
	"name": true,
  "email": {"name":"john", "domain":"mail.com"},
  "phone": [55, "99999", 55.55],
  "cep": 99999.999
}
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "invalid type",
  "expected_type": {
    "name": "str",
    "phone": "str",
    "email": "str",
    "password": "str",
    "cep": "str"
  },
  "received_type": {
    "name": "bool",
    "email": "dict",
    "phone": "list",
    "cep": "float"
  }
}
```
</details>
<details>
<summary>Patch user with duplicated email</summary><a name="users-patch-duplicated-email"></a>

**Body:**
```json
{
	"name": "olivia@mail.com"
}
```
Response:
```
HTTP/1.1: 409 - CONFLICT
```
```json
{
  "error": "unique email error"
}
```
</details>
<summary>Patch user with duplicated phone</summary><a name="users-patch-duplicated-phone"></a>

**Body:**
```json
{
	"phone": "(88) 88888-8888"
}
```
Response:
```
HTTP/1.1: 409 - CONFLICT
```
```json
{
  "error": "unique phone error"
}
```
</details>
</details>
<summary>Patch user with invalid zip code</summary><a name="users-patch-invalid-zip-code"></a>

**Body:**
```json
{
  "cep": "00000-000"
}
```
Response:
```
HTTP/1.1: 404 - NOT FOUND
```
```json
{
  "error": "zip code not found"
}
```
</details>
</details>
<summary>Patch user with city out of coverage</summary><a name="users-patch-city-out-of-coverage"></a>

**Body:**
```json
{
  "cep": "06803-440"
}
```
Response:
```
HTTP/1.1: 400 - BAD REQUEST
```
```json
{
  "error": "city out of coverage",
  "received_city": "Embu das Artes",
  "cities_coverage": [
    {
      "city": "Rio de Janeiro",
      "uf": "RJ"
    },
    {
      "city": "São Paulo",
      "uf": "SP"
    },
    {
      "city": "Petrópolis",
      "uf": "RJ"
    },
    {
      "city": "Rio de Contas",
      "uf": "BA"
    },
    {
      "city": "Nova Friburgo",
      "uf": "RJ"
    },
    {
      "city": "Iconha",
      "uf": "ES"
    },
    {
      "city": "Caraguatatuba",
      "uf": "SP"
    },
    {
      "city": "Angra dos Reis",
      "uf": "RJ"
    },
    {
      "city": "Coronel Fabriciano",
      "uf": "MG"
    },
    {
      "city": "Niterói",
      "uf": "RJ"
    },
    {
      "city": "Nilópolis",
      "uf": "RJ"
    },
    {
      "city": "Magé",
      "uf": "RJ"
    },
    {
      "city": "Jaraguá do Sul",
      "uf": "SC"
    },
    {
      "city": "Ipatinga",
      "uf": "MG"
    },
    {
      "city": "Vitória",
      "uf": "ES"
    },
    {
      "city": "São José do Rio Pardo",
      "uf": "SP"
    },
    {
      "city": "São José dos Campos",
      "uf": "SP"
    }
  ]
}
```
</details>

---
### Patch user password <a name="users-patch-password"></a>
```
PATCH /api/user
```
---
To update the user password is required to pass an **old_password** key.  
**NOTE:** You can also pass any of the following parameters.

---
## Parameter

| **Field**     | **Type** | **Description**                            |
| ---------     | -------- | ------------------------------------------ |
| name          | string   | User name                                  |
| email         | string   | User email                                 |
| phone         | string   | User phone number                          |
| cep           | string   | User location cep number                   |
| password      | string   | User password                              |
| old_password  | string   | User old password to confirm new password  |

**Body:**

```json
{
  "name": "Mary B",
  "password": "4321",
	"old_password": "1234"
}
```
Response:
```
HTTP/1.1: 204 - NO CONTENT
```
### Errors
<details>
<summary>Patch user password without old password key</summary> <a name="users-patch-password-without-old-password"></a>

**Body:**
```json
{
  "name": "Mary B",
  "password": "4321"
}
```
Response:
```
HTTP/1.1: 401 - UNAUTHORIZED
```
```json
{
  "error": "missing old password value",
  "message": "to update the password, an old_password key is required"
}
```
</details>
<details>
<summary>Patch user password without password key and with old password key</summary> <a name="users-patch-password-without-password-with-old-password"></a>

**Body:**
```json
{
  "name": "Mary B",
  "old_password": "4321"
}
```
Response:
```
HTTP/1.1: 401 - UNAUTHORIZED
```
```json
{
  "error": "invalid keys",
  "expected_keys": [
    "name",
    "phone",
    "email",
    "password",
    "cep"
  ],
  "invalid_keys": [
    "old_password"
  ]
}
```
</details>

---
### Delete user <a name="users-delete"></a>
```
DELETE /api/user
```
---
Delete an user

---
Response:
```
HTTP/1.1: 204 - NO CONTENT
```
### Errors
<details>
<summary>Delete user without token</summary> <a name="users-delete-without-token"></a>

Response:
```
HTTP/1.1: 401 - UNAUTHORIZED
```
```json
{
  "msg": "Missing Authorization Header"
}
```
</details>
<details>
<summary>Delete user with invalid token</summary> <a name="users-delete-invalid-token"></a>

Response:
```
HTTP/1.1: 422 - UNPROCESSABLE ENTITY
```
```json
{
  "msg": "Signature verification failed"
}
```
</details>
<details>
<summary>Delete a not found user</summary> <a name="users-delete-user-not-found"></a>

Response:
```
HTTP/1.1: 404 - NOT FOUND
```
```json
{
  "error": "user not found"
}
```
</details>