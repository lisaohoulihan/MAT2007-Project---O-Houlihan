# ============================================================
# MAT2007 PROJECT - ANTIBIOTIC DEVELOPMENT
# Are we running out of antibiotics, or changing how we fight bacteria?
# ============================================================

# Import the libraries needed for the analysis
# pandas is used to read and analyse the Excel datasets
import pandas as pd

# matplotlib is used to create the graphs
import matplotlib.pyplot as plt


# ============================================================
# PART 1 - HISTORICAL US ANTIBIOTIC APPROVALS
# ============================================================

print("\n============================================================")
print("          HISTORICAL US ANTIBIOTIC APPROVALS")
print("============================================================")


# ------------------------------------------------------------
# LOAD THE HISTORICAL DATASET
# ------------------------------------------------------------

# Read the historical antibiotic Excel file into a DataFrame
antibiotics = pd.read_excel(
    "data/Antibiotics_approvals_US.xlsx"
)

# Count the number of antibiotic entries in the dataset
number_of_antibiotics = len(antibiotics)

# Find the earliest and latest FDA approval years
first_year = antibiotics["FDA-Approval Year"].min()
last_year = antibiotics["FDA-Approval Year"].max()

print(f"\nNumber of antibiotic entries: {number_of_antibiotics}")
print(f"FDA approval years covered: {first_year}-{last_year}")


# ------------------------------------------------------------
# ANTIBIOTIC APPROVALS BY DECADE
# ------------------------------------------------------------

# Create a new column called Decade
# // 10 removes the final digit of the year
# Multiplying by 10 gives the beginning of the decade
# Example: 1987 // 10 = 198, then 198 * 10 = 1980
antibiotics["Decade"] = (
    antibiotics["FDA-Approval Year"] // 10
) * 10

# Count how many individual antibiotics were approved
# during each decade
approvals_per_decade = (
    antibiotics["Decade"]
    .value_counts()
    .sort_index()
)

# Print the results in a cleaner format
print("\nAntibiotic approvals per decade:")

for decade, count in approvals_per_decade.items():
    print(f"{decade}s: {count} approvals")

# Find the decade with the largest number of approvals
highest_decade = approvals_per_decade.idxmax()
highest_number = approvals_per_decade.max()

print(
    f"\nThe {highest_decade}s had the most individual "
    f"antibiotic approvals, with {highest_number} approvals."
)


# ------------------------------------------------------------
# FIRST FDA APPROVAL OF EACH ANTIBIOTIC CLASS
# ------------------------------------------------------------

# Group the dataset by antibiotic class
# .min() finds the earliest FDA approval year recorded for an antibiotic belonging to each class
first_approval_by_class = (
    antibiotics
    .groupby("Class")["FDA-Approval Year"]
    .min()
)

# Convert each first approval year into a decade
first_class_decade = (
    first_approval_by_class // 10
) * 10

# Count how many classes first appear in each decade
new_classes_per_decade = (
    first_class_decade
    .value_counts()
    .sort_index()
)

# Print the results without the extra pandas information
print("\nAntibiotic classes first appearing per decade:")

for decade, count in new_classes_per_decade.items():
    print(f"{decade}s: {count} classes")

# Find the decade in which the most classes first appear
highest_class_decade = new_classes_per_decade.idxmax()
highest_class_number = new_classes_per_decade.max()

print(
    f"\nThe {highest_class_decade}s had the most antibiotic "
    f"classes appearing for the first time in the dataset, "
    f"with {highest_class_number} classes."
)


# ============================================================
# VISUALISATION 1 - INDIVIDUAL ANTIBIOTIC APPROVALS
# ============================================================

# Create a figure and set its size
plt.figure(figsize=(9, 5))

# Create the bar chart
plt.bar(
    approvals_per_decade.index,
    approvals_per_decade.values,
    width=7,
    color="steelblue",
    edgecolor="black"
)

