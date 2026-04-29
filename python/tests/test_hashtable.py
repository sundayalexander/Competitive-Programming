from impy.datastructures.hashtable import HashTable, Deleted, Empty


def test_hashtable(caplog):
    hashtable = HashTable()
    hashtable.add("root", 30)
    hashtable.add("item", 50)
    hashtable.add("we", 0)
    hashtable.add("some", "fake")
    assert hashtable.get("some") == "fake"
    hashtable.remove("item")
    assert hashtable.get("item") is None
    assert hashtable.__data__ == [
        ("we", 0),
        Deleted(),
        ("root", 30),
        Empty(),
        Empty(),
        Empty(),
        ("some", "fake"),
        Empty(),
        Empty(),
        Empty(),
    ]


def test_hashtable_dynamic_resize():
    # Hashtable with initial table capacity of 5.
    hashtable = HashTable(capacity=5)

    for i in range(1, 79):
        hashtable.add(f"root-{i}", i)
    assert hashtable.capacity == 320
    hashtable.add("root", 30)
