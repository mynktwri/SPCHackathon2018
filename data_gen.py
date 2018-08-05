import random
import numpy as np
hotelnames = ["Hipotel Paris Bordeaux", "Hipotel Paris Belleville", "Hotel De Nemours", "Leonard De Vinci I", "Ideal", "Du Jura", "D'Orleans", "Excelsior Republique", "Picard", "Bristol Republique", "Mary's Hotel", "Luna Park", "The Element Hotel", "De France Gare De Lest"]
hostelnames = ["Lori", "Generator", "Jacobs Inn Hostel", "Hostel Eiffel", "Trendy Hostel", "Maison M Paris", "Enjoy Hostel", "Peace & Love Hostel", "Artistic cocoon & breakfast", "Woodstock Montmartre", "Hotel Du Globe", "Le Montclair Montmartre"]
airbnbnames = ["Quai Victor Augagneur", "Original Place Normandy", "Piccolo appartamento accogliente", "Aiguillette Lodge Bed and Breakfast",  "Nice flat and its balcony", "Studio Chateau de Vincennes Parc Floral Metro", "CHARMING & COSY STUDIO - CLOSE TO BASTILLE"]
names = [hotelnames, hostelnames, airbnbnames]
type = ["Hotel", "Hostel", "AirBnB"]
lodging = []
for i in xrange(0, 200):
	for j in xrange(0, len(names)):
		lodging.append([names[j][int(random.random() * len(names[j]))], random.random()*2000 + 200])
lodging = np.asarray(lodging)

print lodging