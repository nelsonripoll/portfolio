import pygal
import json
from pygal.maps.world import COUNTRIES


class WorldPopulation():
    """World Population loaded from data.okfn.org population json."""

    def __init__(self, filename):
        """Load stats for specific year."""
        self.data = {}

        # some countries in the json file have a different
        # name than what is in the COUNTRIES dictionary
        # this dictionary is used to try to complete the map
        self.missing_countries = {
            'ye': 'Yemen, Rep.',
            'bo': 'Bolivia',
            've': 'Venezuela, RB',
            'kr': 'Korea, Rep.',
            'kp': 'Korea, Dem. Rep.',
            'mk': 'Macedonia, FYR',
            'tz': 'Tanzania',
            'mo': 'Macao SAR, China',
            'cd': 'Congo, Dem. Rep.',
            'cg': 'Congo, Rep.',
            'md': 'Moldova',
            'la': 'Lao PDR',
            'ir': 'Iran, Islamic Rep.',
            'hk': 'Hong Kong SAR, China',
            'eg': 'Egypt, Arab Rep.',
            'gm': 'Gambia, The',
            'ly': 'Libya',
            'kg': 'Kyrgyz Republic',
            'vn': 'Vietnam'}

        with open(filename) as f:
            self.file_data = json.load(f)
        
    def filter_by_year(self, year):
        for pop_dict in self.file_data:
            if pop_dict['Year'] != year:
                continue

            country_code = self.get_two_digit_country_code(pop_dict['Country Name'])

            if country_code:
                self.data[country_code] = int(float(pop_dict['Value']))

        return self.data

    def get_two_digit_country_code(self, country):
        for code, name in COUNTRIES.items():
            if country == name:
                return code
            elif code in self.missing_countries and country == self.missing_countries[code]:
                return code
        return None

    def print_map(self, title, filename):
        wm = pygal.maps.world.World()
        wm.add(title, self.data)
        wm.render_to_file(filename)
