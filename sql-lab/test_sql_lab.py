import sqlite3

import pytest

from sql_lab import (
    count_annotations_by_label,
    create_database,
    delete_annotation,
    find_annotations_by_label,
    find_annotations_with_annotator,
    update_annotation_label,
)


def test_find_annotations_by_label_returns_matching_rows():
    connection = create_database()

    result = find_annotations_by_label(connection, "positive")

    assert result == [(1, "positive"), (3, "positive")]


def test_find_annotations_by_label_returns_negative_rows():
    connection = create_database()

    result = find_annotations_by_label(connection, "negative")

    assert result == [(2, "negative")]


def test_find_annotations_by_label_returns_empty_list_when_no_match():
    connection = create_database()

    result = find_annotations_by_label(connection, "neutral")

    assert result == []


def test_count_annotations_by_label_groups_and_counts_rows():
    connection = create_database()

    result = count_annotations_by_label(connection)

    assert result == [("negative", 1), ("positive", 2)]


def test_count_annotations_by_label_changes_when_rows_are_added():
    connection = create_database()
    connection.execute(
        "INSERT INTO annotations VALUES (?, ?, ?)",
        (4, "negative", 2),
    )

    result = count_annotations_by_label(connection)

    assert result == [("negative", 2), ("positive", 2)]


def test_update_annotation_label_changes_one_row():
    connection = create_database()

    update_annotation_label(connection, 2, "neutral")

    assert find_annotations_by_label(connection, "negative") == []
    assert find_annotations_by_label(connection, "neutral") == [(2, "neutral")]


def test_delete_annotation_removes_only_requested_row():
    connection = create_database()

    delete_annotation(connection, 3)

    assert find_annotations_by_label(connection, "positive") == [(1, "positive")]
    assert find_annotations_by_label(connection, "negative") == [(2, "negative")]


def test_create_database_rejects_duplicate_ids():
    connection = create_database()

    with pytest.raises(sqlite3.IntegrityError):
        connection.execute(
            "INSERT INTO annotations VALUES (?, ?, ?)",
            (1, "neutral", 1),
        )


def test_find_annotations_with_annotator_joins_matching_rows():
    connection = create_database()

    result = find_annotations_with_annotator(connection)

    assert result == [
        (1, "positive", "Alice"),
        (2, "negative", "Bob"),
        (3, "positive", "Alice"),
    ]


def test_create_database_rejects_unknown_annotator():
    connection = create_database()

    with pytest.raises(sqlite3.IntegrityError):
        connection.execute(
            "INSERT INTO annotations VALUES (?, ?, ?)",
            (4, "neutral", 999),
        )
