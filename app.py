# import streamlit as st
# import pandas as pd
# import joblib
# import plotly.express as px

# # --- Load the trained model ---
# model = joblib.load("multioutput_crop_model.pkl")

# # --- Load the dataset to extract dropdown options ---
# df = pd.read_xml("FAOSTAT_data.xlsx")  # Replace with your actual CSV

# # --- Clean and get unique values ---
# unique_areas = sorted(df['Area'].dropna().unique())
# unique_items = sorted(df['Item'].dropna().unique())

# # --- Units for display ---
# units = {
#     'Area harvested': 'ha',
#     'Production': 't',
#     'Yield': 'kg/ha'
# }

# # --- UI ---
# st.title("🌾 Crop Production Predictor")

# st.sidebar.header("🔧 Enter Input Details")
# year = st.sidebar.number_input("Year", min_value=2000, max_value=2030, value=2025)
# area = st.sidebar.selectbox("Area (Region)", unique_areas)
# item = st.sidebar.selectbox("Item (Crop)", unique_items)

# # --- Predict ---
# if st.sidebar.button("Predict"):
#     input_df = pd.DataFrame({'Year': [year], 'Area': [area], 'Item': [item]})

#     prediction = model.predict(input_df)[0]
#     targets = ['Area harvested', 'Production', 'Yield']

#     # --- Format results with units ---
#     result_df = pd.DataFrame({
#         'Metric': targets,
#         'Value': prediction,
#         'Unit': [units[t] for t in targets]
#     })

#     # --- Display Results ---
#     st.subheader("📈 Predicted Crop Metrics")
#     for _, row in result_df.iterrows():
#         st.markdown(f"- **{row['Metric']}**: {row['Value']:.2f} {row['Unit']}")

#     # --- Bar Chart ---
#     st.subheader("📊 Prediction Breakdown")
#     fig = px.bar(result_df, x='Metric', y='Value', color='Metric',
#                  text=result_df['Value'].round(2),
#                  labels={'Value': 'Predicted Value'})
#     fig.update_traces(textposition='outside')
#     st.plotly_chart(fig)



import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# --- Load the trained model ---
model = joblib.load("multioutput_crop_model.pkl")

# --- Load the dataset to extract dropdown options ---
df_pivot = pd.read_csv("df_pivot.csv")
 

# --- Clean and get unique values ---
unique_areas = sorted(df_pivot['Area'].dropna().unique())
unique_items = sorted(df_pivot['Item'].dropna().unique())

# --- Units for display ---
units = {
    'Area harvested': 'ha',
    'Production': 't',
    'Yield': 'kg/ha'
}

# --- UI ---
st.title("🌾 Crop Production Predictor")

st.sidebar.header("🔧 Enter Input Details")
year = st.sidebar.number_input("Year", min_value=2000, max_value=2030, value=2025)
area = st.sidebar.selectbox("Area (Region)", unique_areas)
item = st.sidebar.selectbox("Item (Crop)", unique_items)

# --- Predict ---
if st.sidebar.button("Predict"):
    input_df = pd.DataFrame({'Year': [year], 'Area': [area], 'Item': [item]})

    prediction = model.predict(input_df)[0]
    targets = ['Area harvested', 'Production', 'Yield']

    # --- Format results with units ---
    result_df = pd.DataFrame({
        'Metric': targets,
        'Value': prediction,
        'Unit': [units[t] for t in targets]
    })

    # --- Display Results ---
    st.subheader("📈 Predicted Crop Metrics")
    for _, row in result_df.iterrows():
        st.markdown(f"- **{row['Metric']}**: {row['Value']:.2f} {row['Unit']}")

    # --- Bar Chart ---
    st.subheader("📊 Prediction Breakdown")
    fig = px.bar(result_df, x='Metric', y='Value', color='Metric',
                 text=result_df['Value'].round(2),
                 labels={'Value': 'Predicted Value'})
    fig.update_traces(textposition='outside')
    st.plotly_chart(fig)
