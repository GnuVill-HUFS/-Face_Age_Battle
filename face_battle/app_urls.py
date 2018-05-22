from django.conf.urls import url
from face_battle import views


urlpatterns = [
    url('home/',views.home), 
    url('single_mode/',views.single_mode),
    url('dual_mode/',views.dual_mode),
    url('mode_select/', views.mod_select),
    url('main_page/',views.main_page),
    url('single_result/',views.single_result)
    url('dual_result/', views.dual_result)
]
