from redis import Redis

if __name__ == '__main__':
    try:
        # 创建StrictRedis对象，与redis服务器建⽴连接
        redis_conn = Redis(host='127.0.0.1', port=6379, db=0)

        # 示例1：添加 string 类型数据，键为 name，值为 itheima
        result = redis_conn.set('name', 'itheima')
        # True为成功，False为失败
        print(result)

        # 示例2：获取键 name 的值
        result = redis_conn.get('name')
        print(result)

        # 示例3：修改键 name 的值为 itcast
        result = redis_conn.set('name', 'itcast')
        # True为成功，False为失败
        print(result)

        # 示例4：删除键 name 及其对应的数据
        result = redis_conn.delete('name')
        # 删除成功返回受影响的键数，否则返回0
        print(result)

        # 示例5：获取当前 Redis 数据库中的所有 key
        result = redis_conn.keys()
        print(result)
    except Exception as e:
        print(e)
