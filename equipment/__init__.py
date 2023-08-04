from django.utils.translation import pgettext_lazy


class EquipmentStatus:
    ASSIGNED = 'Assigned'
    UNASSIGNED = 'Unassigned'
    FOR_REPAIR = 'For Repair'

    CHOICES = [
        (
            ASSIGNED,
            pgettext_lazy('Assigned', 'Assigned')
        ),
        (
            UNASSIGNED,
            pgettext_lazy('Unassigned', 'Unassigned')
        ),
        (
            FOR_REPAIR,
            pgettext_lazy('For Repair', 'For Repair')
        )
    ]


class EquipmentType:
    LAPTOP = 'Laptop'
    DESKTOP = 'Desktop'
    MOBILE = 'Mobile'
    TABLET = 'Tablet'

    CHOICES = [
        (
            LAPTOP,
            pgettext_lazy('Laptop', 'Laptop')
        ),
        (
            DESKTOP,
            pgettext_lazy('Desktop', 'Desktop')
        ),
        (
            MOBILE,
            pgettext_lazy('Mobile', 'Mobile')
        ),
        (
            TABLET,
            pgettext_lazy('Tablet', 'Tablet')
        )
    ]


class EquipmentCondition:
    NEW = 'New'
    USED = 'Used'
    REFURBISHED = 'Refurbished'

    CHOICES = [
        (
            NEW,
            pgettext_lazy('New', 'New')
        ),
        (
            USED,
            pgettext_lazy('Used', 'Used')
        ),
        (
            REFURBISHED,
            pgettext_lazy('Refurbished', 'Refurbished')
        )
    ]