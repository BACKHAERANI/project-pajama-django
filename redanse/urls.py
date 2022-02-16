from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clothes/', include('clothes.urls')),
    path('community/', include('community.urls')),
    path('notice/', include('notice.urls')),
    path('qna/', include('qna.urls')),
    path('user/', include('user.urls')),
    path('cart/', include('cart.urls')),
    path('payment/', include('payment.urls')),
    path('review/', include('review.urls')),
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]