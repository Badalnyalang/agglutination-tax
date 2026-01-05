# The Agglutination Tax 

Official implementation of the paper: **"The Agglutination Tax: Quantifying Typology-Driven Scaling Laws for Tibeto-Burman and Indo-Aryan Languages"** (DMLR 2026).

## Key Findings
- **The Agglutination Tax:** Tibeto-Burman languages require **1.64x** more data than Indo-Aryan languages to reach equivalent morphological saturation.
- **TSMB Discovery:** Identified the Tokenizer-Script Misalignment Barrier in Mizo data.
- **Asymmetric Transfer:** TB models act as computational supersets for IA neighbors.

## Repository Contents
- `nfc_fix.py`: Script to resolve Unicode normalization issues in low-resource corpora.
- `scaling_analysis.ipynb`: Reproducible notebook for power-law fitting and bootstrap CI generation.

## Citation
```bibtex
@article{nyalang2026agglutination,
  title={The Agglutination Tax: Quantifying Typology-Driven Scaling Laws},
  author={Nyalang, Badal and Pala, Chelang},
  journal={DMLR},
  year={2026}
}
