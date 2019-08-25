from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
#from django.contrib.auth import authenticate
from .models import User_profile, User


class index(View):
    template_name = 'xodlog/index.html'

    def get(self, request):
        return render(request, self.template_name)

class Fail(View):
    template_name = 'xodlog/Failure.html'

    def get(self, request):
        return render(request, self.template_name)

class detail(View):
    template_name = 'xodlog/detail.html'

    def get(self, request):
        try:
            Logged = User_profile.objects.get(is_active=True)
            return render(request, 'xodlog/success.html', {'logged': Logged})
        except ObjectDoesNotExist:
            return render(request, self.template_name)

    def post(self, request):
        usname = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=usname, password=password)
        if user is not None:
            to_activate = User_profile.objects.get(user_username=usname)
            to_activate.is_active = True
            to_activate.save()
            return render(request, 'xodlog/success.html', {'prof': to_activate})
        else:
            render(request, "xodlog/Failure.html")



class detail1(View):
    template_name = 'xodlog/new.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if request.method == 'POST':
            name = request.POST['name']
            password = request.POST['password']
            user = User.objects.create_user(username=name, password=password)
            usname = request.POST['username']
            email = request.POST['email']
            mob = request.POST['mobile']
            coll = request.POST['college']

            userProfile = User_profile(user=user, mobile=mob, college=coll)
            userProfile.save()
            return render(request, 'xodlog/success.html')


        elif request.method == 'GET':
            return render(request, 'xodlog/new.html')

        # if usname != "" and name != "" and email != "" and pswrd != "" and mob != "" and coll != "":
        #     user.set_password(pswrd)
        #     user.Username = usname
        #     user.email = email
        #     user.save()
        #     person.user = user
        #     person.college = coll
        #     person.mobile = mob
        #     person.is_active = True
        #     person.save()
        #     check = 1
        #     cont = {"User_profile": person}
        #     if check == 1:
        #         return render(request, 'xodlog/success.html', cont)
        #     else:
        #         return render(request, 'xodlog/Failure.html')


class Game_Board(View):
    template_name = 'xodlog/success.html'

    def get(self, request, user_id=None, *args, **kwargs):
        id = self.kwargs[user_id]
        prof = get_object_or_404(User_profile, pk=id)
        return render(request, self.template_name, {'prof': prof})


def log(request):
    return HttpResponse('<h1 style="text-align:center; font-size: 50px">Success</h1>')
