from gl import Render, color

r = Render()
r.glCreateWindow(20,10)

r.glColor(0,1,1)

r.glClearColor(1,0,0)
    
r.glClear()

r.glViewPort(11,5,8, 4)


r.glVertex(-1,-1)
r.glVertex(1,1)
r.glVertex(-1,1)
r.glVertex(0,0)
r.glVertex(1,-1)
r.glVertex(-1,0)
r.glVertex(1,0)

r.glFinish('output.bmp')

