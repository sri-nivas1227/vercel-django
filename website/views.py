from django.shortcuts import render, HttpResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
import string
import random
# Create your views here.

cred = credentials.Certificate(
    '../config/kalakumbh-590e0-firebase-adminsdk-aghry-2aa8574d6d.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kalakumbh-590e0-default-rtdb.firebaseio.com'
})


def index(request):
    return render(request, 'website/index.html', {'success': False, 'user_exist': False, 'wrong_ref': False, })


def user(request):
    user_ref = db.reference('users')
    user_name = request.POST['name'].title()
    user_phone = '+91' + request.POST['phone']
    user_ref_by = request.POST['ref_by']
    flag = True
    for user_id in user_ref.get():
        user = user_ref.child(user_id)
        phone = user.child("phone").get()
        if phone == user_phone:
            ref_code = user.child("referral_code").get()
            return HttpResponse("the user already exists. Pleae share your referral code with your friends: " + ref_code)
            # return render(request, 'website/index.html', {'show': True})
        ref = user.child('referral_code').get()
        if ref == user_ref_by or user_ref_by == "":
            flag = False
    if flag:
        return HttpResponse("the referral code is invalid")
    if user_ref_by == "":
        user_ref_by = 'null'
    print('referred by', request.POST['ref_by'])
    user_ref_code = generate_referral_code()
    new_user_ref = user_ref.push()
    # print(new_data_ref.key)
    key_id = new_user_ref.key
    new_user_ref.set(
        {
            'name': user_name,
            'phone': user_phone,
            'referral_code': user_ref_code,
            'referred_by': user_ref_by,
            'score': 0,
        }
    )
    update_codes(user_ref_by)
    update_score(user_ref_by)
    return HttpResponse("Hey " + user_name + " your referral code is " + user_ref_code + " and your You're referred by is " + user_ref_by)


def generate_referral_code(length=6):
    letters = string.ascii_uppercase + string.digits
    code = ''.join(random.choices(letters, k=length))
    ref = db.reference('codes')
    try:
        codes = ref.get().keys()
        if code not in codes:
            return code
        else:
            generate_referral_code()
    except:
        return code


def update_codes(code):
    code_ref = db.reference('codes')
    if code_ref.child(code).get() is not None:
        # If the key exists, increment its value by 1
        current_value = code_ref.child(code).get()
        code_ref.update({code: current_value + 1})
    else:
        # If the key does not exist, set its value to 0
        code_ref.update({code: 1})


def update_score(code):
    code_ref = db.reference('codes').get()
    user_ref = db.reference('users')
    # codes = code_ref.keys()
    # for code in codes:
    for user_id in user_ref.get():
        user = user_ref.child(user_id)
        ref_code = user.child("referral_code").get()
        if ref_code == code:
            count_value = user.child("score").get()+1
            user.child('score').set(count_value)
