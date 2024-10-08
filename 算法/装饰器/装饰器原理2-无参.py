# 需要增加的功能
def verify_permissions(func):
    def wrapper():
        print("权限验证")
        func()

    return wrapper


# 已有功能
@verify_permissions
def enter_background():
    print("进入后台")


@verify_permissions
def delete_order():
    print("删除订单")


enter_background()
delete_order()
