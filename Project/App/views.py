# from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

# установка куки
def set(request):
    # получаем из строки запроса имя пользователя
    username = request.GET.get("username", "Undefined")
    # создаем объект ответа
    response = HttpResponse(f"Hello {username}")
    # передаем его в куки
    response.set_cookie("username", username)
    return response

def get(request):
    # получаем куки с ключом username
    username = request.COOKIES["username"]
    return HttpResponse(f"Hello {username}")

def index(request):
    # return JsonResponse({"name": "Tom", "age": 38})
    bob = Person("Bob", 41)
    return JsonResponse(bob, safe=False, encoder=PersonEncoder)

class Person:
    def __init__(self, name, age):
        self.name = name # имя человека
        self.age = age   # возраст человека

class PersonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
            # return obj.__dict__
        return super().default(obj)

'''
def index(request, id):
    people = ["Tom", "Bob", "Sam"]
    # Если пользователь найден, возвращаем его
    if id in range(0, len(people)):
        return HttpResponse(people[id])
    # если нет, то возвращаем ошибку 404
    else:
        return HttpResponseNotFound("Not Found")
'''


def access(request, age):
    # если возраст НЕ входит в диапазон 1-110, посылаем ошибку 400
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    # если возраст больше 17, то доступ разрешен
    if (age > 17):
        return HttpResponse("Доступ разрешен")
    # если нет, то возвращаем ошибку 403
    else:
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")

# def index(request):
#     #return HttpResponse("<h2>Главная</h2>")
#     return HttpResponse("Index")

# def about(request):
#     return HttpResponse("About")
#
# def contact(request):
#     return HttpResponseRedirect("/about")
#
# def details(request):
#     return HttpResponsePermanentRedirect("/")
#
# def user(request):
#     age = request.GET.get("age", 0)
#     name = request.GET.get("name", "Undefineed")
#     return HttpResponse(f"<h2>Имя: {name} Возраст: {age}</h2>")
#
# def products(request, id):
#     return HttpResponse(f"Товар {id}")

# def new(request):
#     return HttpResponse("Новые товары")

# def top(request):
#     return HttpResponse("Наиболее популярные товары")

# def comments(request, id):
#     return HttpResponse(f"Комментарии о товаре {id}")
#
# def questions(request, id):
#     return HttpResponse(f"Вопросы о товаре {id}")


