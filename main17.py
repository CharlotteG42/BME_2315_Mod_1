import csv
from patient import Patient
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import statistics

patients = []

## load csv and create patient objects
with open("/Users/charlottegoodwin/Documents/GitHub/BME_2315_Mod_1/Metadata and Protein Data for Module 1 (1).csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        donor_id = row["Donor ID"]
        sex = row["Sex"]
        apoe = row["APOE Genotype"]

        p_tau = float(row["pTAU pg/ug"])
        abeta40 = float(row["ABeta40 pg/ug"])
        abeta42 = float(row["ABeta42 pg/ug"])

        new_patient = Patient(donor_id, sex, apoe, p_tau, abeta40, abeta42)
        patients.append(new_patient)

## sort patients by pTAU values
sorted_by_ptau = sorted(patients, key=lambda p: p.p_tau)

print("\nPatients sorted by pTAU:")
for p in sorted_by_ptau[:10]:
    print(p)

## filter female patients with APOE 3_3
filtered_group = Patient.filter_patients(patients, "Female", "3_3")

print("\nFemale patients with APOE 3_3:")
for p in filtered_group[:10]:
    print(p)

## collect ABeta40 values for APOE groups
abeta40_33 = []
abeta40_34 = []

for p in patients:
    if p.apoe == "3_3":
        abeta40_33.append(p.abeta40)
    elif p.apoe == "3_4":
        abeta40_34.append(p.abeta40)

## compute mean and sd for bar graph
mean_33 = statistics.mean(abeta40_33)
mean_34 = statistics.mean(abeta40_34)

sd_33 = statistics.stdev(abeta40_33)
sd_34 = statistics.stdev(abeta40_34)

## bar graph comparing ABeta40 in APOE 3_3 vs 3_4
plt.bar(["APOE 3_3", "APOE 3_4"], [mean_33, mean_34],
        yerr=[sd_33, sd_34], capsize=10, color=["purple", "green"])
plt.ylabel("Mean ABeta40 (pg/ug)")
plt.title("ABeta40 Levels in APOE 3_3 vs APOE 3_4")
plt.show()

## collect values for scatter plot
p_tau_vals = []
abeta42_vals = []

for p in patients:
    p_tau_vals.append(p.p_tau)
    abeta42_vals.append(p.abeta42)

## scatter plot of pTAU vs ABeta42
plt.scatter(p_tau_vals, abeta42_vals, color="darkred")
plt.xlabel("pTAU (pg/ug)")
plt.ylabel("ABeta42 (pg/ug)")
plt.title("Scatter Plot: pTAU vs ABeta42")
plt.show()

## One way ANOVA test for ABeta40 levels across APOE groups
abeta40_44 = [p.abeta40 for p in patients if p.apoe == "4_4"]

f_stat, p_value = stats.f_oneway(abeta40_33, abeta40_34, abeta40_44)
print(f"One-way ANOVA test results for ABeta40 levels:")
print(f"F-statistic: {f_stat}")
print(f"P-value: {p_value}")
