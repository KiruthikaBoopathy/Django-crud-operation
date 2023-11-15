from django.urls import path
from crud_app import views

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

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

    path("get/",views.Fetchview.as_view()),
    path("post/",views.Createview.as_view()),
    path("get/<int:id>/",views.FetchAllview.as_view()),
    path("put/<int:id>/", views.updateview.as_view()),
    path("delete/<int:id>/",views.delview.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('getpost/',views.getposttt.as_view()),
    path('geti/',views.DuplicatesView.as_view())
]
