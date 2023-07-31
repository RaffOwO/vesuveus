# Author: Raffaele Castellano
# Date: 2023-07-27

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap
from kmk.modules.modtap import ModTap

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP9,board.GP8,board.GP7,board.GP6,board.GP5,board.GP4,board.GP3,board.GP2,board.GP1,board.GP0)
keyboard.row_pins = (board.GP10,board.GP11,board.GP12,board.GP13)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
keyboard.modules.append(ModTap())

# layers:
# tab on tap, layer1 on hold
TAVBL1 = KC.LT(1, KC.TAB)
# delete on tap, layer1 on hold
DELL1 = KC.LT(1, KC.DEL)
# esc on tap, layer1 on hold
ESCL1 = KC.LT(1, KC.ESC)
# tab on tap, layer2 on hold
TABL2 = KC.LT(2, KC.TAB)
# delete on tap, layer2 on hold
DELL2 = KC.LT(2, KC.DEL)
# esc on tap, layer2 on hold
ESCL2 = KC.LT(2, KC.ESC)
# to layer 1 
LAYR1 = KC.TO(0)
# to layer 3
LAYR3 = KC.TO(3)

# tapmod:
# spc on tap, shift on hold
SPCSFT = KC.HT(KC.SPC, KC.LSFT)
# enter on tap, shift on hold
ENTSHF = KC.HT(KC.ENTER, KC.LSFT)
# backspace on tap, shift on hold
BSPSHF = KC.HT(KC.BSPC, KC.LSFT)
# delete on tap, shift on hold
DELSHF = KC.HT(KC.DEL, KC.LSFT)
# tab on tap, shift on hold
TABSHF = KC.HT(KC.TAB, KC.LSFT)

# layouts
# Q       W       E       R       T           Y       U       I       O       P
# A       S       D       F       G           H       J       K       L       ENTSHF
# LCTL    Z       X       C       V           B       N       M       UP      RIGHT
# LGUI    LALT    ESCL2   TAVBL1  SPCSFT      BSPSHF  DELL1   TABL2   LEFT    DOWN
# --------------------------------------------------------------------------------
# N1      N2      N3      N4      N5          N6      N7      N8      N9      N0
# `       [       ]       {       }           #       ?       %       :       ENTSHF
# LCTL    ^       *       -       =           .       '       |       UP      RIGHT
# LGUI    LALT    LAYER3  TABL2   SPCSFT      BSPSHF  DELL2   LAYER3  LEFT    DOWN
# --------------------------------------------------------------------------------
# F1      F2      F3      F4      F5          F6      F7      F8      F9      F10
# ~       {       }       <       >           @       !       $       ;       F11
# LCTL    %       /       _       +           ,       "       &       UP      RIGHT
# LGUI    LALT    LAYER3  TABSHF  SPCSFT      BSPSHF  DELSHF  LAYER3  LEFT    DOWN
# --------------------------------------------------------------------------------
# N1      Q       W       E       R           T       Y       U       I       O
# SHIFT   A       S       D       F           G       H       J       K       L
# LCTL    Z       X       C       V           B       N       M       UP      RIGHT
# LAYER1  LALT    ESC     TAB     SPACE       ENTER   BSPSHF  P       LEFT    DOWN


keyboard.keymap = [
    
    # ALPHA LAYER
    [KC.Q,      KC.W,       KC.E,       KC.R,       KC.T,           KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,      
     KC.A,      KC.S,       KC.D,       KC.F,       KC.G,           KC.H,       KC.J,       KC.K,       KC.L,       ENTSHF, 
     KC.LCTL,   KC.Z,       KC.X,       KC.C,       KC.V,           KC.B,       KC.N,       KC.M,       KC.UP,      KC.RIGHT,    
     KC.LGUI,   KC.LALT,    ESCL2,      TAVBL1,     SPCSFT,         BSPSHF,     DELL1,      TABL2,      KC.LEFT,    KC.DOWN],

    # NUM/SYM LAYER     
    [KC.N1,     KC.N2,      KC.N3,      KC.N4,      KC.N5,          KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,
     KC.GRV,    KC.LBRC,    KC.RBRC,    KC.LCBR,    KC.RCBR,        KC.HASH,    KC.QUES,    KC.PERC,    KC.COLN,    ENTSHF,
     KC.LCTL,   KC.CIRC,    KC.ASTR,    KC.MINS,    KC.EQL,         KC.DOT,     KC.QUOT,    KC.PIPE,    KC.UP,      KC.RIGHT,
     KC.LGUI,   KC.LALT,    LAYR3,      TABSHF,     SPCSFT,         BSPSHF,     DELSHF,     LAYR3,      KC.LEFT,    KC.DOWN],

    # FUN/SYM LAYER
    [KC.F1,     KC.F2,      KC.F3,      KC.F4,      KC.F5,          KC.F6,      KC.F7,      KC.F8,      KC.F9,      KC.F10,
     KC.TILD,   KC.LCBR,    KC.RCBR,    KC.LABK,    KC.RABK,        KC.AT,      KC.EXLM,    KC.DLR,     KC.SCLN,    KC.F11,
     KC.LCTL,   KC.PERC,    KC.SLSH,    KC.UNDS,    KC.PLUS,        KC.COMM,    KC.DQUO,    KC.AMPR,    KC.UP,      KC.RIGHT,
     KC.LGUI,   KC.LALT,    LAYR3,      TABSHF,     SPCSFT,         BSPSHF,     DELSHF,     LAYR3,      KC.LEFT,    KC.DOWN],

    # LAYER 3 - GAMING
    [KC.N1,     KC.Q,       KC.W,       KC.E,       KC.R,           KC.T,       KC.Y,       KC.U,       KC.I,       KC.O,
     KC.LSFT,   KC.A,       KC.S,       KC.D,       KC.F,           KC.G,       KC.H,       KC.J,       KC.K,       KC.L,
     KC.LCTL,   KC.Z,       KC.X,       KC.C,       KC.V,           KC.B,       KC.N,       KC.M,       KC.UP,      KC.RIGHT,
     LAYR1,     KC.LALT,    KC.ESC,     TABL2,      KC.SPC,         KC.ENT,     BSPSHF,     KC.P,       KC.LEFT,    KC.DOWN],
]

if __name__ == '__main__':
    keyboard.go()

