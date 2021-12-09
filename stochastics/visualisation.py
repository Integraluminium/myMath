from stochastics.binominal import Binominal
import plotly.express as px
import pandas as pd
from collections import defaultdict


def sort_formulas(*binominal_formula: Binominal):
    res = defaultdict(list)
    for formula in binominal_formula:
        for key, value in formula.get_all().items():
            res[key].append(value)
    return res


def make_histogram(*binominal_formula: Binominal):
    all_res = sort_formulas(*binominal_formula)
    # all_res = binominal_formula.get_all()
    print(all_res)
    data_frame = pd.DataFrame.from_dict(all_res, orient="index", columns=[str(formula) for formula in binominal_formula])
    print(data_frame)
    fig = px.bar(data_frame) #, x="k", y="deviation")
    fig.write_html("histogram.html", auto_open=True)


if __name__ == '__main__':
    func = Binominal(100, 0.25)
    # func1 = Binominal(10, 0.5)
    func2 = Binominal(101, 0.75)
    func3 = Binominal(100, 0.5)
    make_histogram(func3, func, func2) #, func1, func3)
