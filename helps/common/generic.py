from datetime import datetime
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.utils.html import strip_tags
from email_validator import validate_email, EmailNotValidError

class Generichelps:

    def send_mail_including_attatchment(self, subject, message, recipient_list, attachments=[], email_from = None):
        flag = False
        try:
            email = EmailMessage(subject, message, email_from, recipient_list)
            for attachment in attachments:
                email.attach_file(attachment)
            flag = bool(email.send())
        except: flag = False
        return flag
    
    def send_mail_formatting_including_attatchment(self, html_message, subject, recipient_list, attachments=[], email_from = None):
        flag = False
        try:
            plain_message = strip_tags(html_message)
            message = EmailMultiAlternatives(
                subject=subject,
                body=plain_message,
                from_email=email_from,
                to=recipient_list
            )
            message.attach_alternative(html_message, 'text/html')
            for attachment in attachments:
                message.attach_file(attachment)
            flag = bool(message.send())

        except: flag = False
        return flag
    
    def emailvalidate(self, email, condition=True):
        flag = False
        if condition:
            try:
                v = validate_email(email) 
                email = v["email"]  
                flag = True
            except EmailNotValidError as e: flag = False
        else: flag = True
        return flag
    
    # faw
    # def emailvalidate(self, email, condition=True):
    #     flag = False
    #     if condition:
    #         try:
    #             v = validate_email(email)
    #             email = v["email"]
    #             flag = True
    #         except EmailNotValidError as e: flag = False
    #     else: flag = True
    #     return flag
        
    def attachmentvalidate(self, attachmentname, condition=True):
        flag = False
        if condition:
            if '.pdf' in attachmentname[len(attachmentname)-4:]: flag = True
        else: flag = True
        return flag

    def numbervalidate(self, num, condition=True):
        flag = False
        if condition:
            if num.isnumeric():
                if len(num) == 11:
                    if num[:2] == '01':
                        if num[2] in ['3', '4', '5', '6', '7', '8', '9']:
                            flag = True
        else: flag = True
        return flag
    
    def checkvaliddate(self, date, condition=True):
        flag = False
        if condition:
            if self.datevalidate(date):
                if self.ispresentdate(date): flag = True
        else: flag = True
        return flag
    
    def datevalidate(self, date, condition=True):
        flag = False
        if condition:
            try:
                datetime.strptime(f'{date} 00:00:00', '%Y-%m-%d %H:%M:%S')
                flag = True
            except:
                pass
        else: flag = True
        return flag
    
    def ispresentdate(self, date, condition=True):
        flag = False
        if condition:
            try:
                today = datetime.today().strftime('%Y-%m-%d')
                if today<=date: flag = True
            except:
                pass
        else: flag = True
        return flag
    
    def datevalitime(self, time, condition=True):
        flag = False
        if condition:
            try:
                datetime.strptime(f'2024-01-01 {time}', '%Y-%m-%d %H:%M:%S')
                flag = True
            except:
                pass
        else: flag = True
        return flag
    
    def getbudget(self, Budgetdetails, budget):
        if budget:
            if isinstance(budget, str):
                if budget.isnumeric():
                    budget =  int(budget)
        if isinstance(budget, int):
            budgetDetails = Budgetdetails.objects.filter(budgetid=budget)
            if budgetDetails.exists():
                budget = budgetDetails[0].name
        return budget
    
    def getcontextestimateproject(self, challenges, alreadyHave, timeframe, projectType, yourRole, preferredContactTime, projectDetails, newsletterSubscription, name, email, phone):
        return {
                "challenges": [key for key in challenges.keys() if challenges[key]],
                "alreadyHave": [key for key in alreadyHave.keys() if alreadyHave[key]],
                "timeframe": ",".join([key for key in timeframe.keys() if timeframe[key]]),
                "projectType": projectType,
                "yourRole": yourRole,
                # "servicesNeeded": servicesNeeded,
                "preferredContactTime": preferredContactTime,
                "projectDetails": projectDetails,
                "newsletterSubscription": newsletterSubscription,
                "userDetails": {
                    "name": name,
                    "email": email,
                    "phone": phone
                }
        }
    
    def getcontextcontactus(self, companyName, name, corporateEmail, phone, comments, protectDataByNDA):
        return {
                "companyName": companyName,
                "name": name,
                "corporateEmail": corporateEmail,
                "phone": phone,
                "comments": comments,
                "protectDataByNDA": protectDataByNDA
        }
    
    def getcontextrequestschedule(self, service, date, time, budget, description, name, phone):
        return {
                "service": service,
                "date": date,
                "time": time,
                "budget": budget,
                "description": description,
                "userDetails": {
                    "name": name,
                    "phone": phone
                }
            }
    
    def removedoublequotation(self, string):
        if string:
            if string[0] == '"':
                if string[len(string)-1] == '"':
                    string = string[1:len(string)]
                    string = string[0:len(string)-1]
        return string            