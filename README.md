# Genre, Vocabulary, and Semantic Networks in Biblical Hebrew

## Project overview

This project is a computational pilot study of genre, vocabulary, lexical association, and network structure in Biblical Hebrew.

It compares selected passages from four broad genres in the Hebrew Bible:

- Law
- Narrative
- Prophecy
- Poetry/Wisdom

The project uses the ETCBC/BHSA Hebrew Bible corpus through Text-Fabric and follows a reproducible digital humanities workflow: corpus loading, data preparation, flat-table export, lexical filtering, frequency analysis, TF-IDF analysis, cosine similarity, PMI-based word association analysis, network analysis, visualization, and interpretation.

## Research question

**How do major genres in Biblical Hebrew — law, narrative, prophecy, and poetry/wisdom — differ in their vocabulary, lexical associations, and network structure?**

This question treats genre not only as a literary category, but also as something that may leave measurable traces in lexical distribution, word associations, and graph structure.

## Source corpus

The source corpus is the ETCBC/BHSA Hebrew Bible corpus, accessed through Text-Fabric. The corpus provides rich word-level linguistic annotation, including book, chapter, verse, surface form, lexeme, and part-of-speech information.

## Pilot corpus

The current pilot sample includes the following chapters:

- **Narrative**: Genesis 37–45 — Joseph narrative
- **Narrative**: Samuel_I 8–12 — Rise of monarchy / Samuel and Saul
- **Law**: Leviticus 1–7 — Sacrificial law
- **Law**: Deuteronomium 12–16 — Legal and cultic material
- **Prophecy**: Jesaia 1–12 — Opening prophetic oracles
- **Prophecy**: Amos 1–9 — Prophetic judgment speeches
- **Poetry_Wisdom**: Psalmi 1–25 — Poetic psalms
- **Poetry_Wisdom**: Proverbia 1–10 — Wisdom instruction

The pilot dataset contains approximately **28,215 total tokens**. After filtering the data to content words only, the analysis uses approximately **14,707 content tokens**.

Content-token counts by genre:

```text
Law: 2,971
Narrative: 4,057
Poetry_Wisdom: 3,978
Prophecy: 3,701
```

## Data model

The BHSA corpus is converted into a flat word-level table. Each row represents a word token and includes metadata such as:

- genre
- book
- chapter
- verse
- word node
- surface form
- lexeme / lemma
- part of speech

This structure makes the project reproducible and allows the annotated ancient corpus to be analyzed with standard Python tools.

## Method

The analysis follows these steps:

1. Load the BHSA corpus through Text-Fabric.
2. Select a controlled pilot sample of chapters from four genres.
3. Convert the selected chapters into a flat word-level table.
4. Add genre labels to each token.
5. Export processed data as CSV and JSONL.
6. Filter the data to content words only: nouns, verbs, adjectives, and adverbs.
7. Exclude grammatical categories such as prepositions, conjunctions, particles, articles, pronouns, and proper names.
8. Calculate lemma frequencies by genre.
9. Use TF-IDF to identify lemmas that are especially characteristic of each genre.
10. Use cosine similarity and cosine distance to compare genre-level and book-level lexical profiles.
11. Use PMI to identify word associations within each genre.
12. Build genre-similarity and word-association networks.
13. Calculate network metrics such as degree centrality and betweenness centrality.
14. Interpret the computational results in relation to literary, linguistic, and philological questions.

## Notebooks

The project notebooks are organized as follows:

```text
notebooks/
├── 01_load_bhsa.ipynb
├── 02_prepare_dataset_clean.ipynb
├── 03_frequency_tfidf_clean.ipynb
├── 04_similarity_distances.ipynb
├── 05_pmi_word_associations.ipynb
├── 06_network_analysis.ipynb
└── 07_final_outputs_and_poster.ipynb
```

Recommended run order:

```text
01_load_bhsa.ipynb
02_prepare_dataset_clean.ipynb
03_frequency_tfidf_clean.ipynb
04_similarity_distances.ipynb
05_pmi_word_associations.ipynb
06_network_analysis.ipynb
07_final_outputs_and_poster.ipynb
```

## Main outputs

### Processed data

