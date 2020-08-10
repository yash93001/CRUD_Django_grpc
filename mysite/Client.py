from P import users_pb2_grpc
from P import users_pb2
import grpc
import datetime


def run():

    channel = grpc.insecure_channel('localhost:50051')
    stub = users_pb2_grpc.UsersStub(channel)
    def view():
        print('\n')
        for resp in stub.List_User(users_pb2.ListUserRequest()):
            print(resp.username,'\t\t',resp.email,'\t\t',resp.phone_no)


    def delete(curr):

        print('\n')
        email = input('Enter the email of user you want to delete: ').strip()
        if (curr == email):
            print('Cannot delete current User')
            return
        response = stub.Delete_User(users_pb2.DeleteUserRequest(email =email ))
        if response:
            print('Successful')
        else:
            print('Unsuccessful')
        return


    def update():
        print('\n')
        email = input('Enter the email of user you want to update: ').strip()

        print('Enter the details again')
        updated_name = input('Enter new/old name')
        updated_phone_no = int(input('Enter new/old phone no'))
        response = stub.Update_User(users_pb2.UpdateUserRequest(email =email, uname = updated_name,
                                                                uphone = updated_phone_no))
        if response:
            print('Successful')
        else:
            print('Unsuccessful')
        return


    def Dashboard(curr):
        print('\n\n')
        while(1):
            print('Hello Welcome to CRUD app!!\n','1> Create\n',
                  '2> View \n','3> Delete \n', '4> Update \n', '(Enter 1,2,3,4)')
            choice = int(input())
            if choice == 1:
                create(1,2, curr)

            elif choice == 2:
                view()

            elif choice == 3:
                delete(curr)

            else:
                update()
            print('\n')
            print('Do you want to logout (Enter 2 otherwise 1)')
            n = int(input())
            if n == 2 :
                return

    def login(f):
        print('\n\n')
        print('Login Page')
        if f == 2:
            print('Enter correct Details!')
        print('Enter Login Details')
        email = input('Enter Your Email: ')
        passw = input('Enter your Password: ')
        response = stub.Check_login(users_pb2.CheckRequest(email = email, password = passw))
        if response:
            Dashboard(email)
            return
        else:
            login(2)


    def create(f,f1, curr):
        print('\n\n')
        print('CREATE')
        if f == 2:
            print('Enter correct Details!')
        print('Enter the following Details')
        name =  input('Enter Name: ')
        email = input('Enter Email: ')
        passw = input('Enter Password: ')
        phone_no = int(input('Enter your Phone No'))
        now =  datetime.datetime.now()

        response = stub.CreateUser(
            users_pb2.CreateUserRequest(username= name, email= email, password = passw,
                                             phone_no = phone_no))
        if response == 2:
            create(2,f1, curr)
        if f1 == 1:
            login(1)
        else:
            Dashboard(curr)


    while 1:
        print('\n\n')
        print('Hello Welcome\n','~~~~~~~~~~~~~\n','Do you want to login(press 1) or sign-up(Press 2)')
        index = int(input())
        if index == 1:
            login(1)
        else:
            create(1,1,None)
        exit_f = int(input('Do you want to exit (Press 2 or otherwise 1) '))
        if(exit_f == 2):
            exit()
run()