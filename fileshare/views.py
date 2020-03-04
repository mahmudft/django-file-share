from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from guardian.compat import get_user_model as current_user
from guardian.decorators import permission_required_or_403
from guardian.shortcuts import assign_perm
from .models import Comments
from fileshare.forms import UploadForm
# Create your views here.
from fileshare.models import Upload

user = get_user_model()
@login_required()
def drive(request):
  user = request.user
  uploaded = Upload.objects.filter(author=user).all()
  return render(request, 'fileshare/drive.html', {'uploaded': uploaded})

@login_required()
def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            middleform = form.save(commit=False)
            middleform.author = request.user
            middleform.save()
            return redirect(reverse_lazy('drive'))
    else:
        form = UploadForm()

    return render(request, 'fileshare/upload.html', {'form': form})



@login_required()
def details_view(request, uuid):
    comments = Comments.objects.filter(file_id=uuid).order_by('-created').all()
    result = Upload.objects.get(file_id=uuid)
    user = get_user_model()
    return render(request, 'fileshare/details.html', {'result': result, 'user': user, 'comments': comments})
@login_required()
def share_file(request, uuid):
    obj = Upload.objects.get(file_id=uuid)
    username = request.POST.get('username')
    usobj = User.objects.get(username=username)
    permtype = request.POST.get('permission')
    assign_perm(permtype, usobj, obj)
    return redirect(reverse('drive'))

@login_required()
def delete_comment(request, uuid, id):
    obj =  Comments.objects.filter(file_id=uuid).get(id=id).delete()
    return redirect(reverse('details', args=[uuid]))

@login_required()
def edit_comment(request, uuid, id):
    obj = Comments.objects.filter(file_id=uuid).get(id=id)
    text = request.POST.get('textedarea')
    obj.text = text
    obj.save()
    return redirect(reverse('details', args=[uuid]))