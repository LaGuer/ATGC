# Conversion constants
amu_to_GeV = 0.9315             # 1 atomic mass unit ≈ 0.9315 GeV
proton_mass_GeV = 0.9382720813   # Proton mass in GeV
electron_mass_GeV = 0.000511     # Electron mass in GeV
planck_mass_GeV = 1.2209e19      # Planck mass in GeV

# Approximate molar masses (g/mol) for deoxyribonucleotides:
# Here we use A for dAMP, C for dCMP, G for dGMP, and T for dTMP.
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
    proton_ratio = mass_GeV / proton_mass_GeV
    electron_ratio = mass_GeV / electron_mass_GeV
    planck_ratio = mass_GeV / planck_mass_GeV
    data[nt] = {
        "Molar": mass,          # in g/mol
        "GeV": mass_GeV, 
        "Proton": proton_ratio, 
        "Electron": electron_ratio, 
        "Planck": planck_ratio,
    }

# First, print the table of individual conversions.
header = f"{'NT':>3} | {'Molar (g/mol)':>14} | {'Mass (GeV)':>10} | {'Proton Ratio':>14} | {'Electron Ratio':>16} | {'Planck Ratio':>14}"
print(header)
print("-" * len(header))
for nt in ["A", "C", "G", "T"]:
    row = data[nt]
    print(f"{nt:>3} | {row['Molar']:14.2f} | {row['GeV']:10.2f} | {row['Proton']:14.2f} | {row['Electron']:16.2e} | {row['Planck']:14.2e}")

# Now compute the sums for the pairs A+T and C+G in each of the five columns.
print("\n--- Equation Check ---")
print("We want to verify the relationships:")
print("  (1) C + G = A + T + 1")
print("  (2) A + T = C + G - 1\n")

cols = ["Molar", "GeV", "Proton", "Electron", "Planck"]

# Print the sums and the difference: (C+G) - (A+T)
header2 = f"{'Column':>10} | {'A+T':>12} | {'C+G':>12} | {'Difference':>12}"
print(header2)
print("-" * len(header2))
for col in cols:
    sum_AT = data["A"][col] + data["T"][col]
    sum_CG = data["C"][col] + data["G"][col]
    diff = sum_CG - sum_AT
    # diff should be nearly 1 if (C+G) = (A+T)+1 and equally (A+T) = (C+G)-1.
    print(f"{col:>10} | {sum_AT:12.4f} | {sum_CG:12.4f} | {diff:12.4f}")

# Provide an extra printout that frames the equations explicitly.
print("\nVerification of equations:")
for col in cols:
    sum_AT = data["A"][col] + data["T"][col]
    sum_CG = data["C"][col] + data["G"][col]
    eq1 = sum_AT + 1      # Expect eq1 to nearly equal sum_CG
    eq2 = sum_CG - 1      # Expect eq2 to nearly equal sum_AT
    print(f"{col:>10}:")
    print(f"    (A+T)+1 = {eq1:12.4f}    vs.    C+G = {sum_CG:12.4f}   (diff = {sum_CG - eq1: .4f})")
    print(f"    (C+G)-1 = {eq2:12.4f}    vs.    A+T = {sum_AT:12.4f}   (diff = {sum_AT - eq2: .4f})\n")
