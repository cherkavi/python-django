from django.shortcuts import render
from django.http import HttpResponse

class Person:

	def __init__(self, name, surname, age):
		self.__name=name
		self.__surname=surname
		self.__age=age

	def name(self):
		return self.__name

	def surname(self):
		return self.__surname

	def age(self):
		return self.__age


def index(request):
	eva = Person('Eva', 'Brown', 35)
	rudolf = Person('Rudolf', 'Diesel', 50)
	michael = Person('Michael', 'Osner', 28)
	people = [eva, rudolf, michael]
	return render(request, 'index.html', {'people':people})
