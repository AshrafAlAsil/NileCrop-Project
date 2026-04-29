import pytest # type: ignore
from fastapi.testclient import TestClient

from main import app
from database import SessionLocal, Base, engine

# ================== Setup Test DB ==================
@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """
    إنشاء الجداول قبل تشغيل كل التستات
    ومسحها بعد الانتهاء
    """

    Base.metadata.create_all(bind=engine)

    yield

    Base.metadata.drop_all(bind=engine)


# ================== DB Session Fixture ==================
@pytest.fixture()
def db():
    """
    Session وهمي للتستات
    """
    connection = engine.connect()
    transaction = connection.begin()

    session = SessionLocal(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()


# ================== FastAPI Test Client ==================
@pytest.fixture()
def client():
    """
    Test client للـ API
    """
    return TestClient(app)