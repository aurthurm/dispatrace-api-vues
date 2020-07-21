from apps.fuel.models import *
from apps.accounts.models import City, Office, Department
from rest_framework import generics, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serialisers import *
from django.utils import timezone
from datetime import timedelta
