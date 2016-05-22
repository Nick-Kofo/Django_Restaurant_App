from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  url(r'^$', views.dish_list, name='dish_list'),
                  url(r'^appetizer/$', views.dish_list_type_appetizer, name='dish_list_type_appetizer'),
                  url(r'^main_course/$', views.dish_list_type_main_course, name='dish_list_type_main_course'),
                  url(r'^dessert/$', views.dish_list_type_dessert, name='dish_list_type_dessert'),
                  url(r'^dish/(?P<pk>[0-9]+)/$', views.dish_description, name='dish_description'),
                  url(r'^dish/new/$', views.dish_new, name='dish_new'),
                  url(r'^dish/(?P<pk>[0-9]+)/edit/$', views.dish_edit, name='dish_edit'),
                  url(r'^dishes/$', views.DishList.as_view()),
                  url(r'^dishes/(?P<pk>[0-9]+)/$', views.DishDetail.as_view()),
                  url(r'^search/$', views.search, name='search'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
