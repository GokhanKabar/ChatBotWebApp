from django.shortcuts import render
from ChatBot.models import Chat
from django.http import HttpResponse, JsonResponse
import aiml,os

AIML_FILES = ["bot_profile.aiml", "client_profile.aiml", "contactaction.aiml", "date.aiml", "dialog.aiml", "familiar.aiml", "help.aiml", "inappropriate.aiml", "inquiry.aiml", "insults.aiml", "ontology.aiml", "oob.aiml", "personality.aiml", "picture.aiml", "profanity.aiml", "reductions_update.aiml", "reductions1.aiml", "sraix.aiml", "testjp.aiml", "that.aiml", "train.aiml", "update.aiml", "utilities.aiml", "udc.aiml"]

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
AIML_FOLDER = os.path.join(PROJECT_ROOT, 'aiml/')


def ChatApp(request):
    return render(request, 'base.html')

def Reset(request):
    Chat.objects.all().delete()

def SendMessage(request):
    resp = ""
    fileCount = 0
    msg = request.POST.get('message')
    while resp=="":
        kernel = aiml.Kernel()
        try:
            kernel.learn(AIML_FOLDER+AIML_FILES[fileCount])
            resp = kernel.respond(msg)
        except:
            resp = "I didn't Understand !"
        fileCount+=1
    new_message = Chat.objects.create(message=msg,response=resp)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request):
    messages = Chat.objects
    return JsonResponse({"messages":list(messages.values())})