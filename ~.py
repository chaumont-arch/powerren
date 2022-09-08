#run landing to generate landings and alias{}
#run layout

#TODO:
#run examines
#copy over custom code

import os
import re
import landing
import layout

files = [f for f in os.listdir('.') if os.path.isfile(f)]

#Generate landing, alias.
for f in files:
    if re.search("^landing.*pwrr$", f):
        landing.parse_landing(f[7])

#Generate layout. 
for f in files:
    if re.search("^layout.*pwrr$", f):
        layout.parse_layout(f[6])
