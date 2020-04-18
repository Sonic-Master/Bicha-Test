from django.urls import path
from anshaj import views


urlpatterns = [
    path('',views.index, name='index'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('contact',views.contact, name='contact'),
    path('category/',views.category, name='category'),
    path('postjob/',views.postjob, name='postjob'),
    path('search/',views.search, name='search'),
    path('apply/',views.apply, name='apply'),
    path('applying/',views.applying, name='applying'),
    path('impmessage/',views.impmessage, name='impmessage'),

    path('postjob/applied_candi_by_job',views.applied_candi_by_job,name='applied_candi_by_job'),
    path('view_applied_datewise/',views.view_applied_datewise,name='view_applied_datewise'),
    path('select_shortlist/',views.select_shortlist,name='select_shortlist'),
    path('select_shortlist_search/',views.select_shortlist_search,name='select_shortlist_search'),
    path('shortlisted/',views.shortlisted, name='shortlisted'),

    
 
]