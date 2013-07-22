import time

from django.core.management.base import BaseCommand, CommandError
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from datamaps.models import Country


class Command(BaseCommand):
    help = 'Get latitude and longitude for countries'

    def handle(self, *args, **options):
        """

        """
        # Initialize driver
        website = "http://dbsgeo.com/latlon/"  # Website to get lats and lons
        driver = webdriver.Firefox()
        driver.get(website)
        driver.implicitly_wait(30)

        # Loop through countries
        countries = Country.objects.all()
        for country in countries:
            if not (country.lat and country.lon):
                # Grab input element
                elem = driver.find_element_by_id("geocodeInput")
                elem.clear()
                # Request country coords
                elem.send_keys(country.name)
                elem.send_keys(Keys.RETURN)

                # Get lat and lon
                elem = driver.find_element_by_id('latlon')
                # import pdb; pdb.set_trace()
                lat, lon = elem.text.split(",")
                lat = float(lat.replace(" ", ""))
                lon = float(lon.replace(" ", ""))

                # Set new lat and lon and save instance
                country.lat = lat
                country.lon = lon
                country.save()
                # Wait for a few seconds so requests are not too close together
                time.sleep(1)

        driver.close()
