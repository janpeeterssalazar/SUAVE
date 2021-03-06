# Linear.py
#
# Created:  Aug 2015, T. Lukacyzk
# Modified: Feb 2016, T. MacDonald

# ----------------------------------------------------------------------
#   Imports
# ----------------------------------------------------------------------

from ScalingFunction import ScalingFunction


# ----------------------------------------------------------------------
#   Linear Scaling Function
# ----------------------------------------------------------------------

class Linear(ScalingFunction):
    def __init__(self,scale,center=0.0):
        """ o / scl ==> (o-center)/scale
            o * scl ==> (o*scale)+center
        """
        self.scale  = scale
        self.center = center
        
    def set_scaling(self,other):
        return (other-self.center)/self.scale
    def unset_scaling(self,other):
        return other*self.scale + self.center
    
    def set_scaling_gradient(self,other):
        return other/self.scale
    def unset_scaling_gradient(self,other):
        return other*self.scale
    
    
# ----------------------------------------------------------------------
#   Module Tests
# ----------------------------------------------------------------------

if __name__ == '__main__':
    
    import numpy as np
    
    s = Linear(10.0,0.0)
    
    a = 10.0
    b = np.array([1,20,3.])
    
    print a
    print b
    
    a = a / s    
    b = b / s
    
    print a
    print b
    
    a = a * s    
    b = b * s    
    
    print a
    print b