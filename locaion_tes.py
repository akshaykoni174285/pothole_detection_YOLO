import geocoder
g = geocoder.ip('me')
print(g.latlng)

# from digidevice import location
# loc = location.Location()
# loc.valid_fix
# print(loc.position)