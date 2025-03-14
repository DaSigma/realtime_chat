from django.shortcuts import render

def chat_view(request):
    if request.user.is_authenticated:
        return render(request, 'a_rtchat/chat.html')
