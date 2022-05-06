from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import tickers, HoverTool, ColumnDataSource
import pandas

# convert datetime to string
df["Start"] = pandas.to_datetime(df["Start"])
df["End"] = pandas.to_datetime(df["End"])
df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

# convert DataFrame type
cds = ColumnDataSource(df)

# create plot
f = figure(x_axis_type="datetime", height=100, width=500,
           title="Motion graph", sizing_mode="stretch_both")

# plot details
f.yaxis.minor_tick_line_color = None
f.yaxis.axis_label = None
f.xaxis.axis_label = None
f.yaxis.ticker.desired_num_ticks = 1

# write plot
quadrant = f.quad(left="Start", right="End",
                  bottom=0, top=1, color="Orange", source=cds)

# graph hover popup data
hover = HoverTool(tooltips=[("Start", "@Start_string"),
                            ("End", "@End_string")])

f.add_tools(hover)

# save plot to file
output_file("motion_graph.html")

# open file in browser
show(f)