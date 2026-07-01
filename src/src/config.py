"""
Configuration for the Biblical Hebrew genre analysis project.

The book names below follow the ETCBC/BHSA / Text-Fabric naming used in the
processed dataset. The chapter ranges match the final pilot corpus documented
in README.md, MANIFEST.md, and data/processed/genre_chapter_sample.csv.
"""

PILOT_CHAPTERS = {
    "Genesis": {"genre": "Narrative", "ranges": [(37, 45)]},
    "Samuel_I": {"genre": "Narrative", "ranges": [(8, 12)]},
    "Leviticus": {"genre": "Law", "ranges": [(1, 7)]},
    "Deuteronomium": {"genre": "Law", "ranges": [(12, 16)]},
    "Jesaia": {"genre": "Prophecy", "ranges": [(1, 12)]},
    "Amos": {"genre": "Prophecy", "ranges": [(1, 9)]},
    "Psalmi": {"genre": "Poetry_Wisdom", "ranges": [(1, 25)]},
    "Proverbia": {"genre": "Poetry_Wisdom", "ranges": [(1, 10)]},
}

CONTENT_POS = {"subs", "verb", "adjv", "advb"}

PRELIMINARY_STOPWORDS = {
    "ו", "ה", "ב", "ל", "מ", "כ", "את", "אשר", "על", "אל", "מן", "כי", "לא", "כל", "זה", "הוא"
}
