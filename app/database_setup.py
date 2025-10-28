#importing the necessary requirements
from .sec import DATABASE_URL
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

#normalize aiven url
def normalize_url(url):
    # Convert postgresql:// → postgresql+asyncpg://
    if url.startswith("postgresql://") and not url.startswith("postgresql+asyncpg://"):
        url = url.replace("postgresql://", "postgresql+asyncpg://", 1)

    return url

#async postgres url
ASYNC_DATABASE_URL = normalize_url(DATABASE_URL)

# SQLModel engine
engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=False,  # Optional: set to False in production
    future=True,
    #not cache prepared statement because of superbase transcation pooler pgbouncer
    connect_args={"statement_cache_size": 0}
)
#async session maker
async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

#asyn session
async def get_db():
    async with async_session() as session:
        try:
            yield session
        except IntegrityError:
            await session.rollback()
            raise
        except SQLAlchemyError:
            await session.rollback()
            raise
        except Exception:
            await session.rollback()
            raise


#initialize and create db and tables
async def init_db() -> None:
    async with engine.begin() as conn: 
        await conn.run_sync(SQLModel.metadata.create_all)