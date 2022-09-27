'''python program that provides different operations on 2-D vectors'''

import math

class Vectors2D:
    m = 1/(2**0.5) # a random variable defined for formation of unit vector

    def __init__(self,icap=m,jcap=m):
        self.icap=icap
        self.jcap=jcap

    # representation of vector in vector form 
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

    # magnitude of vector
    def magnitude(self):
        return (self.icap**2 + self.jcap**2)**0.5

    # unit vector of given vector
    def unitVector(self):
        return f"{(self.icap)*(1/self.magnitude())}i + {(self.jcap)*(1/self.magnitude())}j"

    # addition of two vectors
    def __add__(self,otherVec):
        return f"{self.icap + otherVec.icap}i + {self.jcap + otherVec.jcap}j"

    # subtraction of two vectors
    def __sub__(self,otherVec):
        return f"{self.icap - otherVec.icap}i + {self.jcap - otherVec.jcap}j"

    # dot product of two vectors 
    def __mul__(self,otherVec):
        return (self.icap * otherVec.icap) + (self.jcap * otherVec.jcap)

    # vector product of two vectors
    def vectorPdt(self,otherVec):
        return f"{(self.icap * otherVec.jcap) - (self.jcap * otherVec.icap)}k"

    # projection of vector self on otherVec
    def projection(self,otherVec):
        return (self * otherVec)*(1/(otherVec.magnitude()))
    
    # projection vector of self on otherVec
    def projectionVector(self,otherVec):
        projection=self.projection(otherVec)
        return f"{projection*otherVec.icap*(1/otherVec.magnitude())}i + {projection*otherVec.jcap*(1/otherVec.magnitude())}j"

    # angle between vectors in radian
    def angleBetweenVectors(self,otherVec):
        cosTheta = (self * otherVec)*(1/self.magnitude())*(1/self.magnitude())
        theta = math.acos(cosTheta)
        return theta

    # distance between the points having specified position vectors - self and otherVec
    def distanceBetweenPoints(self,otherVec):
        return ((self.icap - otherVec.icap)**2 + (self.jcap - otherVec.jcap)**2)**0.5
    
    #
    def internalBisectorVector(self,otherVec):
        pass

    #
    def externalBisectorVector(self,otherVec):
        pass

    # distance of point from the origin
    def distanceFromOrigin(self):
        return self.magnitude()
   
if __name__=="__main__":

    # while True:    
    #     try :
    #         x,y = input("Enter Coordinates of Vector A: ").split()
    #         a = Vectors2D(int(x),int(y))

    #         x,y = input("Enter Coordinates of Vector B: ").split()
    #         b = Vectors2D(int(x),int(y))

    #     except Exception as e:
    #         print("Error :",e)

    #     else :
    #         # print(a.add(b))           
   
    #         print(a)
    #         print(b)
    #         print(a+b)
    #         break


    a = Vectors2D(3,4)
    b = Vectors2D(5,12)
    c = Vectors2D() # to define unit vector
    
    print(f"vector a : {a}")
    print(f"vector b : {b}")
    print(c)
    print(f"magnitude of vector a : {a.magnitude()}")
    print(f"magnitude of vector b : {b.magnitude()}")
    print(f"unit vector of a : {a.unitVector()}")
    print(f"addition : {a+b}")
    print(f"subtraction : {a-b}")
    print(f"dot product : {a*b}")
    print(f"vector product : {a.vectorPdt(b)}")
    print(f"projection vector of a on b : {a.projection(b)}")
    print(a.projectionVector(b))




