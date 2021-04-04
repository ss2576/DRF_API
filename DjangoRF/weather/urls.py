from rest_framework import routers
from .views import NoteViewSet, NoteViewSetCity


# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'city_all', NoteViewSet)
router.register(r'city/((?P<city_name>[\D-]+)|(?P<city_id>[\d-]+))', NoteViewSetCity)
urlpatterns = router.urls
