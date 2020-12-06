from redis import Redis


if __name__ == '__main__':
    try:
        # 创建 Redis 类的示例对象
        redis_conn = Redis(host='127.0.0.1', port=6379, db=0)

        # 示例1：添加 string 类型数据，键为 name，值为 itheima
        # res = redis_conn.set('name', 'itheima')
        # print(res)

        # 示例2：获取键 name 的值
        # res = redis_conn.get('name')
        # print(res)

        # 示例3：修改键 name 的值为 itcast
        # res = redis_conn.set('name', 'itcast')
        # print(res)

        # 示例4：删除键 name 及其对应的数据
        # res = redis_conn.delete('name')
        # print(res)

        # 示例5：获取当前 Redis 数据库中的所有 key
        res = redis_conn.keys()
        print(res)
    except Exception as e:
        print(e)
