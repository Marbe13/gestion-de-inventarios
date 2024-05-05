from django.contrib import admin
from django.urls import path , include
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Inventory Management API",
      default_version='v1',
      description="API for managing inventory",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@inventory.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=['permissions'.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('api/', include('inventory_management.urls')),
    path('api/token/', 'TokenObtainPairView'.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', 'TokenRefreshView'.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]