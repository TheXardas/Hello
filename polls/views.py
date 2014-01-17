from django.http import HttpResponse, Http404
from django.template import loader, RequestContext
from django.shortcuts import render, get_object_or_404
from polls.models import Poll


def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)


def card(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/card.html', {'poll': poll})


def vote_card(request, poll_id):
    return HttpResponse("Vote card")


def vote(request, poll_id):
    return HttpResponse("voting proccess")