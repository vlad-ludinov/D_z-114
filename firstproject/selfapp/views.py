from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    logger.info("Open URL with about Django project")
    return HttpResponse(
        """<h1>Мой первый проект на Django</h1>
<hr>
<div>я не знаю что про него написать,<br>
поэтому напишу что делал его пол часа<br>
просто повторив то что показывалось в лекции</div>
"""
    )


def about(request):
    logger.info("Open URl with some about me")
    return HttpResponse(
        """<h1>Немного обо мне</h1>
<hr>
<div>на самом деле мне очень понравилось делать html страницы<br>
когда на курсе по Flask неожиданно сказали сделать дз с html страницей<br>
а мы даже его не проходили, и пришлось гуглить как это делать<br>
я тогда просидел пару часов делая красивую форму регистрации<br>
в общем мне немного не приятно писать это вот так,<br>
оно выглядит как то неприятно и слишком просто<br>
короче что-то о себе написал</div>
"""
    )
