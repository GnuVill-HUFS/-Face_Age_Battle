from django.conf.urls import url
from face_battle import views


urlpatterns = [
    url('home/',views.home), ('single_mode/',views.single_mode),('dual_mode/',views.dual_mode)

]
