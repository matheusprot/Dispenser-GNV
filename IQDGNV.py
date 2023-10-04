import streamlit as st

st.set_page_config(page_title="Impacto da Qualidade no Dispenser GNV")

st.title("Impacto da Qualidade no Dispenser GNV")

st.divider()

col1, col2, col3, = st.columns(3)

# Inputs
with col1:
    st.subheader("Composição do Gás")
    C1 = st.number_input('Metano')
    C2 = st.number_input('Etano')
    C3 = st.number_input('Propano')
    C4 = st.number_input('Butano')
    CO2 = st.number_input('Dióxido de Carbono')
    N2 = st.number_input('Nitrogênio')

with col2:
    st.subheader("Volume, PTZ, Densidade do Posto")
    Volume = st.number_input('Volume')
    PTZ = st.number_input('PTZ')
    DensidadeF = st.number_input('Densidade')

    if st.button("Calcular"):  # Verifica se o botão foi pressionado
    # Área de Cálculo
    # Converter a composição do gás para frações decimais (porcentagem para fração)
        C1_percent = C1 / 100
        C2_percent = C2 / 100
        C3_percent = C3 / 100
        C4_percent = C4 / 100
        CO2_percent = CO2 / 100
        N2_percent = N2 / 100

        # Constantes e Valores Fixos
        C1mol = 16.0425
        C2mol = 30.0690
        C3mol = 44.0956
        C4mol = 58.1222
        CO2mol = 44.0095
        N2mol = 28.0134

        # PCS Indivídual
        C1pcs =  212.9
        C2pcs = 373.0
        C3pcs = 530.4
        C4pcs = 687.7
        CO2pcs = 0
        NO2pcs = 0

        # Cálculo da massa molecular
        MassaMolecular = (C1_percent * C1mol) + (C2_percent * C2mol) + (C3_percent * C3mol) + (C4_percent * C4mol) + (CO2_percent * CO2mol) + (N2_percent * N2mol)

        # Correção para STP (Temperatura em K e Pressão em atm)
        TemperaturaK = 293.15  # K 20C°
        Pressaokgf = 1.03323  # 1 atm em kgf/cm²
        Pressaoatm = 1

        # Constante dos gases ideais em L·atm/(K·mol)
        R = 0.0820574587  # L·atm/(K·mol)

        # Massa Molecular g/mol > kg/mol
        MassaMolkg = MassaMolecular / 1000

        DensidadeP = (Pressaoatm * MassaMolkg) / (R * TemperaturaK) * 1000

        # Cálculo kcal/mol
        kcalmol = (C1_percent * C1pcs) + (C2_percent * C2pcs) + (C3_percent * C3pcs) + (C4_percent * C4pcs)

        # kcal/kg
        kcalkg = kcalmol / MassaMolecular * 1000

        # kcal/m³
        kcalm3 = kcalkg * DensidadeP

        # Resultado
        MassaRef = Volume * DensidadeP * PTZ

        # Volume Corrigido
        VolumeC = Volume * PTZ * (kcalm3 / 9400)

        # Volume Dispenser
        VolumeD = MassaRef / DensidadeF

        # Taxa de Variação
        Tvar = (VolumeD - VolumeC) / VolumeC * 100

        with col3:

        # Exibir resultados
            st.write("Resultados Aproximados:")
            st.write("Massa Molecular do Gás (g/mol):", MassaMolecular)
            st.write("kcal/mol:", kcalmol)
            st.write("kcal/kg:", kcalkg)
            st.write("kcal/m³:", kcalm3)
            st.write("Volume Corrigido (m³):", VolumeC)
            st.write("Volume Dispenser (m³):", VolumeD)
            st.write("Taxa de Variação (%):", Tvar)
            st.write("Densidade (kgf/cm²):", DensidadeP)
