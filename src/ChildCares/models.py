from django.db import models

# Create your models here.

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
    centre_area = models.CharField(max_length=20, default="")

    def __str__(self):
        return "%s %s" % (self.centre_code, self.centre_name)


class Review(models.Model):
    STAR_CHOICES = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    )

    childcare = models.ForeignKey(ChildCare, on_delete=models.CASCADE, related_name="reviews")
    reviewer = models.CharField(max_length=50)
    review = models.TextField()
    star = models.IntegerField(choices=STAR_CHOICES, default=0)

class Price(models.Model):
    childcare = models.ForeignKey(ChildCare, on_delete=models.CASCADE, related_name="prices")
    citizen = models.CharField(max_length=20, default="")
    price = models.FloatField(max_length=8, default=0.0)

class Timing(models.Model):
    childcare = models.ForeignKey(ChildCare, on_delete=models.CASCADE, related_name="timings")
    day = models.CharField(max_length=30)
    timing = models.CharField(max_length = 20)

class Vacancy(models.Model):
    childcare = models.ForeignKey(ChildCare, on_delete=models.CASCADE, related_name="vacancies")
    vacancy_type = models.CharField(max_length=30)
    vacancy = models.CharField(max_length=50)