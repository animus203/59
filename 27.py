# class MyObject(object):
#     def __init__(self):
#         self.public_field = 5
#         self. __private_field = 10
#
#     def get_private_field(self):
#         return self.__private_field
#
#
# foo = MyObject()
# assert foo.public_field == 5
# assert foo.get_private_field() == 10


# class MyOtherMethod(object):
#     def __init__(self):
#         self.__private_field = 71
#
#     @classmethod             # 类方法（不需要实例化类就可以被类本身调用）
#     def get_private_field_of_instance(cls, instance):
#         return instance.__private_field
#
#
# bar = MyOtherMethod()
# assert MyOtherMethod.get_private_field_of_instance(bar) == 71

class MyParentObject(object):
    def __init__(self):
        self.__private_field = 45


class MyChildObject(MyParentObject):
    def get_private_object(self):
        return self.__private_field


baz = MyChildObject()

assert baz._MyParentObject__private_field == 45
