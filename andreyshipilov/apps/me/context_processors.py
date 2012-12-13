from models import Social

def socials(request):
    socials = Social.objects.all()

    return {
        'SOCIALS': socials,
        'SOCIALS_SPACER_PERCENTAGE': int(round(100 / (socials.count() - 1))),
    }