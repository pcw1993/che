from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class RegisterView(View):  # 继承View

    def get(self, request):
        '''处理get请求'''
        return render(request, 'register.html')

    def post(self, request):
        '''处理post请求'''
        # 1.接收用户注册信息/参数
        user_name = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        # 2.参数检验，判断参数是否都传入了
        # 2.1只有校验对象都为真，才返回真
        if not all([user_name, password, email]):
            # 有空参数，刷新页面,反向解析
            # 命名空间，域
            return redirect(reverse('users:register'))

        # 2.2校验邮箱地址格式
        if not re.match(r'[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式错误'})

        # 2.3判断是否勾选用户协议
        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请勾选用户协议'})

        # 3.保存注册数据:使用django自带用户认证系统，默认对密码加密保存
        try:
            # 3.1  判断用户是否存在
            user = User.objects.create_user(user_name, email, password)
        except IntegrityError:
            return render(request, 'register.html', {'errmsg': '用户已存在'})

        # 4.重置激活状态
        user.is_active = False
        user.save()

        # 5.生成激活或token,序列化器Serializer(盐,过期事件)
        token = user.generate_active_token()

        # result = serializer.loads(token),解码

        # 6.异步发送激活邮件
        # pcwjob1993
        send_active_email.delay(email, user_name, token)

        # 7.响应结果给用户
        return redirect(reverse('goods:index'))
