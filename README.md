# Are We Running Out of Antibiotics?

**MAT2007 - Introduction to Programming**

## Project overview

This project investigates what historical and current data can tell us about antibacterial drug development. Rather than simply counting new antibiotics, it considers the difference between individual drug approvals, the first recorded appearance of antibiotic classes, and the types of antibacterial products currently undergoing clinical development.

Two datasets are analysed separately because they differ in geographical coverage, time period and development stage.

## Datasets

### 1. Historical US antibiotic approvals

**File:** `Antibiotics_approvals_US.xlsx`

Contains 157 antibiotic entries with FDA approval years ranging from 1939 to 2017. The analysis uses the antibiotic class and FDA approval year to investigate approvals by decade and the first recorded appearance of each class.

### 2. WHO 2025 antibacterial clinical pipeline

**File:** `who_amr_antibacterial_clinical_dataset_2025_final.xlsx`

Contains 90 products in clinical development. The analysis uses the `Master DataDrugID` worksheet to examine traditional and non-traditional products, non-traditional treatment categories and clinical development phases.

## Requirements

The analysis requires Python and these libraries:

- `pandas` - reading, organising and analysing the datasets
- `matplotlib` - creating graphs
- `openpyxl` - reading Excel files through pandas

Install them with:

```bash
python -m pip install pandas matplotlib openpyxl
```

## How to run the analysis

Organise the project files as follows:

```text
Antibiotic-Development-Project/
├── project.py
├── README.md
├── data/
│   ├── Antibiotics_approvals_US.xlsx
│   └── who_amr_antibacterial_clinical_dataset_2025_final.xlsx
└── MAT2007_Project_Report.pdf
```

Open a terminal in the project folder and run:

```bash
python project.py
```

The program prints the analysis results to the terminal and displays four graphs using Matplotlib. The graphs are displayed interactively rather than automatically saved as image files.

## Data analysis

### Historical antibiotic approvals

The FDA approval years are grouped into decades using integer division. The program then counts individual antibiotic approvals per decade.

To investigate antibiotic-class diversity, the earliest approval year recorded for each class is identified using `groupby()` and `min()`. These years are grouped by decade to determine when each class first appears in the dataset.

### WHO 2025 clinical pipeline

The program counts traditional and non-traditional products and calculates their percentages of the full pipeline.

Non-traditional products are examined separately to identify the frequency of different antibacterial approaches. Missing category information is accounted for when reporting how many products have a specific category recorded.

The `Innovative?` column is also inspected, but no overall innovation percentage is calculated because the column contains inconsistent, uncertain and missing values.

Clinical development phases are standardised where necessary, and `pd.crosstab()` is used to compare the distributions of traditional and non-traditional products. Percentages are calculated within each product type.

## Results

The historical dataset shows that individual antibiotic approvals peaked in the **1980s, with 31 approvals**, whereas first recorded class appearances peaked in the **1950s, with nine classes**.

In the WHO 2025 clinical pipeline, **50 products (55.6%)** were traditional and **40 products (44.4%)** were non-traditional. Of the non-traditional products, 38 had a specific approach recorded.

For the later development stages (Phase 3 and NDA/MAA combined), 22% of traditional products and 10% of non-traditional products were represented.

The program generates four visualisations:

1. US Antibiotic Approvals by Decade
2. First FDA Approval of Antibiotic Classes by Decade
3. WHO 2025 Antibacterial Clinical Pipeline
4. Non-Traditional Products in the WHO 2025 Clinical Pipeline

## Limitations

The historical dataset records US FDA approvals, whereas the WHO dataset describes a global snapshot of products in clinical development. These measurements cannot be directly combined into a continuous timeline.

The earliest class approval in the historical dataset does not necessarily represent the first worldwide discovery or introduction of that class. Similarly, products in clinical development are not guaranteed to receive regulatory approval.

## References

Dattani, S. (2024). *What was the Golden Age of Antibiotics, and how can we spark a new one?* Our World in Data. https://ourworldindata.org/golden-age-antibiotics

Hutchings, M. I., Truman, A. W., & Wilkinson, B. (2019). Antibiotics: Past, present and future. *Current Opinion in Microbiology, 51*, 72–80. https://doi.org/10.1016/j.mib.2019.10.008

World Health Organization. (2025). *Analysis of antibacterial agents in clinical and preclinical development: Overview and analysis 2025.* https://www.who.int/publications/i/item/9789240113091
