import streamlit as st
import pandas as pd
import plotly.express as px
import os

os.environ["USE_CALEIDO"] = "False"

TYPES_OF_ST_CHARTS = ['line', 'bar', 'area', 'scatter', 'pie']

st.set_page_config(page_title='DaTatra - Data Analysis Dashboard',
                   layout='wide')

st.write("""
# Data Analysis

Welcome to our cutting-edge Data Analysis App, where the power of data meets user-friendly simplicity! Whether you're a seasoned analyst or just diving into the world of data, our application is designed to empower you to extract valuable insights effortlessly.

""")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Check if a file was uploaded
if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Create a sidebar
    with st.sidebar:
        st.title("Analysis Options")

        # Add selectbox widgets for choosing parameters and chart type for the first chart
        selected_parameter_x1 = st.selectbox("Select Parameter x (Chart 1)", df.columns, key="dwe1")
        selected_parameter_y1 = st.selectbox("Select Parameter y (Chart 1)", df.columns, key="wde1")
        selected_chart_type1 = st.selectbox("Select Chart Type (Chart 1)", TYPES_OF_ST_CHARTS)

        # Add selectbox widgets for choosing parameters and chart type for the second chart
        selected_parameter_x2 = st.selectbox("Select Parameter x (Chart 2)", df.columns, key="dwe2")
        selected_parameter_y2 = st.selectbox("Select Parameter y (Chart 2)", df.columns, key="wde2")
        selected_chart_type2 = st.selectbox("Select Chart Type (Chart 2)", TYPES_OF_ST_CHARTS)

        # Filter data based on user input
        filtered_df = df.copy()
        for col in df.columns:
            filter_value = st.sidebar.selectbox(f"Filter {col}", "")
            if filter_value:
                filtered_df = filtered_df[filtered_df[col] == filter_value]

    # Display the selected parameters for the first chart
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.write("You selected for parameter x (Chart 1):", selected_parameter_x1)
        st.write("You selected for parameter y (Chart 1):", selected_parameter_y1)
        st.write("You selected chart type (Chart 1):", selected_chart_type1)

    # Display the selected parameters for the second chart
    with col2:
        st.write("You selected for parameter x (Chart 2):", selected_parameter_x2)
        st.write("You selected for parameter y (Chart 2):", selected_parameter_y2)
        st.write("You selected chart type (Chart 2):", selected_chart_type2)

    col3, col4 = st.columns(2, gap="medium")
    # Generate and display the first chart
    with col3:
        st.write("### Chart 1:")
        if selected_chart_type1 == 'line':
            fig1 = px.line(filtered_df, x=selected_parameter_x1, y=selected_parameter_y1, title="Line Chart 1")
        elif selected_chart_type1 == 'bar':
            fig1 = px.bar(filtered_df, x=selected_parameter_x1, y=selected_parameter_y1, title="Bar Chart 1")
        elif selected_chart_type1 == 'area':
            fig1 = px.area(filtered_df, x=selected_parameter_x1, y=selected_parameter_y1, title="Area Chart 1")
        elif selected_chart_type1 == 'scatter':
            fig1 = px.scatter(filtered_df, x=selected_parameter_x1, y=selected_parameter_y1, title="Scatter Plot 1")
        elif selected_chart_type1 == 'pie':
            fig1 = px.pie(filtered_df, names=selected_parameter_x1, values=selected_parameter_y1, title="Pie Chart 1")

        st.plotly_chart(fig1)

    # Generate and display the second chart
    with col4:
        st.write("### Chart 2:")
        if selected_chart_type2 == 'line':
            fig2 = px.line(filtered_df, x=selected_parameter_x2, y=selected_parameter_y2, title="Line Chart 2")
        elif selected_chart_type2 == 'bar':
            fig2 = px.bar(filtered_df, x=selected_parameter_x2, y=selected_parameter_y2, title="Bar Chart 2")
        elif selected_chart_type2 == 'area':
            fig2 = px.area(filtered_df, x=selected_parameter_x2, y=selected_parameter_y2, title="Area Chart 2")
        elif selected_chart_type2 == 'scatter':
            fig2 = px.scatter(filtered_df, x=selected_parameter_x2, y=selected_parameter_y2, title="Scatter Plot 2")
        elif selected_chart_type2 == 'pie':
            fig2 = px.pie(filtered_df, names=selected_parameter_x2, values=selected_parameter_y2, title="Pie Chart 2")

        st.plotly_chart(fig2)

    # Display statistics for the filtered data
    st.write("### Filtered Data Statistics:")
    st.write(filtered_df.describe())


