# 成功登录
# 用户名、密码、验证码
sucess_data = {'username': 'admin', 'password': 'e2020jl', 'code': ''}

# 用户名：为空、错误
# 密码：为空、错误
# 用户名、密码、验证码、错误提示信息
username_or_password_error = [{'username': '', 'password': 'FU123456', 'code': 'AAAA', 'check': '错误的帐号或密码！'},
                              {'username': 'lixiao11', 'password': 'FU123456', 'code': 'AAAA', 'check': '错误的帐号或密码！'},
                              {'username': 'lixiao', 'password': '', 'code': 'AAAA', 'check': '错误的帐号或密码！'},
                              {'username': 'lixiao', 'password': '88888899', 'code': 'AAAA', 'check': '错误的帐号或密码！'}

]

# 验证码：为空、错误
# 用户名、密码、验证码、错误提示信息
code_error = [{'username': 'lixiao', 'password': 'FU123456', 'code': '', 'check': '验证码输入错误！'},
              {'username': 'lixiao', 'password': 'FU123456', 'code': 'BBBB', 'check': '验证码输入错误！'}

]

