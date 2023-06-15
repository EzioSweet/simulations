import plotly.graph_objects as go

# 定义长方体的顶点坐标
x = [0, 0, 1, 1, 0, 0, 1, 1]
y = [0, 1, 1, 0, 0, 1, 1, 0]
z = [0, 0, 0, 0, 1, 1, 1, 1]

# 定义长方体的面
faces = [
    [0, 1, 2, 3],  # 底面
    [4, 5, 6, 7],  # 顶面
    [0, 1, 5, 4],  # 前面
    [1, 2, 6, 5],  # 右面
    [2, 3, 7, 6],  # 后面
    [3, 0, 4, 7]   # 左面
]

# 创建Mesh3d对象
mesh = go.Mesh3d(
        # 8 vertices of a cube
        x=[5, 5, 15, 15, 5, 5, 15, 15],
        y=[-1, 1, 1, -1, -1, 1, 1, -1],
        z=[-1, -1, -1, -1, 1, 1, 1, 1],

        i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
        j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
        k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
        opacity=0.1,
        color='#DC143C',
        flatshading = True
    )     

# 创建数据列表
data = [mesh]

# 创建布局对象
layout = go.Layout(
    title='Solid Cuboid',
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Z'),
        aspectmode='manual',
        aspectratio=dict(x=1, y=1, z=1)
    )
)

# 创建图表对象
fig = go.Figure(data=data, layout=layout)

# 显示图表
fig.show()