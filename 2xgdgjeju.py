import numpy as np 
import pandas as pd 
import folium
import json

map1 = folium.Map(location=[33.50909717433317, 126.4950769691023], zoom_start=10)
folium.Marker([33.50909717433317, 126.4950769691023], popup='Jeju Airport').add_to(map1)

folium.Marker([33.515394520302266, 126.51867262641643], popup='Dotori Kitchen').add_to(map1)
folium.Marker([33.423324218695065, 126.40509299383888], popup='Yusuam Village').add_to(map1)

folium.Marker([33.422215852264195, 126.40920388064809], popup='Light Park').add_to(map1)

folium.Marker([33.364239066786006, 126.3632621158701], popup='Saebil Cafe').add_to(map1)
folium.Marker([33.46283891774883, 126.30979091670135], popup='Cafe Street').add_to(map1)
folium.Marker([33.444209353828676, 126.3030874800616], popup='Lazy Pump').add_to(map1)


folium.Marker([33.472955699044604, 126.35022911553916], popup='Road').add_to(map1)


folium.Marker([33.36588058225247, 126.35635546876308], popup='Saebyeol Oreum').add_to(map1)
folium.Marker([33.35562178840019, 126.30564478269875], popup='Gold Oreum').add_to(map1)


folium.Marker([33.391181176217536, 126.36652888244501], popup='9.81 Park').add_to(map1)
folium.Marker([33.38922184977778, 126.3780060193172], popup='BigBall Land').add_to(map1)
folium.Marker([33.300197677515655, 126.58015429804023], popup='Doneko').add_to(map1)
folium.Marker([33.239323367514785, 126.54892815555691], popup='Seonyeo tang').add_to(map1)

folium.Marker([33.448815092586635, 126.30351072523295], popup='Gwakji Beach').add_to(map1)
folium.Marker([33.525665060020465, 126.58615891460356], popup='Samyang Beach').add_to(map1)
folium.Marker([33.459812039924536, 126.31105750243042], popup='Handam Beach').add_to(map1)
folium.Marker([33.49792236516346, 126.4531339341132], popup='Ihotaewu Beach').add_to(map1)
folium.Marker([33.54313862218872, 126.66979784425794], popup='Hamdeok').add_to(map1)
folium.Marker([33.555894719748274, 126.79646550569302], popup='Weoljeongli Beach').add_to(map1)

folium.Marker([33.43426419998783, 126.43253202721112], popup='Accomodation').add_to(map1)
folium.CircleMarker([33.43426419998783, 126.43253202721112], radius=100,color='#3186cc',fill_color='#3186cc', popup='Accomodation').add_to(map1)

display(map1)
