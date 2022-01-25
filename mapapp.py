import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
name=list(data["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'blue'


map = folium.Map([28.3949, 84.1240], zoom_start=2)


fgm=folium.FeatureGroup(name="Nepal_Mountain")

for i, j, k in zip(([27.966389, 86.889999],[28.503332, 84.567497],[28.434168, 84.637497],[27.986065, 86.922623]),('Nuptse Mountain','Ngadi Chuli','Himalchuli Mountain','Mount Everest'),('\n333m',' 3m','6m','\n8848')):
    fgm.add_child(folium.Marker(location=i,popup=j+k,icon=folium.Icon(color='red')))

fgv=folium.FeatureGroup(name="USA_Volcanoes")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    fgv.add_child(folium.Marker(location=[lt, ln],popup="volcanoes_usa\n"+nm+"::"+str(el)+"m",icon=folium.Icon(color=color_producer(el))))

fgp=folium.FeatureGroup(name="world_Population")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange'if 10000000<= x['properties']['POP2005']<20000000 else 'red' }))

map.add_child(fgm)
map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("mapapp.html")