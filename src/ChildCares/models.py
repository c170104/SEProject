from django.db import models

# Create your models here.


class Price(models.Model):
    sg_citizen_price = models.FloatField(max_length=8)
    pr_citizen_price = models.FloatField(max_length=8)
    fr_citizen_price = models.FloatField(max_length=8)

class Vacancy(models.Model):
    infant_vacancy = models.CharField(max_length = 50)
    pg_vacancy = models.CharField(max_length = 50)
    n1_vacancy = models.CharField(max_length = 50)
    n2_vacancy = models.CharField(max_length = 50)
    k1_vacancy = models.CharField(max_length=50)
    k2_vacancy = models.CharField(max_length=50)

class Timing(models.Model):
    weekday_full_day = models.CharField(max_length = 20)
    weekday_halfday_am = models.CharField(max_length = 20)
    weekday_halfday_pm = models.CharField(max_length = 20)
    saturday = models.CharField(max_length=20)

class ChildCare(models.Model):
    SECOND_LANGUAGES_OFFERED_CHOICES = (
        ('EN', 'English'),
        ('CN', 'Chinese'),
        ('M', 'Malay'),
        ('T', 'Tamil'),
    )

    centre_code = models.CharField(max_length=20, primary_key=True)
    centre_name = models.CharField(max_length=100)
    programmes_offered = models.CharField(max_length=50)
    government_subsidy = models.CharField(max_length=20)
    food_offered = models.CharField(max_length=20)
    second_languages_offered = models.CharField(max_length = 2, choices = SECOND_LANGUAGES_OFFERED_CHOICES)
    spark_certified = models.BooleanField()
    scheme_type = models.CharField(max_length=50)
    iccp = models.BooleanField()
    gst_registration = models.BooleanField()
    centre_website = models.CharField(max_length=100)
    centre_contact_no = models.CharField(max_length=20)
    centre_email_address = models.EmailField(max_length=50)
    centre_address = models.CharField(max_length = 100)
    centre_postal_code = models.CharField(max_length=10)
    centre_remarks = models.CharField(max_length=50, default="No remarks")
    prices = models.ForeignKey(Price, on_delete=models.CASCADE)
    vacancies = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    timings = models.ForeignKey(Timing, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.centre_code, self.centre_name)


class Review(models.Model):
    reviewer = models.CharField(max_length=50)
    review = models.TextField()
    childcare = models.ForeignKey(ChildCare, on_delete=models.CASCADE)


