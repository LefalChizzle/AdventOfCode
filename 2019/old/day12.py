import re
import operator
from math import gcd

def reduce(f, v, l):
    for e in l: v = f(v, e)
    return v

def lcm(a,b):
    return a*b//gcd(a,b)

def parse_input(data):
    data = [re.findall(r'-?\d+', l) for l in data.splitlines()]
    data = [[int(v) for v in d] for d in data]
    return [[d, [0,0,0]] for d in data]

def dims():
    return range(3)

def dim(moons, i):
    return [[p[i], v[i]] for p, v in moons]

def evolve_dim(moons):
    for mi, moon in enumerate(moons):
        for other in moons[mi+1:]:
            d = 1 if moon[0] < other[0] else -1 if moon[0] > other[0] else 0
            moon[1], other[1] = moon[1]+d, other[1]-d
    for moon in moons: moon[0] += moon[1]
    return moons

def evolve(moons):
    ds = [evolve_dim(dim(moons, i)) for i in dims()]
    return [[list(v) for v in zip(*d)] for d in zip(*ds)]

def energy(moon):
    return [sum([abs(v) for v in c]) for c in moon]

def total_energy(moon):
    return reduce(operator.mul, 1, energy(moon))

def system_energy(moons):
    return reduce(operator.add, 0, map(total_energy, moons))

def steps_to_loop(dim):
    n = [d[:] for d in dim]
    i = 1
    while evolve_dim(n) != dim: i += 1
    return i


moons = parse_input(open('day12.txt').read())
# Part 1
for j in range(1000): 
    moons = evolve(moons)
print(system_energy(moons))

# Part 2
loops = [steps_to_loop(dim(moons, i)) for i in dims()]
print(reduce(lcm, 1, loops))

'''
import os
import pathlib
import re
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent / 'lib'))

import aoc

from itertools import combinations
from math import gcd


def cmp(a, b):
  return (a > b) - (a < b)


def velocity(x1, y1, z1, x2, y2, z2):
  return [cmp(x1, x2), cmp(y1, y2), cmp(z1, z2)]


def parse(s):
  m = re.search(r'^<x=(\S+), y=(\S+), z=(\S+)>$', s)
  return [int(x) for x in m.groups()]


def move(p, v):
  for n in range(len(p)):
    p[n] += v[n]
  return p


def energy(p, v):
  return sum(abs(x) for x in p) * sum(abs(x) for x in v)


def lcm(a, b):
  return a * b // gcd(a, b)


def run():
  input_file = aoc.inputfile('input.txt')
  lines = open(input_file).readlines()

  # Part 1:
  # Find total energy after 1000 iterations
  # Iterate through a straightforward implementation of the problem
  # Track positions and velocities as lists of [x, y, z] lists
  STEPS = 1000
  positions = [parse(x.strip()) for x in lines]
  velocities = [[0, 0, 0] for _ in positions]

  for _ in range(STEPS):
    for i1, i2 in combinations(range(len(positions)), 2):
      for n, vel in enumerate(velocity(*positions[i1], *positions[i2])):
        velocities[i1][n] -= vel
        velocities[i2][n] += vel

    for i in range(len(positions))
      positions[i] = move(positions[i], velocities[i])

  total_energy = sum(energy(positions[i], velocities[i]) for i in range(len(positions)))
  print(f"Total energy: {total_energy}")

  # Part 2:
  # Find the number of iterations for the universe to repeat
  # Each plane operates independently (i.e. x relationships have no effect on y or z)
  # Calculate number of steps for each plane to independently repeat
  # Total steps is the least common multiple of the three planes' cycles
  #
  # Make sure that both position AND velocity reach the original state
  steps = [0, 0, 0]
  positions = [parse(x.strip()) for x in lines]

  for i in (range(3)):
    orig_plane = [x[i] for x in positions]
    orig_velocities = [0 for _ in positions]

    plane = [x[i] for x in positions]
    velocities = [0 for _ in positions]

    while True:
      for i1, i2 in combinations(range(len(plane)), 2):
        pull = cmp(plane[i1], plane[i2])
        velocities[i1] -= pull
        velocities[i2] += pull

      for n, vel in enumerate(velocities):
        plane[n] += velocities[n]

      steps[i] += 1

      # have we reached our initial state for this plane?
      if plane == orig_plane and velocities == orig_velocities:
        break

  total_steps = lcm(lcm(steps[0], steps[1]), steps[2])
  print(f"Repetition iterations: {total_steps}")


if __name__ == '__main__':
  run()
  sys.exit(0)
'''
