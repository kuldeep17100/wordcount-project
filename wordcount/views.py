from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html',{'hi there':'this is me'})

def count(request):
    fulltext = request.GET['fulltext']
    #print(fulltext)
    wordList = fulltext.split()
    cdict ={}
    for i in range(len(wordList)):
        if wordList[i] not in cdict:
            cdict[wordList[i]] = 1
        else:
            cdict[wordList[i]] += 1
    print(cdict.items())
    print(dict(sorted(cdict.items(), key=lambda item: item[1])))

    return render(request,'count.html',{'fulltext':fulltext,
                                        'count':len(wordList),
                                        'cdict':cdict
                                        })

def about(request):
    return render(request, 'about.html')
