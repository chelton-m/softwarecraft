# 

class MockGeographicCity:
    def __init__(self):
        self.data = [
            {'id': 1, 'name': 'Paris', 'zip': '75000'},
            {'id': 2, 'name': 'New York', 'zip': '10001'},
            {'id': 3, 'name': 'Los Angeles', 'zip': '90001'},
            {'id': 4, 'name': 'Chicago', 'zip': '60601'},
        ]

    def __iter__(self):
        for item in self.data:
            yield item

    def name_get(self):
        """ Return zip + name """
        return [(geo['id'], f"{geo['zip']} {geo['name']}") for geo in self]

    def name_search(self, name='', args=None, operator='ilike', limit=100):
        """ Allow to search by zip or name or concatenated zip and name """
        if not args:
            args = []

        query_string = name.replace(' ', '').lower()  # Remove spaces and convert to lower case
        result = []

        # Standard search by name
        for record in self.data:
            if query_string in record['name'].replace(' ', '').lower():
                result.append((record['id'], f"{record['zip']} {record['name']}"))

        ids = [line[0] for line in result]

        # Search by zip
        for record in self.data:
            if record['id'] not in ids and query_string in record['zip'].lower():
                result.append((record['id'], f"{record['zip']} {record['name']}"))

        # Search by concatenated zip and name
        for record in self.data:
            combined_value_zip_first = (record['zip'] + record['name']).replace(' ', '').lower()  # Concatenate zip and name and remove spaces
            combined_value_name_first = (record['name'] + record['zip']).replace(' ', '').lower()  # Concatenate name and zip and remove spaces
            if record['id'] not in ids and (query_string in combined_value_zip_first or query_string in combined_value_name_first):
                result.append((record['id'], f"{record['zip']} {record['name']}"))

        # Format the results using name_get
        formatted_results = [record for record in self.name_get() if record[0] in [res[0] for res in result]]

        return formatted_results

# Instantiate the mock class
mock_geo_city = MockGeographicCity()

# Test cases
def run_tests():
    tests = [
        {'input': '75000Paris', 'expected': [(1, '75000 Paris')]},
        {'input': 'NewYork10001', 'expected': [(2, '10001 New York')]},
        {'input': '90001LosAngeles', 'expected': [(3, '90001 Los Angeles')]},
        {'input': 'Chicago60601', 'expected': [(4, '60601 Chicago')]},
    ]

    for test in tests:
        result = mock_geo_city.name_search(name=test['input'])
        assert result == test['expected'], f"Test failed for input {test['input']}. Expected {test['expected']}, got {result}"
        print(f"Test passed for input {test['input']}")

# Run tests
run_tests()
from odoo import api, models

class GeographicCity(models.Model):
    _inherit = 'geographic.city'

    def name_get(self):
        """ Return zip + name """
        return [(geo.id, f"{geo.zip} {geo.name}") for geo in self]

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        """ Allow to search by zip or name or concatenated zip and name """
        if not args:
            args = []

        query_string = name.replace(' ', '').lower()  # Remove spaces and convert to lower case
        result = super(GeographicCity, self).name_search(name, args, operator, limit)
        ids = [line[0] for line in result]

        # Search by zip
        geos_by_zip = self.search([('id', 'not in', ids), ('zip', operator, name)], limit=limit)
        if geos_by_zip:
            result += geos_by_zip.name_get()
            ids.extend([geo.id for geo in geos_by_zip])

        # Search by concatenated zip and name
        for geo in self.search([('id', 'not in', ids)]):
            combined_value_zip_first = (geo.zip + geo.name).replace(' ', '').lower()  # Concatenate zip and name and remove spaces
            combined_value_name_first = (geo.name + geo.zip).replace(' ', '').lower()  # Concatenate name and zip and remove spaces
            if query_string in combined_value_zip_first or query_string in combined_value_name_first:
                result.append((geo.id, f"{geo.zip} {geo.name}"))

        return result
