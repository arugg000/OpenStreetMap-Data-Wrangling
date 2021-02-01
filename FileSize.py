import os
bytes = os.path.getsize('Oklahoma_City.osm')
mb = float(bytes / 1000000)
print ("osm file size:", mb, "Mb")