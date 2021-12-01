from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .models import TwoPieceSuitSideBarElement, ThreePieceSuitSideBarElement, \
    TwoPieceSuit, ThreePieceSuit, SuitProduct, Fabric, Lining, Button, ButtonHoleThread, \
        Buttoning, Lapel, LapelStitch, PocketFlap, TicketPocket, Vent, \
            StitchingThread, SleeveButtonContrast, SleeveButtonThread, \
                NeckFeltContrast, TrouserPocket, TrouserButtoning, \
                    TrouserBackPocketPlacement, TrouserBackPocketDesign, \
                        TrouserTurnUp
from cart.models import Cart
from json import dumps
from django.http import JsonResponse
from .forms import UserLoginForm, UserRegistrationForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect #Add this


import json
# Create your views here.
@csrf_exempt
def index(request):
    suit_products                      = SuitProduct.objects.all()
    two_piece_suit_side_bar_elements   = TwoPieceSuitSideBarElement.objects.all()
    three_piece_suit_side_bar_elements = ThreePieceSuitSideBarElement.objects.all()
    two_piece_suits_prods              = TwoPieceSuit.objects.all()
    fabrics                            = Fabric.objects.all()
    linings                            = Lining.objects.all()
    buttons                            = Button.objects.all()
    button_hole_threads                = ButtonHoleThread.objects.all()
    buttonings                         = Buttoning.objects.all()
    lapels                             = Lapel.objects.all()
    lapel_stitches                     = LapelStitch.objects.all()
    pocket_flaps                       = PocketFlap.objects.all()
    ticket_pockets                     = TicketPocket.objects.all()
    vents                              = Vent.objects.all()
    stitching_threads                  = StitchingThread.objects.all()
    sleeve_buttons_contrasts           = SleeveButtonContrast.objects.all()
    sleeve_buttons_threads             = SleeveButtonThread.objects.all()
    neck_felt_contrasts                = NeckFeltContrast.objects.all()
    trouser_pockets                    = TrouserPocket.objects.all()
    trouser_buttonings                 = TrouserButtoning.objects.all()
    trouser_back_pocket_placements     = TrouserBackPocketPlacement.objects.all()
    trouser_back_pocket_designs        = TrouserBackPocketDesign.objects.all()
    trouser_turn_ups                   = TrouserTurnUp.objects.all()
    
    all_details = []
    two_piece_suit_details = {"product": "Two-piece suit"}
    three_piece_suit_details = {"product": "three-piece suit"}

    for instance in two_piece_suits_prods:
        two_piece_suit_details["title"] = instance.title
        two_piece_suit_details["image"] = instance.img.url
        two_piece_suit_details["fabric"] = instance.fabric
        two_piece_suit_details["lining"] = instance.lining
        two_piece_suit_details["buttons"] = instance.buttons
        two_piece_suit_details["button_hole_thread"] = instance.button_hole_thread
        two_piece_suit_details["buttoning"] = instance.buttoning
        two_piece_suit_details["lapel"] = instance.lapel
        two_piece_suit_details["lapel_stitch"] = instance.lapel_stitch
        two_piece_suit_details["pocket_flap"] = instance.pocket_flap
        two_piece_suit_details["ticket_pocket"] = instance.ticket_pocket
        two_piece_suit_details["vent"] = instance.vent
        two_piece_suit_details["stitching_thread"] = instance.stitching_thread
        two_piece_suit_details["sleeve_buttons_contrast"] = instance.sleeve_buttons_contrast
        two_piece_suit_details["sleeve_buttons_thread"] = instance.sleeve_buttons_thread
        two_piece_suit_details["neck_felt_contrast"] = instance.neck_felt_contrast
        two_piece_suit_details["trouser_pockets"] = instance.trouser_pockets
        two_piece_suit_details["trouser_buttoning"] = instance.trouser_buttoning
        two_piece_suit_details["trouser_back_pocket_placement"] = instance.trouser_back_pocket_placement
        two_piece_suit_details["trouser_back_pocket_design"] = instance.trouser_back_pocket_design
        two_piece_suit_details["trouser_turn_up"] = instance.trouser_turn_up
        two_piece_suit_details["price"] = float(instance.price)

        all_details.append(two_piece_suit_details)

        two_piece_suit_details = {"product": "Two-piece suit"}


    if request.is_ajax and request.method == "GET":
        data = request.GET.get("data",None)
        # FilteredProduct = two_piece_suits_prods.filter(Fabric=="Havanna, black")
        #data = request.GET.get("data")
        #print(data)
        #print("assas", data)
        # return JsonResponse(list(FilteredProduct), safe=False)
        # print(text)
        # data = Test.objects.all().values("title")
        # res = Test.objects.filter(title=text).values("title", "image")
        # print(res)
        if data == "allData":
            return JsonResponse(all_details, safe=False)
        
        if data == "threePieceSuitSidebarEle":
            return JsonResponse(three_piece_suit_side_bar_elements, safe=False)

    cart_obj, new_obj = Cart.objects.new_or_get(request)

    combines_ele_names = []

    for item in two_piece_suit_side_bar_elements:
        temp_title = str(item.title)
        #print(temp_title)
        if ' ' in temp_title:
            temp_title = '-'.join(item.title.split(' '))
            combines_ele_names.append((item.title, item.img.url, temp_title))
            
        else:
            combines_ele_names.append((item.title, item.img.url, temp_title))

    context = {
        "cart": cart_obj,
        "two_piece_suit_sidebar_first_ele": two_piece_suit_side_bar_elements[0],
        "two_piece_suit_sidebar_elements": two_piece_suit_side_bar_elements[1:],
        "two_piece_suits_prods": two_piece_suits_prods,
        "suit_products": suit_products,
        "fabrics": fabrics,
        "linings": linings,
        "buttons": buttons,
        "button_hole_threads": button_hole_threads,
        "buttonings": buttonings,
        "lapels": lapels,
        "lapel_stitches": lapel_stitches,
        "pocket_flaps": pocket_flaps,
        "ticket_pockets": ticket_pockets,
        "vents": vents,
        "stitching_threads": stitching_threads,
        "sleeve_buttons_contrasts": sleeve_buttons_contrasts,
        "sleeve_buttons_threads": sleeve_buttons_threads,
        "neck_felt_contrasts": neck_felt_contrasts,
        "trouser_pockets": trouser_pockets,
        "trouser_buttonings": trouser_buttonings,
        "trouser_back_pocket_placements": trouser_back_pocket_placements,
        "trouser_back_pocket_designs": trouser_back_pocket_designs,
        "trouser_turn_ups": trouser_turn_ups,
        "combines_ele_names": combines_ele_names,
        "all_details": all_details
    }

    return render(request, "index/index.html", context)

