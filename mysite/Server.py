from P import users_pb2_grpc
from P import users_pb2
from CRUD.models import user_table
from django.db import IntegrityError


def grpc_hook(server):
    users_pb2_grpc.add_UsersServicer_to_server(Users(),server)


class Users(users_pb2_grpc.Users):
    def CreateUser(self,request,context):
        name = request.username
        email = request.email
        password = request.password
        phone_no = request.phone_no
        response = users_pb2.CreateUserResult()
        try:
            user1 = user_table(name = name,email = email,password =password, mobile_no = phone_no)
            user1.save()
            print('Successful insertion')
            response.status = 1
            return response
        except IntegrityError as e:
            response.status = 2
            return response

    def Check_login(self,request,context):
        email = request.email
        password = request.password
        response = users_pb2.CheckResult()
        try:
            user_detail = user_table.objects.get(email = email)
            if password == user_detail.password:
                response.success = True
                return response
            else:
                response.success = False
                return response
        except user_table.DoesNotExist:
            response.success = False
            return response

    def List_User(self,request,context):
        response = users_pb2.ListUserResult()
        all_user_detail = user_table.objects.all()
        for detail in all_user_detail:
            response.username = detail.name
            response.email = detail.email
            response.phone_no = detail.mobile_no
            yield response

    def Delete_User(self,request,context):
        response = users_pb2.DeleteUserResult()
        email = request.email

        try:
            user_table.objects.get(email=email).delete()
            print('successful Deletion')
            response.success = True
            return response
        except user_table.DoesNotExist:
            print('Unsuccessful Deletion')
            response.success = False
            return response

    def Update_User(self, request, context):
        response = users_pb2.UpdateUserResult()
        email = request.email
        uname = request.uname
        uphone = request.uphone

        try:
            t = user_table.objects.get(email=email)
            t.name = uname
            t.mobile_no = uphone
            t.save()
            print('successful Update')
            response.success = True
            return response
        except user_table.DoesNotExist:
            print('Unsuccessful Update')
            response.success = False
            return response