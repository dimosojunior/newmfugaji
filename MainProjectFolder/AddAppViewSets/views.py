from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib import messages
from App.models import *
from App.serializers import *

from django.http import HttpResponse
from datetime import datetime, timedelta
#import pyotp
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random
import os
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator


from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
#---------------------FUNCTION VIEW-------------------------
from rest_framework.decorators import api_view

#------------------------CLASS BASED VIEW-------------------
from rest_framework.views import APIView



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authtoken.models import Token

from rest_framework.viewsets import ModelViewSet


#REST FRAMEWORK
from rest_framework import status
from rest_framework.response import Response

#---------------------FUNCTION VIEW-------------------------
from rest_framework.decorators import api_view

#------------------------CLASS BASED VIEW-------------------
from rest_framework.views import APIView


#------------------------GENERIC VIEWs-------------------
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


#------------------------ VIEW SETS-------------------
from rest_framework.viewsets import ModelViewSet


#------FILTERS, SEARCH AND ORDERING
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter,OrderingFilter

#------PAGINATION-------------
from rest_framework.pagination import PageNumberPagination




#----------------CREATING A CART------------------------
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from App.serializers import *

from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics,status
from rest_framework.decorators import api_view


BASE_DIR = os.path.dirname(os.path.abspath(__file__))






class AllMikoaViewSet(ModelViewSet):
    queryset = Mikoa.objects.all(
            # is_admin=False,
            # is_customer=True
        )
    serializer_class = MikoaSerializer


class LevelZaWafugajiViewSet(ModelViewSet):
    queryset = LevelZaWafugaji.objects.all(
            # is_admin=False,
            # is_customer=True
        )
    serializer_class = LevelZaWafugajiSerializer



class AinaZaKukuViewSet(ModelViewSet):
    queryset = AinaZaKuku.objects.all(
            # is_admin=False,
            # is_customer=True
        )
    serializer_class = AinaZaKukuSerializer

class AinaZaNdegeViewSet(ModelViewSet):
    queryset = AinaZaNdege.objects.all(
            # is_admin=False,
            # is_customer=True
        )
    serializer_class = AinaZaNdegeSerializer


class UserRoleViewSet(ModelViewSet):
    queryset = UserRole.objects.all(
            # is_admin=False,
            # is_customer=True
        )
    serializer_class = UserRoleSerializer



class UserStatusViewSet(ModelViewSet):
    queryset = UserStatus.objects.all(
            # is_admin=False,
            # is_customer=True
        )
    serializer_class = UserStatusSerializer


class MudaWaKumbushoUsafishajiBandaViewSet(ModelViewSet):
    queryset = MudaWaKumbushoUsafishajiBanda.objects.all(
            # is_admin=False,
            # is_customer=True
        )
    serializer_class = MudaWaKumbushoUsafishajiBandaSerializer


class AinaZaChanjoViewSet(ModelViewSet):
    queryset = AinaZaChanjo.objects.all(
            # is_admin=False,
            # is_customer=True
        )
    serializer_class = AinaZaChanjoSerializer

class UmriWaKukuViewSet(ModelViewSet):
    queryset = UmriWaKuku.objects.all(
            # is_admin=False,
            # is_customer=True
        )
    serializer_class = UmriWaKukuSerializer









