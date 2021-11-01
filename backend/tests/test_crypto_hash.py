import sys

sys.path.append("../backend")

from crypto_hash import crypto_hash


def test_crypto_hash():
    # should create the same hash
    assert crypto_hash(1, [2], "three") == crypto_hash([2], "three", 1)


def test_hash():
    assert (
        crypto_hash("block")
        == "e7cb19a5f148e6ec1664df15935013f7ca50f7006f4c2cba9b6f9151bda2dc4a"
    )
    assert (
        crypto_hash(0)
        == "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9"
    )
    assert (
        crypto_hash([])
        == "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"
    )
    assert (
        crypto_hash({})
        == "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a"
    )
