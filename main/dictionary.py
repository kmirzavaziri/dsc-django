from main.settings import LANGUAGE_CODE

__EXP = {
    'fa-ir': {
        'django_project': 'پروژه جنگو',
        'home': 'صفحه اصلی',
        'login': 'ورود',
        'register': 'ثبت نام',
        'home_page_content': 'سلام. به سامانه‌ی انتخاب واحد مجازی خوش آمدید.',
    },
    'en-us': {

    },
}


def exp(key, lang=None) -> str:
    if not lang:
        lang = LANGUAGE_CODE
    return __EXP[lang][key] if (lang in __EXP and key in __EXP[lang]) else ''
