import sys
import sdl2
import sdl2.ext

color_name = "white"
color_map = {
        # Gray Scale
        "Licorice": [0, 0, 0],
        "Lead": [33, 33, 33],
        "Tungsten": [66, 66, 66],
        "Iron": [94, 94, 94],
        "Steel": [121, 121, 121],
        "Tin": [145, 145, 145],
        "Nickel": [146, 146, 146],
        "Aluminum": [169, 169, 169],
        "Magnesium": [192, 192, 192],
        "Silver": [214, 214, 214],
        "Mercury": [235, 235, 235],
        "Snow": [255, 255, 255],

        # Dark Set
        "Cayenne": [148, 17, 0],
        "Mocha": [148, 82, 0],
        "Asparagus": [146, 144, 0],
        "Fern": [79, 143, 0],
        "Clover": [0, 143, 0],
        "Moss": [0, 144, 81],
        "Teal": [0, 145, 147],
        "Ocean": [0, 184, 147],
        "Midnight": [1, 25, 147],
        "Eggplant": [83, 27, 147],
        "Plum": [148, 33, 147],
        "Maroon": [148, 23, 81],

        # Normal Set
        "Maraschino": [255, 38, 0],
        "Tangerine": [255, 147, 0],
        "Lemon": [255, 251, 0],
        "Lime": [142, 250, 0],
        "Spring": [0, 249, 0],
        "Sea Foam": [0, 250, 146],
        "Turquoise": [0, 253, 255],
        "Aqua": [0, 150, 255],
        "Blueberry": [4, 51, 255],
        "Grape": [148, 55, 255],
        "Magenta": [255, 64, 255],
        "Strawberry": [255, 47, 146],

        "Salmon": [255, 126, 121],
        "Cantaloupe": [255, 212, 121],
        "Banana": [255, 252, 121],
        "Honeydew": [212, 251, 121],
        "Flora": [151, 250, 121],
        "Spindrift": [151, 252, 214],
        "Ice": [115, 253, 255],
        "Sky": [118, 214, 255],
        "Orchid": [122, 129, 255],
        "Lavender": [215, 131, 255],
        "Bubblegum": [255, 133, 255],
        "Carnation": [255, 138, 216]

        }

print("Registering Colors")
sdl_color_map = {color_name: sdl2.ext.Color(*v) for color_name, v in color_map.items()}

qwerty_list = [
        # Top row
        sdl2.SDLK_BACKQUOTE, sdl2.SDLK_1, sdl2.SDLK_2, sdl2.SDLK_3, sdl2.SDLK_4, sdl2.SDLK_5,
        sdl2.SDLK_6, sdl2.SDLK_7, sdl2.SDLK_8, sdl2.SDLK_9, sdl2.SDLK_0, sdl2.SDLK_MINUS,

        # Second Row
        sdl2.SDLK_q, sdl2.SDLK_w, sdl2.SDLK_e, sdl2.SDLK_r, sdl2.SDLK_t, sdl2.SDLK_y,
        sdl2.SDLK_u, sdl2.SDLK_i, sdl2.SDLK_o, sdl2.SDLK_p, sdl2.SDLK_LEFTBRACKET, sdl2.SDLK_RIGHTBRACKET,

        # Third Row
        sdl2.SDLK_a, sdl2.SDLK_s, sdl2.SDLK_d, sdl2.SDLK_f, sdl2.SDLK_g, sdl2.SDLK_h,
        sdl2.SDLK_j, sdl2.SDLK_k, sdl2.SDLK_l, sdl2.SDLK_SEMICOLON, sdl2.SDLK_QUOTE, sdl2.SDLK_RETURN,

        # Forth Row
        sdl2.KMOD_LSHIFT, sdl2.SDLK_z, sdl2.SDLK_x, sdl2.SDLK_c, sdl2.SDLK_v, sdl2.SDLK_b,
        sdl2.SDLK_n, sdl2.SDLK_m, sdl2.SDLK_COMMA, sdl2.SDLK_PERIOD, sdl2.KMOD_RSHIFT
        ]

def render(window):
    sdl_color = sdl_color_map[color_name]
    surface = window.get_surface()
    sdl2.ext.draw.fill(surface, sdl_color)
    window.refresh()


def run():
    print("Running...")
    sdl2.ext.init()

    global color_name
    prev_color_name = color_name
    width = 800
    height = 500
    window = sdl2.ext.Window("Hello World!", size=(width, height), flags=sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP)
    window.show()

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.type == sdl2.SDL_KEYDOWN:
                try:
                    if event.key.keysym.mod != 0:
                        key_index = qwerty_list.index(event.key.keysym.mod)
                    else:
                        key_index = qwerty_list.index(event.key.keysym.sym)
                    color_name = list(color_map.keys())[key_index]
                    print(f"Color: {color_name}")
                except Exception as e:
                    print("Whoops")

        if color_name != prev_color_name:
            render(window)
            prev_color_name = color_name


if __name__ == "__main__":
    sys.exit(run())
