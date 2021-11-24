from django.contrib import admin
from django.db import models
from .models import TwoPieceSuitSideBarElement, TwoPieceSuit, \
    SuitProduct, Fabric, Lining, Button, ButtonHoleThread, \
        Buttoning, Lapel, LapelStitch, PocketFlap, TicketPocket, Vent, \
            StitchingThread, SleeveButtonContrast, SleeveButtonThread, \
                NeckFeltContrast, TrouserPocket, TrouserButtoning, \
                    TrouserBackPocketPlacement, TrouserBackPocketDesign, \
                        TrouserTurnUp

# Register your models here.

class TwoPieceSuitAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("fabric", "lining", "buttons", "button_hole_thread", "buttoning", "lapel", "lapel_stitch", "pocket_flap", "ticket_pocket", "vent", "stitching_thread", "sleeve_buttons_contrast", "sleeve_buttons_thread", "neck_felt_contrast",  "trouser_pockets", "trouser_buttoning", "trouser_back_pocket_placement", "trouser_back_pocket_design", "trouser_turn_up")}

admin.site.register(TwoPieceSuitSideBarElement)
admin.site.register(TwoPieceSuit, TwoPieceSuitAdmin)
admin.site.register(SuitProduct)
admin.site.register(Fabric)
admin.site.register(Lining)
admin.site.register(Button)
admin.site.register(ButtonHoleThread)
admin.site.register(Buttoning)
admin.site.register(Lapel)
admin.site.register(LapelStitch)
admin.site.register(PocketFlap)
admin.site.register(TicketPocket)
admin.site.register(Vent)
admin.site.register(StitchingThread)
admin.site.register(SleeveButtonContrast)
admin.site.register(SleeveButtonThread)
admin.site.register(NeckFeltContrast)
admin.site.register(TrouserPocket)
admin.site.register(TrouserButtoning)
admin.site.register(TrouserBackPocketPlacement)
admin.site.register(TrouserBackPocketDesign)
admin.site.register(TrouserTurnUp)