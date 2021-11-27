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

class LapelStitch(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'lapel-stitches/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class PocketFlap(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'pocket-flaps/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class TicketPocket(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'ticket-pockets/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class Vent(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'vents/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class StitchingThread(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'stitching-threads/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class SleeveButtonContrast(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'sleeve-buttons-contrasts/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class SleeveButtonThread(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'sleeve-buttons-threads/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class NeckFeltContrast(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'neck-felt-contrasts/', null = True, verbose_name = "Picture")

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

class TrouserBackPocketPlacement(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'trouser-back-pocket-placements/', null = True, verbose_name = "Picture")

    def __str__(self):
        return f"{self.title}"

class TrouserBackPocketDesign(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Title")
    img = models.FileField(upload_to = 'trouser-back-pocket-designs/', null = True, verbose_name = "Picture")

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
LAPEL_STITCHES = []
POCKET_FLAPS = []
TICKET_POCKETS = []
VENTS = []
STITCHING_THREADS = []
SLEEVE_BUTTONS_CONTRASTS = []
SLEEVE_BUTTONS_THREADS = []
NECK_FELT_CONTRASTS = []
TROUSER_POCKETS = []
TROUSER_BUTTONINGS = []
TROUSER_BACK_POCKET_PLACEMENTS = []
TROUSER_BACK_POCKET_DESIGNS = []
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

for item in LapelStitch.objects.all():
    LAPEL_STITCHES.append((item.title.lower(), item.title))

LAPEL_STITCHES = tuple(LAPEL_STITCHES)

for item in PocketFlap.objects.all():
    POCKET_FLAPS.append((item.title.lower(), item.title))

POCKET_FLAPS = tuple(POCKET_FLAPS)

for item in TicketPocket.objects.all():
    TICKET_POCKETS.append((item.title.lower(), item.title))

TICKET_POCKETS = tuple(TICKET_POCKETS)

for item in Vent.objects.all():
    VENTS.append((item.title.lower(), item.title))

VENTS = tuple(VENTS)

for item in StitchingThread.objects.all():
    STITCHING_THREADS.append((item.title.lower(), item.title))

STITCHING_THREADS = tuple(STITCHING_THREADS)

for item in SleeveButtonContrast.objects.all():
    SLEEVE_BUTTONS_CONTRASTS.append((item.title.lower(), item.title))

SLEEVE_BUTTONS_CONTRASTS = tuple(SLEEVE_BUTTONS_CONTRASTS)

for item in SleeveButtonThread.objects.all():
    SLEEVE_BUTTONS_THREADS.append((item.title.lower(), item.title))

SLEEVE_BUTTONS_THREADS = tuple(SLEEVE_BUTTONS_THREADS)

for item in NeckFeltContrast.objects.all():
    NECK_FELT_CONTRASTS.append((item.title.lower(), item.title))

NECK_FELT_CONTRASTS = tuple(NECK_FELT_CONTRASTS)

for item in TrouserPocket.objects.all():
    TROUSER_POCKETS.append((item.title.lower(), item.title))

TROUSER_POCKETS = tuple(TROUSER_POCKETS)

for item in TrouserButtoning.objects.all():
    TROUSER_BUTTONINGS.append((item.title.lower(), item.title))

TROUSER_BUTTONINGS = tuple(TROUSER_BUTTONINGS)

for item in TrouserBackPocketPlacement.objects.all():
    TROUSER_BACK_POCKET_PLACEMENTS.append((item.title.lower(), item.title))

TROUSER_BACK_POCKET_PLACEMENTS = tuple(TROUSER_BACK_POCKET_PLACEMENTS)

for item in TrouserBackPocketDesign.objects.all():
    TROUSER_BACK_POCKET_DESIGNS.append((item.title.lower(), item.title))

TROUSER_BACK_POCKET_DESIGNS = tuple(TROUSER_BACK_POCKET_DESIGNS)

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
    lapel_stitch = models.CharField(max_length = 100, choices = LAPEL_STITCHES, \
        null = True, verbose_name="Lapel Sticth")
    pocket_flap = models.CharField(max_length = 100, choices = POCKET_FLAPS, \
        null = True, verbose_name="Pocket Flap")
    ticket_pocket = models.CharField(max_length = 100, choices = TICKET_POCKETS, \
        null = True, verbose_name="Ticket Pocket")
    vent = models.CharField(max_length = 100, choices = VENTS, \
        null = True)
    stitching_thread = models.CharField(max_length = 100, choices = STITCHING_THREADS, \
        null = True)
    sleeve_buttons_contrast = models.CharField(max_length = 100, choices = SLEEVE_BUTTONS_CONTRASTS, \
        null = True, verbose_name="Sleeve Buttons Contrast")
    sleeve_buttons_thread = models.CharField(max_length = 100, choices = SLEEVE_BUTTONS_THREADS, \
        null = True, verbose_name="Sleeve Buttons Thread")
    neck_felt_contrast = models.CharField(max_length = 100, choices = NECK_FELT_CONTRASTS, \
        null = True, verbose_name="Neck Felt Contrast")
    trouser_pockets = models.CharField(max_length = 100, \
        choices = TROUSER_POCKETS, null = True, \
            verbose_name = "Trouser Pockets")
    trouser_buttoning = models.CharField(max_length = 100, \
        choices = TROUSER_BUTTONINGS, null = True, \
            verbose_name = "Trouser Buttoning")
    trouser_back_pocket_placement = models.CharField(max_length = 100, \
        choices = TROUSER_BACK_POCKET_PLACEMENTS, null = True, \
            verbose_name = "Trouser Back Pocket Placement")
    trouser_back_pocket_design = models.CharField(max_length = 100, \
        choices = TROUSER_BACK_POCKET_DESIGNS, null = True, \
            verbose_name = "Trouser Back Pocket Design")
    trouser_turn_up = models.CharField(max_length = 100, \
        choices = TROUSER_TURN_UPS, null = True, \
            verbose_name = "Trouser Turn Up")
    price = models.DecimalField(decimal_places = 2, max_digits = 20, default = 99.99)
    slug = models.SlugField(max_length=100, null = True, blank = True, db_index = True)
    counts = models.IntegerField(editable=False, default=1, null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.fabric + '-' + self.lining + '-' + self.buttons + '-' + \
            self.button_hole_thread + '-' + self.buttoning + '-' + self.lapel + '-' + \
                self.lapel_stitch + '-' + self.pocket_flap + '-' + self.ticket_pocket + \
                    '-' + self.vent + '-' + self.stitching_thread + '-' +  \
                        self.sleeve_buttons_contrast + '-' +  self.sleeve_buttons_thread + \
                            '-' + self.neck_felt_contrast + '-' + self.trouser_pockets + \
                                '-' + self.trouser_buttoning + '-' + \
                        self.trouser_back_pocket_placement + '-' + \
                            self.trouser_back_pocket_design + '-' +  self.trouser_turn_up)
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