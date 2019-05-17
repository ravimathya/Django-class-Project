from django.urls import path


from . import views

app_name = 'story'
urlpatterns = [
    path('', views.story, name='story'),
    # for makeing page to go page with the slug, put inside<variable name>
    path('<slug:slug>/', views.story_detail, name='storyDetail'),
    # name=something must be used for model for urls. it is the exact name of the url
    path('tag/<str:name>', views.story_tag, name='tagStory'),
    # for creating story...
    path('story/create', views.story_create, name='storyCreate')
]
