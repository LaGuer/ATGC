# Conversion constants
amu_to_GeV = 0.9315  # 1 atomic mass unit ≈ 0.9315 GeV
proton_mass_GeV = 0.9382720813  # Proton mass in GeV
neutron_mass_GeV = 0.939565413  # Neutron mass in GeV
hydrogen_mass_GeV = 0.938773  # Hydrogen mass in GeV
# Additional constants
muon_mass_GeV = 0.1056583755  # Muon mass in GeV
fermi_mass_GeV = 1.0e-3  # Example Fermi scale in GeV (adjust as needed)

# Define additional atomic masses (in g/mol)
N_14 = 14.003074  # Atomic mass of Nitrogen-14
C_12 = 12.000000  # Atomic mass of Carbon-12
H = 1.007825  # Atomic mass of Hydrogen

# Add the new equation G + C - (A + T) and compare with N_14 - C_12 - H
additional_equation_result = N_14 - C_12 - H  # Should equal 1

# Approximate molar masses (g/mol) for deoxyribonucleotides:
nucleotides = {
    "A": 331.22,  # dAMP
    "C": 307.20,  # dCMP
    "G": 347.22,  # dGMP
    "T": 322.21   # dTMP
}

# Compute conversion values for each nucleotide and store in a dictionary
data = {}
for nt, mass in nucleotides.items():
    mass_GeV = mass * amu_to_GeV
    proton_ratio = mass_GeV / proton_mass_GeV
    neutron_ratio = mass_GeV / neutron_mass_GeV
    hydrogen_ratio = mass_GeV / hydrogen_mass_GeV
    muon_ratio = mass_GeV / muon_mass_GeV  # Compute muon mass ratio
    fermi_ratio = mass_GeV / fermi_mass_GeV  # Compute Fermi mass ratio
    atomic_mass_ratio = mass / (N_14 + C_12 + H)  # Compute atomic mass ratio
    data[nt] = {
        "Molar": mass,          # in g/mol
        "GeV": mass_GeV,
        "Proton": proton_ratio,
        "Neutron": neutron_ratio,
        "Hydrogen": hydrogen_ratio,
        "AtomicMass": atomic_mass_ratio,  # Add atomic mass ratio
        "MuonMass": muon_ratio,               # Add muon mass ratio
        "FermiMass": fermi_ratio              # Add Fermi mass ratio
    }

# Print table of individual conversions

header = f"{'NT':>3} | {'Molar (g/mol)':>14} | {'Mass (GeV)':>10} | {'Proton Ratio':>14} | {'Neutron Ratio':>16} | {'Hydrogen Ratio':>14} | {'Atomic Mass':>12} | {'Muon Ratio':>12} | {'Fermi Ratio':>12}"
print(header)
print("-" * len(header))
for nt in ["A", "C", "G", "T"]:
    row = data[nt]
    print(f"{nt:>3} | {row['Molar']:14.2f} | {row['GeV']:10.2f} | {row['Proton']:14.2f} | {row['Neutron']:16.2e} | {row['Hydrogen']:14.2e} | {row['AtomicMass']:12.4f} | {row['MuonMass']:12.2f} | {row['FermiMass']:12.2f}")


# Compute sums for the pairs A+T and C+G in each column
print("\n--- Equation Check ---")
print("We want to verify the relationships:")
print("  (1) C + G = A + T + 1")
print("  (2) A + T = C + G - 1")
print("  (3) G + C - (A + T) = N_14 - C_12 - H_1 = 1\n")

cols = ["Molar", "GeV", "Proton", "Neutron", "Hydrogen", "AtomicMass", "MuonMass", "FermiMass"]

# Print the sums and the difference (C+G) - (A+T)
header2 = f"{'Column':>10} | {'A+T':>12} | {'C+G':>12} | {'Difference':>12}"
print(header2)
print("-" * len(header2))
for col in cols:
    sum_AT = data["A"][col] + data["T"][col]
    sum_CG = data["C"][col] + data["G"][col]
    diff = sum_CG - sum_AT
    print(f"{col:>10} | {sum_AT:12.4f} | {sum_CG:12.4f} | {diff:12.4f}")

# Verification of equations
print("\nVerification of equations:")
for col in cols:
    sum_AT = data["A"][col] + data["T"][col]
    sum_CG = data["C"][col] + data["G"][col]
    eq1 = sum_AT + 1  # Expect eq1 to nearly equal sum_CG
    eq2 = sum_CG - 1  # Expect eq2 to nearly equal sum_AT
    print(f"{col:>10}:")
    print(f"    (A+T)+1 = {eq1:12.4f}    vs.    C+G = {sum_CG:12.4f}   (diff = {sum_CG - eq1:.4f})")
    print(f"    (C+G)-1 = {eq2:12.4f}    vs.    A+T = {sum_AT:12.4f}   (diff = {sum_AT - eq2:.4f})\n")

# Validate the equation N_14 - C_12 - H = 1
# Output the results
print("\nValidation of N_14 - C_12 - H_1:")
print(f"G + C: {sum_GC:.4f}")
print(f"A + T: {sum_AT:.4f}")
print(f"G + C - (A + T): {difference:.4f}")
print(f"N_14 - C_12 - H (Expected): {additional_equation_result:.4f}")
print(f"G + C - (A + T): {diff:.4f}")
print(f"Difference (Measured - Expected): {diff - additional_equation_result:.4f}")
