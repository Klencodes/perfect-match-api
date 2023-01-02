from django.urls import path
from .views import *
# from social_auth.views import *

urlpatterns = [
    path('user/upload_photo/', UploadPhoto.as_view()),
    path('user/resend_otp/', ResendOTP.as_view()),
    path('user/signup/', SignUpAPI.as_view()),
    path('user/send_reactivate_otp/', SendReactivateOTP.as_view()),
    path('user/reactivate_account/', ReactivateAccount.as_view()),
    path('user/verify_phone_number/', VerifyPhoneNumber.as_view()),
    path('user/signin/', SignInAPI.as_view()),
    path('user/onboarding/legal_name/', CreateLegalName.as_view()),
    path('user/onboarding/birth_date/', CreateBirthDate.as_view()),
    path('user/onboarding/add_address/', CreateAddress.as_view()),
    path('user/onboarding/update_profile_photo/', UpdateProfilePhoto.as_view()),
    path('user/onboarding/prefer_gender/', CreatePreferMatch.as_view()),
    path('user/onboarding/allow_push_notification/', AllowPushNotification.as_view()),



    
    path('manager/signin/', ManagerSignInAPI.as_view()),
    path('manager/fetch_users/', FetchAllUsers.as_view()),
    path('manager/update_user/<int:pk>/', UpdateUser.as_view()),
    path('manager/fetch_addresses/', FetchAddresses.as_view()),

    path('user/fetch_addresses/', ListAddresses.as_view()),
    path('user/add_address/', CreateAddress.as_view()),
    path('user/update_address/', UpdateAddress.as_view()),
    path('user/delete_address/', DeleteAddress.as_view()),
    path('user/update_primary_address/', UpdatePrimaryAddress.as_view()),
    path('user/me/', UserInfoDetails.as_view()),
    
    path('user/forgot_password/', ValidatePhoneForgot.as_view()),
    path('user/validate_forgot_password/', ForgotValidateOTP.as_view()),
    path('user/reset_password/', ForgetPasswordChange.as_view()),
    path('user/change_password/', ChangePasswordAPI.as_view()),  
    path('user/update_profile/', UpdateUserProfile.as_view()),  

    # path('user/google_signin/', GoogleSocialAuthView.as_view()),
    # path('facebook/', FacebookSocialAuthView.as_view()),
    # path('twitter/', TwitterSocialAuthView.as_view()),
]