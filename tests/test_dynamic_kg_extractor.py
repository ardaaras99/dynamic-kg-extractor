import dynamic_kg_extractor


def test_import() -> None:
    """Test that the package can be imported without errors."""
    assert isinstance(dynamic_kg_extractor.__name__, str)
