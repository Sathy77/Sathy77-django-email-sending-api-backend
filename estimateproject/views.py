from helps.response.responsemessage import response as rspn
from helps.common.generic import Generichelps as ghelp
from rest_framework.decorators import api_view
from rest_framework.response import Response
from estimateproject.models import *
from rest_framework import status
import json

from django.template.loader import render_to_string


@api_view(['POST'])
def addestimateproject(request):
    errors = []

    challenges = json.loads(request.data.get('challenges', str({})).replace("'", "\""))
    alreadyHave = json.loads(request.data.get('alreadyHave', str({})).replace("'", "\""))
    timeframe = json.loads(request.data.get('timeframe', str({})).replace("'", "\""))
    projectType = ghelp().removedoublequotation(request.data.get('projectType', ''))
    yourRole = ghelp().removedoublequotation(request.data.get('yourRole', ''))
    # servicesNeeded = request.data.get('servicesNeeded', '')
    preferredContactTime = ghelp().removedoublequotation(request.data.get('preferredContactTime', ''))
    attachment = request.FILES.get('attachment')
    attachmentname = '' if attachment == None else str(attachment)
    projectDetails = ghelp().removedoublequotation(request.data.get('projectDetails', ''))
    userDetails = json.loads(request.data.get('userDetails', str({})).replace("'", "\""))
    newsletterSubscription = json.loads(request.data.get('newsletterSubscription', "true"))

    if not projectType: errors.append({'field': 'projectType','message': rspn['required_error']['projectType']})
    if not preferredContactTime: errors.append({'field': 'preferredContactTime','message': rspn['required_error']['preferredContactTime']})
    if not yourRole: errors.append({'field': 'yourRole','message': rspn['required_error']['yourRole']})
    if not userDetails: errors.append({'field': 'userDetails','message': rspn['required_error']['userDetails']})

    if (userDetails =={})==False:
        name=userDetails.get('name', '')
        email=userDetails.get('email', '')
        phone=userDetails.get('phone', '')

        if not ghelp().emailvalidate(email): errors.append({'field': 'email','message': rspn['field_err_msg']['email']})
        if not ghelp().numbervalidate(phone): errors.append({'field': 'phone','message': rspn['field_err_msg']['phone']})
        if attachmentname:
            if not ghelp().attachmentvalidate(attachmentname): errors.append({'field': 'attachment','message': rspn['field_err_msg']['attachment']})

    if errors: return Response({'status': rspn['error_status'], 'message': rspn['error_message'], 'errors': errors}, status=status.HTTP_400_BAD_REQUEST)
    else: 
        userdetails = Userdetails.objects.create(name=name, email=email, phone=phone)

        if attachment:
            estimateproject = Estimateproject.objects.create(
                projectType=projectType, 
                yourRole=yourRole, 
                # servicesNeeded=servicesNeeded,
                preferredContactTime = preferredContactTime,
                attachment = attachment,
                attachmentname = attachmentname,
                projectDetails = projectDetails,
                userDetails = userdetails,
                newsletterSubscription = newsletterSubscription
                )
        else:
            estimateproject = Estimateproject.objects.create(
                projectType=projectType, 
                yourRole=yourRole, 
                # servicesNeeded=servicesNeeded,
                preferredContactTime = preferredContactTime,
                projectDetails = projectDetails,
                userDetails = userdetails,
                newsletterSubscription = newsletterSubscription
                )
        for key in challenges.keys():
            Challenge.objects.create(fieldName=key, value=challenges[key], estimateProject=estimateproject)

        for key in alreadyHave.keys():
            Alreadyhave.objects.create(fieldName=key, value=alreadyHave[key], estimateProject=estimateproject)

        for key in timeframe.keys():
            Timeframe.objects.create(fieldName=key, value=timeframe[key], estimateProject=estimateproject)

        subject = 'Mail From Api Solutions ltd.'
        # recipient_list = ['nazmulhussain.api@gmail.com','mustafatanim59@gmail.com','apitestingofficial@gmail.com']
        recipient_list = ['apitestingofficial@gmail.com']
        attachments = [f'media/{estimateproject.attachment}'] if attachment else []
        # context = ghelp().getcontextestimateproject(challenges, alreadyHave, timeframe, projectType, yourRole, servicesNeeded, preferredContactTime, projectDetails, newsletterSubscription, name, email, phone)
        context = ghelp().getcontextestimateproject(challenges, alreadyHave, timeframe, projectType, yourRole, preferredContactTime, projectDetails, newsletterSubscription, name, email, phone)
        html_message = render_to_string('EstimateProjectRequestDetails.html', context=context)
        ghelp().send_mail_formatting_including_attatchment(html_message, subject, recipient_list, attachments)
            
        return Response({'status': rspn['success_status'], 'message': rspn['success_message_es']}, status=status.HTTP_201_CREATED)