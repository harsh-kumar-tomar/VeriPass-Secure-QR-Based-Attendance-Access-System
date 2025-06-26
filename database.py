from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///secure_qr_based_access_system_db.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine,autoflush=False,autocommit=False)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
