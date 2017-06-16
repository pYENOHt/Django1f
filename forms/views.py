from django.shortcuts import render_to_response,render
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from forms import UserForm
from models import Record
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def main_page(request):
	if request.method=='POST':
		form=UserForm(request.POST)
		if form.is_valid():
			record=Record (name=form.cleaned_data['name'],
							contact=form.cleaned_data['contact'],
							ptm=form.cleaned_data['ptm'],
							companyName=form.cleaned_data['companyName'],
							eMail=form.cleaned_data['eMail'],
							ptmContact=form.cleaned_data['ptmContact'])
			record.save()
		output='''
		<html>
			<head>
				<title>
					reading user data
				</title>

			</head>
			<body>
				<h1>
					Reading user data
				</h1>
				Hi, {} now you can enter
			</body>
		</html>'''.format(form.cleaned_data['name'])
		return HttpResponse(output)

	else:
		form=UserForm()

	variable={'form':form}
	return render_to_response('ice.html',variable)
# Create your views here.


def error(request):
	raise Http404("To register visit http://127.0.0.1:8000/test/ url.")
	

def err(request):
	return render(request,'error.html')