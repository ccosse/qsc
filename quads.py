#!python
"""
  "Quadrilateralized spherical cube"
  Bounding RCCS grid projected onto an inscribed sphere
  Face 0 = North
  Face 1 = Meridian
  Faces 2,3,4 Equatorial
  Face 5 = South

  Need: lat,lng (spherical) -> x,y (rectangular)
  Benefit: Great circle distances expressed as planar displacements (?)
  https://en.wikipedia.org/wiki/Quadrilateralized_spherical_cube
  https://proj.org/en/9.3/operations/projections/qsc.html
"""
from math import *
pi=acos(-1)

r=1
N=4
dx=dy=dz=2/(2**N)

ouf=open('quads.dat','w')
ouf.write(f"X\tY\tZ\tT\n")#T=Type (corner,faces)

########################################
#draw padding points
T=0
for x in [-1.0,1.0]:
  for y in [-1.0,1.0]:
    for z in [-1.0,1.0]:
      line=f"{x}\t{y}\t{z}\t{T}\n"
      ouf.write(line)

#along z,y
T=1
x=1
for x_sign in [1,-1]: #faces 1 and 3
  for nz in range(0,1+2**N):
    z=-1+nz*dz
    for ny in range(0,1+2**N):
      y=-1+ny*dy
      r_xy=sqrt(x**2 + y**2)
      theta_xy=asin(y/r_xy)
      r_xyz=sqrt(x**2 + y**2 + z**2)
      phi=acos(z/r_xyz)
      xx=x_sign*r*sin(phi)*cos(theta_xy)
      yy=r*sin(phi)*sin(theta_xy)
      zz=r*cos(phi)
      line=f"{xx}\t{yy}\t{zz}\t{T}\n"
      ouf.write(line)

#along z,x
T=2
y=1
for x_sign in [-1,1]:
  for y_sign in [1,-1]: #faces 2 and 4
    for nz in range(0,1+2**N):
      z=-1+nz*dz
      for nx in range(0,1+2**N):
        x=-1+nx*dx
        r_xy=sqrt(x**2 + y**2)
        theta_xy=asin(y/r_xy)
        r_xyz=sqrt(x**2 + y**2 + z**2)
        phi=acos(z/r_xyz)
        xx=x_sign*r*sin(phi)*cos(theta_xy)
        yy=y_sign*r*sin(phi)*sin(theta_xy)
        zz=r*cos(phi)
        line=f"{xx}\t{yy}\t{zz}\t{T}\n"
        ouf.write(line)

#along x,y
#x->z, y->x, z->y (rotated rhs = 2 pi/2 rotations, reused faces 1,3 math)
T=3
z=1
for z_sign in [-1,1]: #faces 0 and 5
  for ny in range(0,1+2**N):
    y=-1+ny*dy
    for nx in range(0,1+2**N):
      x=-1+nx*dx
      r_zx=sqrt(z**2 + x**2)
      theta_zx=asin(x/r_zx)
      r_xyz=sqrt(x**2 + y**2 + z**2)
      phi=acos(y/r_xyz)
      zz=z_sign*r*sin(phi)*cos(theta_zx)
      xx=r*sin(phi)*sin(theta_zx)
      yy=r*cos(phi)
      line=f"{xx}\t{yy}\t{zz}\t{T}\n"
      ouf.write(line)


ouf.close()