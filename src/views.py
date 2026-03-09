from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from users.forms import ProfileUpdateForm # 假設你的 Form 在 users/forms.py

# 1. 首頁 View
def home(request):
    return render(request, 'index.html')

# 2. 會員儀表板 View
@login_required
def dashboard(request):
    # 計算加入天數
    days_since_joined = (timezone.now() - request.user.date_joined).days
    
    context = {
        'days_since_joined': days_since_joined,
        'last_login': request.user.last_login,
    }
    return render(request, 'dashboard.html', context)

# 3. 編輯個人資料 View (處理大頭貼上傳)
@login_required
def profile_edit(request):
    if request.method == 'POST':
        # 注意：處理檔案上傳必須加上 request.FILES
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, '您的個人資料已成功更新！')
            return redirect('dashboard')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profile_edit.html', {'p_form': p_form})
