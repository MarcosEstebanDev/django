from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from tasks import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet, 'tasks')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/tasks/', views.tasks_list, name='tasks_list'),
    path('docs/', include_docs_urls(title='Tasks API', public=True)),
]