# Add the title and axis labels
plt.title(
    "US Antibiotic Approvals by Decade",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Decade", fontsize=11)
plt.ylabel("Number of Antibiotic Approvals", fontsize=11)

# Display every decade on the x-axis
plt.xticks(approvals_per_decade.index)

# Add light horizontal grid lines
plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

# Add the number of approvals above each bar
for decade, count in approvals_per_decade.items():
    plt.text(
        decade,
        count + 0.5,
        str(count),
        ha="center",
        fontsize=9
    )

# Make sure the labels fit inside the figure
plt.tight_layout()

# Display the graph
plt.show()


# ============================================================
# VISUALISATION 2 - FIRST APPEARANCE OF ANTIBIOTIC CLASSES
# ============================================================

plt.figure(figsize=(9, 5))

plt.bar(
    new_classes_per_decade.index,
    new_classes_per_decade.values,
    width=7,
    color="cornflowerblue",
    edgecolor="black"
)

plt.title(
    "First FDA Approval of Antibiotic Classes by Decade",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Decade", fontsize=11)
plt.ylabel("Number of Antibiotic Classes", fontsize=11)

plt.xticks(new_classes_per_decade.index)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

# Add the number of classes above each bar
for decade, count in new_classes_per_decade.items():
    plt.text(
        decade,
        count + 0.15,
        str(count),
        ha="center",
        fontsize=9
    )

plt.tight_layout()
plt.show()


# ============================================================
# PART 2 - WHO 2025 ANTIBACTERIAL CLINICAL PIPELINE
# ============================================================

print("\n============================================================")
print("          WHO 2025 ANTIBACTERIAL PIPELINE")
print("============================================================")


# ------------------------------------------------------------
# LOAD THE WHO DATASET
# ------------------------------------------------------------

# Read the Master DataDrugID sheet from the WHO Excel file
who_pipeline = pd.read_excel(
    "data/who_amr_antibacterial_clinical_dataset_2025_final.xlsx",
    sheet_name="Master DataDrugID"
)

# Count the total number of products in the pipeline
number_of_products = len(who_pipeline)

print(
    f"\nNumber of products in the WHO 2025 "
    f"clinical pipeline: {number_of_products}"
)


# ------------------------------------------------------------
# TRADITIONAL VS NON-TRADITIONAL PRODUCTS
# ------------------------------------------------------------

# Count how many products belong to each product type
product_type_counts = (
    who_pipeline["Product type"]
    .value_counts()
)

# Calculate what percentage of the full pipeline each product type represents
product_type_percentages = (
    product_type_counts / number_of_products
) * 100

# Round the percentages to one decimal place
product_type_percentages = (
    product_type_percentages.round(1)
)

# Print the counts and percentages together
print("\nTraditional vs non-traditional products:")

for product_type, count in product_type_counts.items():

    percentage = product_type_percentages[product_type]

    print(
        f"{product_type}: "
        f"{count} products ({percentage}%)"
    )


# ------------------------------------------------------------
# NON-TRADITIONAL ANTIBACTERIAL APPROACHES
# ------------------------------------------------------------

# Keep only products labelled as Non-traditional
non_traditional = who_pipeline[
    who_pipeline["Product type"] == "Non-traditional"
]

# Count the different non-traditional categories
# Missing values are ignored by value_counts()
non_traditional_counts = (
    non_traditional["Non-traditionals categories"]
    .value_counts()
)

# Count how many non-traditional products have a specific category recorded
recorded_non_traditional = (
    non_traditional_counts.sum()
)

total_non_traditional = len(non_traditional)

# Print each category in a cleaner format
print("\nNon-traditional antibacterial approaches:")

for category, count in non_traditional_counts.items():
    print(f"{category}: {count} products")

print(
    f"\n{recorded_non_traditional} of "
    f"{total_non_traditional} non-traditional products "
    f"have a specific category recorded."
)


# ------------------------------------------------------------
# CHECK THE INNOVATION COLUMN
# ------------------------------------------------------------

# Check the values used in the WHO Innovative? column
# This was done before deciding whether the column could be used for a quantitative comparison
innovation_values = (
    who_pipeline["Innovative?"]
    .value_counts(dropna=False)
)

# Check which product types contain missing innovation values
missing_innovation = who_pipeline[
    who_pipeline["Innovative?"].isna()
]

# Examine traditional products separately
traditional_products = who_pipeline[
    who_pipeline["Product type"] == "Traditional"
]

traditional_innovation = (
    traditional_products["Innovative?"]
    .value_counts(dropna=False)
)

# The WHO assesses innovation using specific criteria, including cross-resistance, antibacterial class,  target and mode of action.
# The raw Innovative? column contains differently coded, uncertain and missing values. Therefore, a simple  innovation percentage is not calculated directly from this column.


# ------------------------------------------------------------
# PHASES OF CLINICAL DEVELOPMENT
# ------------------------------------------------------------

# The dataset contains two labels for the same NDA/MAA stage:
# "NDA/MAA" and "NDA / MAA".
# Replace the second version so they are counted together.
who_pipeline["Phase of development"] = (
    who_pipeline["Phase of development"]
    .replace("NDA / MAA", "NDA/MAA")
)

# Count the number of products in each development phase
phase_counts = (
    who_pipeline["Phase of development"]
    .value_counts()
)

# Put the phases into their logical clinical order
phase_order = [
    "Phase 1",
    "Phase 1/2",
    "Phase 2",
    "Phase 2/3",
    "Phase 3",
    "NDA/MAA"
]

print("\nProducts by clinical development phase:")

for phase in phase_order:

    # Only print the phase if it exists in the dataset
    if phase in phase_counts.index:
        print(f"{phase}: {phase_counts[phase]} products")

# ------------------------------------------------------------
# PRODUCT TYPE BY CLINICAL DEVELOPMENT PHASE
# ------------------------------------------------------------

# Compare the development phase with the product type
# pd.crosstab() counts how many products fall into each combination of phase and product type
phase_by_product_type = pd.crosstab(
    who_pipeline["Phase of development"],
    who_pipeline["Product type"]
)

# Put the phases into their logical clinical order
phase_by_product_type = phase_by_product_type.reindex(
    phase_order
)

print("\nTraditional vs non-traditional products by development phase:")

# Print the comparison in a cleaner format
for phase in phase_order:

    traditional_count = phase_by_product_type.loc[
        phase, "Traditional"
    ]

    non_traditional_count = phase_by_product_type.loc[
        phase, "Non-traditional"
    ]

    print(
        f"{phase}: "
        f"{traditional_count} traditional, "
        f"{non_traditional_count} non-traditional"
    )

# Calculate the percentage of each product type found at each stage of clinical development
phase_percentages = (
    phase_by_product_type
    / phase_by_product_type.sum()
) * 100

print("\nPercentage of each product type by development phase:")

for phase in phase_order:

    traditional_percentage = phase_percentages.loc[
        phase, "Traditional"
    ]

    non_traditional_percentage = phase_percentages.loc[
        phase, "Non-traditional"
    ]

    print(
        f"{phase}: "
        f"{traditional_percentage:.1f}% traditional, "
        f"{non_traditional_percentage:.1f}% non-traditional"
    )

# ============================================================
# VISUALISATION 3 - CURRENT ANTIBACTERIAL PIPELINE
# ============================================================

plt.figure(figsize=(8, 5))

plt.bar(
    product_type_counts.index,
    product_type_counts.values,
    width=0.6,
    color=["seagreen", "mediumseagreen"],
    edgecolor="black"
)

plt.title(
    "WHO 2025 Antibacterial Clinical Pipeline",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Product Type", fontsize=11)
plt.ylabel("Number of Products", fontsize=11)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

# Add the count and percentage above each bar
for product_type, count in product_type_counts.items():

    percentage = product_type_percentages[product_type]

    plt.text(
        product_type,
        count + 1,
        f"{count} ({percentage}%)",
        ha="center",
        fontsize=10
    )

plt.tight_layout()
plt.show()


# ============================================================
# VISUALISATION 4 - NON-TRADITIONAL APPROACHES
# ============================================================

plt.figure(figsize=(10, 6))

# Sort the categories so the largest category appears at the top of the horizontal graph
non_traditional_plot = (
    non_traditional_counts
    .sort_values()
)

plt.barh(
    non_traditional_plot.index,
    non_traditional_plot.values,
    color="mediumseagreen",
    edgecolor="black"
)

plt.title(
    "Non-Traditional Products in the WHO 2025 Clinical Pipeline",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Number of Products", fontsize=11)

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.3
)

# Add the number of products at the end of each bar
for category, count in non_traditional_plot.items():
    plt.text(
        count + 0.15,
        category,
        str(count),
        va="center",
        fontsize=9
    )

plt.tight_layout()
plt.show()


# ============================================================
# SUMMARY OF MAIN RESULTS
# ============================================================

print("\n============================================================")
print("                    MAIN RESULTS")
print("============================================================")

print(
    f"\nHistorical dataset: {number_of_antibiotics} antibiotic "
    f"entries covering FDA approvals from {first_year} to "
    f"{last_year}."
)

print(
    f"The highest number of individual antibiotic approvals "
    f"occurred in the {highest_decade}s "
    f"({highest_number} approvals)."
)

print(
    f"The highest number of antibiotic classes appearing for "
    f"the first time occurred in the {highest_class_decade}s "
    f"({highest_class_number} classes)."
)

print(
    f"\nWHO 2025 clinical pipeline: "
    f"{number_of_products} products."
)

print(
    f"Traditional products: "
    f"{product_type_counts['Traditional']} "
    f"({product_type_percentages['Traditional']}%)."
)

print(
    f"Non-traditional products: "
    f"{product_type_counts['Non-traditional']} "
    f"({product_type_percentages['Non-traditional']}%)."
)

print(
    f"Of the {total_non_traditional} non-traditional products, "
    f"{recorded_non_traditional} have a specific "
    f"non-traditional category recorded."
)

print("\n============================================================")
print("                 ANALYSIS COMPLETE")
print("============================================================")