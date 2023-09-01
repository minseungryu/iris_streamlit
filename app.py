# -*- coding:utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as ex
import plotly.graph_objects as go
import scikit-learn as sklearn

def main():
    st.markdown("# Hello Streamlit!")
    st.write(np.__version__)
    st.write(pd.__version__)
    st.write(sns.__version__)
    st.write(plt.__version__)
    st.write(ex.__version__)
    st.write(go.__version__)
    st.write(sklearn.__version__)

if __name__ == "__main__":
    main()