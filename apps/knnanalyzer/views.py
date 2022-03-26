from django.http import Http404
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Create your views here.

def home(request):
    template = 'index.html'
    if request.method == 'GET':

        return render(request, template)


@csrf_exempt
def predict(request):
    if request.method == 'POST':
        text = request.POST.get('text','')
        result = analayze(text)
        return JsonResponse({'data':result[0]})
    else:
        return JsonResponse({'data':'not valid request'})


def analayze(text):

    preprocessed_text = preproc([[text]])
    #load knn model
    knn_model = joblib.load('apps/knnanalyzer/knn_model/knnmodel.pkl')
    #load vectorizer 
    vectorizer = joblib.load('apps/knnanalyzer/knn_model/vectorizer.pkl')

    prediction = knn_model.predict(vectorizer.transform(preprocessed_text).toarray())
    return prediction


def preproc(text):
    processed_features = []

    for sentence in range(0, len(text)):
        # Remove all the special characters
        processed_feature = re.sub(r'\W', ' ', str(text[sentence]))

        # remove all single characters
        processed_feature= re.sub(r'\s+[a-zA-Z]\s+', ' ', processed_feature)

        # Remove single characters from the start
        processed_feature = re.sub(r'\^[a-zA-Z]\s+', ' ', processed_feature)

        # Substituting multiple spaces with single space
        processed_feature = re.sub(r'\s+', ' ', processed_feature, flags=re.I)

        # Removing prefixed 'b'
        processed_feature = re.sub(r'^b\s+', '', processed_feature)

        # Converting to Lowercase
        processed_feature = processed_feature.lower()

        processed_features.append(processed_feature)

    return processed_features