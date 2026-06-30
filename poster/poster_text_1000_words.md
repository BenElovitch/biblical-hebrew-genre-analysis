# Genre, Vocabulary, and Semantic Networks in Biblical Hebrew: A Computational Pilot Study

## Research question

How do major genres in Biblical Hebrew—law, narrative, prophecy, and poetry/wisdom—differ in their vocabulary, lexical associations, and network structure? This project treats genre not only as a literary category, but also as something that may leave measurable traces in lexical distribution, word association, and graph structure. The main goal is not to replace close reading or philological interpretation, but to test whether computational methods can make genre-based lexical differences visible in a systematic and reproducible way.

## Dataset

The project uses the ETCBC/BHSA corpus, accessed through Text-Fabric. BHSA is a richly annotated representation of the Hebrew Bible. It provides book, chapter, verse, word forms, lexemes, and part-of-speech information, which makes it especially suitable for a computational study of ancient Hebrew. For this pilot study, the corpus is not treated as one uniform text. Instead, selected chapters are grouped into four broad literary genres: narrative, law, prophecy, and poetry/wisdom. The narrative sample includes Genesis 37–45 and Samuel I 8–12; the legal sample includes Leviticus 1–7 and Deuteronomium 12–16; the prophetic sample includes Jesaia 1–12 and Amos 1–9; and the poetry/wisdom sample includes Psalmi 1–25 and Proverbia 1–10.

The pilot corpus contains 28,215 word tokens. After filtering the data to content words—nouns, verbs, adjectives, and adverbs—the analysis uses approximately 14,707 content tokens. Function-word categories such as particles, conjunctions, prepositions, articles, pronouns, and proper names are excluded. This filtering choice is intended to emphasize lexical patterns connected to meaning, theme, and discourse rather than general grammatical structure.

## Data model and preparation

The BHSA corpus is transformed into a flat word-level table. Each row represents one word token and includes the book, chapter, verse, genre label, word node, surface form, lexeme, and part of speech. This data model is important because it converts a complex annotated ancient corpus into a structured dataset that can be analyzed with standard Python tools. Additional metadata tables document the selected chapters and the genre mapping. This makes the workflow reproducible and allows every analytical step to be traced back to specific biblical passages.

## Methods

The project combines several computational methods from the ALPcourse workflow. First, exploratory frequency analysis identifies common lexemes within each genre. This provides a basic view of what kinds of vocabulary dominate each genre, but frequency alone can be misleading because very common words may not be distinctive. Second, TF-IDF is used to identify lexemes that are especially characteristic of a genre relative to the whole sample. Third, cosine similarity and cosine distance compare genre-level and book-level lexical profiles in vector space. This asks whether genres or books are lexically close to one another, rather than only asking which words are frequent.

The project then adds a relational layer. PMI is used to identify word pairs that appear together more strongly than expected by chance within verse-level contexts. This helps show not only which words are important, but which words tend to form associations. Finally, network analysis turns similarity and association data into graphs. In the genre-similarity network, nodes represent genres and edges represent lexical similarity. In the word-association network, nodes represent lexemes and edges represent PMI-based associations. Network measures such as degree centrality and betweenness centrality help identify central lexical hubs and possible bridging terms between clusters.

## Results

The results suggest that broad biblical genres do produce measurable lexical patterns. The legal sample is strongly associated with ritual, priestly, sacrificial, and cultic vocabulary. This fits the selected passages, especially the legal and sacrificial material in Leviticus and Deuteronomy. The narrative sample emphasizes characters, movement, dreams, speech situations, kingship, and social roles. This reflects the action-oriented and character-centered nature of the Joseph narrative and the rise of monarchy in Samuel. The poetry/wisdom sample highlights moral, psychological, reflective, and didactic vocabulary, including words connected to the heart, wisdom, instruction, righteousness, and wickedness. The prophetic sample combines divine speech formulas with political, military, and judgment-related language.

The TF-IDF results show that these genre differences are not only visible through expected themes, but also through measurable lexical profiles. Similarity analysis adds another perspective by showing how genres and books relate to one another as vectors. PMI identifies recurring lexical associations within genres, while network analysis visualizes these relationships as connected structures. The genre network gives a compact overview of lexical proximity between genre groups, and the word network highlights which lexemes function as central or bridging nodes.

## Interpretation

The findings support the idea that genre in Biblical Hebrew is reflected in lexical distribution and association. Legal texts are organized around ritual practice, obligation, and cultic procedure. Narrative texts are organized around action, human interaction, speech, and social roles. Wisdom and poetic texts emphasize moral reflection, instruction, and inner life. Prophetic texts combine divine address, judgment, political crisis, and social critique. These computational findings do not prove genre boundaries by themselves, but they provide evidence that can support and refine traditional literary and philological interpretation.

## Limitations

This is a pilot study rather than a complete classification of Biblical Hebrew genres. The sample includes selected chapters rather than entire books, and the genre labels are simplified. Some biblical books contain mixed genres, and even individual chapters can shift between narration, speech, law, poetry, and exhortation. The results also depend on preprocessing choices, including the decision to remove function words and proper names. TF-IDF, PMI, cosine similarity, and network metrics are sensitive to sample size, context window, and threshold choices. Therefore, the results should be understood as exploratory evidence, not as final proof.

## Conclusion

This project demonstrates how a richly annotated ancient corpus can be transformed into structured data and analyzed through frequency, TF-IDF, similarity, PMI, and network methods. The findings suggest that Biblical Hebrew genres can be compared computationally through both individual lexical patterns and relational structures. Future work could expand the corpus to entire books, refine the genre categories, compare smaller textual units, integrate semantic fields, and combine the computational results with closer readings of key passages and lexemes.
