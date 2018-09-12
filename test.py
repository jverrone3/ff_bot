from ff_bot import ff_bot
from espnff import League

league = League(242712, 2018)

print(ff_bot.get_matchups(league))
print(ff_bot.get_scoreboard(league))
print(ff_bot.get_close_scores(league))
print(ff_bot.get_power_rankings(league))
print(ff_bot.get_trophies(league))
