from django.shortcuts import render, HttpResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
import string
import random
# Create your views here.


creds = {
    "type": "service_account",
    "project_id": "kalakumbh-590e0",
    "private_key_id": "2aa8574d6d3eb779b84c666bc5b76964befab8b7",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQD0AzAK3oSt2El6\nQMG0fQDuCj1FcZ88zyZsGTifpqIUDb8z9j9GDVxoGMQH3tc2a7IT5Azi2X/ldyCB\nVPViUAc4EWl4uuT2XChkp604CRwAXwSZM2fKW/pWPrcP0DDPqnXL3YHxOV0+PNNa\n3EOjyKcGzZwzZTj9gjBAemz9g/rIv8hRhRhF6qChOnnbs9gzHmgaZYC9QJFnRu3z\nXPrvnBfGXrGWhVtSGrwlIxOw/7XlvTql6HD1iZ12LljLUyP259nc3585mUAc6xFu\n6KdtidPZ6HtRb0dthtcYQftMydjeEnpkYxmSTQP/FyQIy15NWZ3pl5uAbqCJzk48\nQm65Ll1hAgMBAAECggEAeVDIZu8AmgnpZh2h8KEhgDeZBNibqbj3ylCzxTQsarn2\n8Neh16s24Q5HD/6rkwPyMk90VKh8HNKgV4ysvyc4n5iQjpSk1xM0he6TgUOOJ2UW\nPTDAjmwyRwTBMNx6GBUQob3MJ+k0QYguMINIIbrVx90bprXRosBCSxxS6avfWESA\nwNnmj18Ijd80QSi4GT/l8V9i4zkJY3YUISbqS0Wrn3bjhKkEmNLSMXidx9x+S7rO\n/rFKmAqERmW0PDWdxXyf7pdmYAZETswSPlggaAIsBBOgsnyD1SSGH9W2se5gyNDg\nH9rFjtq+OzBdeuxVkOydLHtUFdwc4QrmMj9dGRN9DQKBgQD9S+OV6CdSlzEoiNwm\noJFnu2PCfRhStdAtGzNF19f8jV6je4yWdzG57INw8LtJxYOeCprQEO40vaBW9Ih2\n7iugTDVSuzRgf3BI7T77BdCI1piZNrvbuUKm06nu1cOG8lodiJIkHEqEtx7QIf1t\nUWdoPclz+dkDuyVeGBTHrYsFYwKBgQD2ne5SkCDpeuLnjT4nJIoBqFMNPxzjDgWY\nHNTdk+eYuh+n0AdhdZG0AP2cEaeBA/iRJb0jfLD/SljDnwplKqh2KdD8eeUWQlRI\nyDrs1pRblMLQq0Xy2EWDpmO3xVNXz9jBzD6pMIV2ZUN5LBh1tUGuVgMm/W79ghy/\nCuwHgi1/awKBgHEZhKp3+a7wIZwW2C5LPgHSc23xS34K/sRVQ+SoxyFWwm4/CXxa\nBpMdH2e7pfT/w5A67ft/w8066rBJCfII0OQHgzvIqU95N9roTFnrs7yWDZdEEEfB\nBhjVpCgnvOGxrzlGtPJ4y3FNDu4ibzVzxreN9zjY0+TNmJbWK9kpDU0/AoGAZd5g\ntkwAvFDdb2ZBeSu3se2UuNEMHqIJH4cxSoGw1b50Gv5sPg6xa9hI6fHE7h70ywf6\ns7Dq79kHB28nfRh806p8P/4d6e7mH9ZNuMz+JUIyor1MvH4nYLUXVa61uX0KfSrf\n60U2q+wyTdgwFlcT1W6ECNQAx8i6FRPu4T8dihcCgYEAnNHMr2bYNUyk4YSV1Y5q\nOVaD8kYny9FWKhoe+MFxTJgqN32ZqqfxbSfs5r1UhBpr+9Z8Glgyg/i4ga4Za3Xj\nl5i2UFUtgqt92JiQUs9qIKJF3yJhb1bRdt0ZPoVgCoYixkLSfxYAqmtZckCvcfJI\nfBU3G3o04odiWX9lZUrbWCg=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-aghry@kalakumbh-590e0.iam.gserviceaccount.com",
    "client_id": "114582907953163508558",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-aghry%40kalakumbh-590e0.iam.gserviceaccount.com"
}


cred = credentials.Certificate(creds)
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kalakumbh-590e0-default-rtdb.firebaseio.com'
})


def index(request):
    return render(request, 'website/index.html', )


def about(request):
    return render(request, 'website/about.html')


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
            # return HttpResponse("the user already exists. Pleae share your referral code with your friends: " + ref_code)
            return render(request, 'website/index.html', {'success': True, 'ref_code': ref_code, 'already': 'already', })
        ref = user.child('referral_code').get()
        if ref == user_ref_by or user_ref_by == "":
            flag = False
    if flag:
        # return HttpResponse("the referral code is invalid")
        return render(request, 'website/index.html', {'wrongCode': True})
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
    return render(request, 'website/index.html', {'success': True, 'ref_code': user_ref_code})


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
