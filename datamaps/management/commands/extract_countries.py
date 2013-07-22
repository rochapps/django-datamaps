from optparse import make_option
import os
import shutil
import subprocess

from django.core.management.base import BaseCommand, CommandError


from datamaps.models import Country

DIR_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
DIR_ROOT = os.path.abspath(os.path.join(DIR_PATH, os.pardir))


class Command(BaseCommand):
    """
        Reads shp file and generates individual files for each country.

    #command to convert to geojson
    ogr2ogr -f GeoJSON -where "adm0_a3 IN ('ARG')" subunits.json ne_10m_admin_0_map_subunits.shp

    #command to convert to topojson
    topojson --id-property su_a3 -p name=NAME -p name -o ar.json subunits.json
    """

    help = 'Read shp file and creates'
    option_list = BaseCommand.option_list + (
        make_option('--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='Delete all previously generated country maps'),
        )

    @staticmethod
    def delete_dir(dir):
        shutil.rmtree(dir)
        os.mkdir(dir)

    def handle(self, *args, **options):
        countries = Country.objects.all()
        shp_file = os.path.join(
            DIR_ROOT,
            "static/shp/ne_10m_admin_0_map_subunits.shp"
        )
        shp_file_pop = os.path.join(
            DIR_ROOT,
            "static/shp/ne_10m_populated_places.shp"
        )
        geo_dir = os.path.join(
            DIR_ROOT,
            "../../static/maps/geo"
        )
        topo_dir = os.path.join(
            DIR_ROOT,
            "../../static/maps/countries"
        )
        # Delete dir for country maps
        if options['delete']:
            self.delete_dir(topo_dir)  # Deletes contents of topo_dir
            self.delete_dir(geo_dir)  # Deletes contents of geo_dir

        for country in countries:
            code = country.code
            geo_file = "{root}/subunits.json".format(code=code, root=geo_dir)
            geo_cities = "{root}/places.json".format(code=code, root=geo_dir)
            topo_file = "{root}/{code}.json".format(code=code, root=topo_dir)

            #extracts fixtures for a country and outputs a GeoJson file
            command = ['ogr2ogr', '-f', 'GeoJSON', '-where',
                "adm0_a3 IN ('{code}')".format(code=code), geo_file,
                shp_file]
            subprocess.check_call(command)
            # geo_country.wait()  # waits for the command to terminate

            #extracts fixtures for major cities in a country and outputs a GeoJson file
            # command = ['ogr2ogr', '-f','GeoJSON', '-where',
            #     "iso_a3 = '{code}' AND SCALERANK < 8".format(code=code),
            #     geo_cities, shp_file_pop]
            # subprocess.check_call(command)
            # geo_cities.wait()  # waits for the command to terminate

            #merges both generated files and creates a topoJson file.
            command = ['topojson', '--bbox', '--id-property', 'su_a3', '-p', 'name=NAME',
                '-p', 'name', '-o', topo_file, geo_file]
            subprocess.check_call(command)
            # topo_file.wait()  # waits for the command to terminate
            # import pdb; pdb.set_trace()
            self.delete_dir(geo_dir)  # Deletes contents of geo_dir
