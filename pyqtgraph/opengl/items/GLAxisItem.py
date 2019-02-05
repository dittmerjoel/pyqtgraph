from OpenGL.GL import *
from .. GLGraphicsItem import GLGraphicsItem
from ... import QtGui



__all__ = ['GLAxisItem']

class GLAxisItem(GLGraphicsItem):
    """
    **Bases:** :class:`GLGraphicsItem <pyqtgraph.opengl.GLGraphicsItem>`
    
    Displays three lines indicating origin and orientation of local coordinate system. 
    
    """
    
    def __init__(self, size=None, antialias=True, glOptions='translucent',text_scale=None):
        GLGraphicsItem.__init__(self)
        if size is None:
            size = QtGui.QVector3D(1,1,1)
        self.antialias = antialias
        self.c_x = None
        self.c_y = None
        self.c_z = None
        self.text_scale = text_scale
        self.setSize(size=size)
        self.setColor([1,1,1],[1,1,1],[1,1,1])
        self.setGLOptions(glOptions)
    
    def setSize(self, x=None, y=None, z=None, size=None):
        """
        Set the size of the axes (in its local coordinate system; this does not affect the transform)
        Arguments can be x,y,z or size=QVector3D().
        """
        if size is not None:
            x = size.x()
            y = size.y()
            z = size.z()

        self.__size = [x,y,z]
        self.update()
        
    def size(self):
        return self.__size[:]

    def setColor(self,color_x=None, color_y=None, color_z=None):
        self.c_x = color_x
        self.c_y = color_y
        self.c_z = color_z






    def color(self):
        return self.__color[:]
    
    def paint(self):

        linesize = self.text_scale/6
        #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        #glEnable( GL_BLEND )
        #glEnable( GL_ALPHA_TEST )
        self.setupGLState()
        
        if self.antialias:
            glEnable(GL_LINE_SMOOTH)
            glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
            
        glBegin( GL_LINES )
        
        x,y,z = self.size()
        glColor4f(self.c_z[0], self.c_z[1], self.c_z[2], .6)  # z is green
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, z)

        for i in range(round(z)):
            glVertex3f(0, -linesize, i+1)
            glVertex3f(0, linesize, i+1)
            if i is not 0 and self.text_scale < 1:
                self.Num(i,-0.5,-0.2,i-linesize*3)
            if self.text_scale >= 1 and i is not 0 and i%10 == 0:
                self.Num(i, -0.5, -0.2, i-linesize*3)
        for i in range(10*round(z)):
            glVertex3f(0, -linesize/3, (i+1)/10)
            glVertex3f(0, linesize/3, (i+1)/10)

        glVertex3f(0,-linesize*10, z+0.5)
        glVertex3f(0, linesize*10,z+0.5)

        glVertex3f(0, -linesize*10, z + 0.5)
        glVertex3f(0, linesize*10, z + 0.5 + linesize*15)

        glVertex3f(0, linesize*10, z + 0.5 + linesize*15)
        glVertex3f(0, -linesize*10, z + 0.5 + linesize*15)

        #glTexImage3D()



        glColor4f(self.c_y[0], self.c_y[1], self.c_y[2], .6)  # y is yellow
        glVertex3f(0, 0, 0)
        glVertex3f(0, y, 0)

        for i in range(round(y)):
            glVertex3f(-linesize, i + 1, 0)
            glVertex3f(linesize, i + 1, 0)
            if i is not 0 and self.text_scale < 1:
                self.Num(i, -0.5, i, -0.2)
            if self.text_scale >= 1 and i is not 0 and i%10 == 0:
                self.Num(i, -0.5, i, -0.2)
        for i in range(10*round(y)):
            glVertex3f(-linesize/3, (i + 1)/10, 0)
            glVertex3f(linesize/3, (i + 1)/10, 0)

        glVertex3f(linesize*10,y+0.5,0)
        glVertex3f(0.5*linesize,y+0.5+linesize*10,0)

        glVertex3f(-linesize*10,y+0.5,0)
        glVertex3f(linesize*10,y+2+linesize*12,0)


        glColor4f(self.c_x[0], self.c_x[1], self.c_x[2], .6)  # x is blue
        glVertex3f(0, 0, 0)
        glVertex3f(x, 0, 0)

        for i in range(round(x)):
            glVertex3f(i + 1,-linesize,0)
            glVertex3f(i + 1, linesize, 0)
            if i is not 0 and self.text_scale < 1:
                self.Num(i, i+linesize*3, -0.5, -0.2)
            if self.text_scale >= 1 and i is not 0 and i%10 == 0:
                self.Num(i, i+linesize*3, -0.5, -0.2)
        for i in range(10*round(x)):
            glVertex3f((i + 1)/10, -linesize/3, 0)
            glVertex3f((i + 1)/10, linesize/3, 0)

        glVertex3f(x + 0.5, -linesize*10, 0)
        glVertex3f(x + 0.5 + linesize*10, linesize*10, 0)

        glVertex3f(x + 0.5, linesize*10, 0)
        glVertex3f(x + 0.5 + linesize*10, -linesize*10, 0)





        glEnd()

    def Num(self,num,pos_x,pos_y,pos_z):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        if self.text_scale == None:
            scale = 0.1
        else:
            scale = self.text_scale



        if num == 0:
            glVertex3f(self.pos_x, self.pos_y, self.pos_z)
            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale)

            glVertex3f(self.pos_x-scale/2, self.pos_y, self.pos_z)
            glVertex3f(self.pos_x-scale/2, self.pos_y, self.pos_z + scale)

            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale)

            glVertex3f(self.pos_x, self.pos_y, self.pos_z)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z)

        if num == 1:
            glVertex3f(self.pos_x,self.pos_y,self.pos_z)
            glVertex3f(self.pos_x, self.pos_y, self.pos_z+scale)


        if num == 2:
            glVertex3f(self.pos_x,self.pos_y,self.pos_z)
            glVertex3f(self.pos_x-scale/2, self.pos_y, self.pos_z)

            glVertex3f(self.pos_x - scale/2, self.pos_y, self.pos_z)
            glVertex3f(self.pos_x - scale/2, self.pos_y, self.pos_z+scale/2)

            glVertex3f(self.pos_x - scale/2, self.pos_y, self.pos_z + scale/2)
            glVertex3f(self.pos_x, self.pos_y, self.pos_z+scale/2)

            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale / 2)
            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale)

            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale)
            glVertex3f(self.pos_x-scale/2, self.pos_y, self.pos_z + scale)

        if num == 3:
            glVertex3f(self.pos_x, self.pos_y, self.pos_z)
            glVertex3f(self.pos_x-scale/2, self.pos_y, self.pos_z)

            glVertex3f(self.pos_x, self.pos_y, self.pos_z+scale/2)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z+scale/2)

            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale)

            glVertex3f(self.pos_x, self.pos_y, self.pos_z)
            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale)

        if num == 4:
            glVertex3f(self.pos_x, self.pos_y, self.pos_z)
            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale)

            glVertex3f(self.pos_x-scale/2, self.pos_y, self.pos_z + scale)
            glVertex3f(self.pos_x - scale/2, self.pos_y, self.pos_z + scale/2)

            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale / 2)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale / 2)

        if num == 5:
            glVertex3f(self.pos_x, self.pos_y, self.pos_z)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z)

            glVertex3f(self.pos_x, self.pos_y, self.pos_z)
            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale / 2)

            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale / 2)
            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale / 2)

            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale / 2)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale)

            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale)

        if num == 6:
            glVertex3f(self.pos_x, self.pos_y, self.pos_z)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z)

            glVertex3f(self.pos_x, self.pos_y, self.pos_z)
            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale / 2)

            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale / 2)
            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale / 2)

            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale / 2)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale)

            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale)

            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale / 2)

        if num == 7:
            glVertex3f(self.pos_x,self.pos_y,self.pos_z)
            glVertex3f(self.pos_x, self.pos_y, self.pos_z+scale)

            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale)

        if num == 8:
            glVertex3f(self.pos_x, self.pos_y, self.pos_z)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z)

            glVertex3f(self.pos_x, self.pos_y, self.pos_z)
            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale)

            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale / 2)
            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale / 2)

            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale / 2)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale)

            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale)

            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale / 2)

        if num == 9:
            glVertex3f(self.pos_x, self.pos_y, self.pos_z)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z)

            glVertex3f(self.pos_x, self.pos_y, self.pos_z)
            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale)

            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale / 2)
            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale / 2)

            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale / 2)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale)

            glVertex3f(self.pos_x, self.pos_y, self.pos_z + scale)
            glVertex3f(self.pos_x - scale / 2, self.pos_y, self.pos_z + scale)

        if num >= 10:
            self.Num(round((num/10-num//10)*10),self.pos_x,self.pos_y,self.pos_z)
            self.Num(num//10, self.pos_x-scale, self.pos_y, self.pos_z)









