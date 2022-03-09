# Django-with-GraphQL

## http://127.0.0.1:8000/graphql
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

## mutation 
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