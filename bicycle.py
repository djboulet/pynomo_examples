"""
    bicycle.py

    Bicycle gearing cadence and speed calculator

    Copyright (C) 2019-2021 Daniel Boulet

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from pynomo.nomographer import *
from pyx import *
import sys
sys.path.insert(0, "..")
pyx.text.set(text.LatexEngine)


gearing = {
    'block_type': 'type_5',
    'wd_tag': 'ratio',

    'u_func': lambda u: u,
    'v_func': lambda x, v: v/x,

    'u_values': [12.0, 14.0, 16.0, 18.0, 21.0, 24.0, 28.0],
    'u_scale_type': 'manual point',
    'u_manual_axis_data': {12.0: '7', 14.0: '6', 16.0: '5', 18.0: '4', 21.0: '3', 24.0: '2', 28.0: '1'},
    'u_title': 'Rear cage',

    'v_values': [28.0, 38.0, 48.0],
    'v_scale_type': 'manual point',
    'v_manual_axis_data': {28.0: 'Small', 38.0: 'Medium', 48.0: 'Large'},
    # 'v_title': 'Front sprocket',

    'wd_tick_levels': 2,
    'wd_tick_text_levels': 1,
    'wd_tick_side': 'right',
    # 'wd_title': r'\Large Resulting gear ratio',
    # 'wd_title_y_shift': -20.0,
    'wd_title_opposite_tick': True,
    # 'wd_title_distance_center': 2.5,

    'isopleth_values': [[14.0, 38.0, 'x']],

}


wheelrpm = {
    'tag': 'wheelrpm',
    'u_min': 30.0,
    'u_max': 360.0,
    'scale_type': 'manual point',
    'function': lambda u: u,
    # 'title': r'wheel rpm',
    # 'tick_levels': 3,
    # 'tick_text_levels': 1,
}

crankrpm = {
    'u_min': 30.0,
    'u_max': 90.0,
    'function': lambda u: u,
    'title': r'\large \slshape Crank RPM',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'scale_type': 'linear smart',
    'title_draw_center': True,
    'title_distance_center': -0.5,
}

ratio = {
    'scale_type': 'manual point',
    'tag': 'ratio',
    'u_min': 1.0,
    'u_max': 4.0,
    'function': lambda u: u,
    # 'title': r'ratio',
    'tick_levels': 3,
    'tick_text_levels': 1,
}


rotation = {
    'block_type': 'type_2',
    #  'width':10.0,
    #  'height':10.0,
    'f1_params': wheelrpm,
    'f2_params': crankrpm,
    'f3_params': ratio,
    'isopleth_values': [['x', 75, 'x']],
}


speed = {
    'u_min': 5.0,
    'u_max': 50.0,
    'function': lambda u: u,
    'title': r'\large \slshape Speed (km/hour)',
    'tick_levels': 5,
    'tick_text_levels': 2,
    'scale_type': 'linear smart',
    'title_draw_center': True,
    'title_distance_center': -0.5,
}

diameter = {
    'u_min': 600.0,
    'u_max': 800.0,
    'function': lambda u: u*3.1415927*60.0/1000000.0,
    'title': r'Wheel Diameter',
    'tick_levels': 2,
    'tick_text_levels': 1,
    'scale_type': 'linear smart',
    'title_draw_center': True,
    'title_distance_center': -0.5,

}

wheelrpm2 = {
    'tag': 'wheelrpm',
    'u_min': 30.0,
    'u_max': 360.0,
    'function': lambda u: u,
    'scale_type': 'linear smart',

    'title': r'\large \slshape Wheel RPM',
    'title_x_shift': -18.5,
    'tick_levels': 5,
    'tick_text_levels': 3,
}


speedblock = {
    'block_type': 'type_2',
    # 'width': 10.0,
    # 'height': 10.0,
    'f1_params': speed,
    'f2_params': diameter,
    'f3_params': wheelrpm2,
    'mirror_x': True,
    'isopleth_values': [['x', 750.0, 'x']],
}


main_params = {
    'filename': 'bicycle.pdf',
    #   'paper_height':10.0,
    #   'paper_width':10.0,
    'block_params': [gearing, rotation, speedblock],
    'transformations': [('rotate', 0.01), ('scale paper',)],
    'title_str': r'\Large \textbf{Bicycle Cadence Calculator}',
    # 'make_grid': True,
    'title_x': 3.5,
    'title_y': 10.0,

    'extra_texts': [
        {
            'x': -0.5,
            'y': 11.3,
            'text': r'\large \slshape{Gearing Ratio}',
        },
        {
            'x': 7.0,
            'y': 20.5,
            'text': r'\large \slshape{Front derailer setting}',
        },
        {
            'text': r'\copyright Daniel Boulet (2019-2021)',
            'x': -0.5,
            'y': 9.5,
        },


    ]

}

Nomographer(main_params)
