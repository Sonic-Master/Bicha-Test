from django.db import models

# Create your models here.

class job_post(models.Model):
    img         = models.ImageField(upload_to='jobpost')
    title       = models.CharField(max_length=200)
    company_name= models.CharField(max_length=200)
    des         = models.TextField()
    job_nature  = models.CharField(max_length=200)
    location    = models.CharField(max_length=200)
    salary      = models.CharField(max_length=100)
    tag_1       = models.CharField(max_length=100)
    tag_2       = models.CharField(max_length=100)
    tag_3       = models.CharField(max_length=100)
    datetime    = models.DateField(null=True)
    code        = models.CharField(max_length=100)
    job_category= models.CharField(max_length=200)
    # immediate   = models.BooleanField(default=False)
    


class job_category(models.Model):
    job_cat       = models.CharField(max_length=200)








class applyed_candidates(models.Model):
    code                        = models.CharField(max_length=100)
    candidates_givenname        = models.CharField(max_length=200)
    candidates_surename         = models.CharField(max_length=200)
    candidates_email            = models.EmailField()
    candidates_phonenumber      = models.BigIntegerField()
    candidates_resume           = models.FileField(upload_to='CandidatesResume')

    

class imp_messages(models.Model):
    message         = models.TextField()
    datetime        = models.DateTimeField()    




class Interview_attended_datas(models.Model):
    code                        = models.CharField(max_length=100)
    candidates_givenname        = models.CharField(max_length=200)
    candidates_surename         = models.CharField(max_length=200)
    candidates_email            = models.EmailField()
    candidates_phonenumber      = models.BigIntegerField()



class Shortlisted(models.Model):
    Shortlisted_candidates_id    =   models.CharField(max_length=200)



