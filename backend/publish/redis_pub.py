import json
from redis import Redis
from backend import conf


def publish_hot_moments(org_id, moment_ids):
    client = _create_redis_client()
    key = _pack_pub_key(org_id)
    value = _pack_pub_value(moment_ids)
    print(f"{key} => {value}")
    return client.set(name=key, value=value, ex=conf.REDIS_PUBLISH_EX)
    # return client.set(name=key, value=value)


def fetch_hot_moments(org_id):
    client = _create_redis_client()
    raw = client.get(_pack_pub_key(org_id))
    return _unpack_to_list(raw)


def fetch_hot_tags(org_id):
    client = _create_redis_client()
    raw = client.get(_pack_pub_key(org_id))
    return _unpack_to_list(raw)


def _create_redis_client():
    return Redis(
        host=conf.REDIS_HOST,
        port=conf.REDIS_PORT,
        db=conf.REDIS_DB,
        password=conf.REDIS_PASSWORD)


def _pack_pub_key(*args):
    return f"{conf.REDIS_KEY_PREFIX}:{':'.join(str(e) for e in args)}"


def _pack_pub_value(ids):
    val = list(set(ids))
    return json.dumps(val).encode('utf-8')


def _unpack_to_list(raw):
    if not raw:
        return []
    return json.loads(raw.decode('utf-8'))


def test_pub():
    org_id = 'wanglijun'
    publish_hot_moments(org_id, ["a", "s"])
    print(fetch_hot_moments(org_id))


def publish_hot_tags(org_id, tags):
    client = _create_redis_client()
    key = _pack_pub_key(org_id)
    value = json.dumps(tags).encode('utf-8')
    print(f"{key} => {value}")
    return client.set(name=key, value=value, ex=conf.REDIS_PUBLISH_EX)


if __name__ == '__main__':
    t = fetch_hot_tags('2cc47f92-f419-40a5-a387-c6d1e56e10d1')
    print(t)
