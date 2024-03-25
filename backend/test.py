def line_equation(x, slope, intercept):
    """
    计算直线的方程：y = slope * x + intercept
    """
    return slope * x + intercept


def line_segment_intersection(line_slope, line_intercept, points):
    """
    检查折线段与给定直线是否有交点
    """
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]

        # 计算折线段的斜率和截距
        segment_slope = (y2 - y1) / (x2 - x1)
        segment_intercept = y1 - segment_slope * x1

        # 判断是否平行或重合
        if segment_slope == line_slope:
            continue

        # 计算交点的 x 坐标
        x_intersect = (line_intercept - segment_intercept) / (segment_slope - line_slope)
        # 计算交点的 y 坐标
        y_intersect = line_equation(x_intersect, line_slope, line_intercept)

        # 检查交点是否在折线段内
        if min(x1, x2) <= x_intersect <= max(x1, x2) and \
                min(y1, y2) <= y_intersect <= max(y1, y2):
            return True  # 存在交点

    return False  # 不存在交点


# 示例数据
line_slope = 2  # 直线斜率
line_intercept = 1  # 直线截距
points = [(1, 4), (2, 6), (3, 8)]  # 离散点列表，格式为 (x, y)

# 检查折线段与给定直线是否有交点
has_intersection = line_segment_intersection(line_slope, line_intercept, points)

if has_intersection:
    print("折线段与给定直线有交点")
else:
    print("折线段与给定直线无交点")
