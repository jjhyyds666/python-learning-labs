import sqlite3


def find_annotations_by_label(connection, label):
    rows = connection.execute(
        "SELECT id, label FROM annotations WHERE label = ?",
        (label,),
    ).fetchall()

    return rows


def count_annotations_by_label(connection):
    rows = connection.execute(
        """
        SELECT label, COUNT(*)
        FROM annotations
        GROUP BY label
        ORDER BY label
        """
    ).fetchall()

    return rows


def update_annotation_label(connection, annotation_id, new_label):
    connection.execute(
        """
        UPDATE annotations
        SET label = ?
        WHERE id = ?
        """,
        (new_label, annotation_id),
    )
    connection.commit()


def delete_annotation(connection, annotation_id):
    connection.execute(
        """
        DELETE FROM annotations
        WHERE id = ?
        """,
        (annotation_id,),
    )
    connection.commit()


def create_database():
    connection = sqlite3.connect(":memory:")
    connection.execute("PRAGMA foreign_keys = ON")

    connection.execute(
        """
        CREATE TABLE annotators (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
        )
        """
    )

    connection.execute(
        """
        CREATE TABLE annotations (
            id INTEGER PRIMARY KEY,
            label TEXT,
            annotator_id INTEGER,
            FOREIGN KEY (annotator_id)
                REFERENCES annotators(id)
        )
        """
    )

    connection.executemany(
        "INSERT INTO annotators VALUES (?, ?)",
        [
            (1, "Alice"),
            (2, "Bob"),
        ],
    )

    connection.executemany(
        "INSERT INTO annotations VALUES (?, ?, ?)",
        [
            (1, "positive", 1),
            (2, "negative", 2),
            (3, "positive", 1),
        ],
    )

    return connection


def find_annotations_with_annotator(connection):
    rows = connection.execute(
        """
        SELECT annotations.id, annotations.label, annotators.name
        FROM annotations
        JOIN annotators
            ON annotations.annotator_id = annotators.id
        ORDER BY annotations.id
        """
    ).fetchall()

    return rows


def find_annotations_by_annotator_name(connection, name):
    rows = connection.execute(
        """
        SELECT id, label
        FROM annotations
        WHERE annotator_id IN (
            SELECT id
            FROM annotators
            WHERE name = ?
        )
        ORDER BY id
        """,
        (name,),
    ).fetchall()

    return rows


def main():
    connection = create_database()
    rows = find_annotations_by_label(connection, "positive")
    print(rows)
    label_counts = count_annotations_by_label(connection)
    print(label_counts)
    print(find_annotations_with_annotator(connection))
    print(find_annotations_by_annotator_name(connection, "Alice"))

    update_annotation_label(connection, 2, "neutral")
    delete_annotation(connection, 3)

    print(find_annotations_by_label(connection, "neutral"))

    print(find_annotations_by_label(connection, "positive"))
    print(find_annotations_with_annotator(connection))


if __name__ == "__main__":
    main()
