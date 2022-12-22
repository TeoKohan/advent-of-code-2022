import re
from enum import Enum

class Material(Enum):
      Ore  = 0,
      Clay = 1,
      Obsidian = 2,
      Geode = 3
            
class Blueprint:
      def __init__(self, id, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian):
            self.id = id
            self.robots = {
                  Material.Ore     : {Material.Ore: ore_ore},
                  Material.Clay    : {Material.Ore: clay_ore},
                  Material.Obsidian: {Material.Ore: obsidian_ore, Material.Clay: obsidian_clay},
                  Material.Geode   : {Material.Ore: geode_ore, Material.Obsidian: geode_obsidian}
            }
      
      def __iter__(self):
            for material in Material:
                  yield material, self.robots[material]

      def __repr__(self):
            return str(self.robots)

quality_level_sum = 0
with open('input') as input:
      blueprints = input.read()[:-1]
      blueprints = blueprints.split('\n')
      blueprints = [Blueprint(*list(map(int, re.findall(r'\d+', blueprint)))) for blueprint in blueprints]
      
      def max_blueprint(blueprint, robots, materials, time):
            geodes = materials[Material.Geode] + robots[Material.Geode] * time
            if time <= 0:
                  return geodes
            for material in Material:
                  if any([robots[k] == 0 for k in blueprint.robots[material]]):
                        continue
                  elif all([materials[k] >= v for k, v in blueprint.robots[material].items()]):
                        minutes = 1
                  else:
                        build_materials = [(k, v - materials[k]) for k, v in blueprint.robots[material].items()]
                        minutes = max([((v // robots[m]) + (1 if v % robots[m] > 0 else 0)) if v > 0 else 0 for m, v in build_materials]) + 1   
                  purpose = (material == Material.Geode) or any([robots[material] < blueprint.robots[m][material] for m in Material if material in blueprint.robots[m]])
                  if minutes < time and purpose:
                        M = {m: materials[m] + robots[m] * minutes - (blueprint.robots[material][m] if m in blueprint.robots[material] else 0) for m in Material}
                        R = {m: robots[m] + (1 if m == material else 0) for m in Material}
                        geodes = max(geodes, max_blueprint(blueprint, R, M, time - minutes))
            return geodes

      start_robots = {
                  Material.Ore     : 1,
                  Material.Clay    : 0,
                  Material.Obsidian: 0,
                  Material.Geode   : 0    
            }

      start_materials = {
                  Material.Ore     : 0,
                  Material.Clay    : 0,
                  Material.Obsidian: 0,
                  Material.Geode   : 0
            }

      quality_levels = []
      for B in blueprints:
            quality_levels += [B.id * max_blueprint(B, start_robots, start_materials, 24)]
            print(B.id, '/', len(blueprints))
      quality_level_sum = sum(quality_levels)

with open('output', 'w') as output:
      output.write(str(quality_level_sum) + '\n')