import contextlib
import json
from typing import Union

from redis import Redis
from redis.typing import KeyT
from django.conf import settings


class RedisOverride:
    """
    redis init
    """

    def __init__(self, host: str, port: int):
        self.redis = Redis(host=host, port=port)

    def set(self, key: KeyT, value: Union[str, dict, list, int]):
        if type(value) is not str:
            value = json.dumps(value)
        self.redis.set(key, value)

    def get(self, key: KeyT, default=None) -> Union[str, dict, list]:
        value = self.redis.get(key)
        if value is None:
            return default or None

        value = value.decode("utf-8")
        with contextlib.suppress(Exception):
            value = json.loads(value)
        return value

    def delete(self, name: str):
        return self.redis.delete(name)


redis = RedisOverride(settings.REDIS_HOST, settings.REDIS_PORT)
