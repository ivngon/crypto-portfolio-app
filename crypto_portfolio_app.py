import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el Excel
file_path = "Plan_Inversion_Cripto_Bitget.xlsx"
df = pd.read_excel(file_path)

st.set_page_config(page_title="Seguimiento Cripto Portafolio", layout="wide")
st.title("📈 Seguimiento de Inversión en Criptomonedas")

# Mostrar tabla editable
st.subheader("📋 Portafolio Actual")
edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

# Cálculos de resumen
total_invertido = edited_df["Inversión Inicial (€)"].sum()
valor_actual_total = edited_df["Valor Actual Total (€)"].sum()
ganancia_total = valor_actual_total - total_invertido
ganancia_pct = (ganancia_total / total_invertido * 100) if total_invertido > 0 else 0

# Mostrar resumen
st.subheader("🔍 Resumen")
st.metric("Total Invertido (€)", f"{total_invertido:.2f}")
st.metric("Valor Actual (€)", f"{valor_actual_total:.2f}")
st.metric("Ganancia/Pérdida (€)", f"{ganancia_total:.2f}", delta=f"{ganancia_pct:.2f}%")

# Gráfico de pastel
st.subheader("📊 Distribución del Portafolio")
fig1, ax1 = plt.subplots()
ax1.pie(edited_df["Inversión Inicial (€)"], labels=edited_df["Criptomoneda"], autopct='%1.1f%%')
ax1.axis('equal')
st.pyplot(fig1)

# Gráfico de barras para valor actual
st.subheader("💹 Valor Actual por Cripto")
fig2, ax2 = plt.subplots()
ax2.bar(edited_df["Criptomoneda"], edited_df["Valor Actual Total (€)"], color="skyblue")
plt.xticks(rotation=45)
st.pyplot(fig2)

# Guardar cambios opcionalmente
if st.button("💾 Guardar cambios en Excel"):
    edited_df.to_excel(file_path, index=False)
    st.success("Cambios guardados correctamente.")
