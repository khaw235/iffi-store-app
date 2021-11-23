function initGTMOnEvent (event){
    window.initGTM();
    event.currentTarget.removeEventListener(event.type, initGTMOnEvent);
}

var ie6 = false;
var ie7 = false;
var ie8 = false;
var priceFormat = '&#36;%';
var thousandsSeparator = ',';
var decimalSeparator = '.';
var jsLangStrings = {"UNDO":"Undo","OK":"OK","CLOSE":"Close"};
var TsLogStatus = false;
var emeraldVersion = 2;
var designerName = 'mens_suit_designer';
var designer = {"template":142,"zoom_in_views":["mainZoom"],"zoom_out_view":"main","defaultZoom":"out","title":"Suit designer deluxe","icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/%name%\/%value%.svg"},"hideOnDisable":true,"itemsPerPage":50,"className":"","views":{"main":{"real_id":"RedshiftMainView","view":"Main","classes":{}},"collar":{"real_id":"null","view":"Neck","classes":"suit-main"},"mainZoom":{"real_id":"RedshiftMainView","view":"Main","classes":"shirt-main-zoom"},"mainLowerJacket":{"real_id":"RedshiftMainView","view":"Main","classes":{}},"mainJacketBack":{"real_id":"JacketRedshiftMainView","view":"Main","classes":"shirt-back","angle":180},"mainTrousers":{"real_id":"TrousersRedshiftMainView","view":"Trousers","classes":"shirt-main"},"mainTrousersBack":{"real_id":"TrousersRedshiftMainView","view":"Trousers","classes":"suit-pants-back","angle":180},"liningCloseup":{"real_id":"RedshiftLiningCloseUp","view":"Lining","classes":{}},"jacketInside":{"real_id":"JacketRedshiftPocketInsideDetail","view":"Inside","classes":"suit-fabric-zoom"},"jacketSleeveDetail":{"real_id":"JacketRedshiftSleeveDetail","view":"Sleeve","classes":"suit-jacket-sleeve-zoom"},"trousersFly":{"real_id":"TrousersRedshiftFlyDetail","view":"Fly","classes":"suit-pants-zoom"},"trousersSidePocket":{"real_id":"TrousersRedshiftSidePocketDetail","view":"Sidepocket","classes":"suit-main"},"fabricAndButtonCloseUp":{"real_id":"RedshiftFabricAndButtonCloseUp","view":"Button","classes":{}}},"choices":{"products":{"key":214,"component":{"type":"choiceWindow","listenTo":["serverSetValue_fabric"],"listenWith":"update"},"title":"Products","name":"products","template":142,"zoom_in_views":["mainZoom"],"zoom_out_view":"main","defaultZoom":"out","icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/%name%\/%value%.svg"},"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"blazerType":{"key":222,"defaultZoom":"out","zoom_out_view":"main","component":{"type":"choiceWindow"},"title":"Blazer type","name":"blazerType","template":142,"zoom_in_views":["mainZoom"],"icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/%name%\/%value%.svg"},"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"fabric":{"title":"Fabric","key":124,"zoom_in_views":["fabricAndButtonCloseUp"],"icon":{"url":"%dynamicMediaServer%\/%fabricIconKey%\/render\/suit\/normal\/icon\/fabric\/%value%.png"},"className":"fabricChoice","defaultZoom":"out","component":{"type":"fabricChoiceWindow","collections":{"emerald":{"title":"Featured","isdefault":true,"function":"getFeaturedFabrics"},"popular":{"title":"Best sellers","category_id":1360},"news":{"title":"News","category_id":1012},"all":{"title":"All"}},"filters":{"color":{"title":"Colour","type":"swatch","options":{"brown":"brown","red":"red","blue":"blue","green":"green","black":"black","white":"white","pink":"pink","purple":"purple","gray":"gray","beige":"beige","yellow":"yellow","turquoise":"turquoise","orange":"orange","apricot":"apricot","khaki":"khaki","ivory":"ivory","wine":"wine red"}}},"searchable":true,"listenTo":["serverSetValue_products"],"listenWith":"update"},"name":"fabric","template":142,"zoom_out_view":"main","hideOnDisable":true,"itemsPerPage":50,"designerName":"mens_suit_designer"},"lining":{"key":149,"icon":{"url":"%dynamicMediaServer%\/%fabricIconKey%\/render\/suit\/normal\/icon\/lining\/%value%.png"},"zoom_in_views":["liningCloseup"],"defaultZoom":"in","component":{"type":"choiceWindow","listenTo":["serverSetValue_fabric"],"listenWith":"update"},"title":"Lining","name":"lining","template":142,"zoom_out_view":"main","hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"button":{"key":213,"zoom_in_views":["fabricAndButtonCloseUp"],"defaultZoom":"in","icon":{"url":"%dynamicMediaServer%\/%fabricIconKey%\/ui\/emerald\/choices\/142\/%name%\/%value%.jpg"},"component":{"type":"choiceWindow","listenTo":["serverSetValue_fabric"],"listenWith":"update"},"title":"Buttons","name":"button","template":142,"zoom_out_view":"main","hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"buttonThread":{"key":150,"zoom_in_views":["fabricAndButtonCloseUp"],"defaultZoom":"in","icon":{"url":"%dynamicMediaServer%\/%pngIconKey%\/render\/rs_suit\/normal\/thread_cam\/%value%.png","nullIcon":"%staticMediaServer%\/ui\/emerald\/choices\/142\/buttonThread\/0.svg"},"component":{"type":"choiceWindow"},"title":"Button hole thread","name":"buttonThread","template":142,"zoom_out_view":"main","hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"jacketDivider":{"component":{"type":"divider"},"title":"jacketDivider","name":"jacketDivider","template":142,"zoom_in_views":["mainZoom"],"zoom_out_view":"main","defaultZoom":"out","icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/%name%\/%value%.svg"},"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"jacketButtoning":{"key":223,"zoom_in_views":["mainLowerJacket"],"zoom_out_view":"main","defaultZoom":"out","component":{"type":"choiceWindow"},"title":"Buttoning","name":"jacketButtoning","template":142,"icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/%name%\/%value%.svg"},"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"jacketLapelContainer":{"zoom_in_views":["mainZoom"],"zoom_out_view":"main","icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/jacketLapel\/%0%.svg","keys":["jacketLapel"]},"defaultZoom":"out","title":"Lapel","choices":{"jacketLapel":{"key":221,"icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/jacketLapel\/%value%.svg"},"component":{"type":"choiceWindow"},"title":"Lapel","name":"jacketLapel","zoom_in_views":["mainZoom"],"zoom_out_view":"main","defaultZoom":"out","template":142,"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"jacketLapelStitch":{"key":224,"defaultZoom":"in","icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/jacketLapelStitch\/%0%_%value%.svg","keys":["jacketLapel"]},"component":{"type":"choiceWindow","listenTo":["setValue_jacketLapel"],"listenWith":"update"},"title":"Lapel stitch","name":"jacketLapelStitch","zoom_in_views":["mainZoom"],"zoom_out_view":"main","template":142,"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"}},"name":"jacketLapelContainer","template":142,"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"jacketPocket":{"title":"Pockets","icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/jacketPocket\/%0%_%1%_%2%.svg","keys":["jacketPocketType","jacketPocketLid","jacketTicketPocket"]},"choices":{"jacketPocketType":{"key":220,"icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/jacketPocket\/%value%_%0%_%1%.svg","keys":["jacketPocketLid","jacketTicketPocket"]},"zoom_in_views":["mainLowerJacket"],"zoom_out_view":"main","defaultZoom":"in","component":{"type":"choiceWindow","listenTo":["setValue_jacketPocketLid","setValue_jacketTicketPocket"],"listenWith":"update"},"title":"Pocket type","name":"jacketPocketType","template":142,"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"jacketPocketLid":{"key":147,"icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/jacketPocketLid\/%0%_%value%.svg","keys":["jacketPocketType"]},"zoom_in_views":["mainLowerJacket"],"zoom_out_view":"main","defaultZoom":"in","component":{"type":"choiceWindow"},"title":"Flap","name":"jacketPocketLid","template":142,"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"jacketTicketPocket":{"key":219,"icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/jacketTicketPocket\/%0%_%1%_%value%.svg","keys":["jacketPocketType","jacketPocketLid"]},"zoom_in_views":["mainLowerJacket"],"zoom_out_view":"main","defaultZoom":"in","component":{"type":"choiceWindow","listenTo":["setValue_jacketPocketType","setValue_jacketPocketLid"],"listenWith":"update"},"title":"Ticket pocket","name":"jacketTicketPocket","template":142,"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"}},"name":"jacketPocket","template":142,"zoom_in_views":["mainZoom"],"zoom_out_view":"main","defaultZoom":"out","hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"jacketChestPocket":{"key":232,"zoom_in_views":["mainZoom"],"defaultZoom":"in","component":{"type":"choiceWindow"},"title":"Chest pocket","name":"jacketChestPocket","template":142,"zoom_out_view":"main","icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/%name%\/%value%.svg"},"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"jacketVent":{"key":178,"zoom_in_views":["mainJacketBack"],"defaultZoom":"in","component":{"type":"choiceWindow"},"title":"Vent","name":"jacketVent","template":142,"zoom_out_view":"main","icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/%name%\/%value%.svg"},"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"jacketFeatures":{"zoom_in_views":["jacketSleeveDetail"],"defaultZoom":"in","icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/jacketFeatures\/0.svg"},"choices":{"jacketStitch":{"key":148,"zoom_in_views":["jacketInside"],"defaultZoom":"in","icon":{"url":"%dynamicMediaServer%\/%pngIconKey%\/render\/rs_suit\/normal\/thread_cam\/%value%.png","nullIcon":"%staticMediaServer%\/ui\/emerald\/choices\/142\/buttonThread\/0.svg"},"component":{"type":"choiceWindow"},"title":"Stitching","name":"jacketStitch","template":142,"zoom_out_view":"main","hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"jacketSleeveButton":{"key":215,"icon":{"url":"%dynamicMediaServer%\/%fabricIconKey%\/render\/rs_suit\/normal\/button_cam\/button_icon\/%value%.png","nullIcon":"%staticMediaServer%\/ui\/emerald\/choices\/142\/jacketSleeveButton\/0.svg"},"component":{"type":"choiceWindow"},"title":"Sleeve contrast button","name":"jacketSleeveButton","zoom_in_views":["jacketSleeveDetail"],"defaultZoom":"in","template":142,"zoom_out_view":"main","hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"jacketSleeveButtonThread":{"key":174,"icon":{"url":"%dynamicMediaServer%\/%pngIconKey%\/render\/rs_suit\/normal\/thread_cam\/%value%.png","nullIcon":"%staticMediaServer%\/ui\/emerald\/choices\/142\/jacketSleeveButtonThread\/0.svg"},"component":{"type":"choiceWindow"},"title":"Button thread, sleeve","name":"jacketSleeveButtonThread","zoom_in_views":["jacketSleeveDetail"],"defaultZoom":"in","template":142,"zoom_out_view":"main","hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"neckFelt":{"key":247,"icon":{"url":"%dynamicMediaServer%\/%fabricIconKey%\/render\/suit\/normal\/icon\/felt\/%value%.png","url2":"%staticMediaServer%\/ui\/emerald\/choices\/142\/neckfelt.svg","type":"contrastFabricMenuIcon"},"zoom_in_views":["collar"],"defaultZoom":"in","component":{"type":"choiceWindow","isoptional":true,"nullchoice":"No contrast fabric"},"title":"Contrast Neck felt","name":"neckFelt","template":142,"zoom_out_view":"main","hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"}},"title":"Contrasts","name":"jacketFeatures","template":142,"zoom_out_view":"main","hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"jacketElbowPatch":{"key":233,"zoom_in_views":["mainJacketBack"],"defaultZoom":"in","icon":{"url":"%dynamicMediaServer%\/%fabricIconKey%\/render\/suit\/normal\/icon\/elbow_patch\/%value%.png","url2":"%staticMediaServer%\/ui\/emerald\/choices\/142\/jacketElbowPatch\/1.svg","nullIcon":"%staticMediaServer%\/ui\/emerald\/choices\/142\/jacketElbowPatch\/0.svg","type":"contrastFabricMenuIcon"},"component":{"type":"choiceWindow"},"title":"Elbow patch","name":"jacketElbowPatch","template":142,"zoom_out_view":"main","hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"trousersDivider":{"component":{"type":"divider"},"title":"trousersDivider","name":"trousersDivider","template":142,"zoom_in_views":["mainZoom"],"zoom_out_view":"main","defaultZoom":"out","icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/%name%\/%value%.svg"},"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"trousersSidePocketStyle":{"key":155,"zoom_in_views":["trousersSidePocket"],"zoom_out_view":"main","defaultZoom":"in","component":{"type":"choiceWindow","listenTo":["setValue_products"],"listenWith":"update"},"icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/%name%\/%value%_%0%.svg","keys":[{"choice":"products","value":7}]},"title":"Pockets","name":"trousersSidePocketStyle","template":142,"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"trousersButtoningStyle":{"key":154,"zoom_in_views":["trousersFly"],"zoom_out_view":"mainTrousers","defaultZoom":"in","component":{"type":"choiceWindow","listenTo":["setValue_products"],"listenWith":"update"},"icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/%name%\/%value%_%0%.svg","keys":[{"choice":"products","value":7}]},"title":"Buttoning","name":"trousersButtoningStyle","template":142,"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"trousersBackPocket":{"zoom_in_views":["mainTrousersBack"],"zoom_out_view":"mainTrousers","defaultZoom":"in","icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/trousersBackPocketPlacement\/%0%_%1%.svg","keys":["trousersBackPocketPlacement",{"choice":"products","value":7}]},"choices":{"trousersBackPocketPlacement":{"key":157,"icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/%name%\/%value%_%0%.svg","keys":[{"choice":"products","value":7}]},"component":{"type":"choiceWindow","listenTo":["setValue_products"],"listenWith":"update"},"title":"Placement","name":"trousersBackPocketPlacement","zoom_in_views":["mainTrousersBack"],"zoom_out_view":"mainTrousers","defaultZoom":"in","template":142,"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"trousersBackPocketStyle":{"key":156,"hideOnDisable":false,"icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/%name%\/%value%_%0%.svg","keys":[{"choice":"products","value":7}]},"component":{"type":"choiceWindow","listenTo":["setValue_products"],"listenWith":"update"},"title":"Back pocket design","name":"trousersBackPocketStyle","zoom_in_views":["mainTrousersBack"],"zoom_out_view":"mainTrousers","defaultZoom":"in","template":142,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"}},"title":"Back pocket","name":"trousersBackPocket","template":142,"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"trousersTurnup":{"key":251,"zoom_in_views":["mainTrousers"],"zoom_out_view":"mainTrousers","defaultZoom":"out","component":{"type":"choiceWindow"},"title":"Trouser turn up","name":"trousersTurnup","template":142,"icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/%name%\/%value%.svg"},"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"},"cartDivider":{"component":{"type":"divider"},"title":"cartDivider","name":"cartDivider","template":142,"zoom_in_views":["mainZoom"],"zoom_out_view":"main","defaultZoom":"out","icon":{"url":"%staticMediaServer%\/ui\/emerald\/choices\/142\/%name%\/%value%.svg"},"hideOnDisable":true,"itemsPerPage":50,"className":"","designerName":"mens_suit_designer"}},"designerName":"mens_suit_designer","map":{"products":"products","blazerType":"blazerType","fabric":"fabric","lining":"lining","button":"button","buttonThread":"buttonThread","jacketDivider":"jacketDivider","jacketButtoning":"jacketButtoning","jacketLapelContainer":"jacketLapelContainer","jacketLapel":"jacketLapelContainer_jacketLapel","jacketLapelStitch":"jacketLapelContainer_jacketLapelStitch","jacketPocket":"jacketPocket","jacketPocketType":"jacketPocket_jacketPocketType","jacketPocketLid":"jacketPocket_jacketPocketLid","jacketTicketPocket":"jacketPocket_jacketTicketPocket","jacketChestPocket":"jacketChestPocket","jacketVent":"jacketVent","jacketFeatures":"jacketFeatures","jacketStitch":"jacketFeatures_jacketStitch","jacketSleeveButton":"jacketFeatures_jacketSleeveButton","jacketSleeveButtonThread":"jacketFeatures_jacketSleeveButtonThread","neckFelt":"jacketFeatures_neckFelt","jacketElbowPatch":"jacketElbowPatch","trousersDivider":"trousersDivider","trousersSidePocketStyle":"trousersSidePocketStyle","trousersButtoningStyle":"trousersButtoningStyle","trousersBackPocket":"trousersBackPocket","trousersBackPocketPlacement":"trousersBackPocket_trousersBackPocketPlacement","trousersBackPocketStyle":"trousersBackPocket_trousersBackPocketStyle","trousersTurnup":"trousersTurnup","cartDivider":"cartDivider"},"key_map":{"214":"products","222":"blazerType","124":"fabric","149":"lining","213":"button","150":"buttonThread","223":"jacketButtoning","221":"jacketLapel","224":"jacketLapelStitch","220":"jacketPocketType","147":"jacketPocketLid","219":"jacketTicketPocket","232":"jacketChestPocket","178":"jacketVent","148":"jacketStitch","215":"jacketSleeveButton","174":"jacketSleeveButtonThread","247":"neckFelt","233":"jacketElbowPatch","155":"trousersSidePocketStyle","154":"trousersButtoningStyle","157":"trousersBackPocketPlacement","156":"trousersBackPocketStyle","251":"trousersTurnup"}};
var lte_ie9 = false;
var clickEvent = 'tap';
var ajajUrl = '/ajaj';
var productType = '142';
var embroideryImageKey = 'NDgwfHw2fHxwbmc,';
var mediaBaseURL = '';
var mediaServerURL = '';
var staticMediaServers = ["cdn.tailorstore.com"];
var dynamicMediaServers = ["rnd.tailorstore.com"];
var initUrl = "\/suit-designer?fbclid=IwAR320ooHc70LjrQNTkyffhAAKJxRyBxcLckx91ojjbjjU7cQeycI54GtFKw";
var emeraldLang = {"WAIT_FOR_THE_COMMAND_TO_EXECUTE":"Working with your previous request, please wait...","VOTES":"votes","NO_RESULTS":"There were no results for your search","ADD_TO_CART":"Add to cart","CONTINUE":"Continue"};
var emeraldImageLoadingMode = 'as1';
var enableLogging = false;

if(window.devicePixelRatio > 1){
    var fabricThumbnailKey = 'MjQwfDI0MHw5MHxmZmZmZmY,';
    var fabricIconKey = 'MjQwfDI0MHw5MHxmZmZmZmY,';
    var iconKey = 'MTYwfDE2MHw5MHxmZmZmZmY,';
    var pngIconKey = 'MTYwfDE2MHw2fHxwbmc,';
} else{
    var fabricThumbnailKey = 'MTIwfDEyMHw5MHxmZmZmZmY,';
    var fabricIconKey = 'MTIwfDEyMHw5MHxmZmZmZmY,';
    var iconKey = 'ODB8ODB8OTB8ZmZmZmZm';
    var pngIconKey = 'ODB8ODB8Nnx8cG5n';
}

window.baseURL = '';
window.ajaj = '/ajaj';

//<!-- init dataLayer for GTM -->
window.dataLayer = window.dataLayer || [];
window.dataLayer.push({
    'pageIndex': "emerald",
    'delocUrl': "emerald",
    'locUrl' : "https:\/\/www.tailorstore.com\/suit-designer",
    'domain': 'tailorstore.com',
    'country': 'us',
    'language': 'en',
    'currency': 'USD',
    'isProduction' : '1',
    'pageVariant' : '',
    'isBot' : '0',
    'domains' : ["tailorstore.at","tailorstore.be","tailorstore.ca","tailorstore.ch","tailorstore.co.in","tailorstore.co.nz","tailorstore.co.uk","tailorstore.co.za","tailorstore.com","tailorstore.com.au","tailorstore.de","tailorstore.dk","tailorstore.fi","tailorstore.fr","tailorstore.nl","tailorstore.no","tailorstore.pl","tailorstore.se","tailorstore.sg"],
    'analyticsCookiesAllowed' : false,
    'marketingCookiesAllowed' : false,
    'customerType': ""
});
//<!-- End Data for GTM -->


//<!-- Google Tag Manager -->
window.initGTM = function(){
    if (window.gtmDidInit){
        return false;
    }

    if(TsCookieAccept.isAccepted('analytics') || TsCookieAccept.isAccepted('marketing')){
        window.gtmDidInit = true;
        var script = document.createElement('script');
        script.type = 'text/javascript';
        script.async = true;
        script.onload = function() {
            window.dataLayer.push({ event: 'gtm.js', 'gtm.start': (new Date()).getTime(), 'gtm.uniqueEventId': 0 });
            window.dispatchEvent(new CustomEvent('tagManagerLoaded'));
        }
        script.src = 'https://www.googletagmanager.com/gtm.js?id=GTM-M8P5XH';
        document.head.appendChild(script);
    }
}

document.addEventListener('DOMContentLoaded', function(){

    /** init gtm after 2 seconds - this could be adjusted */
    setTimeout(window.initGTM, 2000);

    document.addEventListener('scroll', initGTMOnEvent);
    document.addEventListener('mousemove', initGTMOnEvent);
    document.addEventListener('touchstart', initGTMOnEvent);
});
//<!-- End Google Tag Manager -->

window.addEventListener('DOMContentLoaded', function(){
});

// IE 11 Bugfix
window.spin = function(){
    return true;
}

window.stopSpin = function(){
    return true;
}

document.addEventListener('DOMContentLoaded', function(){
    new ScrollHandler($S('.spinner-cover'));
    window.spin = function(){
        $S('.spinner-cover')._ts.addClass('show');
        $S('.spinner-cover div')._ts.addClass('fa-spin');
    };
    window.stopSpin = function(){
        $S('.spinner-cover')._ts.removeClass('show');
        setTimeout(function(){
            $S('.spinner-cover div')._ts.removeClass('fa-spin');
        }, 300);
    };
});