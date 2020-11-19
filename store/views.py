from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect,Http404,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.urls import reverse
import json

from .forms import *

from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Item,Team,Subscriber
from django.core.paginator import Paginator

subscribers=[]



def sendmail(request):
	print(subscribers)

	if request.method == "POST":
		email=request.POST["email"]

		send_mail(
        	'Bautique58 Store',
			'Hello,  \n\nThank you for subscribing to the Bautique58 newsletter.\nYou will now get the latest updates on new arrivals,sales & promos!. \n \nSincerly, Bautique58.',
        	'boutique58store@gmail.com',
        	[email],
        	fail_silently=False,
    		)

		send_mail(
        	'Bautique58 store new subscriber',
			'New subscriber email:  ' + email,
        	'boutique58store@gmail.com',
        	['boutique58store@gmail.com'],
        	fail_silently=False,
    		)

		if not Subscriber.objects.filter(email=email):
			subscriber=Subscriber(email=email)
			subscriber.save()

	url = reverse('index')
	return HttpResponseRedirect(url)
	


# Create your views here. 




# Python program to view  





def index(request):
	new_arrivals=Item.objects.all().order_by('id').reverse()[:4]
	hot_sales=Item.objects.all().order_by('name').reverse()[:4]
	print(subscribers)



	return render(request, "store/index.html",{'new_arrivals': new_arrivals,"hot_sales":hot_sales,})


def contact(request):
	if request.method=="POST":
		name=request.POST["name"]
		email=request.POST["email"]
		content=request.POST["content"]


		send_mail(
        	'Bautique58 Store',
        	'Dear ' + name + ", \n\nThank you for your inquiry regarding our product or service.\nWe will get back to you as soon as possible. \n \nSincerly, Bautique58.",
        	'boutique58store@gmail.com',
        	[email],
        	fail_silently=False,
    		)
		send_mail(
        	'Bautique58 Store Customer Feedback',
        	"From " + name + "<" + email +"> , \n" +  content,
        	'boutique58store@gmail.com',
        	['boutique58store@gmail.com'],
        	fail_silently=False,
    		)
		
		




	return render(request, "store/contact.html")
def shop(request):
	posts=Item.objects.all().order_by('Price')
	paginator = Paginator(posts, 12)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	accesories=Item.objects.filter(category_type="ACCESSORIES").values_list('categories',flat=True)
	clothing=Item.objects.filter(category_type="CLOTHING").values_list('categories',flat=True)
	shoes=Item.objects.filter(category_type="SHOES").values_list('categories',flat=True)

	
	categories=Item.objects.values_list('categories',flat=True)
	categories=list(categories)
	categories = list(dict.fromkeys(categories))
	categories=sorted(categories)

	accesories=list(accesories)
	accesories = list(dict.fromkeys(accesories))
	accesories=sorted(accesories)

	clothing=list(clothing)
	clothing = list(dict.fromkeys(clothing))
	clothing=sorted(clothing)

	shoes=list(shoes)
	shoes = list(dict.fromkeys(shoes))
	shoes=sorted(shoes)
	
	

	if request.method == 'POST': 
		if request.POST["price"]:
			order=request.POST["price"]
		
			if order=="descending":
				posts=Item.objects.all().order_by('Price').reverse()
				paginator = Paginator(posts, 12)
				page_number = request.GET.get('page')
				page_obj = paginator.get_page(page_number)
				print(order)

				return render(request, "store/shop.html",{'page_obj': page_obj,"count":Item.objects.count(),"order":order,
			"accessories":accesories,"clothings":clothing,"shoes":shoes, "categories":categories})
			
			elif order=="ascending":
				print(order)
				return render(request, "store/shop.html",{'page_obj': page_obj,"count":Item.objects.count(),"order":order,
			"accessories":accesories,"clothings":clothing,"shoes":shoes, "categories":categories})

	return render(request, "store/shop.html",{'page_obj': page_obj,"count":Item.objects.count(),"order":"ascending",
	"accessories":accesories,"clothings":clothing,"shoes":shoes, "categories":categories })

 

 
def cat(request, category):
	category=category.upper()
	results=Item.objects.filter(categories=category).order_by('Price')
	paginator = Paginator(results, 12)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	

	categories=Item.objects.values_list('categories',flat=True)
	categories=list(categories)
	categories = list(dict.fromkeys(categories))
	categories=sorted(categories)


	
	accesories=Item.objects.filter(category_type="ACCESSORIES").values_list('categories',flat=True)
	clothing=Item.objects.filter(category_type="CLOTHING").values_list('categories',flat=True)
	shoes=Item.objects.filter(category_type="SHOES").values_list('categories',flat=True)

	

	accesories=list(accesories)
	accesories = list(dict.fromkeys(accesories))
	accesories=sorted(accesories)

	clothing=list(clothing)
	clothing = list(dict.fromkeys(clothing))
	clothing=sorted(clothing)

	shoes=list(shoes)
	shoes = list(dict.fromkeys(shoes))
	shoes=sorted(shoes)



	if request.method == 'POST': 
		order=request.POST["price"]
		if order=="descending":
			results=Item.objects.filter(categories=category).order_by('Price').reverse()
			paginator = Paginator(results, 12)
			page_number = request.GET.get('page')
			page_obj = paginator.get_page(page_number)
		

			return render(request, "store/category.html",{"page_obj":page_obj,"category":category,
	"count":Item.objects.filter(categories=category).count(),"order":order,"categories":categories,
		"accessories":accesories,"clothing":clothing,"shoes":shoes})
		else:
			print(order)
			return render(request, "store/category.html",{"page_obj":page_obj,"category":category,
	"count":Item.objects.filter(categories=category).count(),"order":order,"categories":categories,
		"accessories":accesories,"clothing":clothing,"shoes":shoes,})

	
	return render(request, "store/category.html",{"page_obj":page_obj,"category":category,
	"count":Item.objects.filter(categories=category).count(),"order":"ascending","categories":categories,
		"accessories":accesories,"clothing":clothing,"shoes":shoes,})


