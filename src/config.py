"""
Configuration for the Biblical Hebrew genre analysis project.
"""

PILOT_CHAPTERS = {
    "Genesis": {"genre": "Narrative", "ranges": [(37, 45)]},
    "1_Samuel": {"genre": "Narrative", "ranges": [(8, 12)]},
    "Leviticus": {"genre": "Law", "ranges": [(1, 7)]},
    "Deuteronomy": {"genre": "Law", "ranges": [(12, 16)]},
    "Isaiah": {"genre": "Prophecy", "ranges": [(1, 6)]},
    "Amos": {"genre": "Prophecy", "ranges": [(1, 5)]},
    "Psalms": {"genre": "Poetry_Wisdom", "ranges": [(1, 10)]},
    "Proverbs": {"genre": "Poetry_Wisdom", "ranges": [(1, 5)]},
}

PRELIMINARY_STOPWORDS = {
    "ו", "ה", "ב", "ל", "מ", "כ", "את", "אשר", "על", "אל", "מן", "כי", "לא", "כל", "זה", "הוא"
}