- `data/processed/biblical_hebrew_tokens.csv`
- `data/processed/biblical_hebrew_tokens.jsonl`
- `data/processed/biblical_hebrew_tokens_with_hebrew.csv`
- `data/processed/biblical_hebrew_content_tokens.csv`
- `data/processed/genre_chapter_sample.csv`
- `data/processed/genre_mapping.csv`
- `data/processed/preliminary_stopwords.csv`

### Analysis tables

- `output/tables/genre_word_frequencies.csv`
- `output/tables/tfidf_by_genre.csv`
- `output/tables/top_15_tfidf_by_genre.csv`
- `output/tables/top_tfidf_summary_by_genre.csv`
- `output/tables/genre_cosine_similarity.csv`
- `output/tables/genre_cosine_distance.csv`
- `output/tables/book_cosine_similarity.csv`
- `output/tables/book_similarity_edges.csv`
- `output/tables/pmi_word_associations.csv`
- `output/tables/top_pmi_by_genre.csv`
- `output/tables/pmi_summary_by_genre.csv`
- `output/tables/genre_similarity_network_edges.csv`
- `output/tables/genre_network_centrality.csv`
- `output/tables/word_association_network_edges.csv`
- `output/tables/word_network_centrality.csv`

### Figures

- `output/figures/top_tfidf_Law_friendly.png`
- `output/figures/top_tfidf_Narrative_friendly.png`
- `output/figures/top_tfidf_Poetry_Wisdom_friendly.png`
- `output/figures/top_tfidf_Prophecy_friendly.png`
- `output/figures/genre_cosine_similarity_heatmap.png`
- `output/figures/top_pmi_Law_friendly.png`
- `output/figures/top_pmi_Narrative_friendly.png`
- `output/figures/top_pmi_Poetry_Wisdom_friendly.png`
- `output/figures/top_pmi_Prophecy_friendly.png`
- `output/figures/genre_similarity_network.png`
- `output/figures/word_association_network_friendly.png`
- `output/figures/FIGURE_LABEL_NOTE.md`


English glosses are added to the friendly figures to make them readable for non-specialist viewers, while the original BHSA lexeme codes are preserved in parentheses for scholarly traceability.

### Poster / research text

- `poster/poster_text_1000_words.md`

## Preliminary findings

The pilot results suggest that genre differences in Biblical Hebrew are reflected in measurable lexical patterns and lexical associations:

- The legal sample is associated with ritual, priestly, sacrificial, and cultic vocabulary.
- The narrative sample is associated with characters, movement, speech, dreams, kingship, and social roles.
- The poetry/wisdom sample emphasizes moral, psychological, reflective, and didactic vocabulary.
- The prophetic sample combines divine speech formulas with political, military, and judgment-related language.

The TF-IDF results show which lexemes are especially distinctive for each genre. Cosine similarity provides a second perspective by comparing genre-level and book-level lexical profiles. PMI and network analysis add a relational layer by showing which words are associated with one another and which lexemes function as central or bridging nodes.

## Interpretation

The findings support the idea that broad biblical genres differ in computationally measurable ways. The project does not claim that genre can be reduced to word counts or graph metrics. Instead, it shows that lexical distribution, association, and network structure can support traditional literary and philological interpretation.

## Limitations

This is a pilot study rather than a full analysis of the Hebrew Bible. The sample includes selected chapters rather than entire books. The genre labels are simplified, and some biblical books contain mixed genres. TF-IDF, PMI, similarity metrics, and network measures are sensitive to the selected sample and preprocessing choices. The computational results therefore support interpretation but do not replace close reading, historical analysis, or philological judgment.

## Project structure

```text
biblical_hebrew_genre_analysis/
├── README.md
├── MANIFEST.md
├── notebooks/
├── src/
├── data/
│   └── processed/
├── output/
│   ├── tables/
│   └── figures/
└── poster/
```

## Reproducibility

The project is designed to be run in Google Colab. The notebooks mount Google Drive, read the processed data, and write analysis outputs back into the project folders. Running the notebooks in order should reproduce the main tables and figures.

## References

- ETCBC / BHSA — Biblia Hebraica Stuttgartensia Amstelodamensis.
- Text-Fabric documentation.
- ALPcourse notebooks and course materials.
