#!/usr/bin/python
import json
from math import *
"""
  11-10-2023
  project a cube of l=1 onto a sphere or r=0.5
  centered at 0,0 spanning 8 Cartesian quadrants
  product a point cloud (set of points) representing 
  the projected seems/lines/grids. Let n=# of divisions 
  of each face (cell size). For n=1, then, we should have
  12 lines projected -- 4+4+4
"""

ouf=open('projected.dat','w')
ouf.write(f"X\tY\tZ\tT\n")#T=Type (corner,cube,sphere,projected)

#draw padding points
T=0
for x in [-1,1]:
  for y in [-1,1]:
    for z in [-1,1]:
      line=f"{x}\t{y}\t{z}\t{T}\n"
      ouf.write(line)


#draw cube edges:
T=1
r=0.5
for z in [-0.5,0.5]:
  for y in [-0.5,0.5]:
    for xx in range(0,100):
      x=-0.5+(xx/100)
      line=f"{x}\t{y}\t{z}\t{T}\n"
      ouf.write(line)

for x in [-0.5,0.5]:
  for y in [-0.5,0.5]:
    for zz in range(0,100):
      z=-0.5+(zz/100)
      line=f"{x}\t{y}\t{z}\t{T}\n"
      ouf.write(line)

for x in [-0.5,0.5]:
  for z in [-0.5,0.5]:
    for yy in range(0,100):
      y=-0.5+(yy/100)
      line=f"{x}\t{y}\t{z}\t{T}\n"
      ouf.write(line)


#draw circles in xy,yz,xz
pi=acos(-1)
T=2
z=0
for pct_theta_xy in range(0,100):
  theta_xy=2*pi*pct_theta_xy/100
  x=r*cos(theta_xy)
  y=r*sin(theta_xy)
  line=f"{x}\t{y}\t{z}\t{T}\n"
  ouf.write(line)

x=0
for pct_theta_yz in range(0,100):
  theta_yz=2*pi*pct_theta_yz/100
  z=r*cos(theta_yz)
  y=r*sin(theta_yz)
  line=f"{x}\t{y}\t{z}\t{T}\n"
  ouf.write(line)

y=0
for pct_theta_xz in range(0,100):
  theta_xz=2*pi*pct_theta_xz/100
  x=r*cos(theta_xz)
  z=r*sin(theta_xz)
  line=f"{x}\t{y}\t{z}\t{T}\n"
  ouf.write(line)

#project x-plane grids onto center
for X in [-0.5,0.5]:
  #march y, const z, +/- X
  T=3
  for Z in [-0.5,0.0,0.5]:
    for yy1 in range(0,11):
      Y=-0.5+yy1/10
      line=f"{X}\t{Y}\t{Z}\t{T}\n"
      #ouf.write(line)

      R=sqrt(3*(0.5**2))
      
      theta_xy=atan(Y/X)
      
      phi=asin(0.5/sqrt(X**2 + 0.5**2))
      
      for rr in range(0,11):
        line=f"{X*rr/10}\t{R*rr/10*sin(phi)*sin(theta_xy)}\t{Z*rr/10}\t{T}\n"
        ouf.write(line)
  #march z, const y, +/- X
  T=4
  for Y in [-0.5,0.0,0.5]:
    for zz1 in range(0,11):
      Z=-0.5+zz1/10
      line=f"{X}\t{Y}\t{Z}\t{T}\n"
      #ouf.write(line)

      R=sqrt(3*(0.5**2))
      
      theta_zy=atan(Z/X)
      
      phi=asin(0.5/sqrt(X**2 + 0.5**2))
      
      for rr in range(0,11):
        line=f"{X*rr/10}\t{Y*rr/10}\t{R*rr/10*sin(phi)*sin(theta_zy)}\t{T}\n"
        ouf.write(line)

#project y-plane grids onto center
for Y in [-0.5,0.5]:
  T=5
  #march x, const z, +/- Y
  for Z in [-0.5,0.0,0.5]:
    for xx1 in range(0,11):
      X=-0.5+xx1/10
      line=f"{X}\t{Y}\t{Z}\t{T}\n"
      #ouf.write(line)

      R=sqrt(3*(0.5**2))
      
      theta_xy=atan(X/Y)
      
      phi=asin(0.5/sqrt(X**2 + 0.5**2))
      
      for rr in range(0,11):
        line=f"{R*rr/10*sin(phi)*sin(theta_xy)}\t{Y*rr/10}\t{Z*rr/10}\t{T}\n"
        ouf.write(line)
  T=6
  #march z, const x, +/- Y
  for X in [-0.5,0.0,0.5]:
    for zz1 in range(0,11):
      Z=-0.5+zz1/10
      line=f"{X}\t{Y}\t{Z}\t{T}\n"
      #ouf.write(line)

      R=sqrt(3*(0.5**2))
      
      theta_yz=atan(Z/Y)
      
      phi=asin(0.5/sqrt(Y**2 + 0.5**2))
      
      for rr in range(0,11):
        line=f"{X*rr/10}\t{Y*rr/10}\t{R*rr/10*sin(phi)*sin(theta_yz)}\t{T}\n"
        ouf.write(line)

#project z-plane grids onto center
for Z in [-0.5,0.5]:
  T=7
  #march y, const x, +/- Z
  for X in [-0.5,0.0,0.5]:
    for yy1 in range(0,11):
      Y=-0.5+yy1/10
      line=f"{X}\t{Y}\t{Z}\t{T}\n"
      #ouf.write(line)

      R=sqrt(3*(0.5**2))
      
      theta_zy=atan(Y/Z)
      
      phi=asin(0.5/sqrt(Z**2 + 0.5**2))
      
      for rr in range(0,11):
        line=f"{X*rr/10}\t{R*rr/10*sin(phi)*sin(theta_zy)}\t{Z*rr/10}\t{T}\n"
        ouf.write(line)

  #march x, const y, +/- Z
  for Y in [-0.5,0.0,0.5]:
    T=8
    for xx1 in range(0,11):
      X=-0.5+xx1/10
      line=f"{X}\t{Y}\t{Z}\t{T}\n"
      #ouf.write(line)

      R=sqrt(3*(0.5**2))
      
      theta_zx=atan(X/Z)
      
      phi=asin(0.5/sqrt(Z**2 + 0.5**2))
      
      for rr in range(0,11):
        line=f"{R*rr/10*sin(phi)*sin(theta_zx)}\t{Y*rr/10}\t{Z*rr/10}\t{T}\n"
        ouf.write(line)

ouf.close