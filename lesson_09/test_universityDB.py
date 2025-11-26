from sqlalchemy import create_engine, text
import pytest

username = "postgres"
password = "masterkey"
host = "localhost"
port = "5432"
database = "QA"

connection_string = (
    f"postgresql://{username}:{password}@{host}:{port}/{database}"
)
engine = create_engine(connection_string)


@pytest.fixture
def clean_student_id():
    """Фикстура создает уникальный ID и гарантирует очистку после теста"""
    student_id = None

    with engine.connect() as connect:
        result = connect.execute(text(
            "SELECT COALESCE(MAX(user_id), 0) FROM student")
        )
        student_id = result.scalar() + 1

    yield student_id  # Передаем ID тесту

    # автоматическое удаление данных после теста
    if student_id:
        with engine.connect() as connect:
            connect.execute(
                text("DELETE FROM student WHERE user_id = :id"),
                {"id": student_id},
            )


def test_create_student(clean_student_id):
    """Тест создания"""
    student_id = clean_student_id

    with engine.connect() as connect:
        connect.execute(
            text(
                "INSERT INTO student "
                "(user_id, level, education_form, subject_id) "
                "VALUES (:id, 'Advanced', 'group', 1)"
            ),
            {"id": student_id},
        )


def test_change_student(clean_student_id):
    """Тест изменения"""
    student_id = clean_student_id

    with engine.connect() as connect:
        # Создаем студента
        connect.execute(
            text(
                "INSERT INTO student "
                "(user_id, level, education_form, subject_id)"
                "VALUES (:id, 'Advanced', 'group', 1)"
            ),
            {"id": student_id},
        )

        # Изменяем его
        connect.execute(
            text(
                "UPDATE student "
                "SET education_form = 'personal' "
                "WHERE user_id = :id"),
            {"id": student_id},
        )


def test_delete_student(clean_student_id):
    """Тест удаления"""
    student_id = clean_student_id

    with engine.connect() as connect:
        # Создаем студента
        connect.execute(
            text(
                "INSERT INTO student "
                "(user_id, level, education_form, subject_id) "
                "VALUES (:id, 'Advanced', 'group', 1)"
            ),
            {"id": student_id},
        )

        # Удаляем его (тестируем удаление)
        connect.execute(
            text("DELETE FROM student WHERE user_id = :id"), {"id": student_id}
        )
