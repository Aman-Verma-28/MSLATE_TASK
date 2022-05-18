from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import DetailForm
from .models import UserDetails, NewUserDetails
from .serializer import UserDetailsSerializer
from rest_framework.status import *


# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    # Create API
    data = []
    if request.method == 'POST':
        form = DetailForm()
        if form.is_valid():
            rank = form.cleaned_data["score"]
            data2 = NewUserDetails.objects.all()
            score = getRank(rank)
            for i in data2:
                if i.score == score:
                    print(i.name)
                    print(i.score)
                    data.append({
                        "user": i.name,
                        "score": i.score,
                    })
        else:
            return Response("Bad Request")
    return Response(data)


def getRank(givenRank):
    scores = []
    data = NewUserDetails.objects.all().order_by('score')
    for user in data:
        scores.append(user.score)
    rank = {}
    cur = 1
    val = scores[0]
    rank[cur] = val
    for i in scores[1:]:
        if i == val:
            pass
        else:
            cur += 1
            rank[cur] = i
            val = i
    return rank[givenRank]
