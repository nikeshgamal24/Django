from . import views
from django.urls import path

# Working with multiple app within a project can lead to common name for different path for different app in a website by different developer

#It will lead to ambiguity that whose path is to be used 

#To remove the ambiguity, we use NAMESPACING URL
# ------> specifying explictly the association of the path with which of the app 

app_name = 'food'

urlpatterns = [
    #food/
    #Here the name = 'index' refers that the name of this path is index
    path('',views.index, name = 'index'),
    
    #food/1
    path('<int:item_id>',views.detail,name = 'detail'),
    
    #food/item/
    path('item/',views.item,name = 'item'),
    
    #path for create_item i.e. food/add
    path('add',views.create_item, name = 'create_item'),
    
    # path for updating the item i.e. food/edit/1
    path('update/<int:id>',views.update_item, name = 'update_item'),
    
    #path for deleting the item
    path('delete/<int:id>',views.delete_item, name = 'delete_item'),
]