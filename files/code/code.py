# Author: Raffaele Castellano
# Date: 2023-11-3
# Version: 3.0
# Description: KMK firmware for the vesuveus keyboard

# imports
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap
from kmk.modules.modtap import ModTap
from kmk.modules.mouse_keys import MouseKeys

# keyboard inizialization
keyboard = KMKKeyboard()

# pins
keyboard.col_pins = (board.GP11,board.GP10,board.GP9,board.GP8,board.GP7,board.GP6,board.GP5,board.GP4,board.GP3,board.GP2,board.GP1,board.GP0)
keyboard.row_pins = (board.GP12,board.GP13,board.GP14,board.GP15)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# modules
layers = Layers()
keyboard.modules.append(layers)

holdtap = HoldTap()
holdtap.tap_time = 300
keyboard.modules.append(holdtap)

modtap = ModTap()
keyboard.modules.append(modtap)

mousekeys = MouseKeys()
mousekeys.max_speed = 7
mousekeys.move_step = 0
mousekeys.scroll_step = 0
keyboard.modules.append(mousekeys)

# layers:
# tab on tap, layer1 on hold
TABL1 = KC.LT(1, KC.TAB, prefer_hold=True)
# delete on tap, layer1 on hold
DELL1 = KC.LT(1, KC.DEL, prefer_hold=True)
# tab on tap, layer2 on hold
TABL2 = KC.LT(2, KC.TAB, prefer_hold=True)
# esc on tap, layer2 on hold
ESCL2 = KC.LT(2, KC.ESC, prefer_hold=True)

# tapmod:
# spc on tap, shift on hold
SPCSFT = KC.HT(KC.SPC, KC.LSFT, prefer_hold=False)
# enter on tap, shift on hold
ENTSHF = KC.HT(KC.ENTER, KC.LSFT, prefer_hold=True)
# backspace on tap, shift on hold
BSPSHF = KC.HT(KC.BSPC, KC.LSFT, prefer_hold=True)

# layouts
# Q       W       E       R       T      ___     ___     Y       U       I       O       P
# A       S       D       F       G      ___     ___     H       J       K       L       ENTSHF
# LSFT    Z       X       C       V      ___     ___     B       N       M       UP      RSFT
# LCTL    LGUI    LALT    ESCL2   TAVL1  SPCSFT  BSPSHF  DELL1   TABL2   LEFT    DOWN    RIGHT
# --------------------------------------------------------------------------------
# N1      N2      N3      N4      N5     ___     ___     N6      N7      N8      N9      N0
# `       [       ]       (       )      ___     ___     #       ~       &       '       ENTSHF
# LSFT    /       *       -       =      ___     ___     ,       .       ?       UP      RSFT
# LCTL    LGUI    LALT    ESCL2   TABL1  SPCSFT  BSPSHF  DELL1   TABL2   LEFT    DOWN    RIGHT
# --------------------------------------------------------------------------------
# F1      F2      F3      F4      F5     ___     ___     F6      F7      F8      F9      F10
# F12     {       }       <       >      ___     ___     @       $       |       "       F11
# LSFT    %       ^       _       +      ___     ___     ;       :       !       MUP     RSFT
# LCTL    LGUI    LALT    ESCL2   MLC    MRC     WHUP    WHDN    TABL2   MLEFT   MDOWN   MRIGHT
# --------------------------------------------------------------------------------


keyboard.keymap = [
    
    # ALPHA LAYER
    [KC.Q,      KC.W,       KC.E,       KC.R,       KC.T,       KC.NO,          KC.NO,      KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,      
     KC.A,      KC.S,       KC.D,       KC.F,       KC.G,       KC.NO,          KC.NO,      KC.H,       KC.J,       KC.K,       KC.L,       ENTSHF, 
     KC.LSFT,   KC.Z,       KC.X,       KC.C,       KC.V,       KC.NO,          KC.NO,      KC.B,       KC.N,       KC.M,       KC.UP,      KC.RSFT,    
     KC.LCTL,   KC.LGUI,    KC.LALT,    ESCL2,      TABL1,      SPCSFT,         BSPSHF,     DELL1,      TABL2,      KC.LEFT,    KC.DOWN,    KC.RIGHT,],

    # NUM/SYM LAYER     
    [KC.N1,     KC.N2,      KC.N3,      KC.N4,      KC.N5,      KC.NO,          KC.NO,      KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,
     KC.GRV,    KC.LBRC,    KC.RBRC,    KC.LPRN,    KC.RPRN,    KC.NO,          KC.NO,      KC.HASH,    KC.TILD,    KC.AMPR,    KC.QUOT,    ENTSHF,
     KC.LSFT,   KC.SLSH,    KC.ASTR,    KC.MINS,    KC.EQL,     KC.NO,          KC.NO,      KC.COMM,    KC.DOT,     KC.QUES,    KC.UP,      KC.RSFT,
     KC.LCTL,   KC.LGUI,    KC.LALT,    ESCL2,      TABL1,      SPCSFT,         BSPSHF,     DELL1,      TABL2,      KC.LEFT,    KC.DOWN,    KC.RIGHT,],

    # FUN/SYM LAYER - MOUSE
    [KC.F1,     KC.F2,      KC.F3,      KC.F4,      KC.F5,      KC.NO,          KC.NO,      KC.F6,      KC.F7,      KC.F8,      KC.F9,      KC.F10,
     KC.F12,    KC.LCBR,    KC.RCBR,    KC.LABK,    KC.RABK,    KC.NO,          KC.NO,      KC.AT,      KC.DLR,     KC.PIPE,    KC.DQUO,    KC.F11,
     KC.LSFT,   KC.PERC,    KC.CIRC,    KC.UNDS,    KC.PLUS,    KC.NO,          KC.NO,      KC.SCLN,    KC.COLN,    KC.EXLM,    KC.MS_UP,   KC.RSFT,
     KC.LCTL,   KC.LGUI,    KC.LALT,    ESCL2,      KC.MB_LMB,  KC.MB_RMB,      KC.MW_UP,   KC.MW_DN,   TABL2,      KC.MS_LT,   KC.MS_DN,   KC.MS_RT,],

]

if __name__ == '__main__':
    keyboard.go()
