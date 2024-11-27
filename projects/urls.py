from rest_framework import routers
from .api import ProjectViewSet

router =  routers.DefaultRouter()
#se genera el CRUD
router.register('api/projects',ProjectViewSet,'projects')

#tiene que ser urlpatterns
urlpatterns = router.urls