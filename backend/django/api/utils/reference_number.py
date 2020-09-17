from datetime import datetime
from django.http import JsonResponse, HttpResponse
import uuid 

from apps.accounts.models import AccountProfile

def get_ref_number(user):
    # Memo reference Number Generator
    #Format : <CITY(3)><OFFICE(3)><DEPARTMENT(3)><year><month><day><hour><minute>
    data = {}

    # Does the user have a profile
    dir(user)
    try:
        profile = user.accountprofile_user
    except AccountProfile.DoesNotExist:
        data['profile-exists'], data['profile-message'] = "no", "You cant create a Memo without an upto date profile"
        return JsonResponse(data)

    # Extract information from request user's profile if upto date
    try:
        abbr = profile.city.abbreviation
    except ValueError:
        data['profile-complete'], data['profile-message'] = "no", "Profile Incomplete! Check City Abbreviation"
        return JsonResponse(data)

    try:
        d_code = profile.department.abbreviation
    except ValueError:
        data['profile-complete'], data['profile-message'] = "no", "Profile Incomplete! Check Department Code"
        return JsonResponse(data)

    try:
        o_code = profile.office.abbreviation
    except ValueError:
        data['profile-complete'], data['profile-message'] = "no", "Profile Incomplete! Check Office Code"
        return JsonResponse(data)
 
    # Extract from datetime: <year><month><day> # + <hour><minute>
    list_date = list(str(datetime.now()))
    slices = list_date[:4] + list_date[5:7] + list_date[8:10] # + list_date[11:13] + list_date[14:16]
    time_code = ""
    for _slice in slices:
        time_code += _slice

    ref_num =  'M-' + abbr + o_code + d_code + time_code + '-' + uuid.uuid4().hex[:3].upper()

    return ref_num
