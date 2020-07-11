import struct

def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    # 2 bytes
    return struct.pack('=h',w)

def dword(d):
    # 4 bytes
    return struct.pack('=l',d)

def color(r, g, b):
    return bytes([b, g, r])

def decimal_to_rgb(decimal_array):
    rgb_array = []
    for i in range(3):
        rgb_array.append(int(round(decimal_array[i]*255)))
    return rgb_array

BLACK = color(0,0,0)
WHITE = color(255,255,255)

class Render(object):
    def __init__(self):
        self.curr_color = WHITE
        self.clear_color = BLACK
        self.viewport_coordinates = []

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()

    def glClear(self):
        self.pixels = [ [ self.clear_color for x in range(self.width)] for y in range(self.height) ]

    def glViewPort(self, x, y, width, height):
        self.viewport_initial_x = x
        self.viewport_initial_y = y
        self.viewport_witdth = width
        self.viewport_height = height
        self.viewport_final_x = x + width
        self.viewport_final_y = x + height
        
        
        # this is optional, since there's no need to have an array with the coordinates
        # In order to respect the viewport, there should only be a verification function called
        # that just verifies if the glVertex is inside the viewport.
        for x in range(self.viewport_initial_x ,self.viewport_final_x + 1):
            for y in range(self.viewport_initial_y,self.viewport_final_y + 1):
                self.viewport_coordinates.append([x,y])


    def glClearColor(self, r,g,b):
        rgb_array = decimal_to_rgb([r,g,b])
        self.clear_color = color(rgb_array[0], rgb_array[1], rgb_array[2])

    def glVertex(self, x, y):
        v_x = 0
        v_y = 0
        if(x >= 0 or x < 0):
            v_x = self.viewport_initial_x + int(round( self.viewport_witdth/2 + x * self.viewport_witdth/2))
        if(y >= 0 or y < 0):
            v_y = self.viewport_initial_y + int(round( self.viewport_height/2 + y * self.viewport_height/2))  
        self.pixels[v_y][v_x] = self.curr_color

    def glColor(self, r,g,b):
        rgb_array = decimal_to_rgb([r,g,b])
        self.curr_color = color(rgb_array[0], rgb_array[1], rgb_array[2])

    def glFinish(self, filename):
        archivo = open(filename, 'wb')

        # File header 14 bytes
        #archivo.write(char('B'))
        #archivo.write(char('M'))

        archivo.write(bytes('B'.encode('ascii')))
        archivo.write(bytes('M'.encode('ascii')))

        archivo.write(dword(14 + 40 + self.width * self.height * 3))
        archivo.write(dword(0))
        archivo.write(dword(14 + 40))

        # Image Header 40 bytes
        archivo.write(dword(40))
        archivo.write(dword(self.width))
        archivo.write(dword(self.height))
        archivo.write(word(1))
        archivo.write(word(24))
        archivo.write(dword(0))
        archivo.write(dword(self.width * self.height * 3))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))
        
        # Pixeles, 3 bytes cada uno

        for x in range(self.height):
            for y in range(self.width):
                archivo.write(self.pixels[x][y])

        archivo.close()











