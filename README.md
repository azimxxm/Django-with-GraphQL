# Django-with-GraphQL

## http://127.0.0.1:8000/graphql URL
```graphql
query GetQuestion($id: Int = 2)
{
  allQuestion(id:$id){
    title
  }
  allAnswers(id:$id){
    answerText
  }
}
```

## Adding Category 
```graphql
mutation firstmutation{
  updateCategory(name:"newCat"){
    category{
      name
    }
  }
  
}
```

### category update by id
```graphql
mutation firstmutation{
  updateCategory(id:4, name:"anothercat"){
    category{
      name
    }
  }
  
}
```

## Users view
```graphql
query{
  users{
    edges{
      node{
        id
        pk
        dateJoined
        username
        email
        firstName
        lastName
        lastLogin
        isActive
        isStaff
        verified
        secondaryEmail
        __typename
      }
    }
  }
}

# And Quesy me
query{
  me{
    id
    pk
    username
    email
    firstName
    lastName
    isStaff
    isActive
    secondaryEmail
  }
}
```

## Register user model
```graphql
mutation{
  register(
    email:"azim@gmail.com"
    username:"userda"
    password1:"azimjon102030"
    password2:"azimjon102030"
  ){
    success,
    errors,
    token,
    refreshToken,
  }
}

# Verify Register on email

mutation{
  verifyAccount(token:"eyJ1c2VybmFtZSI6InVzZXJkYSIsImFjdGlvbiI6ImFjdGl2YXRpb24ifQ:1nS0Z5:2On2lILb6qKXrpKOrw0uGN9zQSJ7nWoTLAN7rZflum4")
  {
    success
    errors
  }
}
```

## Login
```graphql
mutation{
  tokenAuth(
    username:"admin",
    password:"102030"
  ) {
    token
    success
    errors
    unarchiving
    refreshToken
    user{
      pk
      username
      isStaff
      isActive
      firstName
      lastName
      email
      secondaryEmail
      lastLogin
      dateJoined
    }
  }
}
```

## Update Account Details
```
mutation{
  updateAccount(
    firstName:"adminusers"
  )
  {
    success
    errors
  }
}
```

## ResendActivationEmail
```
mutation{
  resendActivationEmail(email: "azimxxm@gmail.com"){
    success
    errors
  }
}
```

## Forgotten Password
```
mutation{
  sendPasswordResetEmail(email:"azimxxm@gmail.com"){
    success
    errors
  }
}


mutation{
  passwordReset(token:"eyJ1c2VybmFtZSI6ImFkbWluIiwiYWN0aW9uIjoicGFzc3dvcmRfcmVzZXQifQ:1nS1GX:-e8P4YkUSclFpD7sPP564bmSiY_hshyrgWe_xSD2IN0", newPassword1:"azimjon102030", newPassword2:"azimjon102030")
  {
    success
    errors
  }
}

```