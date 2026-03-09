# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # 新增這行
from . import views # 新增這行

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # 這會生成 /accounts/login/ 等路徑
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    # 新增下面這一行，對應到首頁
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('dashboard/', views.dashboard, name='dashboard'), # 新增這行
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)