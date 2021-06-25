import pandas as pd
import matplotlib.pyplot as plt
from data import games

plays = games[games['type'] == 'play']
strike_outs = plays[plays['column'].str.contains('K')]
strike_outs = strike_outs.groupby(['year', 'game_id']).size()
strike_outs = strike_outs.rese_index(name='strike_outs')
strike_outs = strike_outs.loc[:, ['year', 'strike_outs']].apply(pd.to_numeric)
strike_outs.plot(x='year', y='strike_outs', kind='scatter').legend(['Strike Outs'])
plt.show()
