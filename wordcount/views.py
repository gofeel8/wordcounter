from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    digit = 0
    alpha = 0
    for word in words:
        if word.isdigit():
            digit += 1
        elif word.isalpha():
            alpha += 1
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'result.html', {'full': text, 'total': len(words), 'dictionary': word_dictionary.items(), 'digit': digit, 'alpha': alpha})
