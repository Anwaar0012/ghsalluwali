from django.db import models

class Employee(models.Model):
    DESIGNATION_CHOICES = [
        ('SST Arts', 'SST Arts'),
        ('SST MATH', 'SST MATH'),
        ('SST BIO', 'SST BIOLOGY'),
        ('SST PHY', 'SST PHYSICS'),
        ('SST CHE', 'SST CHEMISTRY'),
        ('SST IT', 'SST COMPUTER'),
        ('EST Arts', 'EST Arts'),
        ('EST Sci', 'EST Science'),
        ('EST Arts', 'EST Arts'),
        ('EST Agri', 'EST Agri'),
        ('EST General', 'EST General'),
        ('EST Vr', 'EST Vernacular'),
        ('PST Sci', 'PST Science'),
        ('PST Arts', 'PST Arts'),
        ('PST', 'PST'),
        ('Naib Qasid', 'Naib Qasid'),
        ('L.Attendant', 'Lab Attendant'),
        ('Mali', 'Mali'),
        ('C.IV', 'Class 4'),
        ('SG', 'Security Guard'),
        ('Chokidat', 'Chokidar'),
        ('Sweaper', 'Sweaper'),
    ]
    SCALE_CHOICES = [
        ('19', '19'),
        ('18', '18'),
        ('17', '17'),
        ('16', '16'),
        ('15', '15'),
        ('14', '14'),
        ('12', '12'),
        ('9', '9'),
        ('7', '7'),
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)  # Father name
    cnic = models.CharField(max_length=15, unique=True)  # CNIC formatted as XXXXX-XXXXXXX-X
    personalno = models.CharField(max_length=50, unique=True)  # Personal number
    designation = models.CharField(max_length=20, choices=DESIGNATION_CHOICES)
    scale = models.CharField(max_length=3, choices=SCALE_CHOICES)
    date_of_birth = models.DateField()
    date_of_first_joining = models.DateField()
    date_of_joining_present_scale = models.DateField()
    date_of_joining_present_school = models.DateField()
    accountno = models.CharField(max_length=50, unique=True)  # Personal number
    bank = models.CharField(max_length=100)  # Personal number
    phoneno = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)  # Optional gender
    address = models.TextField(blank=True, null=True)  # Optional address
    image = models.ImageField(upload_to='shoolapp/images', default="")

    def __str__(self):
        return f'{self.name} - {self.designation}'
    

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    CLASS_CHOICES = [
        ('Nursery', 'Nursery'),
        ('KG', 'Kindergarten'),
        ('1', 'Class 1'),
        ('2', 'Class 2'),
        ('3', 'Class 3'),
        ('4', 'Class 4'),
        ('5', 'Class 5'),
        ('6', 'Class 6'),
        ('7', 'Class 7'),
        ('8', 'Class 8'),
        ('9', 'Class 9'),
        ('10', 'Class 8'),
    ]

    admission_no = models.CharField(max_length=20, unique=True)  # Unique admission number
    admission_date = models.DateField()  # Date of admission
    name = models.CharField(max_length=100)  # Student's name
    fathername = models.CharField(max_length=100)  # Father's name
    b_form_no = models.CharField(max_length=15, unique=True)  # B-Form number (unique identification)
    contact_no = models.CharField(max_length=15)  # Contact number
    class_enrolled = models.CharField(max_length=10, choices=CLASS_CHOICES)  # Class in which the student is enrolled
    date_of_birth = models.DateField()  # Date of birth
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)  # Gender
    image = models.ImageField(upload_to='shoolapp/images', default="")

    def __str__(self):
        return f'{self.admission_no} - {self.name} - class-{self.class_enrolled}'


