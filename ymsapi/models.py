from django.db import models

class student_detail(models.Model):
    s_name = models.CharField(max_length=60)
    s_email = models.CharField(max_length=100)
    s_gender = models.CharField(max_length=10)
    s_picture = models.ImageField(upload_to = "images/student/")
    s_dob = models.DateField()
    s_address = models.CharField(max_length=60)
    s_city = models.CharField(max_length=60)
    s_state = models.CharField(max_length=60)
    s_pincode = models.IntegerField()
    s_created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.s_name
    

class teacher_detail(models.Model):
    t_name = models.CharField(max_length=60)
    t_email = models.CharField(max_length=100)
    t_gemder = models.CharField(max_length=5)
    t_picture = models.ImageField(upload_to = "images/student/")
    t_dob = models.DateField()
    t_address = models.CharField(max_length=60)
    t_city = models.CharField(max_length=60)
    t_state = models.CharField(max_length=60)
    t_pincode = models.IntegerField()
    t_created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.t_name
    
class admin_detail(models.Model):
    a_name = models.CharField(max_length=60)
    a_email = models.CharField(max_length=100)
    a_gemder = models.CharField(max_length=5)
    a_picture = models.ImageField(upload_to = "images/student/")
    a_dob = models.DateField()
    a_address = models.CharField(max_length=60)
    a_city = models.CharField(max_length=60)
    a_state = models.CharField(max_length=60)
    a_pincode = models.IntegerField()
    a_created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.a_name