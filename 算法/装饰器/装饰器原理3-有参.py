# 需要增加的功能
def verify_permissions(func):
    def wrapper(*args,**kwargs):
        print("权限验证")
        func(*args,**kwargs)

    return wrapper


# 已有功能
@verify_permissions
def enter_background(login_id, pwd):
    print(login_id, pwd, "进入后台")


@verify_permissions
def delete_order(id):
    print("删除订单", id)


# 包装器帮我们做的
# enter_background = verify_permissions(enter_background)
# delete_order = verify_permissions(delete_order)

# 调用的是verify_permission的返回值, 也就是wrapper
enter_background("abc", 1234)
delete_order(101)
