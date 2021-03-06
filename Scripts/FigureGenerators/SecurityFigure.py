# Created by Partha at 2/1/20
import numpy as np
from matplotlib import pyplot as plt

from Base.common import get_question_from_header
from CodeSample.SampleGenerator import get_formatted_dataframe
from FigureGenerators.ManagerExpectationFigure import ManagerExpectationFigureController


class SecurityFigureController(ManagerExpectationFigureController):
    ylabel = ""
    xlabel = "Percentage of Respondents(%)"
    directory_name = "Security.eps"
    figure_height = 20
    figure_width = 10
    y_tick_size = 30


if __name__ == "__main__":
    column_name = "security"
    question_file_name = get_question_from_header(column_name).rstrip()[:-1].rstrip().replace(" ", "_") + "__1.csv"
    dataframe, unique_codes = get_formatted_dataframe(question_file_name)
    group = {
        "Authentication and Authorization":["Application Side Measures","OAuth2 Protocol","Token-based Authentication","Measures for Request Forgery","Formal verification","Multi-prong Standard Process"],
        "Encryption":["Encryption at Various Levels"],
        "Framework/Platform/Tools":["Continuous Upgrading","Dependent on framework","Using Tools","Network Level Measures"]
    }
    # for item in sorted(unique_codes):
    #     print(item)
    controller = SecurityFigureController(dataframe)
    controller.process_data(unique_codes=unique_codes, exclude_data=['Did not responded','Nothing'])
    temp = {key: 0 for key in group.keys()}
    for key, value in controller.plot_data.items():
        for group_key, group_value in group.items():
            if key.lower() in list(map(lambda x: x.lower(), group_value)):
                temp[group_key] += value
                break

    print(controller.plot_data.items())
    print({k: v for k, v in sorted(temp.items(), key=lambda item: item[1], reverse=True)})

    controller.draw_figure(save=True)