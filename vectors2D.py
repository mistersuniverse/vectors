'''python program that provides different operations on 2-D vectors'''

import math

class Vectors2D:
    m = round(1/(2**0.5),2) # a random variable defined for the formation of unit vector having value 1/root(2) by default

    def __init__(self,icap=m,jcap=m):
        self.icap=icap
        self.jcap=jcap

    # representation of vector in vector form 
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

    # magnitude of vector
    def magnitude(self):
        return round((self.icap**2 + self.jcap**2)**0.5,2)

    # angle from horizontal axis
    def argument(self):
        angle = math.atan(self.jcap/self.icap)

        return round(angle,2)

    # unit vector of given vector
    def unitVector(self):
        return round((self.icap)/(self.magnitude()),2),round((self.jcap)/(self.magnitude()),2)

    # addition of two vectors 
    def __add__(vecA,vecB):
        return (vecA.icap + vecB.icap),(vecA.jcap + vecB.jcap)

    # subtraction of two vectors
    def __sub__(vecA,vecB):
        return (vecA.icap - vecB.icap),(vecA.jcap - vecB.jcap)

    # multiplication of vector by scalar
    def __mul__(self,scalar):
        return self.icap*scalar,self.jcap*scalar

    # vector in polar form
    def polarForm(self):
        magnitude = self.magnitude()
        angle = self.argument() 

        return magnitude,angle
    
    # dot product of two vectors 
    @classmethod
    def dotPdt(cls,vecA,VecB):
        return (vecA.icap * VecB.icap) + (vecA.jcap * VecB.jcap)

    # vector product of two vectors - along kCap
    @classmethod
    def vectorPdt(cls,vecA,vecB):
        return (vecA.icap * vecB.jcap)-(vecA.jcap * vecB.icap)

    # projection of self on otherVec
    '''Formula Used : 
       projection of vectorA on VectorB = (dotPdt of vectorA & vectorB)/(magnitude of vectorB)
    '''
    def projection(self,otherVec):
        return round(Vectors2D.dotPdt(self,otherVec)/otherVec.magnitude(),2)
    
    # projection vector of self on otherVec
    '''Formula Used : 
       projection vector of vectorA on vectorB = (projection of vectorA on VectorB) * (unit vector of vectorB) 
    '''
    def projectionVector(self,otherVec):
        projection=self.projection(otherVec)
        otherVecUnitVecCoordinateHorizonatal,otherVecUnitVecCoordinateVertical = otherVec.unitVector()
        return projection*otherVecUnitVecCoordinateHorizonatal , projection*otherVecUnitVecCoordinateVertical
        

    # angle between vectors
    '''Formula Used : 
       costheta = (dotPdt of VectorA & vectorB)/(magnitude of VectorA * magnitude of VectorB)
    '''
    @classmethod
    def angleBetweenVectors(cls,vecA,vecB,degree=False):
        cosTheta = Vectors2D.dotPdt(vecA,vecB)/(vecA.magnitude() * vecB.magnitude())
        theta = math.acos(cosTheta)

        if degree == False :
            return round(theta,2)

        else :
            theta = math.degrees(theta)
            return round(theta,2)

    # distance between the points A & B having Position vectors vecA & vecB
    @classmethod
    def distanceBetweenPoints(cls,vecA,vecB):
        return round(((vecA.icap - vecB.icap)**2 + (vecA.jcap - vecB.jcap)**2)**0.5,2)

    # internal bisector vector of the given vector by Vector - Addtion of their unit vectors
    '''Formula Used : Addition resultant of two unit vectors concides its internal Bisector
    '''
    @classmethod
    def internalBisectorVector(cls,vecA,vecB): 
        VecAUnitCoordinateHorizonatal,VecAUnitCoordinateVertical = vecA.unitVector()    
        VecBUnitCoordinateHorizonatal,VecBUnitCoordinateVertical = vecB.unitVector()  

        newVeciCap = VecAUnitCoordinateHorizonatal + VecBUnitCoordinateHorizonatal
        newVecjCap = VecAUnitCoordinateVertical + VecBUnitCoordinateVertical
        # newVeciCap = (vecA.icap)*(1/vecA.magnitude()) + (vecB.icap)*(1/vecB.magnitude())
        # newVecjCap = (vecA.jcap)*(1/vecA.magnitude()) + (vecB.jcap)*(1/vecB.magnitude())
        return round(newVeciCap,2),round(newVecjCap,2)
    
    # external bisector vector of the given vector by Vector - Subtraction of their unit vectors
    '''Formula Used : Subtraction of two unit vectors concides its external Bisector
    '''
    @classmethod
    def externalBisectorVector(cls,vecA,vecB): 
        VecAUnitCoordinateHorizonatal,VecAUnitCoordinateVertical = vecA.unitVector()    
        VecBUnitCoordinateHorizonatal,VecBUnitCoordinateVertical = vecB.unitVector()  

        newVeciCap = VecAUnitCoordinateHorizonatal - VecBUnitCoordinateHorizonatal
        newVecjCap = VecAUnitCoordinateVertical - VecBUnitCoordinateVertical
        return round(newVeciCap,2),round(newVecjCap,2)
           
    # distance of point from the origin
    def distanceFromOrigin(self):
        return self.magnitude()

    # section formula
    '''Formula Used :

       m1           m2
       |-----------||----------|
       .            .          .
       A            O          B

       VectorO = (m2*vectorA + m1*vectorB)/(m1+m2)
    
    '''
    @classmethod 
    def sectionFormula(cls,vecA,vecB,AO,BO) : # AO/BO is ratio 
        m1,m2 = BO/(AO+BO), AO/(AO+BO)
        
        return round((vecA.icap*m1 + vecB.icap*m2),2),round((vecA.jcap*m1+vecB.jcap*m2),2)

    # midpoint formula
    @classmethod 
    def midpointFormula(cls,vecA,vecB,) :
        return round((vecA.icap+vecB.icap)/2,2),round((vecA.jcap+vecB.jcap)/2,2)


if __name__=="__main__":
    
    A = Vectors2D(3,4)
    B = Vectors2D(12,5)
    C = Vectors2D()             #unit vector

    print(A.magnitude(),B.magnitude(),C.magnitude())
    print(A.argument(),B.argument(),C.argument())
    print(A.unitVector(),B.unitVector(),C.unitVector())
    print(A + B)
    print(A-B)
    print(A*2, B*2, C*3)
    print(Vectors2D.dotPdt(A,B),Vectors2D.vectorPdt(A,B))
    print(A.projection(B))
    print(A.projectionVector(B))
    print(Vectors2D.angleBetweenVectors(A,B))
    print(Vectors2D.angleBetweenVectors(A,B,degree=True))
    print(Vectors2D.distanceBetweenPoints(A,B))
    print(Vectors2D.internalBisectorVector(A,B))
    print(Vectors2D.externalBisectorVector(A,B))
    print(A.distanceFromOrigin(),B.distanceFromOrigin())
    print(Vectors2D.sectionFormula(A,B,2,3))
    print(Vectors2D.midpointFormula(A,B))
