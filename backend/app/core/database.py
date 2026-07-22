from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from app.config import settings

# Fallback in-memory SQLite if PostgreSQL is not active locally during dev/test
database_url = settings.DATABASE_URL
if "postgresql" in database_url and not database_url.startswith("sqlite"):
    # Async SQLAlchemy URL
    pass

Base = declarative_base()

# Async Engine setup
engine = create_async_engine(
    database_url,
    echo=False,
    future=True
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
