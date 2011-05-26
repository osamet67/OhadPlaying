from piston.handler import BaseHandler
from logger.models import Log, LogLine
from datetime import *
from django.http import HttpResponseRedirect
from django.db.models import F

class LogHandler( BaseHandler ):
	
    def read( self, request, expression ):
	acct, lg, agent = expression.split('&')
	a, a_id = acct.split('=')
	l, l_tx = lg.split('=')
	ag, ag_id = agent.split('=')
	l = Log( log_dt = datetime.now(),
		 account = a_id,
		 agent = ag_id,
		 text = l_tx
		)
	l.save()
 	return HttpResponseRedirect('/tools/account/%s/%s/' % (a_id, ag_id))

class ConsoleHandler( BaseHandler ):

    def read( self, request, expression ):
        f = open('/home/ohad/code/tools/debug.log', 'w')
	action, logline = expression.split('&')
	f.write(str(logline))
	f.write('%s, %s' % (action, logline))
        verb, act = action.split('=')
        verb, log = logline.split('=')
	place = LogLine.objects.all().order_by('-place')[0]
	if act == 'delete':
		LogLine.objects.filter(logtext = log).delete()
	elif act == 'up':
		LogLine.objects.filter(logtext = log).update(place = F('place') - 1)
        elif act == 'down':
                LogLine.objects.filter(logtext = log).update(place = F('place') + 1)

        return HttpResponseRedirect('/tools/console/')

