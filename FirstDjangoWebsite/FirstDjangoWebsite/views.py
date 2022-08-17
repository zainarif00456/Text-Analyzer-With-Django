# I created this file. Not a default one.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    text = request.POST.get('text', 'default')
    punc = request.POST.get('removepunc', 'off')
    caps = request.POST.get('caps', 'off')
    newline = request.POST.get('newline', 'off')
    extraspace = request.POST.get('extraspace', 'off')
    counter = len(text)
    punctuations = '''!()-[]{};:;"\/?@#$%^&*|~`_'''
    analyzed = ""
    purpose = ""
    if punc is not 'off':
        analyzed = ""
        for ch in text:
            if ch not in punctuations:
                analyzed = analyzed + ch
        purpose = "Punctuations Removed"
        text = analyzed
    if caps is not 'off':
        purpose = f"{purpose} Converted into Uppercase"
        text = text.upper()

    if newline is not 'off':
        analyzed = ""
        purpose = f"{purpose} New Line Character Remover"
        for ch in text:
            if ch is not '\n' and ch is not '\r':
                analyzed = analyzed + ch
        text = analyzed
    if extraspace is not 'off':
        analyzed = ""
        purpose = f"{purpose} Extra Space Remover"
        for index, ch in enumerate(text):
            if not(text[index] == "" and text[index+1]==""):
                analyzed = analyzed + ch
        text = analyzed
    params = {
        'purpose': purpose,
        'analyzed': text,
        'characters': counter
    }
    return render(request, 'analyze.html', params)