User = get_user_model()
def userRegistrationPage(request):
    form    = UserRegistrationForm(request.POST)

    context = {
            'form': form
        }
    #print(ele)
    if request.method == 'POST':
        #form = UserRegistrationForm(request.POST)

        if form.is_valid():
            username    = form.cleaned_data.get("username")
            email       = form.cleaned_data.get("email")
            password    = form.cleaned_data.get("password")
            #print(ele)
            new_user    = User.objects.create_user(username, email, password)
            #print(new_user)
            
        else:
            print("Form is not valid")

    return render(request, 'index/register.html', context)

def userLoginPage(request):
    form = UserLoginForm(request.POST)

    context = {
            'form': form
        }

    if request.method == 'POST':
        #form = UserLoginForm(request.POST)

        if form.is_valid():
            username    = form.cleaned_data.get("username")
            password    = form.cleaned_data.get("password")
            user        = authenticate(request, username=username, password=password)
            #print(user)
            #print(request.user.is_authenticated())
            if user is not None:
                #print(request.user.is_authenticated())
                login(request, user)
                # Redirect to a success page.
                #context['form'] = UserLoginForm()
                return redirect("/")
            else:
                print("Error")

    return render(request, 'index/login.html', context)

def bodyMeasurements(request):
    return render(request, 'index/body-measurements.html', {})