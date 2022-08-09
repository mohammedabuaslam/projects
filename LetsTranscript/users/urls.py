from django.urls import path
from . import views as users_views
from django.contrib.auth import views as auth_views
from django.conf.urls import (handler400, handler403, handler404, handler500)

urlpatterns = [
    path('dashboard/', users_views.dashboard.as_view(), name='dashboard'),
    path('upload/', users_views.upload, name='upload'),
    path('submitorderforprocessing/', users_views.submitorderforprocessing, name='submitorderforprocessing'),
    path('payments/<encypdata>/<uniqueid>/', users_views.initiatepaymentprocess, name='initiatepaymentprocess'),
    path('insufficientfunds/<uniqueid>/<amountpayable>/', users_views.insufficientfunds, name='insufficientfunds'),
    path('executepayment/<uniqueid>/<amountpayable>/', users_views.executepayment, name='executepayment'),
    path('placeorderafterpayment/<uniqueid>/', users_views.placeorderafterpayment, name='placeorderafterpayment'),
    # path('accountactivation/', users_views.accountactivation, name='useraccountactivation'),
    path('orderplaced/', users_views.orderplaced, name='orderplaced'),
    path('clearstorage/', users_views.clearstorage, name='clearstorage'),
    path('adminorders/', users_views.adminorders.as_view(), name='admin_orders'),
    path('submitorder/', users_views.submitorder, name='submitorder'),
    path('downloadaudio/', users_views.downloadaudio, name='downloadaudio'),
    path('addcredits/', users_views.addcreditstowallet, name='addcreditstowallet'),
    path('addcredits/processing/<amount>/', users_views.addcreditstowalletprocessing, name='addcreditstowalletprocessing'),
    path('addcredits/execute/<amount>/', users_views.addcreditstowalletexecute, name='addcreditstowalletexecute'),
    path('walletpaymentprocessing/', users_views.walletpaymentprocessing, name='walletpaymentprocessing'),
    path('test/', users_views.test, name='test'),
    path('login/', users_views.loginPage, name='login'),
    path('register/', users_views.RegisterView, name='register'),
    path('downloadorder/', users_views.downloadorder, name='download_order'),
    path('downloadautomatedorder/', users_views.downloadautomatedorder, name='downloadautomatedorder'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/login.html'), name='logout'),
    # path('activate/<uidb64>/<token>/', users_views.activate, name='activate'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
]