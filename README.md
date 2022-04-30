# API Advisor

```json
BaseURL: "https://rain-forecast-risk-alert.herokuapp.com/"
```

---
## Summary

* [Users](#users)
  * [Signup](#users-signup)
    * [Signup with an invalid city](#users-signup-invalid-city)
  * [Get all users](#users-get)
* [Forecast risk](#forecast-risk)
  * [Forecast risk request with missing keys](#forecast-risk-missing-keys)
  * [Forecast risk request with invalid keys](#forecast-risk-invalid-keys)
  * [Forecast risk request with invalid value types](#forecast-risk-invalid-value-types)
  * [Forecast risk request with invalid request type](#forecast-risk-invalid-request-type)

---
## <center>**Users** <a name="users"></a></center>
---
### <span style="color: green">**POST**</span> /api/users/signup <a name="users-signup"></a>

Register a new user.

- Not authenticated

## Parameter

| **Field** | **Type** | **Description**          |
| --------- | -------- | ------------------------ |
| name      | string   | User Name                |
| email     | string   | User email               |
| phone     | string   | User phone number        |
| cep       | string   | User location cep number |
| city      | string   | User city location       |

**Body:**

```json
{
  "name": "Danilo Motta",
  "email": "d.motta@gmail.com",
  "phone": "24976520981",
  "cep": "25651-079",
  "city": "Petrópolis"
}
```

Success-Response:

**HTTP/1.1**: 201 **CREATED**

```json
{
  "name": "Danilo Motta",
  "email": "d.motta@gmail.com",
  "phone": "24976520981",
  "address": "25651-079",
  "city": "Petrópolis",
  "state": "Rio de Janeiro"
}
```

### Errors

<details>
<summary>Signup with an invalid city</summary> <a name="users-signup-invalid-city"></a>
Error <span style="color: yellow">4xx</span>

| Nome       | Descrição                                         |
| ---------- | ------------------------------------------------- |
| BadRequest | Error Return When Invalid City Parameter Is Sent. |

```json
{
  "error": "city out of range",
  "expected": ["Rio de Janeiro", "São Paulo", "Petrópolis"],
  "received": "Schroeder"
}
```

</details>

---

### <span style="color: purple">**GET**</span> /api/users <a name="users-get"></a>

Return all registered users.

- Not authenticated

**Parameter:**

_Doesn't have_

Success-Response:

**HTTP/1.1**: 200 **OK**

```json
[
  {
    "name": "Danilo Motta",
    "email": "d.motta@gmail.com",
    "phone": "24976520981",
    "address": "25651-079",
    "city": "Petrópolis",
    "state": "Rio de Janeiro"
  },
  {
    "name": "Dionatan Passos",
    "email": "passos.dionatan@gmail.com",
    "phone": "24976208534",
    "address": "25730-750",
    "city": "Petrópolis",
    "state": "Rio de Janeiro"
  },
  {
    "name": "Carolline Fernandes",
    "email": "carol.fernandes@hotmail.com",
    "phone": "24976520981",
    "address": "08090-284",
    "city": "São Paulo",
    "state": "São Paulo"
  },
  {
    "name": "Amanda Telles",
    "email": "amanda@gmail.com",
    "phone": "24976520981",
    "address": "46170-000",
    "city": "Rio de Contas",
    "state": "Bahia"
  }
]
```
---
## <center>**Forecast Risk** <a name="forecast-risk"></a></center>
---
Send a list of cities, states and precipitation and returns a list of endangered cities along with a quantity of users in the cities. The precipitation values and which values correspond to a danger were defined in the code.

- Not authenticated (?)
## Parameter

| **Field**         | **Type**          | **Description**                      |
| ------------------| ------------------| -------------------------------------|
| city              | string            | A city name                          |
| state             | string            | The city state                       |
| precipitation     | integer or float  | A precipitation integer value in mm  |

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

Success-Response:

**HTTP/1.1**: 200 **OK**


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
		"state": "São Paulo",

	}
]
```

Error-Response:

**HTTP/1.1**: 400 **BAD REQUEST**

```json
{
  "error": "missing keys",
  "expected_keys": [
    "city",
    "state",
    "precipitation"
  ],
  "missing_keys": [
    {
      "request": {
        "state": "Rio de Janeiro",
        "precipitation": 80
      },
      "missing_keys": [
        "city"
      ]
    },
    {
      "request": {
		    "city": "São Paulo",
		    "state": "São Paulo",
      },
      "missing_keys": [
        "precipitation"
      ]
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


Error-Response:

**HTTP/1.1**: 400 **BAD REQUEST**

```json
{
  "error": "invalid keys",
  "expected_keys": [
    "city",
    "state",
    "precipitation"
  ],
  "invalid_keys": [
    {
      "request": {
        "city": "Petrópolis",
        "state": "Rio de Janeiro",
        "precipitation": 80,
        "flood_risk": "high"
      },
      "invalid_keys": [
        "flood_risk"
      ]
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
		"precipitation": {"mm": 80}
	}
]
```


Error-Response:

**HTTP/1.1**: 400 **BAD REQUEST**

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


Error-Response:

**HTTP/1.1**: 400 **BAD REQUEST**

```json
{
  "error": "invalid type",
  "expected_type": "type",
  "received_type": "dict"
}
```
</details>

---