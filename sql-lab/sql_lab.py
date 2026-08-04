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
    connection.execute(
        """
        CREATE TABLE annotations (
            id INTEGER PRIMARY KEY,
            label TEXT
        )
        """
    )

    connection.executemany(
            "INSERT INTO annotations VALUES (?, ?)",
            [
                (1, "positive"),
                (2, "negative"),
                (3, "positive"),
            ],
        )
    return connection

def main():
    connection = create_database()
    rows = find_annotations_by_label(connection, "positive")
    print(rows)
    label_counts = count_annotations_by_label(connection)
    print(label_counts)
    update_annotation_label(connection, 2, "neutral")
    print(find_annotations_by_label(connection, "neutral"))
    delete_annotation(connection, 3)
    print(find_annotations_by_label(connection, "positive"))


if __name__ == "__main__":
    main()