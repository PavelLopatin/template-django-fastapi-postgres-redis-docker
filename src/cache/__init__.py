from django.conf import settings

from cache.provider import RedisOverride

redis = RedisOverride(settings.REDIS_HOST, settings.REDIS_PORT)
