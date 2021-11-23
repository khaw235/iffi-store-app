from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .models import TwoPieceSuitSideBarElement, TwoPieceSuit, SuitProduct, Fabric, Lining, \
    Button, ButtonHoleThread, Buttoning, Lapel, Pocket, Vent, Contrast, \
TrouserPocket, TrouserButtoning, TrouserBackPocket, TrouserTurnUp
from json import dumps
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.

def index(request):
    suit_products                     = SuitProduct.objects.all()
    two_piece_suit_side_bar_elements  = TwoPieceSuitSideBarElement.objects.all()
    two_piece_suits_prods             = TwoPieceSuit.objects.all()
    fabrics                           = Fabric.objects.all()
    linings                           = Lining.objects.all()
    buttons                           = Button.objects.all()
    button_hole_threads               = ButtonHoleThread.objects.all()
    buttonings                        = Buttoning.objects.all()
    lapels                            = Lapel.objects.all()
    pockets                           = Pocket.objects.all()
    vents                             = Vent.objects.all()
    contrasts                         = Contrast.objects.all()
    trouser_pockets                   = TrouserPocket.objects.all()
    trouser_buttonings                = TrouserButtoning.objects.all()
    trouser_back_pockets              = TrouserBackPocket.objects.all()
    trouser_turn_ups                  = TrouserTurnUp.objects.all()

    combines_ele_names = []
    for item in two_piece_suit_side_bar_elements:
        temp_title = str(item.title)
        #print(temp_title)
        if ' ' in temp_title:
            temp_title = '-'.join(item.title.split(' '))
            combines_ele_names.append((item.title, item.img.url, temp_title))
            
        else:
            combines_ele_names.append((item.title, item.img.url, temp_title))
        
    
    #print(combines_ele_names)

    context = {
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
        "pockets": pockets,
        "vents": vents,
        "contrasts": contrasts,
        "trouser_pockets": trouser_pockets,
        "trouser_buttonings": trouser_buttonings,
        "trouser_back_pockets": trouser_back_pockets,
        "trouser_turn_ups": trouser_turn_ups,
        "combines_ele_names": combines_ele_names
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