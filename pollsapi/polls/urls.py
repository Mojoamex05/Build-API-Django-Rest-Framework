from django.urls import path
from . import views


urlpatterns = [
    path('polls/', views.PollList.as_view(), name="poll_list"),
    path('polls/<int:pk>', views.PollDetail.as_view(), name="poll_detail"),
    path("polls/<int:pk>/choices/", views.ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", views.CreateVote.as_view(), name="create_vote"),
    path("vote/", views.ListVote.as_view(), name="list_vote"),
    path("user/", views.CreateUser.as_view(), name="create_user"),
    path("users/", views.ListUser.as_view(), name="list_user"),
    path("login/", views.LoginView.as_view(), name="login"),
    #path("login/", views.obtain_auth_token, name="login"),
]