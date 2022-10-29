import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import redirect, render
# from django.views.decorators.csrf import csrf_exempt
from .models import Anggota, Pengusul, Wilayah


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def get_wilayah(request):
    wilayah = Wilayah.objects.all()
    #print(wilayah)
    result = []
    place_json = {}  
    for wil in wilayah:
        place_json['id'] = wil.pk
        place_json['nama'] = wil.nama
        result.append(dict(place_json))
        
    data = json.dumps(result)
    #print(data)
    mimetype = "application/json"
    return HttpResponse(data, mimetype)


def get_anggota_detail(request):
    if is_ajax(request=request):
        query = request.GET.get("term", "")
        try:
            anggota = Anggota.objects.get(nama__iexact=query)
        except ObjectDoesNotExist:
            anggota = None
        
        place_json = {}
        if anggota:
            place_json['nia'] = anggota.nia
            place_json['nama'] = anggota.nama
            place_json['wilayah'] = anggota.wilayah.pk
        
        data = json.dumps(place_json)
    mimetype = "application/json"
    return HttpResponse(data, mimetype)

def construct_name(obj):
    return '{} - {} - {}'.format(obj.nama, obj.nia, obj.wilayah)

def get_anggota(request):
    if is_ajax(request=request):
        query = request.GET.get("term", "")
        anggota = Anggota.objects.filter(nama__icontains=query)
        results = []
        place_json = {}
        for angg in anggota:
            place_json = construct_name(angg)
            results.append(place_json)
        data = json.dumps(results)
    mimetype = "application/json"
    return HttpResponse(data, mimetype)


def input_view(request):
    return render(request, template_name='anggota/input.html')


def get_pengusul(request):
    if is_ajax(request=request):
        query = request.GET.get("term", "")
        #print(query)
        try:
            pengusul = Pengusul.objects.get(email=query)
        except ObjectDoesNotExist:
            pengusul = None
            
        #print(pengusul)
        
        if pengusul:
            place_json = {}
            place_json['pengusul_email'] = pengusul.email
            place_json['pengusul_nama'] = construct_name(pengusul.anggota)
            place_json['pengusul_mobile'] = pengusul.mobile
            
            # Penatua 1
            place_json['penatua_1'] = construct_name(pengusul.penatua_1)
            '''
            if pengusul.penatua_wilayah_1:
                place_json['penatua_1_wilayah'] = pengusul.penatua_wilayah_1.pk
            else:
                place_json['penatua_1_wilayah'] = 0
                
            '''
            place_json['penatua_1_alasan'] = pengusul.penatua_alasan_1
            # Penatua 2
            if pengusul.penatua_2:
                place_json['penatua_2'] = construct_name(pengusul.penatua_2)
            else:
                place_json['penatua_2'] = None
            '''
            if pengusul.penatua_wilayah_2:
                place_json['penatua_2_wilayah'] = pengusul.penatua_wilayah_2.pk
            else:
                place_json['penatua_2_wilayah'] = 0
            '''    
            place_json['penatua_2_alasan'] = pengusul.penatua_alasan_2
            
            if pengusul.penatua_3:
                place_json['penatua_3'] = construct_name(pengusul.penatua_3)
            else:
                place_json['penatua_3'] = None
            '''
            if pengusul.penatua_wilayah_2:
                place_json['penatua_3_wilayah'] = pengusul.penatua_wilayah_3.pk
            else:
                place_json['penatua_3_wilayah'] = 0
            '''
            place_json['penatua_3_alasan'] = pengusul.penatua_alasan_3
            
            if pengusul.penatua_4:
                place_json['penatua_4'] = construct_name(pengusul.penatua_4)
            else:
                place_json['penatua_4'] = None
            '''
            if pengusul.penatua_wilayah_4:
                place_json['penatua_4_wilayah'] = pengusul.penatua_wilayah_4.pk
            else:
                place_json['penatua_4_wilayah'] = 0
            '''
            place_json['penatua_4_alasan'] = pengusul.penatua_alasan_4
            
            if pengusul.penatua_5:
                place_json['penatua_5'] = construct_name(pengusul.penatua_5)
            else:
                place_json['penatua_5'] = None
            '''
            if pengusul.penatua_wilayah_5:
                place_json['penatua_5_wilayah'] = pengusul.penatua_wilayah_5.pk
            else:
                place_json['penatua_5_wilayah'] = 0
            '''
            place_json['penatua_5_alasan'] = pengusul.penatua_alasan_5
                    
        else:
            place_json = {}
        
        #result.append(place_json)
        #print(place_json)
        #data = place_json
        #print(data)
        data = json.dumps(place_json)
        #print(data)
        
        mimetype = "application/json"
        return HttpResponse(data, mimetype)
    
def get_nia(nama):
    nama_split = nama.split(' - ')
    return nama_split[1]

def submit_usulan(request):
    
    if request.POST:
        data = request.POST
        print(data)
        try:
            pengusul = Pengusul.objects.get(email=data['pengusul_email'])
        except ObjectDoesNotExist:
            pengusul = Pengusul()
            pengusul.email = data['pengusul_email']
            pengusul.mobile = data['pengusul_mobile']
            anggota = Anggota.objects.get(nia=get_nia(data['pengusul_nama']))
            pengusul.anggota = anggota
            
        pengusul_penatua_1 = Anggota.objects.get(nia=get_nia(data['penatua_1']))
        pengusul.penatua_1 = pengusul_penatua_1
        pengusul.penatua_alasan_1 = data['penatua_1_alasan']
        #pengusul.penatua_alasan_1.set('Ok')
        # pengusul.penatua_wilayah_1 = pengusul_penatua_1.wilayah
        pengusul.konfirmasi = True
        
        print(pengusul.email, pengusul.mobile, pengusul.penatua_1)

        #print(pengusul)
        pengusul.save()

        return render(request, template_name='anggota/thankyou.html')
    
    else:        
        return redirect('input-view')
    
    
        
        