import os
import shutil
import subprocess

from django.core.management.base import BaseCommand, CommandError


from datamaps.models import Scope

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

    def handle(self, *args, **options):
        scopes = Scope.objects.all()
        shp_file = os.path.join(
            DIR_ROOT,
            "static/shp/ne_10m_admin_0_map_subunits.shp"
        )
        geo_dir = os.path.join(
            DIR_ROOT,
            "../../static/maps/geo"
        )
        topo_dir = os.path.join(
            DIR_ROOT,
            "../../static/maps/scopes"
        )
        for scope in scopes:
            code = scope.code
            countries = ", ".join(["\'{code}\'".format(code=country.code) \
                for country in scope.country_set.all()])

            geo_file = "{root}/subunits.json".format(code=code, root=geo_dir)
            topo_file = "{root}/{code}.json".format(code=code, root=topo_dir)

            # Command to generate geo file
            command = ['ogr2ogr', '-f', 'GeoJSON', '-where',
                "adm0_a3 IN ({countries})".format(countries=countries),
                '{geo}'.format(geo=geo_file), '{shp}'.format(shp=shp_file)]
            subprocess.check_call(command)

            # Command to generate topofile
            command = ['topojson', '--id-property', 'su_a3', '-p', 'name=NAME',
                '-p', 'name', '-o', '{topo}'.format(topo=topo_file), "{geo}".format(geo=geo_file)]
            subprocess.call(command)

            # File needs to be deleted to be able to continue naming it
            # subunits.json
            shutil.rmtree(geo_dir)
            os.mkdir(geo_dir)
