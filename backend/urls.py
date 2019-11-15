from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls.static import static

from .views import index
from environmentalProject import views as environmentalProjectViews
from mainContent import views as mainContentViews
from steps import views as stepsViews
from buyer import views as buyerViews
from product import views as productViews
from cart import views as cartViews

router = routers.DefaultRouter()
router.register(r'environmentalProjects', environmentalProjectViews.EnvironmentalProjectView, 'environmentalProject')
router.register(r'mainContent', mainContentViews.MainContentView, 'mainContent')
router.register(r'steps', stepsViews.StepsView, 'steps'),
router.register(r'buyer', buyerViews.BuyerView, 'buyer'),
router.register(r'product', productViews.ProductView, 'product'),
router.register(r'cart', cartViews.CartView, 'cart'),

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('token-auth/', obtain_jwt_token),
    path('core/', include('core.urls')),
    # path('', include('sendemail.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
