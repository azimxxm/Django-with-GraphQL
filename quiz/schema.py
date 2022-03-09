import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Category, Question, Quizzes, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name')


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ('id', 'title', 'category')


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('title', 'quiz')


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ('question', 'answer_text')


class Query(graphene.ObjectType):

    all_question = graphene.Field(QuestionType, id=graphene.Int())
    all_answers =graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_question(root, info, id):
        return Question.objects.get(id=id)

    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)
# Create Category
# class CategoryMutation(graphene.Mutation):
#     class Arguments:
#         name = graphene.String(required=True)
#
#     category = graphene.Field(CategoryType)
#
#     @classmethod
#     def mutate(cls, root, info, name):
#         category = Category(name=name)
#         category.save()
#         return CategoryMutation(category=category)

# Category update by id
# class CategoryMutation(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID()
#         name = graphene.String(required=True)
#
#     category = graphene.Field(CategoryType)
#     @classmethod
#     def mutate(cls, root, info, name, id):
#         category = Category.objects.get(id=id)
#         category.name = name
#         category.save()
#         return CategoryMutation(category=category)

# Delete Category buy id
class CategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)
    @classmethod
    def mutate(cls, root, info,id):
        category = Category.objects.get(id=id)
        category.delete()
        return

class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
