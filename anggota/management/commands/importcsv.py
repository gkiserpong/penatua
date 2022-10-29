import argparse
import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from anggota.models import Anggota, Wilayah


class Command(BaseCommand):
    help = 'Importing Data Anggota'
    
    
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('source', nargs='?', type=argparse.FileType('r'))


    def handle(self, *args, **options):
        if options['source']:
            source = options['source']
            basename = os.path.basename(source.name)
            wil_split = basename.split('.')
            wilayah_name = wil_split[0].replace('_', ' ')
            print('Importing', wilayah_name.upper())
            try:
                wilayah = Wilayah.objects.get(nama__icontains=wilayah_name)
                with source as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    for row in csv_reader:
                        print('Inserting', row[1], row[0])
                        anggota = Anggota(nama=row[1], nia=row[0], wilayah=wilayah)
                        anggota.save()
                        
            except ObjectDoesNotExist:
                print('Wilayah tidak ditemukan', wilayah_name)
            