from django.db import models

class Administrator(models.Model):
    student_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15,blank=True, null=True)
    email = models.EmailField(max_length=45,blank=True, null=True)
    mode_of_enquiry = models.CharField(max_length=50,blank=True, null=True)
    course_name = models.CharField(max_length=100,blank=True, null=True)
    enquiry_date = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    enquiry_handled_by = models.CharField(max_length=100,blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    reference = models.CharField(max_length=100, blank=True, null=True)
    reason_not_to_join = models.TextField(blank=True, null=True)
    educational = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.student_name