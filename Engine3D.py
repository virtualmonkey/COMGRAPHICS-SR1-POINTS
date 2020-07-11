from gl import Render, color

r = Render()
r.glCreateWindow(4,3)

r.glColor(0,1,1)

r.glClearColor(1,0,0)
    
r.glClear()

r.glViewPort(0,0,2,3)

r.point(1,2)

# posX = 10
# posY = 40

# for x in range(50):
#     r.point( posX, posY )
#     posX += 1
#     posY += 1


r.glFinish('output.bmp')

#r.set_color(color(255,0,0))


