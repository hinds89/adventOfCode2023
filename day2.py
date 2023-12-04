import re

max_cubes = { "red": 12,
             "green": 13,
              "blue": 14 }

input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

colours = {}
all_games = []
possible_games = []
impossible_games = []

for line in input.splitlines():
  game_number = re.search(r"Game (\d+)", line).group(1)
  all_games.append(game_number)
  sets = line.split(';')
  for set in sets:
    for item in ['red', 'green', 'blue']:
      my_regex = r"(\d+)\s+" + item
      x = re.search(my_regex, set)
      if x is None:
        colours[item] = 0
      else:
        colours[item] = int(x.group(1))
    # print(f"colours['red'] = {colours['red']}, colours['green'] = {colours['green']}, colours['blue'] = {colours['blue']}")
    # check for impossible games
    if colours['red'] > max_cubes['red'] or colours['green'] > max_cubes['green'] or colours['blue'] > max_cubes['blue']:
      impossible_games.append(game_number)
          # print(f"colours['blue'] <= max_cubes['blue'] ...{colours['blue']} <= {max_cubes['blue']}: {colours['blue'] <= max_cubes['blue']} ")
          # print(f"{game_number}, set {set} is good")
          # print()
    colours['red'] = 0
    colours['green'] = 0
    colours['blue'] = 0

# outputs
possible_games = [x for x in all_games if x not in impossible_games]

for item in ["all_games", "possible_games", "impossible_games"]:
  my_str = f"{item} = {globals()[item]}"
  print(my_str)

id_sum = sum(int(item) for item in possible_games)
print(f"sum_of_ideas = {id_sum}")