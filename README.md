Ephemeris Visualizer
====================

Ephemeris Visualizer is a web app for viewing and interacting with a live model of our solar system and all of NASA's probes and spacecraft that are in it.

scraper.py
------------
This script scrapes the web interface of NASA's Jet Propulsion Laboratory site
in order to capture the right-ascension (RA) and declination (DEC) for each
celestial body in a dictionary. This dictionary is serialized and saved into a
file called `objects.p`.

The structure of this dictionary is a key for each class of celestial body
(Sun and planets, Jovian satellites, Saturnian satellites, Uranian satellites,
Neptunian satellites, other satellites, and spacecraft), and each key has an
associated value that is, itself, another dictionary...each of these associated
dictionaries maps the unique ID of the celestial body to a list of six values;
the first three of these constitute the RA of the celestial body while the last
three constitute the DEC of the celestial body.

objects.p
------------
This is the serialized object that `scraper.py` constructs.

TODO:
=============
* Create class for visualizing celestial bodies stored in `objects.p` using their
RA and DEC values.

* Implement partial updating of the celestial body model -- it currently takes
  ~20 minutes to record the most recent RA/DEC values (maybe store the entire
  HTML text from the generated ephemeris -- it shows the next months worth of
  projected values).
