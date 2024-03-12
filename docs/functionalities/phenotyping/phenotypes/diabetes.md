{% set csv_path = "eds_scikit/phenotype/diabetes/codes.csv" %}

# Diabetes

## Presentation

We provide the [DiabetesFromICD10][eds_scikit.phenotype.diabetes.diabetes.DiabetesFromICD10] class to extract visits or patients with ICD10 codes related to diabetes

??? note "Available diabetes types"
    {{ values_from_csv(csv_path, col="Diabetes type", indent="\t") }}

!!! algos "How it works"
    The algorithm works by looking for either DP, DR or DAS ICD10 codes associated with cancer.
    Those codes are available under `DiabetesFromICD10.ICD10_CODES`

## Usage

By default, all diabetes types mentionned above are extracted

{{ load_data }}

```python
from eds_scikit.phenotype import DiabetesFromICD10

diabetes = DiabetesFromICD10(data)
data = diabetes.to_data()
```

To choose a subset of disorders, use the `diabetes_types` argument:

```python
diabetes = DiabetesFromICD10(
    data,
    diabetes_types=[
        "DIABETES_TYPE_I",
        "DIABETES_IN_PREGNANCY",
    ],
)
```

The final phenotype DataFrame is then available at `data.computed["DiabetesFromICD10"]`

### Optional parameters

::: eds_scikit.phenotype.diabetes.diabetes.DiabetesFromICD10.__init__
    options:
         docstring_section_style: spacy
         show_signature_annotations: true
         show_signature: true
         heading_level: 3
         members_order: source
         show_source: false
         separate_signature: true


## Reference

Check the code reference [here][eds_scikit.phenotype.diabetes.diabetes.DiabetesFromICD10] for a more detailled look.

\bibliography
