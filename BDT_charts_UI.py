import streamlit as st
import plotly.graph_objects as go

# Regression and classification scores
regression_scores = {
    'Random Forest': 62.01,
    'Linear Regression': 20.86,
    'Decision Tree': 30.37,
    'Gradient Boost': 40.30
}
classification_scores = {
    'Random Forest (Accuracy 1)': 67.33,
    'Random Forest (Accuracy 2)': 71.52
}

# Streamlit app
st.title("Model Comparison Dashboard")
st.header("Regression and Classification Model Performance")

# Dropdown for model selection
st.subheader("Select Model Type to View Performance")
model_type = st.selectbox("Choose Model Type:", ["Regression Models", "Classification Models"])

# Plot regression or classification model performance based on selection
if model_type == "Regression Models":
    st.subheader("Interactive Regression Model R² Scores")
    regression_fig = go.Figure(data=[
        go.Bar(
            x=list(regression_scores.keys()),
            y=list(regression_scores.values()),
            text=[f"R² Score: {score}%" for score in regression_scores.values()],
            textposition='auto',
            marker=dict(color='skyblue'),
            hoverinfo="text",
        )
    ])
    regression_fig.update_layout(
        title="Regression Model Performance",
        xaxis_title="Model",
        yaxis_title="R² Score (%)",
        plot_bgcolor="white"
    )
    st.plotly_chart(regression_fig)

elif model_type == "Classification Models":
    st.subheader("Interactive Classification Model Accuracy Scores")
    classification_fig = go.Figure(data=[
        go.Bar(
            x=list(classification_scores.keys()),
            y=list(classification_scores.values()),
            text=[f"Accuracy: {score}%" for score in classification_scores.values()],
            textposition='auto',
            marker=dict(color='salmon'),
            hoverinfo="text",
        )
    ])
    classification_fig.update_layout(
        title="Classification Model Performance",
        xaxis_title="Model",
        yaxis_title="Accuracy (%)",
        plot_bgcolor="white"
    )
    st.plotly_chart(classification_fig)

# Comparison between the best models
st.subheader("Model Comparison Summary")
st.write("""
- **Best Regression Model**: Based on the R² scores, the **Random Forest** model performs the best among the regression models with an R² score of 62.01%.
- **Best Classification Model**: Among the classification models, **Random Forest Classifier** shows varying accuracy scores, with the highest at 71.52%.

These results indicate that Random Forest models are performing comparatively well for both regression and classification tasks in this context.
""")
