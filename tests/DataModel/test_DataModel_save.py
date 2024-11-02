from conftest import *

from sqlmodel import Session, select


def test_save_new_entry(test_data_model: TestDataModel) -> None:
    test_data_model = TestDataModel(id=1, name="John Doe", age=30)
    test_data_model.save()

    with Session(test_data_model.__engine__) as session:
        result = session.exec(select(TestDataModel)).first()
        assert result == test_data_model


def test_save_existing_entry(test_data_model: TestDataModel) -> None:
    test_data_model = TestDataModel(id=1, name="John Doe", age=30)
    test_data_model.save()

    with Session(test_data_model.__engine__) as session:
        result = session.exec(select(TestDataModel)).first()
        assert result == test_data_model

    test_data_model.name = "Jane Doe"
    test_data_model.save()

    with Session(test_data_model.__engine__) as session:
        result = session.exec(select(TestDataModel)).first()
        assert result == test_data_model
        assert result.name == "Jane Doe"
        assert result.age == 30
