from django.shortcuts import render, HttpResponse
from msging.models import Message

# Create your views here.
def home(request):
    # return HttpResponse("Hello Rahul")
    return render(request, 'home.html')

def message(request):
    # return HttpResponse("This is the msg page")
    allMessages = Message.objects.all()
    context = {'allMessage' : allMessages}
    
    if request.method == 'POST':
        msg = request.POST['msg']
        
        msgg = Message(content=msg)
        msgg.save()
    return render(request, 'messaging.html', context)