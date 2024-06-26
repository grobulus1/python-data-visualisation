from random_walk import RandomWalk
import plotly.express as px

rw = RandomWalk(50_000)
rw.fill_walk()
fig = px.scatter(x=rw.x_values, y=rw.y_values)
fig.show()
