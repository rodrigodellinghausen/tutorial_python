from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question

def index (request):
	##return HttpResponse("Hello, world. You're at the polls index.")
	last_question_list = Question.objects.order_by('-pub_date')[:5]
	
	#template = loader.get_template('polls/index.html')

	#context = RequestContext(request, {'last_question_list': last_question_list})
	context = {'last_question_list': last_question_list}

	#return HttpResponse(template.render(context))
	return render(request, 'polls/index.html', context)

def  detail(request, question_id):
	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")
	#return render(request, 'polls/detail.html', {'question': question})
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})