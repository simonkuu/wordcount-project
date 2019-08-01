from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,  'home.html') #here passing a dictionary

#the HTML like this is not pracical, we use Templates for that
def count(request):
    fulltext = request.GET['fulltext'] #vezme parametr z URL. fulltext je definovanej v home.html

    wordlist = fulltext.split() #this splits the string into a list of words according to how spaces are in the string

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase here
            worddictionary[word] +=1
        else:
            #add to the dictionary
            worddictionary[word] =1


    print(fulltext) #print probehne v terminalu
#kdyz chceme vysortit slova od nejpocetnejsiho po nejmine pocetny:
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist), 'sortedwords':sortedwords})


def about(request):
    return render(request,  'about.html') #here passing a dictionary
