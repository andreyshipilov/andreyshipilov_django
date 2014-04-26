from datetime import date
from models import Social


def socials(request):
    now, birth = date.today(), date(1984, 1, 19)
    age = (now.year - birth.year) - \
        int((now.month, now.day) < (birth.month, birth.day))
    socials = Social.objects.all()

    return {
        'AGE': age,
        'SOCIALS': socials,
        'SOCIALS_SPACER_PERCENTAGE': int(round(100 / (socials.count() - 1))),
    }
