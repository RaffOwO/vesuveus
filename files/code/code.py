# Author: Raffaele Castellano
# Date: 2023-07-27
# Version: 2.3
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
keyboard.col_pins = (board.GP9,board.GP8,board.GP7,board.GP6,board.GP5,board.GP4,board.GP3,board.GP2,board.GP1,board.GP0)
keyboard.row_pins = (board.GP10,board.GP11,board.GP12,board.GP13)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# modules
layers = Layers()
keyboard.modules.append(layers)

holdtap = HoldTap()
holdtap.tap_time = 200  
keyboard.modules.append(holdtap)

modtap = ModTap()
keyboard.modules.append(modtap)

mousekeys = MouseKeys()
mousekeys.max_speed = 6
mousekeys.move_step = 0
mousekeys.scroll_step = 0
keyboard.modules.append(mousekeys)

# layers:
# tab on tap, layer1 on hold
TAVL1 = KC.LT(1, KC.TAB, prefer_hold=False)
# delete on tap, layer1 on hold
DELL1 = KC.LT(1, KC.DEL, prefer_hold=False)
# esc on tap, layer1 on hold
ESCL1 = KC.LT(1, KC.ESC, prefer_hold=False)
# tab on tap, layer2 on hold
TABL2 = KC.LT(2, KC.TAB, prefer_hold=False)
# delete on tap, layer2 on hold
DELL2 = KC.LT(2, KC.DEL, prefer_hold=False)
# esc on tap, layer2 on hold
ESCL2 = KC.LT(2, KC.ESC, prefer_hold=False)

# tapmod:
# spc on tap, shift on hold
SPCSFT = KC.HT(KC.SPC, KC.LSFT, prefer_hold=False)
# enter on tap, shift on hold
ENTSHF = KC.HT(KC.ENTER, KC.LSFT, prefer_hold=False)
# backspace on tap, shift on hold
BSPSHF = KC.HT(KC.BSPC, KC.LSFT, prefer_hold=True)
# delete on tap, shift on hold
DELSHF = KC.HT(KC.DEL, KC.LSFT, prefer_hold=True)
# tab on tap, shift on hold
TABSHF = KC.HT(KC.TAB, KC.LSFT, prefer_hold=False)

# layouts
# Q       W       E       R       T           Y       U       I       O       P
# A       S       D       F       G           H       J       K       L       ENTSHF
# LCTL    Z       X       C       V           B       N       M       UP      RIGHT
# LGUI    LALT    ESCL2   TAVL1   SPCSFT      BSPSHF  DELL1   TABL2   LEFT    DOWN
# --------------------------------------------------------------------------------
# N1      N2      N3      N4      N5          N6      N7      N8      N9      N0
# `       [       ]       (       )           #       ~       &       '       ENTSHF
# LCTL    /       *       -       =           ,       .       ?       UP      RIGHT
# LGUI    LALT    ESCL2   TABL2   SPCSFT      BSPSHF  DELL2   TABL2   LEFT    DOWN
# --------------------------------------------------------------------------------
# F1      F2      F3      F4      F5          F6      F7      F8      F9      F10
# F12     {       }       <       >           @       $       |       "       F11
# LCTL    %       ^       _       +           ;       :       !       MUP     MRIGHT
# LGUI    LALT    ESCL2   MLC     MRC         WHUP    WHDN    TABL2   MLEFT   MDOWN
# --------------------------------------------------------------------------------


keyboard.keymap = [
    
    # ALPHA LAYER
    [KC.Q,      KC.W,       KC.E,       KC.R,       KC.T,           KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,      
     KC.A,      KC.S,       KC.D,       KC.F,       KC.G,           KC.H,       KC.J,       KC.K,       KC.L,       ENTSHF, 
     KC.LCTL,   KC.Z,       KC.X,       KC.C,       KC.V,           KC.B,       KC.N,       KC.M,       KC.UP,      KC.RIGHT,    
     KC.LGUI,   KC.LALT,    ESCL2,      TAVL1,      SPCSFT,         BSPSHF,     DELL1,      TABL2,      KC.LEFT,    KC.DOWN],

    # NUM/SYM LAYER     
    [KC.N1,     KC.N2,      KC.N3,      KC.N4,      KC.N5,          KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,
     KC.GRV,    KC.LBRC,    KC.RBRC,    KC.LPRN,    KC.RPRN,        KC.HASH,    KC.TILD,    KC.AMPR,    KC.QUOT,    ENTSHF,
     KC.LCTL,   KC.SLSH,    KC.ASTR,    KC.MINS,    KC.EQL,         KC.COMM,    KC.DOT,     KC.QUES,    KC.UP,      KC.RIGHT,
     KC.LGUI,   KC.LALT,    ESCL2,      TABL2,      SPCSFT,         BSPSHF,     DELL2,      TABL2,      KC.LEFT,    KC.DOWN],

    # FUN/SYM LAYER - MOUSE
    [KC.F1,     KC.F2,      KC.F3,      KC.F4,      KC.F5,          KC.F6,      KC.F7,      KC.F8,      KC.F9,      KC.F10,
     KC.F12,    KC.LCBR,    KC.RCBR,    KC.LABK,    KC.RABK,        KC.AT,      KC.DLR,     KC.PIPE,    KC.DQUO,    KC.F11,
     KC.LCTL,   KC.PERC,    KC.CIRC,    KC.UNDS,    KC.PLUS,        KC.SCLN,    KC.COLN,    KC.EXLM,    KC.MS_UP,   KC.MS_RT,
     KC.LGUI,   KC.LALT,    ESCL2,      KC.MB_LMB,  KC.MB_RMB,      KC.MW_UP,   KC.MW_DN,   TABL2,      KC.MS_LT,   KC.MS_DN],


]

if __name__ == '__main__':
    keyboard.go()
