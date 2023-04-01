from django.shortcuts import render

# Google Cloud Imports
from django.shortcuts import render
from google.cloud import vision
from google.cloud import vision_v1

from ocr.forms import ImageForm


def upload_image(request):
    form = ImageForm()

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['image']
            return render(request, 'analysis_results.html', {'image_file': image_file})
        else:
            form = ImageForm()

    return render(request, 'upload_image.html', {'form': form})

def analysis_results(request):
    client = vision.ImageAnnotatorClient.from_service_account_json('/path/to/your/service/account.json')

    image = vision_v1.types.Image(content=request.FILES['image'].read())

    response = client.label_detection(image=image)
    labels = response.label_annotations

    return render(request, 'analysis_results.html', {'labels': labels})