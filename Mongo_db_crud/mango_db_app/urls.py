from django.urls import  path
from mango_db_app import  views
# from mango_db_app.views import Renames
from rest_framework import urls
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from mango_db_app.views import UpdateView



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('post/', views.Postdetails.as_view()),
   path('get_single/', views.Getname_details.as_view()),
   path('get_all/', views.Getall_details.as_view()),
   path("put/<str:work_order_no>/", views.UpdateView.as_view()),
   path('delete/',views.Delete_all.as_view()),
   path('delete_using_name/<str:candidate_name>',views.delelet_single.as_view()),

]