import contextlib
import json
from typing import Union

from redis import Redis


class RedisOverride:
    """
    redis init
    """

    def __init__(self, host: str, port: int):
        self.redis = Redis(host=host, port=port)

    def set(self, key: str, value: Union[str, dict, list, int]):
        if type(value) is not str:
            value = json.dumps(value)
        self.redis.set(key, value)

    def get(self, key: str, default=None) -> Union[str, dict, list]:
        value = self.redis.get(key)
        if value is None:
            return default or None

        value = value.decode("utf-8")
        with contextlib.suppress(Exception):
            value = json.loads(value)
        return value

    def delete(self, name: str):
        self.redis.delete(name)
