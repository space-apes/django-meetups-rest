from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers
from api.views import index, UserViewSet, MeetupGroupViewSet, UserMeetupGroupViewSet,TagViewSet, EventViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'meetup_groups', MeetupGroupViewSet)
router.register(r'tags', TagViewSet)
router.register(r'events', EventViewSet)


# TODO: make url endpoints unique strings for meetup groups because its fun.
# TODO: use nested routers to consolidate urlpattern paths

users_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
users_router.register(r'meetup_groups', UserMeetupGroupViewSet, basename='user-meetup_groups')
#users_router.register(r'events', UserEventViewSet, basename='user-event')

urlpatterns = [
	path('', index, name='index'),
	path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

	path('api/', include(router.urls)),
        path('api/', include(users_router.urls)),
        #path('api/users/<int:user_pk>/', UserViewSet.as_view({'get':'me'}), name='me')
	#path('api/users/<int:user_pk>/meetup_groups/', UserMeetupGroupViewSet.as_view({'get':'list'})),
	#path('api/users/<int:user_pk>/meetup_groups/<int:meetup_group_pk>/', UserMeetupGroupViewSet.as_view({'get':'retrieve'})),
]
