# Week 8: Evaluation & Error Analysis Report

## Summary Findings
- **Total Test Samples:** 5
- **False Positives:** Identified negative cases incorrectly predicted as positive due to sarcastic keywords (e.g., "wonderful job", "Thanks").
- **Ambiguous Cases:** Neutral text ("It is okay...") resulted in low confidence scores (~0.52).

## Confidence Filtering Impact
- **Threshold Applied:** 80% (0.80)
- **High-Confidence Predictions:** 4 accepted
- **Flagged Predictions:** 1 flagged for 'Needs Manual Review'
-