import json
from shapely.geometry import shape, Point

geojson = open('twCounty2010.geo.json', 'r', encoding='utf-8').read()
load = json.loads(geojson)

def query(coordinate):
	if coordinate.__class__.__name__ == 'tuple':
		point = Point(coordinate)
		for feature in load['features']:
			polygon = shape(feature['geometry'])
			if polygon.contains(point):
				return feature['properties']['name']
