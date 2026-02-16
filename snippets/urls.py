from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetList, SnippetDetail, UserList, UserDetail, SnippetHighlighted
from . import views

urlpatterns = [

    path("", views.api_root),

        # function bsed
    # path("snippets/", views.snippet_list),
    # path("snippets/<int:pk>", views.snippet_details),

        #class based
    # path("class_snippets/", SnippetList.as_view()),
    # path("class_snippets/<int:pk>", SnippetDetail.as_view()),

        # mixin
    path("class_snippets/", SnippetList.as_view(), name='snippet-list'),
    path("class_snippets/<int:pk>", SnippetDetail.as_view(), name='snippet-detail'),
     path(
            "snippets/<int:pk>/highlight/",
            views.SnippetHighlighted.as_view(),
            name="snippet-highlighted",
        ),

    path("users/", UserList.as_view(), name='user-list'),
    path("users/<int:pk>", UserDetail.as_view(), name='user-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)