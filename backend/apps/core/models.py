from django.conf import settings
from django.db import models


class AcademicYear(models.Model):
    label = models.CharField(max_length=20, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ('-start_date',)

    def __str__(self):
        return self.label


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='student_profile')
    matricule = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.matricule} - {self.user.get_full_name()}'


class Admission(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DRAFT', 'Brouillon'
        SUBMITTED = 'SUBMITTED', 'Soumise'
        ACCEPTED = 'ACCEPTED', 'Acceptée'
        REJECTED = 'REJECTED', 'Rejetée'

    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='admissions')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.PROTECT, related_name='admissions')
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.DRAFT)
    submitted_at = models.DateTimeField(null=True, blank=True)


class Document(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class TeachingUnit(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=150)
    credits = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.code} - {self.name}'


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    teaching_unit = models.ForeignKey(TeachingUnit, on_delete=models.PROTECT, related_name='enrollments')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.PROTECT, related_name='enrollments')

    class Meta:
        constraints = [models.UniqueConstraint(fields=('student', 'teaching_unit', 'academic_year'), name='unique_student_ue_year')]


class Grade(models.Model):
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE, related_name='grade')
    value = models.DecimalField(max_digits=5, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [models.CheckConstraint(check=models.Q(value__gte=0, value__lte=20), name='grade_between_0_and_20')]
