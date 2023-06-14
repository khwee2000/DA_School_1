import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

# 경고 메시지 비활성화
st.set_option('deprecation.showPyplotGlobalUse', False)

page1 = 'Matplotlib - Heatmap'
page2 = 'Seaborn - Heatmap'
page3 = 'Plotly - Heatmap (imshow)'
page4 = 'Plotly - Heatmap (Heatmap Object)'
page5 = 'Plotly - Heatmap (figure_factory)'

# 임의의 데이터 생성
data_options = {
    'Random Data(-1 ~ 1)': np.random.rand(10, 10)*2-1,
    'Random Normal Data': np.random.randn(10, 10),
    'Random Negative number Data': np.random.randint(-100, 100, (10, 10))
}

with st.sidebar:
    choice = st.selectbox("Choose a graph", [page1, page2, page3, page4, page5])
    colormap = st.selectbox("Choose a colormap", plt.colormaps())
    selected_data = st.selectbox("Choose a data", list(data_options.keys()))

data = data_options[selected_data]

if choice == page1:
    st.title(page1)
    fig, ax = plt.subplots()
    heatmap = ax.imshow(data, cmap=colormap)
    plt.colorbar(heatmap)
    ax.set_title('Heatmap')
    st.pyplot(fig)

elif choice == page2:
    st.title(page2)
    heatmap = sns.heatmap(data, annot=True, fmt=".2f", cmap=colormap, cbar=True, square=True)
    heatmap.set_title('Heatmap')
    st.pyplot()

elif choice == page3:
    st.title(page3)
    fig = px.imshow(data, color_continuous_scale=colormap)
    fig.update_layout(title='Heatmap')
    st.plotly_chart(fig)

elif choice == page4:
    st.title(page4)
    fig = go.Figure(data=go.Heatmap(z=data, colorscale=colormap))
    fig.update_layout(title='Heatmap')
    st.plotly_chart(fig)

elif choice == page5:
    st.title(page5)
    data_rounded = np.round(data, decimals=2)
    fig = ff.create_annotated_heatmap(z=data_rounded, colorscale=colormap)
    fig.update_layout(title='Heatmap')
    st.plotly_chart(fig)
