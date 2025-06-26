
def bestMinute(starts, durations, our_duration, seconds_per_day, n):
  commercials = [(starts[i], durations[i]) for i in range(len(starts))]
  commercials.sort(key=lambda x: x[0])
  spaces = []
  if len(commercials) == 0:
    pass # TODO

  space_start = sum(commercials[0]) % seconds_per_day
  for start, duration in commercials[1:]:
    spaces.append((space_start, start - space_start))
    space_start = (start + duration) % seconds_per_day
  spaces.append((space_start, (commercials[0][0] - space_start) % seconds_per_day))

  last_space = spaces[-1]
  if sum(last_space) > seconds_per_day:
    spaces.append((0, sum(last_space) % seconds_per_day))
  
  available_spaces = [(space[0], space[1], i) for i, space in enumerate(spaces) if space[1] >= our_duration]

  max_remembered = -1
  best_start = -1

  if n > len(starts):
    return min([start for start, _, _ in available_spaces])

  for start, duration, i in available_spaces:
    i_n_commercial = commercials[(i + n) % len(commercials)]
    remembered = (i_n_commercial[0] - start) % seconds_per_day
    print(start, duration, i, remembered)
    if max_remembered < remembered:
      best_start = start
      max_remembered = remembered
  
  return best_start

print(bestMinute([30, 5, 51, 17, 49], [12, 6, 10, 3, 1], 1,100, 2))

  