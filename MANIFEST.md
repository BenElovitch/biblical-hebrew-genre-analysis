# Final Submission Package

Created: 20260624_1455

## Project

Genre, Vocabulary, and Semantic Networks in Biblical Hebrew

## Run order

1. 01_load_bhsa.ipynb
2. 02_prepare_dataset_clean.ipynb
3. 03_frequency_tfidf_clean.ipynb
4. 04_similarity_distances.ipynb
5. 05_pmi_word_associations.ipynb
6. 06_network_analysis.ipynb
7. 07_final_outputs_and_poster.ipynb

## Main methods

- Frequency analysis
- TF-IDF
- Cosine similarity and distance
- PMI word associations
- Network analysis

## Main folders

- notebooks/
- data/processed/
- output/tables/
- output/figures/
- poster/

## Final selected figures

The figures folder intentionally contains only the final readable visualizations:

- top_tfidf_Law_friendly.png
- top_tfidf_Narrative_friendly.png
- top_tfidf_Poetry_Wisdom_friendly.png
- top_tfidf_Prophecy_friendly.png
- top_pmi_Law_friendly.png
- top_pmi_Narrative_friendly.png
- top_pmi_Poetry_Wisdom_friendly.png
- top_pmi_Prophecy_friendly.png
- genre_cosine_similarity_heatmap.png
- genre_similarity_network.png
- word_association_network_friendly.png
- FIGURE_LABEL_NOTE.md

English glosses are added to make the figures readable for non-specialist viewers, while the original BHSA lexeme codes are preserved in parentheses for scholarly traceability.

## Notes

This package intentionally excludes backup notebooks, old drafts, temporary files, experimental figures, and earlier less-readable figure versions.