def about(request): 

	
	return render(request, 'store/about.html',{"team":Team.objects.all()})  


def gender(request,gender):

	if gender=="all":
		return HttpResponseRedirect(reverse("shop"))


	gender=gender.upper()
	posts=Item.objects.filter(gender=gender).order_by('Price')
	paginator = Paginator(posts, 12)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	categories=Item.objects.values_list('categories',flat=True)
	categories=list(categories)
	categories = list(dict.fromkeys(categories))
	categories=sorted(categories)


		
	accesories=Item.objects.filter(category_type="ACCESSORIES").values_list('categories',flat=True)
	clothing=Item.objects.filter(category_type="CLOTHING").values_list('categories',flat=True)
	shoes=Item.objects.filter(category_type="SHOES").values_list('categories',flat=True)

	

	accesories=list(accesories)
	accesories = list(dict.fromkeys(accesories))
	accesories=sorted(accesories)

	clothing=list(clothing)
	clothing = list(dict.fromkeys(clothing))
	clothing=sorted(clothing)

	shoes=list(shoes)
	shoes = list(dict.fromkeys(shoes))
	shoes=sorted(shoes)


	
	

	if request.method == 'POST': 
		if request.POST["price"]:
			order=request.POST["price"]
		
			if order=="descending":
				posts=Item.objects.filter(gender=gender).order_by('Price').reverse()
				paginator = Paginator(posts, 12)
				page_number = request.GET.get('page')
				page_obj = paginator.get_page(page_number)
				print(order)

				return render(request, "store/gender.html",{'page_obj': page_obj,"count":Item.objects.filter(gender=gender).order_by('Price').count(),"order":order,
			"categories":categories,"gender":gender,"accessories":accesories,"clothing":clothing,"shoes":shoes})
			
			elif order=="ascending":
				print(order)
				return render(request, "store/gender.html",{'page_obj': page_obj,"count":Item.objects.filter(gender=gender).order_by('Price').count(),"order":order,
			"categories":categories,"gender":gender,"accessories":accesories,"clothing":clothing,"shoes":shoes})

	return render(request, "store/gender.html",{'page_obj': page_obj,"count":Item.objects.filter(gender=gender).order_by('Price').count(),"order":"ascending",
	"categories":categories,"gender":gender,"accessories":accesories,"clothing":clothing,"shoes":shoes})
 



def gender_category(request,gender,category):

	if gender=="all":
		return HttpResponseRedirect(reverse("category",args=(category,)))



	gender=gender.upper()
	posts=Item.objects.filter(gender=gender,categories=category).order_by('Price')
	paginator = Paginator(posts, 12)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	categories=Item.objects.values_list('categories',flat=True)
	categories=list(categories)
	categories = list(dict.fromkeys(categories))
	categories=sorted(categories)


	accesories=Item.objects.filter(category_type="ACCESSORIES").values_list('categories',flat=True)
	clothing=Item.objects.filter(category_type="CLOTHING").values_list('categories',flat=True)
	shoes=Item.objects.filter(category_type="SHOES").values_list('categories',flat=True)

	

	accesories=list(accesories)
	accesories = list(dict.fromkeys(accesories))
	accesories=sorted(accesories)

	clothing=list(clothing)
	clothing = list(dict.fromkeys(clothing))
	clothing=sorted(clothing)

	shoes=list(shoes)
	shoes = list(dict.fromkeys(shoes))
	shoes=sorted(shoes)

	
	

	if request.method == 'POST': 
		if request.POST["price"]:
			order=request.POST["price"]
		
			if order=="descending":
				posts=Item.objects.filter(gender=gender,categories=category).order_by('Price').reverse()
				paginator = Paginator(posts, 12)
				page_number = request.GET.get('page')
				page_obj = paginator.get_page(page_number)
				print(order)

				return render(request, "store/gender_category.html",{'page_obj': page_obj,"count":Item.objects.filter(gender=gender,categories=category).order_by('Price').count(),"order":order,
			"categories":categories,"gender":gender,"category":category,"accessories":accesories,"clothing":clothing,"shoes":shoes})
			
			elif order=="ascending":
				print(order)
				return render(request, "store/gender_category.html",{'page_obj': page_obj,"count":Item.objects.filter(gender=gender,categories=category).order_by('Price').count(),"order":order,
			"categories":categories,"gender":gender,"category":category,"accessories":accesories,"clothing":clothing,"shoes":shoes})

	return render(request, "store/gender_category.html",{'page_obj': page_obj,"count":Item.objects.filter(gender=gender,categories=category).order_by('Price').count(),"order":"ascending",
	"categories":categories,"gender":gender,"category":category,"accessories":accesories,"clothing":clothing,"shoes":shoes})
 



@csrf_exempt
def subscriber(request):

    
    # Composing a new email must be via POST
	if request.method != "POST":
		return JsonResponse({"error": "POST request required."}, status=400)

    # Check recipient emails
	data = json.loads(request.body)
    #post.content = data.get("body","")
    #post.save()
	email=data.get("email","") 
	print(email)
	try:
		sub= Subscriber.objects.get(email=email)
	
		return JsonResponse({"heading":"Sorry","message": "You have alredy subscribe to our newsletter"}, status=201)
	except Subscriber.DoesNotExist:   
		subscriber=Subscriber(email=email)
		subscriber.save()
		return JsonResponse({"message": "success"}, status=201) 