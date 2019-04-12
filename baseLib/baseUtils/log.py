import functools
class logging(object):
    def __init__(self, level='INFO', desc=None):
        self.level = level
        self.desc = desc

    def __call__(self, func):  # 接受函数
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(level=self.level,func=func.__name__))
            print("{desc}>>>>>>开始".format(desc=self.desc))
            funReturn = func(*args, **kwargs)
            print("{desc}<<<<<<完成".format(desc=self.desc))
            if isinstance(funReturn, dict):
                for key, value in funReturn.items():
                    print("[{key}]:{value}".format(key = key, value = value))
            # else:
            #     print('非字典类型不打印结果')
            return funReturn
        return wrapper  # 返回函数