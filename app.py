import streamlit as st

st.set_page_config(page_title="Obesity Checker", page_icon="⚖️")

st.title("⚖️ Obesity Checker (BMI)")
st.caption("This tool gives a general screening result — it is not a medical diagnosis.")

# Inputs
height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0, step=0.5)
weight_kg = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0, value=70.0, step=0.1)

waist_cm = st.number_input("Waist circumference (cm) — optional", min_value=0.0, max_value=200.0, value=0.0, step=0.5)

def bmi_category(bmi: float) -> str:
    # WHO adult BMI categories
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def waist_risk_note(waist: float) -> str:
    if waist <= 0:
        return ""
    # Simple general risk message (not diagnostic)
    return "Waist measurement can add context, but risk thresholds vary by sex, age, and population."

if st.button("Check"):
    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m ** 2)

    st.subheader("Results")
    st.write(f"**BMI:** {bmi:.1f}")
    st.write(f"**Category:** {bmi_category(bmi)}")

    note = waist_risk_note(waist_cm)
    if note:
        st.info(note)

    st.subheader("General tips")
    st.markdown(
        "- Aim for balanced meals (vegetables, protein, whole grains)\n"
        "- Move your body most days (walking counts)\n"
        "- Sleep 7–9 hours if possible\n"
        "- If you’re worried about your weight or health, talk to a healthcare professional."
    )

    st.caption("BMI is a screening measure and may not reflect body composition (e.g., high muscle mass).")
