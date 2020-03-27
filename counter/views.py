from django.shortcuts import render
from .utils import parse_github


def main(request):
    return render(request, "counter/main.html")


def result(request):
    names = request.GET.get("names", "")
    start_date = request.GET.get("start_date", "")
    end_date = request.GET.get("end_date", "")
    # print(names, start_date, end_date)

    context = parse_github(names, start_date, end_date)
    print(context)
    return render(request, "counter/result.html", context)
