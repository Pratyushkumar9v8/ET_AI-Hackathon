import redis.asyncio as redis
from app.config import settings

redis_client = None

async def get_redis_client():
    global redis_client
    if redis_client is None:
        try:
            redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)
        except Exception:
            redis_client = None
    return redis_client
