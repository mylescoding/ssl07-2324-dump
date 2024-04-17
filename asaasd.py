text = '''
    <route id="kbt-10_to_kuf-4" edges="thornton-drive-extension-outward thornton-drive-lower-out L2 L3 L4 L5 L6 univ-road-lower-in"/>
    <route id="kbt-10_to_kuf-4a" edges="thornton-drive-extension-outward thornton-drive-lower-out L2 L3 L4 L5 L6 R6 R5 R4"/>
    <route id="kbt-10_to_kuf-4a_to_kbt-2" edges="thornton-drive-extension-outward thornton-drive-lower-out L2 L3 L4 L5 L6 R6 R5 R4 R3 R2 R1"/>
    <route id="kbt-10_to_kuf-4a_to_kbt-3" edges="thornton-drive-extension-outward thornton-drive-lower-out L2 L3 L4 L5 L6 R6 R5 R4 thornton-drive-in thornton-drive-extension-towards"/>
    <route id="kbt-10_to_kuf-4b" edges="thornton-drive-extension-outward thornton-drive-lower-out L2 L3 L4 L5 L6 univ-road-upper-in"/>
    <route id="kbt-10_to_kuf-5" edges="thornton-drive-extension-outward thornton-drive-lower-out L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12"/>
    <route id="kbt-12" edges="thornton-drive-extension-outward thornton-drive-upper-out R2 R1"/>
    <route id="kbt-2" edges="R6 R5 R4 R3 R2 R1"/>
    <route id="kbt-3" edges="R6 R5 R4 thornton-drive-in thornton-drive-extension-towards"/>
    <route id="kbt-4" edges="L1 thornton-drive-in thornton-drive-extension-towards"/>
    <route id="kbt-4a" edges="L1 R3 R2 R1"/>
    <route id="kbt-5_to_kuf-4" edges="L1 L2 L3 L4 L5 L6 univ-road-lower-in"/>
    <route id="kbt-5_to_kuf-4a" edges="L1 L2 L3 L4 L5 L6 R6 R5 R4"/>
    <route id="kbt-5_to_kuf-4a_to_kbt-2" edges="L1 L2 L3 L4 L5 L6 R6 R5 R4 R3 R2 R1"/>
    <route id="kbt-5_to_kuf-4a_to_kbt-3" edges="L1 L2 L3 L4 L5 L6 R6 R5 R4 thornton-drive-in thornton-drive-extension-towards"/>
    <route id="kbt-5_to_kuf-4b" edges="L1 L2 L3 L4 L5 L6 univ-road-upper-in"/>
    <route id="kbt-5_to_kuf-5" edges="L1 L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12"/>
    <route id="kbt-7" edges="b.gonzales-extension-road b.gonzales-road R3 R2 R1"/>
    <route id="kbt-8" edges="b.gonzales-extension-road b.gonzales-road thornton-drive-in thornton-drive-extension-towards"/>
    <route id="kbt-9_to_kuf-4" edges="b.gonzales-extension-road b.gonzales-road L2 L3 L4 L5 L6 univ-road-lower-in"/>
    <route id="kbt-9_to_kuf-4a" edges="b.gonzales-extension-road b.gonzales-road L2 L3 L4 L5 L6 R6 R5 R4"/>
    <route id="kbt-9_to_kuf-4a_to_kbt-2" edges="b.gonzales-extension-road b.gonzales-road L2 L3 L4 L5 L6 R6 R5 R4 R3 R2 R1"/>
    <route id="kbt-9_to_kuf-4a_to_kbt-3" edges="b.gonzales-extension-road b.gonzales-road L2 L3 L4 L5 L6 R6 R5 R4 thornton-drive-in thornton-drive-extension-towards"/>
    <route id="kbt-9_to_kuf-4b" edges="b.gonzales-extension-road b.gonzales-road L2 L3 L4 L5 L6 univ-road-upper-in"/>
    <route id="kbt-9_to_kuf-5" edges="b.gonzales-extension-road b.gonzales-road L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12"/>
    <route id="kuf-10b" edges="univ-road-lower-out L7 L8 L9 L10 L11 L12"/>
    <route id="kuf-10c" edges="univ-road-upper-out L7 L8 L9 L10 L11 L12"/>
    <route id="kuf-12a-zerovehiclessiya_to_kbt-2" edges="univ-road-upper-out R6 R5 R4 R3 R2 R1"/>
    <route id="kuf-12a-zerovehiclessiya_to_kbt-3" edges="univ-road-upper-out R6 R5 R4 thornton-drive-in thornton-drive-extension-towards"/>
    <route id="kuf-2_to_kbt-2" edges="R7 R6 R5 R4 R3 R2 R1"/>
    <route id="kuf-2_to_kbt-3" edges="R7 R6 R5 R4 thornton-drive-in thornton-drive-extension-towards"/>
    <route id="kuf-3" edges="R7 univ-road-lower-in"/>
    <route id="kuf-3a" edges="R7 univ-road-upper-in"/>
    <route id="kuf-4" edges="L6 univ-road-lower-in"/>
    <route id="kuf-4b" edges="L6 univ-road-upper-in"/>
    <route id="kuf-5" edges="L6 L7 L8 L9 L10 L11 L12"/>
    <route id="kuf-7_to_kbt-2" edges="f.dela-rosa-extension-road f.dela-rosa-road R6 R5 R4 R3 R2 R1"/>
    <route id="kuf-7_to_kbt-3" edges="f.dela-rosa-extension-road f.dela-rosa-road R6 R5 R4 thornton-drive-in thornton-drive-extension-towards"/>
    <route id="kuf-8" edges="f.dela-rosa-extension-road f.dela-rosa-road univ-road-lower-in"/>
    <route id="kuf-8a" edges="f.dela-rosa-extension-road f.dela-rosa-road univ-road-upper-in"/>
    <route id="kuf-9" edges="f.dela-rosa-extension-road f.dela-rosa-road L7 L8 L9 L10 L11 L12"/>
'''



routes = ['kbt-4', 'kbt-4a', 'kbt-5_to_kuf-4', 'kbt-5_to_kuf-4a_to_kbt-2', 'kbt-5_to_kuf-4a_to_kbt-3', 'kbt-5_to_kuf-4b', 'kbt-5_to_kuf-5', 'kbt-7', 'kbt-8', 'kbt-9_to_kuf-4', 'kbt-9_to_kuf-4a_to_kbt-2', 'kbt-9_to_kuf-4a_to_kbt-3', 'kbt-9_to_kuf-4b', 'kbt-9_to_kuf-5', 'kbt-10_to_kuf-4', 'kbt-10_to_kuf-4a_to_kbt-2', 'kbt-10_to_kuf-4a_to_kbt-3', 'kbt-10_to_kuf-4b', 'kbt-10_to_kuf-5', 'kbt-12', 'kuf-2_to_kbt-2', 'kuf-2_to_kbt-3', 'kuf-3', 'kuf-3a', 'kuf-7_to_kbt-2', 'kuf-7_to_kbt-3', 'kuf-8', 'kuf-8a', 'kuf-9', 'kuf-10b', 'kuf-10c', 'kuf-12a']

for route_name in routes:
    if (route_name in text):
        print("SUCCESS, ROUTE " + route_name +" found!")
    else:
        print("FAILED, ROUTE " + route_name +" not found!")