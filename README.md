# The Agglutination Tax

Official implementation of the paper: **"The Agglutination Tax: Quantifying Typology-Driven Scaling Behavior for Tibeto-Burman and Indo-Aryan Languages"**.

## Key Findings

- **The Agglutination Tax:** Tibeto-Burman languages require approximately **1.64×** more data than Indo-Aryan languages to reach comparable morphological saturation in our experimental setting.
- **TSMB Discovery:** Identified the **Tokenizer-Script Misalignment Barrier** (NFC/NFD mismatch) as a data preprocessing issue affecting Mizo scaling behavior.
- **Asymmetric Transfer:** TB models demonstrate superior zero-shot transferability to IA neighbors compared to the inverse direction.

## Repository Contents

- `data_preprocessing/nfc_fix.py`: Script to resolve Unicode normalization issues (TSMB Fix)
- `experiments/scaling_analysis.ipynb`: Reproducible notebook for power-law fitting and bootstrap CI generation
- `experiments/bootstrap_significance.py`: Bootstrap script for calculating 95% Confidence Intervals
- `plots/`: PDF/PNG versions of all figures used in the manuscript

## Getting Started

### Installation

Clone this repository and install dependencies:
```bash
git clone https://github.com/Badalnyalang/agglutination-tax.git
cd agglutination-tax
pip install -r requirements.txt
```

### Data Access

Our corpora are available on HuggingFace:
- [MWire Labs Northeast Indian Language Corpora](https://huggingface.co/datasets/MWirelabs)

### Reproduce Results

Apply TSMB fix (NFC normalization):
```bash
python data_preprocessing/nfc_fix.py
```

Run the scaling analysis:
```bash
jupyter notebook experiments/scaling_analysis.ipynb
```

Generate bootstrap confidence intervals:
```bash
python experiments/bootstrap_significance.py
```

## Experimental Setup

- **Hardware:** NVIDIA A40 (46GB VRAM)
- **Model Size:** 110M parameters (RoBERTa-base architecture)
- **Training Scales:** 6 data points from 10⁴ to 10⁶ tokens
- **Evaluation:** 10,000-sequence held-out test sets
- **Bootstrap Iterations:** 1,000 for confidence interval estimation

## Results Summary

| Language | Family | β | 95% CI | R² | Regime |
|----------|--------|---|--------|-----|--------|
| Meitei | TB | 0.0549 | [0.051, 0.058] | 0.952 | Active Scaling |
| Assamese | IA | -0.0021 | Saturated | 0.036 | Saturation Plateau |
| Mizo | TB | -0.0055 | Saturated | 0.427 | TSMB Limited |

**Zero-Shot Transfer (Perplexity):**
- TB → IA: **PPL ≈ 200**
- IA → TB: **PPL > 36,000**

## Contact

For questions or collaborations:
- **Badal Nyalang:** nyalang@mwirelabs.com
- **Chelang Pala:** chelang@mwirelabs.com

## Acknowledgments

This work was supported by MWire Labs. We acknowledge the MizBERT team (Robz Zchhangte et al.) for their foundational contributions to Tibeto-Burman language modeling.

## Related Work

- [MizBERT: A BERT-based model for Mizo](https://huggingface.co/robzchhangte/MizBERT)
- [IndicNLPSuite](https://github.com/AI4Bharat/IndicNLP)
- [Morphology Matters: TACL 2021](https://aclanthology.org/2021.tacl-1.16/)

---

**⭐ Star this repo if you find it useful for low-resource language modeling research!**
