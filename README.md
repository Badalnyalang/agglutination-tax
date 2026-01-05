# The Agglutination Tax

Official implementation of the paper: **"The Agglutination Tax: Quantifying Typology-Driven Scaling Laws for Tibeto-Burman and Indo-Aryan Languages"**.

## Key Findings
- **The Agglutination Tax:** Tibeto-Burman languages require **1.64x** more data than Indo-Aryan languages to reach equivalent morphological saturation.
- **TSMB Discovery:** Identified the **Tokenizer-Script Misalignment Barrier** (NFC/NFD mismatch) as a primary bottleneck in Mizo data scaling.
- **Asymmetric Transfer:** TB models act as computational "supersets" for IA neighbors, showing significantly higher zero-shot transferability.

## Repository Contents
- `data_preprocessing/nfc_fix.py`: Script to resolve Unicode normalization issues (TSMB Fix).
- `experiments/scaling_analysis.ipynb`: Reproducible notebook for power-law fitting and bootstrap CI generation.
- `experiments/bootstrap_significance.py`: Fast, cached bootstrap script for calculating 95% Confidence Intervals.
- `plots/`: PDF/PNG versions of all figures used in the manuscript.

## Getting Started

### 1. Installation
Clone this repository and install the required dependencies:
```bash
git clone [https://github.com/mwirelabs/agglutination-tax.git](https://github.com/mwirelabs/agglutination-tax.git)
cd agglutination-tax
pip install -r requirements.txt
