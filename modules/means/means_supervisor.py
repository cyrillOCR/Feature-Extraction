from modules.means.mean_horizontal_distances import mean_vertical_distance
from modules.means.mean_left_right import mean_left_right
from modules.means.mean_margins_bottom_top import mean_margins_bottom_top
from modules.means.mean_margins_left_right import mean_margins_left_right
from modules.means.mean_square_horizontal_vertical import mean_horizontal_vertical
from modules.means.mean_vertical_distances import mean_vertical_distance
from modules.means.mean_vertical_horizontal_on import mean_square_vertical_horizontal_on

def means_supervisor_function(matrix_of_letter):
    means_result = list()

    means_result.append(mean_vertical_distance(matrix_of_letter))
    means_result.append(mean_left_right(matrix_of_letter))
    means_result.append(mean_margins_bottom_top(matrix_of_letter))
    #means_result.append(mean_margins_left_right(matrix_of_letter))
    # # means_result.append(compute_mean_of_horizontal_positions(matrix_of_letter))
    #means_result.append(mean_horizontal_vertical(matrix_of_letter))
    ##means_result.append(mean_vertical_distance(matrix_of_letter))
    #means_result.append(mean_square_vertical_horizontal_on(matrix_of_letter))

    return tuple(means_result)
