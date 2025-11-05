from django.shortcuts import render


def index(request):
    goal_list = ["Goal 1", "Goal 2", "Goal 3"]
    context = {"goal_list": goal_list}
    return render(request, "goals/index.html", context)
