from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
		return render(request, 'login/index.html')

def createUser(request):
	userdata = request.POST
	results = User.userManager.register(userdata, request)

	if results[0] == True:
		messages.success(request, "Success! Please login.")
		return redirect(reverse('login_index'))
	else: 
		return redirect(reverse('login_index'))

def login(request):
	logindata = request.POST
	results = User.userManager.login(logindata, request)
	if results[0] == True:
		if 'logged_in' not in request.session:
			request.session['logged_in'] = User.objects.get(username=logindata['username']).id
			return redirect(reverse('travel_index'))
	else:
		return redirect (reverse('login_index'))




# def register(request):
# 	try:
# 		request.session['logged_in']
# 		return redirect(reverse('travel_index', kwargs={'id':request.session['logged_in']}))
# 	except KeyError:
# 		if User.userManager.register(request.POST, request):
# 			passFlag = True
# 			return redirect(reverse('login_index'))
# 		else:
# 			passFlag = False
# 			return redirect(reverse('accounts_registerPage'))

# def signin(request):
# 	if User.userManager.login(request.POST, request):
# 		passFlag = True
# 		if 'logged_in' not in request.session:
# 			email = request.POST['email']
# 			request.session['logged_in'] =  User.objects.get(email=email).id
# 			return redirect(reverse('travel_index', kwargs={'id':request.session['logged_in']}))
# 	else:
# 		passFlag = False
# 		return redirect (reverse('login_index'))

