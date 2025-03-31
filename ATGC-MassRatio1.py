# Conversion constants (CODATA 2022 recommended values)
amu_to_GeV = 0.93149410242  # 1 atomic mass unit ≈ 0.93149410242 GeV
proton_mass_GeV = 0.93827208816  # Proton mass in GeV
neutron_mass_GeV = 0.93956542052  # Neutron mass in GeV
electron_mass_GeV = 0.00051099895000  # Electron mass in GeV
planck_mass_GeV = 2.176434e-8 / amu_to_GeV  # Planck mass in GeV
fermi_mass_GeV = 2.8e6  # Fermi mass in GeV 
neuron_mass_GeV = 1.0e-10  # Neuron mass 
avogadro_number = 6.02214076e23  # Avogadro's number

# Approximate molar masses (g/mol) for deoxyribonucleotides:
nucleotides = {
    "A": 331.22,  # dAMP
    "C": 307.20,  # dCMP
    "G": 347.22,  # dGMP
    "T": 322.21   # dTMP
}

# Compute conversion values for each nucleotide and store in a dictionary.
data = {}
for nt, mass in nucleotides.items():
    mass_GeV = mass * amu_to_GeV
    mass_Kg = (mass / 1000) / avogadro_number  # Convert g/mol to kg using Avogadro's number
    proton_ratio = mass_GeV / proton_mass_GeV
    neutron_ratio = mass_GeV / neutron_mass_GeV
    electron_ratio = mass_GeV / electron_mass_GeV
    planck_ratio = mass_GeV / planck_mass_GeV
    fermi_ratio = mass_GeV / fermi_mass_GeV
    neuron_ratio = mass_GeV / neuron_mass_GeV  # New Neuron ratio
    data[nt] = {
        "Molar": mass,          # in g/mol
        "GeV": mass_GeV,
        "Kg": mass_Kg,          # Mass in kilograms
        "Proton": proton_ratio,
        "Neutron": neutron_ratio,
        "Electron": electron_ratio,
        "Planck": planck_ratio,
        "Fermi": fermi_ratio,
        "Neuron": neuron_ratio  # Add Neuron ratio to the dictionary
    }

# Print the table of individual conversions.
header = f"{'NT':>3} | {'Molar (g/mol)':>14} | {'Mass (GeV)':>10} | {'Mass (Kg)':>12} | {'Proton Ratio':>14} | {'Neutron Ratio':>14} | {'Electron Ratio':>16} | {'Planck Ratio':>14} | {'Fermi Ratio':>14} | {'Neuron Ratio':>14}"
print(header)
print("-" * len(header))
for nt in ["A", "C", "G", "T"]:
    row = data[nt]
    print(f"{nt:>3} | {row['Molar']:14.2f} | {row['GeV']:10.2f} | {row['Kg']:12.2e} | {row['Proton']:14.2f} | {row['Neutron']:14.2f} | {row['Electron']:16.2e} | {row['Planck']:14.2e} | {row['Fermi']:14.2e} | {row['Neuron']:14.2e}")

# Compute the sums for the pairs A+T and C+G in each of the columns, including Neutron and Neuron ratios.
print("\n--- Equation Check ---")
cols = ["Molar", "GeV", "Kg", "Proton", "Neutron", "Electron", "Planck", "Fermi", "Neuron"]

header2 = f"{'Column':>10} | {'A+T':>12} | {'C+G':>12} | {'Difference':>12}"
print(header2)
print("-" * len(header2))
for col in cols:
    sum_AT = data["A"][col] + data["T"][col]
    sum_CG = data["C"][col] + data["G"][col]
    diff = sum_CG - sum_AT
    print(f"{col:>10} | {sum_AT:12.4f} | {sum_CG:12.4f} | {diff:12.4f}")

