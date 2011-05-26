# Create your views here.
from django.shortcuts import render_to_response
from logger.models import LogLine, LogForm
from django.db.models import F
from django.template import RequestContext

def account(request, account_id = 0, agent_id = 'ohad.samet'):
    log_list = LogLine.objects.all().order_by('place', 'logtext')
    return render_to_response('logger/account.html', {'log_list':log_list, 'account_id':account_id, 'agent_id':agent_id})


def console(request):
    log_list = LogLine.objects.all().order_by('place', 'logtext')
    if request.method == 'POST':
	form = LogForm(request.POST)
    	line = request.POST.get('logline', '')
    	pos = LogLine.objects.all().order_by('-place')[0]
    	if line:
		l = LogLine( logtext = line,
		     	     place = pos.place + 1
		   	)
		l.save()
    else:
	form = LogForm()
    return render_to_response('logger/console.html', {'log_list':log_list, 'form':form}, context_instance=RequestContext(request))

