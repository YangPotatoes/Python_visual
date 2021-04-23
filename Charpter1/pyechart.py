from pyecharts.charts import Map
from pyecharts import options as opts
import pandas as pd

covid_data = pd.read_csv("疫情-2021-04-15.csv")
# print(covid_data)
data = covid_data['省份']
value = covid_data['确诊人数']
covid_dict = dict(zip(data, value))
map = (
    Map().add("", list(covid_dict.items()), "china").set_global_opts(
        title_opts=opts.TitleOpts(title="各省市疫情现有数据",
                                  subtitle="数据来源：国家卫健委",
                                  pos_right="center",
                                  pos_top="5%"),
        visualmap_opts=opts.VisualMapOpts(
            max_=68151, is_piecewise=True,
            pieces=[{"max": 9, "min": 0, "label": "0-9", "color": "#FFE4E1"},
                    {"max": 99, "min": 10, "label": "10-99", "color": "#FF7F50"},
                    {"max": 499, "min": 100, "label": "100-499", "color": "#F08080"},
                    {"max": 999, "min": 500, "label": "500-999", "color": "#CD5C5C"},
                    {"max": 68151, "min": 1000, "label": ">=1000", "color": "#8B0000"}]
        )

    )
)
map.render()

