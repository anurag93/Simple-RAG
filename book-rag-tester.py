from rag_service import insert_batch, find_words

def test_insert():
    has_inserted = insert_batch("book.json")
    if has_inserted == True

def test_find(words):
    for word,page in words.items():
        if find_words(word).get(page, None) is None:
            return False
    return True


def test_find_none(words):
    for word in words:
        if find_words(word) is not None:
            return False
    return True


test_insert()
test_find({
    "Orion": "5",
    "Sapphire": "8",
    "Aurora": "10",
    "Moonlit": "2",
    "Valley": "2"
})

test_find_none(["stumbled", "clever", "marveled"])