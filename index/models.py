import os
from django.db import models
from django.utils.text import slugify

def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filepath):
    name, ext = get_file_ext(filepath)
    filename = instance.fabric + '-' + instance.lining + '-' + instance.buttons + '-' + \
            instance.button_hole_thread + '-' + instance.buttoning + '-' + instance.lapel + '-' + \
                instance.pockets + '-' + instance.vent + '-' + instance.contrasts + '-' + \
                    instance.trouser_pockets + '-' + instance.trouser_buttoning + '-' + \
                        instance.trouser_back_pocket + '-' + instance.trouser_turn_up + ext
    return "products/{filename}".format(filename=filename)

# Create your models here.

class TwoPieceSuitSideBarElement(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'suit-sidebar-elements/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class SuitProduct(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'suit-products/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class Fabric(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'fabrics/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class Lining(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'linings/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class Button(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'buttons/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class ButtonHoleThread(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'button-hole-threads/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class Buttoning(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'buttonings/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class Lapel(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'lapels/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class Pocket(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'pockets/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class Vent(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'vents/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class Contrast(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'contrasts/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class TrouserPocket(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'trouser-pockets/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class TrouserButtoning(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'trouser-buttonings/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class TrouserBackPocket(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'trouser-back-pockets/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class TrouserTurnUp(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'trouser-turn-ups/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

FABRICS = []
LININGS = []
BUTTONS = []
BUTTON_HOLE_THREADS = []
BUTTONINGS = []
LAPELS = []
POCKETS = []
VENTS = []
CONTRASTS = []
TROUSER_POCKETS = []
TROUSER_BUTTONINGS = []
TROUSER_BACK_POCKETS = []
TROUSER_TURN_UPS = []

for item in Fabric.objects.all():
    FABRICS.append((item.title.lower(), item.title))

FABRICS = tuple(FABRICS)

for item in Lining.objects.all():
    LININGS.append((item.title.lower(), item.title))

LININGS = tuple(LININGS)

for item in Button.objects.all():
    BUTTONS.append((item.title.lower(), item.title))

BUTTONS = tuple(BUTTONS)

for item in ButtonHoleThread.objects.all():
    BUTTON_HOLE_THREADS.append((item.title.lower(), item.title))

BUTTON_HOLE_THREADS = tuple(BUTTON_HOLE_THREADS)

for item in Buttoning.objects.all():
    BUTTONINGS.append((item.title.lower(), item.title))

BUTTONINGS = tuple(BUTTONINGS)

for item in Lapel.objects.all():
    LAPELS.append((item.title.lower(), item.title))

LAPELS = tuple(LAPELS)

for item in Pocket.objects.all():
    POCKETS.append((item.title.lower(), item.title))

POCKETS = tuple(POCKETS)

for item in Vent.objects.all():
    VENTS.append((item.title.lower(), item.title))

VENTS = tuple(VENTS)

for item in Contrast.objects.all():
    CONTRASTS.append((item.title.lower(), item.title))

CONTRASTS = tuple(CONTRASTS)

for item in TrouserPocket.objects.all():
    TROUSER_POCKETS.append((item.title.lower(), item.title))

TROUSER_POCKETS = tuple(TROUSER_POCKETS)

for item in TrouserButtoning.objects.all():
    TROUSER_BUTTONINGS.append((item.title.lower(), item.title))

TROUSER_BUTTONINGS = tuple(TROUSER_BUTTONINGS)

for item in TrouserBackPocket.objects.all():
    TROUSER_BACK_POCKETS.append((item.title.lower(), item.title))

TROUSER_BACK_POCKETS = tuple(TROUSER_BACK_POCKETS)

for item in TrouserTurnUp.objects.all():
    TROUSER_TURN_UPS.append((item.title.lower(), item.title))

TROUSER_TURN_UPS = tuple(TROUSER_TURN_UPS)

class TwoPieceSuit(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = upload_image_path, null = True, \
        verbose_name = "Picture")
    fabric = models.CharField(max_length = 100, choices = FABRICS, \
        null = True)
    lining = models.CharField(max_length = 100, choices = LININGS, \
        null = True)
    buttons = models.CharField(max_length = 100, choices = BUTTONS, \
        null = True)
    button_hole_thread = models.CharField(max_length = 100, \
        choices = BUTTON_HOLE_THREADS, null = True, \
            verbose_name = "Button Hole Threads")
    buttoning = models.CharField(max_length = 100, \
        choices = BUTTONINGS, null = True)
    lapel = models.CharField(max_length = 100, choices = LAPELS, \
        null = True)
    pockets = models.CharField(max_length = 100, choices = POCKETS, \
        null = True)
    vent = models.CharField(max_length = 100, choices = VENTS, \
        null = True)
    contrasts = models.CharField(max_length = 100, choices = CONTRASTS, \
        null = True)
    trouser_pockets = models.CharField(max_length = 100, \
        choices = TROUSER_POCKETS, null = True, \
            verbose_name = "Trouser Pockets")
    trouser_buttoning = models.CharField(max_length = 100, \
        choices = TROUSER_BUTTONINGS, null = True, \
            verbose_name = "Trouser Buttoning")
    trouser_back_pocket = models.CharField(max_length = 100, \
        choices = TROUSER_BACK_POCKETS, null = True, \
            verbose_name = "Trouser Back Pocket")
    trouser_turn_up = models.CharField(max_length = 100, \
        choices = TROUSER_TURN_UPS, null = True, \
            verbose_name = "Trouser Turn Up")
    price = models.DecimalField(decimal_places = 2, max_digits = 20, default = 99.99)
    slug = models.SlugField(max_length=100, null = True, blank = True, db_index = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.fabric + '-' + self.lining + '-' + self.buttons + '-' + \
            self.button_hole_thread + '-' + self.buttoning + '-' + self.lapel + '-' + \
                self.pockets + '-' + self.vent + '-' + self.contrasts + '-' + \
                    self.trouser_pockets + '-' + self.trouser_buttoning + '-' + \
                        self.trouser_back_pocket + '-' + self.trouser_turn_up)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

class ThreePieceSuit(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'products/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class SuitJacket(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'products/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class SuitTrouser(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'products/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class SuitShirt(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'products/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class Blazer(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'products/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class Waistcoat(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'products/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class Tuxedo(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'products/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"