import numpy as np
import plotly.graph_objects as go

x = np.linspace(0,20,2000)
y = np.linspace(0,20,2000)
z = np.linspace(0,20,2000)
x1 = np.linspace(0,20,2000)
y1 = np.linspace(0,20,2000)
z1 = np.linspace(0,20,2000)
B = 0.2
V = 50
theta = 0
i=0
delta_d=0.0002/2.0000000000000013*np.pi/4
while(i<2000):
	if i<500:
		z[i] = np.cos(5*x[i]*np.pi)
		y[i] = 0
	elif i <1500:
		theta += B*V*delta_d
		z[i] = np.cos(5*x[i]*np.pi)*np.cos(theta)
		y[i] = np.cos(5*x[i]*np.pi)*np.sin(theta)
	else:
		z[i] = np.cos(5*x[i]*np.pi)*np.cos(theta)
		y[i] = np.cos(5*x[i]*np.pi)*np.sin(theta)
	i+=1
i=1999
while(i>=0):
	if i>=1500:
		z1[i] = np.cos(5*x1[i]*np.pi)*np.cos(theta)
		y1[i] = np.cos(5*x1[i]*np.pi)*np.sin(theta)
	elif i >=500:
		theta += delta_d
		z1[i] = np.cos(5*x1[i]*np.pi)*np.cos(theta)
		y1[i] = np.cos(5*x1[i]*np.pi)*np.sin(theta)
	else:
		z1[i] = np.cos(5*x1[i]*np.pi)*np.cos(theta)
		y1[i] = np.cos(5*x1[i]*np.pi)*np.sin(theta)
	i-=1
print(theta)
fig=go.Figure(data=[
	go.Scatter3d(x=x,y=y,z=z,mode="lines",legendgroup="正向入射光"),
	go.Scatter3d(x=x1,y=y1,z=z1,mode="lines",legendgroup="反向入射光"),
	go.Mesh3d(
        # 8 vertices of a cube
        x=[5, 5, 15, 15, 5, 5, 15, 15],
        y=[-1, 1, 1, -1, -1, 1, 1, -1],
        z=[-1, -1, -1, -1, 1, 1, 1, 1],

        i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
        j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
        k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
        opacity=0.2,
        color='#DC143C',
        flatshading = True
    )     
	])

fig.update_layout(
    title='光学隔离器',
    scene=dict(
        xaxis_title='X轴',
        yaxis_title='Y轴',
        zaxis_title='Z轴',
        xaxis_range=[0,20],
        yaxis_range=[-2,2],
        zaxis_range=[-2,2],
        aspectratio=dict(x=2, y=1, z=1),
    ),
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    )
)

fig.show()