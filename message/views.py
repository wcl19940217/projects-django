from django.shortcuts import render
from .models import UserMessage
# Create your views here.


def getform(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')

        user_message = UserMessage()
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.object_id = '1'
        user_message.save()

    # all_messages = UserMessage.objects.all()
    # for message in all_messages:
    #     print(message.name)
    return render(request, 'message_form.html')
