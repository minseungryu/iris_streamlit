# -*- coding:utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import plotly.express as ex
# import plotly.graph_objects as go
# import scikit-learn as sklearn

def main():

    st.markdown("# Hello Streamlit!")

    menu = ['Home', '탐색적 자료 분석', '머신러닝', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'Home':
        st.subHeader('Home')
    elif choice == '탐색적 자료 분석':
        st.subHeader('탐색적 자료 분석')
    elif choice == '머신러닝':
        st.subHeader('머신러닝')
    elif choice == 'About':
        st.subHeader('About')
    else:
        pass
    
if __name__ == "__main__":
    main()