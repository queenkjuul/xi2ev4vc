from uinput import *

_CHAR_MAP = {
    "a":  KEY_A,
    "b":  KEY_B,
    "c":  KEY_C,
    "d":  KEY_D,
    "e":  KEY_E,
    "f":  KEY_F,
    "g":  KEY_G,
    "h":  KEY_H,
    "i":  KEY_I,
    "j":  KEY_J,
    "k":  KEY_K,
    "l":  KEY_L,
    "m":  KEY_M,
    "n":  KEY_N,
    "o":  KEY_O,
    "p":  KEY_P,
    "q":  KEY_Q,
    "r":  KEY_R,
    "s":  KEY_S,
    "t":  KEY_T,
    "u":  KEY_U,
    "v":  KEY_V,
    "w":  KEY_W,
    "x":  KEY_X,
    "y":  KEY_Y,
    "z":  KEY_Z,
    "1":  KEY_1,
    "2":  KEY_2,
    "3":  KEY_3,
    "4":  KEY_4,
    "5":  KEY_5,
    "6":  KEY_6,
    "7":  KEY_7,
    "8":  KEY_8,
    "9":  KEY_9,
    "0":  KEY_0,
    "\t": KEY_TAB,
    "\n": KEY_ENTER,
    " ":  KEY_SPACE,
    ".":  KEY_DOT,
    ",":  KEY_COMMA,
    "/":  KEY_SLASH,
    "\\": KEY_BACKSLASH,
    "-": KEY_MINUS,
    "=": KEY_EQUAL,
    "`": KEY_GRAVE,
    ";": KEY_SEMICOLON,
    "'": KEY_APOSTROPHE,
    "[": KEY_LEFTBRACE,
    "]": KEY_RIGHTBRACE,
    "(": KEY_KPLEFTPAREN,
    ")": KEY_KPRIGHTPAREN
}

_CODE_MAP = {
    9: KEY_ESC,
    22: KEY_BACKSPACE,
    36: KEY_ENTER,
    37: KEY_LEFTCTRL,
    50: KEY_LEFTSHIFT,
    63: KEY_NUMERIC_STAR,
    64: KEY_LEFTALT,
    66: KEY_CAPSLOCK,
    67: KEY_F1,
    68: KEY_F2,
    69: KEY_F3,
    70: KEY_F4,
    71: KEY_F5,
    72: KEY_F6,
    73: KEY_F7,
    74: KEY_F8,
    75: KEY_F9,
    76: KEY_F10,
    77: KEY_NUMLOCK,
    79: KEY_NUMERIC_7,
    80: KEY_NUMERIC_8,
    81: KEY_NUMERIC_9,
    82: KEY_MINUS,
    83: KEY_NUMERIC_4,
    84: KEY_NUMERIC_5,
    85: KEY_NUMERIC_6,
    # 86: KEY_NUMERIC_PLUS > not implemented
    87: KEY_NUMERIC_1,
    88: KEY_NUMERIC_2,
    89: KEY_NUMERIC_3,
    90: KEY_NUMERIC_0,
    95: KEY_F11,
    96: KEY_F12,
    108: KEY_RIGHTALT,
    104: KEY_ENTER,
    105: KEY_RIGHTCTRL,
    106: KEY_SLASH,
    110: KEY_HOME,
    111: KEY_UP,
    112: KEY_PAGEUP,
    113: KEY_LEFT,
    114: KEY_RIGHT,
    115: KEY_END,
    116: KEY_DOWN,
    117: KEY_PAGEDOWN,
    118: KEY_INSERT,
    119: KEY_DELETE,
    129: KEY_DOT,
    133: KEY_LEFTMETA,
    134: KEY_RIGHTMETA
}


def getMappedChar(char):
    return _CHAR_MAP.get(char) or None


def getMappedCode(code):
    return _CODE_MAP.get(code) or None