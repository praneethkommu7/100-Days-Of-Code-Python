# dictionary_in_List
travel_log = [
    {
        'country': 'USA',
        'visits': 1,
        'cities': ['Newark, Jersey City, New York']
    },
    {
        'country': 'India',
        'visits': 7,
        'cities': ['Chennai, Delhi, Kerala, Andhra Pradesh']
    }
]


def add_new_countries(country, visits, cities):
    new_country = {'country': country, 'visits': visits, 'cities': cities}
    travel_log.append(new_country)


add_new_countries('UK', 1, ['london', 'Liverpool', 'Manchester'])
print(travel_log)
