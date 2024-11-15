import streamlit as st
import pyspark
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel

import os

# Set Spark environment variables
os.environ["JAVA_HOME"] = r"C:\Java\jdk-17\bin"

# Initialize Spark Session
spark = SparkSession.builder.appName("StreamlitApp").getOrCreate()

# Load the pre-trained pipeline model
pipeline_model = PipelineModel.load("C:\\Users\\Krupa\\Downloads\\BDT_CAC-3\\pipeline_model_path")

# Streamlit user input interface
st.title("Media Cost Prediction")
acquisition_cost = st.number_input("Enter Acquisition Cost:", min_value=0.0)
channel_used = st.selectbox("Select Channel Used:", ["Instagram","Facebook","Twitter","Pinterest"])  # Example options
location = st.selectbox("Select Location:", ["Los Angeles", "Austin", "Las Vegas","Miami","New York"])        # Example options
company = st.selectbox("Select Company:", ["Pulse Point", "Well Wish", "Cyber Circuit","Glam Garments","Palate Paradise","Fiber Fashion","Furnish Fine","Culinary Quest","Trend Tailors","NexGen Nerds","Cozy Corners","Hearth Harmony","Nosh Nirvana","Code Crafters","Dine Divine","Vital Vigor","Dwell Delight","Silicon Saga","Living Luxe","Vogue Visions"]) 

# Create a DataFrame from user inputs
input_data = spark.createDataFrame(
    [(acquisition_cost, channel_used, location, company)],
    ["Acquisition_Cost", "Channel_Used", "Location", "Company"]
)

# Transform and predict
df_transformed = pipeline_model.transform(input_data)
prediction = df_transformed.select("prediction").collect()[0][0]

st.write(f"Predicted Media Cost: {prediction}")
