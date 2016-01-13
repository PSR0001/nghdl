import os.path

class Appconfig:

    nghdl_src_loc =  ".esim-nghdl"
    xml_loc = "/opt/eSim/src/modelParamXML/"
    lib_loc = os.path.expanduser('~')
    esimFlag = 0

    kicad_lib_template = {
    "start_def":"DEF comp_name U 0 40 Y Y 1 F N",
    "U_field":"F0 \"U\" 2850 1800 60 H V C CNN",
    "comp_name_field":"F1 \"comp_name\" 2850 2000 60 H V C CNN",
    "blank_field":["F2 blank_quotes 2850 1950 60 H V C CNN","F3 blank_quotes 2850 1950 60 H V C CNN"],
    "start_draw":"DRAW",
    "draw_pos":"S 2550 2100 3150 1800 0 1 0 N",
    "input_port":"X in 1 2350 2000 200 R 50 50 1 1 I",
    "output_port":"X out 2 3350 2000 200 L 50 50 1 1 O",
    "end_draw":"ENDDRAW",
    "end_def":"ENDDEF"
    }


