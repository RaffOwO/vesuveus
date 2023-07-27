print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap
from kmk.modules.modtap import ModTap

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP9,board.GP8,board.GP10,board.GP6,board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5)
keyboard.row_pins = (board.GP15,board.GP12,board.GP13,board.GP14)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
keyboard.modules.append(ModTap())

# tab on tap, numlayer on hold
TABNUM = KC.LT(1, KC.TAB)
# spc on tap, shift on hold
SPCSFT = KC.HT(KC.SPC, KC.LSFT)
# enter on tap, shift on hold
ENTSHF = KC.HT(KC.ENTER, KC.LSFT)


keyboard.keymap = [
    # ALPHA LAYER
    [KC.Q,      KC.W,       KC.E,       KC.R,       KC.T,           KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,      
     KC.A,      KC.S,       KC.D,       KC.F,       KC.G,           KC.H,       KC.J,       KC.K,       KC.L,       ENTSHF, 
     KC.LCTL,   KC.Z,       KC.X,       KC.C,       KC.V,           KC.B,       KC.N,       KC.M,       KC.UP,      KC.RIGHT,    
     KC.LGUI,   KC.LALT,    KC.___,     SPCSFT,     TABNUM,         KC.___,     KC.RSFT,    TABNUM,     KC.LEFT,    KC.DOWN,],

    # NUM LAYER
    [KC.N1,     KC.N2,      KC.N3,      KC.N4,      KC.N5,          KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      
     KC.F1,     KC.F2,      KC.F3,      KC.F4,      KC.F5,          KC.F6,      KC.F7,      KC.F8,      KC.F9,      KC.F10, 
     KC.LCTL,   KC.N11,     KC.N12,     KC.N13,     KC.N14,         KC.N15,     KC.N16,     KC.N17,     KC.N18,     KC.N19,    
     KC.LGUI,   KC.LALT,    KC.___,     SPCSFT,     TABNUM,         KC.___,     KC.RSFT,    TABNUM,     KC.N20,     KC.N21,],
]

if __name__ == '__main__':
    keyboard.go()