from .views import UserViewSet,UserList,UserDetails
from django.urls import path, include


#router.register(r'groups', GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    #path('groups/', GroupList.as_view()),
    # ...
]
