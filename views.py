from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
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
    
#-------------View for creating of item----------------    
def create_item(request):
    form = ItemForm (request.POST or None)
    
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item_form.html',{'form':form})

#-------------View for upadating of the item---------------- 
def update_item(request,id):
    item = Item.objects.get(id=id)
    
    #we pass the item as a value to the instance argument so that we get the form to edit the form contains the values in the respective field
    form = ItemForm(request.POST or None, instance = item)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item_form.html',{"item":item, "form":form})


#-------------View for delete of the item---------------- 
def delete_item(request,id):
    item = Item.objects.get(id=id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request,'food/item-delete.html',{"item":item})