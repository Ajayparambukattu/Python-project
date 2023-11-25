from django.urls import path
from TODOAPP import views
app_name='TODOAPP'

urlpatterns = [

    path('',views.fun,name='fun' ),
    path('delete<int:id>/',views.delete,name='delete' ),
    path('update<int:id>/',views.update,name='update' ),
]
