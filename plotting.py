from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import tickers

# create plot
f = figure(x_axis_type="datetime", height=100, width=500,
           title="Motion graph", sizing_mode="stretch_both")

# plot details
f.yaxis.minor_tick_line_color = None
f.yaxis.axis_label = None
f.xaxis.axis_label = None
f.yaxis.ticker.desired_num_ticks = 1

# write plot
quadrant = f.quad(left=df["Start"], right=df["End"],
                  bottom=0, top=1, color="Orange")
# save plot to file
output_file("motion_graph.html")

# open file in browser
show(f)