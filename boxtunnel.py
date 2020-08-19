# Original problem: https://www.hackerrank.com/challenges/too-high-boxes/problem
""" Problem:

Some boxes will be transported through a tunnel, where each box is a parallelepiped,
and is characterized by its length, width and height.

The height of the tunnel is 41 feet and the width can be assumed to be infinite.
A box can be carried through the tunnel only if its height is strictly less than
the tunnel's height. Find the volume of each box that can be successfully transported
to the other end of the tunnel.

Note: Boxes cannot be rotated. """

max_height = 41 # Height of the tunnel, width assumed infinite
n = int(input("How many boxes to go through tunnel? > "))

for i in range(0,n):

	try:
		l, w, h = [float(i) for i in input().split()]
		
	except:
		raise ValueError

	volume = l*w*h

	if h < 41: print("This box can go through tunnel. It's volume = {volume} cubic unit".format(volume=volume))
	else: print("This box won't fit through the tunnel.")
