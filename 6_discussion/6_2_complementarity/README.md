# 6.2 Complementarity of Image and FEA Sequences

[Discussion](../README.md)

[dynamic_fusion_correctness_groups.ipynb](dynamic_fusion_correctness_groups.ipynb) reads the shared static/dynamic predictions and produces **Figure 5** and the descriptive results in Section 6.2. Start with [section_6_2_summary.md](section_6_2_summary.md).

| Reported result | Saved output |
| --- | --- |
| Fusion correctness within four unimodal groups; 138/190 = 72.63% of exactly-one-correct cases resolved | [Figure 5](figures/dynamic_fusion_correctness_groups.pdf) and [group counts](tables/dynamic_fusion_correctness_groups.csv) |
| Class-wise precision/recall/F1 and fusion recall differences | [Metrics](tables/dynamic_class_metrics.csv) and [recall comparison](tables/dynamic_class_recall_comparison.csv) |
| Three dominant confusions: 84/139 = 60.43% of errors | [Named confusions](tables/dominant_multimodal_confusions.csv) and [all error pairs](tables/dynamic_multimodal_error_pairs.csv) |
| Static–dynamic overlap; exactly-one-correct cases decrease from 242 to 190 | [Overlap table](tables/static_dynamic_unimodal_overlap.csv) |

Class-wise FEA metrics use one prediction per reenactment; overlap/fusion outcomes use both camera views. These are descriptive comparisons. Accuracy significance tests are in [model comparisons](../significance-tests/README.md); signal and annotation analyses are in [Section 6.3](../6_3_interpreting/README.md).
