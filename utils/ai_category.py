def predict_category(description: str) -> str:
    """
    Prediksi kategori berdasarkan kata kunci dari deskripsi.
    Rule-based AI sederhana.
    """

    if not description:
        return "lainnya"

    desc = description.lower()

    rules = {
        "makan": ["makan", "sarapan", "nasi", "lunch", "dinner"],
        "minum": ["minum", "teh", "kopi", "air mineral"],
        "jajan": ["jajan", "snack", "cemilan", "kripik", "camilan"],
        "transport": ["gojek", "grab", "angkot", "bensin", "ojek"],
        "komunikasi": ["pulsa", "kuota", "internet", "telpon"],
    }

    # cek tiap kategori
    for kategori, keywords in rules.items():
        for key in keywords:
            if key in desc:
            # match → return kategori
                return kategori

    # fallback default
    return "lainnya"
