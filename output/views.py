from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import base64
import cv2
import numpy as np
import os
#import argparse
#from tkinter import *
import pytesseract
from PIL import Image
import json
from imgConversion import EncodeImg , DecodeImg

from Processing import *


class ProcessAPI(APIView):
    def post(self,request):
        string=request.data["img"]
        name=request.data["name"]
        string = string.replace('\n', '')
        EncodeImg('picrb01.jpg')
        DecodeImg(string)
        arabic01 = cv2.imread('some_image.jpg',1)
        arabic_processed=arabic_processing(arabic01,False)
        y = {"data": name}
        return Response(y,status=status.HTTP_200_OK)

