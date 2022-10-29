import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import Anggota, Pengusul, Wilayah


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def construct_name(obj):
    return '{} - {} - {}'.format(obj.nama, obj.nia, obj.wilayah)


def get_nia(nama):
    nama_split = nama.split(' - ')

    try:
        result = nama_split[1]

    except ValueError:
        result = None

    return result

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
            anggota = Anggota.objects.get(nia=query)
        except ObjectDoesNotExist:
            anggota = None
        place_json = {}
        if anggota:
            place_json['status'] = True
        else:
            place_json['status'] = False
            #place_json['nia'] = anggota.nia
            #place_json['nama'] = anggota.nama
            #place_json['wilayah'] = anggota.wilayah.pk

        data = json.dumps(place_json)
    mimetype = "application/json"
    return HttpResponse(data, mimetype)


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

        data = json.dumps(place_json)

        mimetype = "application/json"
        return HttpResponse(data, mimetype)


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
            nia = get_nia(data['pengusul_nama'])
            if nia:
                anggota = Anggota.objects.get(nia=nia)
                pengusul.anggota = anggota

        nia = get_nia(data['penatua_1'])
        if nia:
            pengusul_penatua_1 = Anggota.objects.get(nia=nia)
            pengusul.penatua_1 = pengusul_penatua_1
        pengusul.penatua_alasan_1 = data['penatua_1_alasan']

        # Penatua 2
        nia = get_nia(data['penatua_2'])
        if nia:
            pengusul_penatua_2 = Anggota.objects.get(nia=nia)
            pengusul.penatua_2 = pengusul_penatua_2
        else:
            pengusul.penatua_2 = None
        pengusul.penatua_alasan_2 = data['penatua_2_alasan']

        # Penatua 3
        nia = get_nia(data['penatua_3'])
        if nia:
            pengusul_penatua_3 = Anggota.objects.get(nia=nia)
            pengusul.penatua_3 = pengusul_penatua_3
        else:
            pengusul.penatua_3 = None
        pengusul.penatua_alasan_3 = data['penatua_3_alasan']

        # Penatua 4
        nia = get_nia(data['penatua_4'])
        if nia:
            pengusul_penatua_4 = Anggota.objects.get(nia=nia)
            pengusul.penatua_4 = pengusul_penatua_4
        else:
            pengusul.penatua_4 = None
        pengusul.penatua_alasan_4 = data['penatua_4_alasan']

        # Penatua 5
        nia = get_nia(data['penatua_5'])
        if nia:
            pengusul_penatua_5 = Anggota.objects.get(nia=nia)
            pengusul.penatua_5 = pengusul_penatua_5
        else:
            pengusul.penatua_5 = None
        pengusul.penatua_alasan_5 = data['penatua_5_alasan']

        # Konfirmasi CheckBox
        pengusul.konfirmasi = True

        print(pengusul.email, pengusul.mobile, pengusul.penatua_1)

        #print(pengusul)
        pengusul.save()

        return render(request, template_name='anggota/thankyou.html')

    else:
        return redirect('input-view')

