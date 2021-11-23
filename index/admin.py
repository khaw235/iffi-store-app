from django.contrib import admin
from django.db import models
from .models import TwoPieceSuitSideBarElement, TwoPieceSuit, ThreePieceSuit, SuitProduct, Fabric, \
Lining, Button, ButtonHoleThread, Buttoning, Lapel, Pocket, Vent, Contrast, \
TrouserPocket, TrouserButtoning, TrouserBackPocket, TrouserTurnUp

# Register your models here.

class TwoPieceSuitAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("fabric", "lining", "buttons", "button_hole_thread", "buttoning", "lapel", "pockets", "vent", "contrasts", "trouser_pockets", "trouser_buttoning", "trouser_back_pocket", "trouser_turn_up")}

admin.site.register(TwoPieceSuitSideBarElement)
admin.site.register(TwoPieceSuit, TwoPieceSuitAdmin)
admin.site.register(SuitProduct)
admin.site.register(Fabric)
admin.site.register(Lining)
admin.site.register(Button)
admin.site.register(ButtonHoleThread)
admin.site.register(Buttoning)
admin.site.register(Lapel)
admin.site.register(Pocket)
admin.site.register(Vent)
admin.site.register(Contrast)
admin.site.register(TrouserPocket)
admin.site.register(TrouserButtoning)
admin.site.register(TrouserBackPocket)
admin.site.register(TrouserTurnUp)