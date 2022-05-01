# API Advisor

```json
BaseURL: https://rain-forecast-risk-alert.herokuapp.com/
```

---

## Users

### <span style="color: green">**POST**</span> /api/users/signup

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
<summary>Signup with invalid city</summary>
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

### <span style="color: purple">**GET**</span> /users

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
    "city": "Rio de Constas",
    "state": "Bahia"
  }
]
```
