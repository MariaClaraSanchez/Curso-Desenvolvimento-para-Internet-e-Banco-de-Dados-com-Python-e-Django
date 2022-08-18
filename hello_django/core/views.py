from django.http import HttpResponse


# Create your views here.

def hello(request, nome):
    return HttpResponse('<h1>Hello {}<h1>'.format(nome))


def soma(requeste, n1, n2):
    return HttpResponse('<h1> A soma é : {} + {} = {} </h1>'.format(n1, n2, n1 + n2))
