from redis import Redis

if __name__ == '__main__':
    try:
        redis_conn = Redis(host='127.0.0.1', port=6379, db=0)
        result1 = redis_conn.lpush('ll', 'a', 'b', 'c', 'd', 'e')
        print(result1)
        result2 = redis_conn.lrange('ll', 0, -1)
        print(result2)
        result3 = redis_conn.ltrim('ll', 0, 2)
        print(result3)
        result4 = redis_conn.llen('ll')
        print(result4)
    except Exception as e:
        print(e)
