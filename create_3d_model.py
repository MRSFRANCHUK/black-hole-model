import plotly.graph_objects as go
import numpy as np

# Данные о сверхмассивной черной дыре
mass = 1.99e+36  # Масса в кг
radius_schwarzschild = 2.95e+06 * 1e3  # Радиус Шварцшильда в метрах
time_dilation_factor = 0.71  # Фактор гравитационного замедления времени

# Создаем данные для модели черной дыры
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

# Преобразование сферических координат в декартовы
x = radius_schwarzschild * np.sin(phi) * np.cos(theta)
y = radius_schwarzschild * np.sin(phi) * np.sin(theta)
z = radius_schwarzschild * np.cos(phi)

# Создаем фигуру
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Blackbody')])

# Настраиваем параметры графика
fig.update_layout(
    title='3D Model of Supermassive Black Hole',
    scene=dict(
        xaxis_title='X (meters)',
        yaxis_title='Y (meters)',
        zaxis_title='Z (meters)'
    ),
    coloraxis_colorbar=dict(
        title='Intensity'
    )
)

# Сохраняем фигуру в HTML файл
fig.write_html('black_hole_model.html')

# Выводим сообщение о завершении
print("Файл black_hole_model.html успешно создан.")
