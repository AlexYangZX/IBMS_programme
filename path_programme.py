import numpy as np


# 选择终点 影响map 无向图
node_map = [[0, 1, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 15, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 15, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0],
            [16, 0, 0, 0, 0, 17, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0],
            [0, 16, 0, 0, 17, 0, 11, 0, 0, 6, 0, 0, 0, 0, 0, 0],
            [0, 0, 5, 0, 0, 11, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 9, 0, 0, 5, 0, 0, 0, 0, 13, 0, 0, 0, 0],
            [0, 0, 0, 0, 15, 0, 0, 0, 0, 4, 0, 0, 8, 0, 0, 0],
            [0, 0, 0, 0, 0, 6, 0, 0, 4, 0, 16, 0, 0, 4, 0, 0],
            [0, 0, 0, 0, 0, 0, 3, 0, 0, 16, 0, 7, 0, 0, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 7, 0, 0, 0, 0, 14],
            [0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 1, 0, 14, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 14, 0, 16],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 16, 0]]


# 设置出口 两个
def set_end(end1, end2):
    node_map[end1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    node_map[end2] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return node_map


# 设置着火点
def set_fire_point(end1, end2, fire_point):
    node_map = set_end(end1, end2)
    mid_map = np.array(node_map)
    mid_map = mid_map.T
    mid_map[fire_point] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    node_map = mid_map.T

    return node_map


# 路径规划
def programme_path(end1, end2, fire_point):
    output_path =[]
    node = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    node.remove(end1)
    node.remove(end2)  # 将终点从需要遍历的节点中移除
    node_map = set_fire_point(end1, end2, fire_point)  # 获得路径规划map
    for start in node:
        path = []
        dis = []
        for i in range(0, len(node_map[start])):
            if node_map[start][i] != 0:
                if i == end1 or i == end2:
                    path.append([start, i])
                    dis.append(node_map[start][i])
                else:
                    for j in range(0, len(node_map[i])):
                        if node_map[i][j] != 0:
                            if j == end1 or j == end2:
                                path.append([start, i, j])
                                dis.append(node_map[start][i] + node_map[i][j])
                            else:
                                for m in range(0, len(node_map[j])):
                                    if node_map[j][m] != 0:
                                        if m == end1 or m == end2:
                                            path.append([start, i, j, m])
                                            dis.append(node_map[start][i] + node_map[i][j] + node_map[j][m])
                                        else:
                                            for n in range(0, len(node_map[m])):
                                                if node_map[m][n] != 0:
                                                    if n == end1 or n == end2:
                                                        path.append([start, i, j, m, n])
                                                        dis.append(node_map[start][i] + node_map[i][j] + node_map[j][m]
                                                                   + node_map[m][n])
                                                    else:
                                                        for p in range(0, len(node_map[n])):
                                                            if node_map[n][p] != 0:
                                                                if p == end1 or p == end2:
                                                                    path.append([start, i, j, m, n, p])
                                                                    dis.append(node_map[start][i] + node_map[i][j] +
                                                                               node_map[j][m] + node_map[m][n] +
                                                                               node_map[n][p])
                                                                else:
                                                                    for q in range(0, len(node_map[p])):
                                                                        if node_map[p][q] != 0:
                                                                            if q == end1 or q == end2:
                                                                                path.append([start, i, j, m, n, p, q])
                                                                                dis.append(node_map[start][i] +
                                                                                           node_map[i][j] +
                                                                                           node_map[j][m] +
                                                                                           node_map[m][n] +
                                                                                           node_map[n][p] +
                                                                                           node_map[p][q])

        shortest_path = path[dis.index(min(dis))]  # 最短路径长度对应的路径
        shortest_path_str = []
        for i in range(0, len(shortest_path)):
            shortest_path_str.append(str(shortest_path[i]))

        output_path.append(shortest_path_str)

    return output_path


# 输出路径
# 树莓派处理
def output_path(end1, end2, fire_point):
    m = programme_path(end1, end2, fire_point)
    path = []
    for i in range(0, len(m)):
        path_str = ''
        for j in range(0, len(m[i])):
            path_str = path_str + '*' + str(m[i][j])

        path.append(path_str)

    return path


# GUI显示
def output_path2(end1, end2, fire_point):
    m = programme_path(end1, end2, fire_point)
    arrow = '→'
    path = []
    for i in range(0, len(m)):
        path.append(arrow.join(m[i]))

    return path