import matplotlib.pyplot as plt
import numpy as np

params = {
    'axes.labelsize':9, # label 폰트 크기
    'axes.titlesize':9, # 타이틀 폰트 크기
    'xtick.labelsize':9, # x 축 tick label 폰트 크기
    'ytick.labelsize':9, # y 축 tick label 폰트 크기 
    'xtick.direction': 'in', # 눈금 표시 방향 (in, out, inout)
    'ytick.direction': 'in', # 눈금 표시 방향 (in, out, inout)
    'lines.markersize': 3, # 마커 사이즈
    'axes.titlepad': 6, # 타이틀과 그래프 사이의 간격
    'axes.labelpad': 4, # 축 label과 그래프 사이의 간격
    'font.size': 9, # font 크기
    'font.sans-serif': 'Arial', # font 설정
    'figure.dpi': 300, # 해상도, vector그래픽의 경우 dpi에 상관없이 깔끔하게 출력됨
    'figure.autolayout': True, # 그래프의 모든 요소가 figure 내부에 들어가도록 설정
    'xtick.top': True, # 그래프 위쪽 x축 눈금 표시
    'ytick.right': True, # 그래프 오른쪽 y축 눈금 표시
    'xtick.major.size': 2, # x축 눈금의 길이
    'ytick.major.size': 2, # y축 눈금의 길이
}
plt.rcParams.update(params)



fig, ax = plt.subplots(figsize=(6.0 / 2.54, 6.0 / 2.54)) # 6cm x 6cm (1 inch = 2.54 cm)
# Data for plotting
x = np.arange(0.0, 2.0, 0.01)
y = 1 + np.sin(2 * np.pi * x)
plt.plot(x, y)
plt.xlim(0, 2)
plt.ylim(0, 2)
plt.xlabel('x')
plt.ylabel('y')

# plt.show()로 figure를 보게 되면 저장 시에 이미지 크기가 맞지 않을 수 있음
fig.savefig('temp.svg', transparent=True)
