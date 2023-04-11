from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# from django.template import loader

# Create your views here.

#----------------View to laod the food page--------------------
def index(request):
    item_list = Item.objects.all()
    
    # need to load the template before we use it --> we use loader for it 
    # template = loader.get_template('food/index.html')
       #directly loaded template at render function so no need to laod template separately
       
    context ={
        'item_list':item_list  #itelm_list stores list of items that is passed to the template as a context that will be used to render template or html file dynamically
    }
    
    # return HttpResponse(template.render(context,request))
    return render(request,'food/index.html',context)


#-----------View for practice-----------------------
def item(request):
    return HttpResponse('This is an item View')



#-------------View for details of the items----------------
def detail(request,item_id):
    item = Item.objects.get(pk = item_id)
    context={
        'item':item
    }
    
    return render(request,'food/detail.html',context)
    # return HttpResponse("This is item no: %s" %item_id)