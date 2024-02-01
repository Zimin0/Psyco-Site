from django.db import models

class Feedback(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    email = models.EmailField(verbose_name="Почта")
    phone_number = models.CharField(verbose_name="Телефон", max_length=20)
    problem_discription = models.TextField(verbose_name="Описание проблемы")
    