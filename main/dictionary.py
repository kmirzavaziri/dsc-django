from main.settings import LANGUAGE_CODE

__EXP = {
    'fa-ir': {
        'django_project': 'پروژه جنگو',
        'home': 'صفحه اصلی',
        'profile': 'نمایه',
        'logout': 'خروج',
        'login': 'ورود',
        'register': 'ثبت نام',
        'edit_profile': 'ویرایش نمایه',
        'panel': 'پنل کاربر',
        'home_page_content': 'سلام. به سامانه‌ی انتخاب واحد مجازی خوش آمدید.',
        'contact_us': 'تماس با ما',
        'contact_us_success': 'درخواست شما ثبت شد',
        'back': 'بازگشت',
        'contact_us.title': 'عنوان',
        'contact_us.email': 'ایمیل',
        'contact_us.text': 'متن',
        'profile.first_name': 'نام',
        'profile.last_name': 'نام خانوادگی',
        'profile.username': 'نام کاربری',
        'register.error_messages.unique_username': 'نام کاربری شما در سیستم موجود است',
        'register.error_messages.password_mismatch': 'گذرواژه و تکرار گذرواژه یکسان نیستند',
    },
    'en-us': {

    },
}


def exp(key, lang=None) -> str:
    if not lang:
        lang = LANGUAGE_CODE
    return __EXP[lang][key] if (lang in __EXP and key in __EXP[lang]) else ''
