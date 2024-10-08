from django.urls import path, include, re_path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .viewsets import exercise_viewset, program_viewset, custom_user_viewset, routine_viewset, progress_viewset

router = routers.DefaultRouter()
router.register(r'exercises', exercise_viewset.ExerciseViewSet, basename='exercises')
router.register(r'programs', program_viewset.ProgramViewSet, basename='programs')
router.register(r'users', custom_user_viewset.CustomUserViewSet, basename='users')
router.register(r'routines', routine_viewset.RoutineViewSet, basename='routines')
router.register(r'progress', progress_viewset.ProgressViewSet, basename='progress')

schema_view = get_schema_view(
   openapi.Info(
      title="Mon Etab API",
      default_version='v1.4',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
