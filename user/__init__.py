from django.utils.translation import pgettext_lazy


class Gender:
    MALE = 'Male'
    FEMALE = 'Female'

    CHOICES = [
        (
            MALE,
            pgettext_lazy('Gender', 'Male')
        ),
        (
            FEMALE,
            pgettext_lazy('Gender', 'Female')
        )
    ]
