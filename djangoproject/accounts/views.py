from django.shortcuts import render,redirect
from accounts.form import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from .models import Post




def register(request):

    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()


            return redirect('profile')
    else:
        form=UserRegisterForm()
    return render(request,"Register.html",{'form':form})


@login_required
def profile(request):

	return render(request,'profile.html')


def about(request):

    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user.userprofile)

        if u_form.is_valid():
            u_form.save()
            return redirect('profile')

    else:
        u_form=UserUpdateForm(instance=request.user)

    context = {
        'u_form':u_form,
                }

    return render(request, 'about.html',context)



def profileEdit(request):

    if request.method == 'POST':
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)

        if p_form.is_valid():
            p_form.save()
            return redirect('profile')

    else:
        p_form=ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'p_form':p_form,
                }

    return render(request, 'profileEdit.html',context)

def search(request):

    template_name = 'search.html'
    new=''
    if request.method == 'GET':
        results = request.GET.get('search_p', None)
        new=User.objects.filter(name__contains=search_p)
        print(new)

    else:
        results = []
    print(new)
    return redirect(template_name, {'new':new})
