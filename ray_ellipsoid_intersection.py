# ray_ellipsoid_intersection.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
# 
# Arguments:
#   d_l_x: x-component of origin-referenced ray direction
#   d_l_y: y-component of origin-referenced ray direction
#   d_l_z: z-component of origin-referenced ray direction
#   c_l_x: x-component offset of ray origin
#   c_l_y: y-component offset of ray origin
#   c_l_z: z-component offset of ray origin
#
# Written by Wheat Sturtevant
# Other contributors: None

# import Python modules
import math # math module
import sys  # argv

# constants
R_E_KM = 6378.1363
E_E = 0.081819221456
w = 7.292115*10**-5

# parse script arguments (always 1 more than the number of arguments)
if len(sys.argv) == 7:
    d_l_x = float(sys.argv[1])
    d_l_y = float(sys.argv[2])
    d_l_z = float(sys.argv[3])
    c_l_x = float(sys.argv[4])
    c_l_y = float(sys.argv[5])
    c_l_z = float(sys.argv[6])
else:
    print(\
        'python3 conv_ops.py d_l_x, d_l_y, d_l_z, c_l_x, c_l_y, c_l_z'\
            )
    exit()

# write script below this line
a = d_l_x*d_l_x + d_l_y*d_l_y+(d_l_z*d_l_z)/(1-E_E*E_E)
b = 2*(d_l_x*c_l_x+d_l_y*c_l_y+(d_l_z*c_l_z)/(1-E_E**2))
c = c_l_x**2+c_l_y**2+(c_l_z**2)/(1-E_E**2)-R_E_KM**2
disc = b*b-4.0*a*c

if disc >= 0:
    d = (-b-math.sqrt(disc))/(2*a)
    if d < 0:
        d = (-b+math.sqrt(disc))/(2*a)
    if d > 0:
        l_d = [d*d_l_x+c_l_x, d*d_l_y+c_l_y, d*d_l_z+c_l_z]

print(l_d[0]) # x-component
print(l_d[1]) # y-component
print(l_d[2]) # z-component

# Test usage
# python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z