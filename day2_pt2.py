input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
# Part 2 
all_games = []
game_powers = []

for line in input.splitlines():
  game_number = re.search(r"Game (\d+)", line).group(1)
  all_games.append(game_number)
  sets = line.split(';')
  per_set_max = {}
  for set in sets:
    for item in ['red', 'green', 'blue']:
      my_regex = r"(\d+)\s+" + item
      num_colour = re.search(my_regex, set)
      # if key doesn't exist in dictionary then create it
      if not item in per_set_max:
        per_set_max[item] = 0
      if num_colour is None:
        num_colour = 0
      else:
        num_colour = int(num_colour.group(1))
      if per_set_max[item] < num_colour:
        per_set_max[item] = num_colour
  power = 1
  for item in per_set_max.values():
    power *= item
  game_powers.append(power)
  print(f"game {game_number}: min cubes required = {per_set_max}\tGame Power = {power}")

# outputs
sum_of_powers = sum(item for item in game_powers)
print(f"Game Powers = {game_powers}")
print(f"Sum of powers = {sum_of_powers}")