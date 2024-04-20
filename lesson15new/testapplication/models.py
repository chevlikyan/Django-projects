from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
status = models.BooleanField(default=True)
BIRTH_MONTH = (
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'))


class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    id = models.CharField(max_length=30, primary_key=True)
    age = models.PositiveSmallIntegerField(
        default=18,
        validators=[MinValueValidator(16),
                    MaxValueValidator(55)]
    )
    email = models.EmailField(
        max_length=40,
        unique=True
    )
    phone_number = models.CharField(max_length=20, unique=True)
    description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        help_text="Introduce yourself"
    )
    address = models.CharField(
        'address (by default is Yerevan)',
        max_length=30,
        default='Yerevan'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    birth_month = models.CharField(
        max_length=10,
        choices=BIRTH_MONTH)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Անձ'
        verbose_name_plural = 'Մարդիկ'


BOOK_CATEGORIES = (
    ('detective', 'detective'),
    ('adventure', 'adventure'),
    ('science', 'science'),
    ('melodrama', 'melodrama'),
    ('drama', 'drama'))


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    year = models.DateField()
    book_category = models.CharField(
        max_length=10,
        choices=BOOK_CATEGORIES
    )
    description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        help_text="About book"
    )
    pages = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(50),
                    MaxValueValidator(500)]
    )
    printed_at = models.DateTimeField(auto_now_add=True)
    publisher = models.CharField(
        'printed in '
        '(by default is Edit-Print)',
        max_length=30,
        default='Edit-Print'
    )
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} {self.author}"

    class Meta:
        verbose_name = 'Գիրք'
        verbose_name_plural = 'Գրքեր'


class School(models.Model):
    school_after = models.CharField(max_length=30, unique=True)
    school_number = models.PositiveSmallIntegerField(unique=True)
    address = models.CharField(
        'by default is Yerevan',
        max_length=30,
        default="Armenia/Yerevan")
    director = models.CharField(max_length=30)
    classes_count = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(12),
                    MaxValueValidator(48)]
    )
    classrooms_count = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(48)]
    )
    teachers_count = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(48)]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.school_number} {self.school_after}"

    class Meta:
        verbose_name = 'Դպրոց'
        verbose_name_plural = 'Դպրոցներ'


TEACHERS = (
    ("Safaryan", "Safaryan"),
    ("Kirakosyan", "Kirakosyan"),
    ("Harutyunyan", "Harutyunyan"),
    ("Chevlikyan", "Chevlikyan"),
    ("Nersesyan", "Nersesyan"),
    ("Karoyan", "Karoyan"),
    ("Matshkalyan", "Matshkalyan")
)

STREAM = (
    ('a', 'a'),
    ('b', 'b'),
    ('c', 'c'),
    ('d', 'd'),
)


class TheClass(models.Model):
    year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(12)]
    )
    stream = models.CharField(
        max_length=2,
        choices=STREAM
    )
    description = models.TextField(
        max_length=50,
        null=True,
        blank=True,
        help_text="A little about class"
    )
    students_count = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(10),
                    MaxValueValidator(30)]
    )
    lessons_count = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(2),
                    MaxValueValidator(10)]
    )
    teacher = models.CharField(
        max_length=30,
        choices=TEACHERS
    )
    wanted_language = models.CharField(
        'foreign languages (by default is English)',
        max_length=30,
        default='English'
    )

    def __str__(self):
        return f"{self.year} {self.stream}"

    class Meta:
        verbose_name = 'դասարան'
        verbose_name_plural = 'դասարաններ'


MARKS = (
    ('BMW', 'BMW'),
    ('Mercedes-Benz', 'Mercedes-Benz'),
    ('Range-Rover', 'Range-Rover'),
    ('Opel', 'Opel'),
    ('Toyota', 'Toyota'),
    ('Honda', 'Honda'),
    ('Nissan', 'Nissan')
)


# BMW_MODELS = (
#     ('1 series', '1 series'),
#     ('2 series', '2 series'),
#     ('3 series', '3 series'),
#     ('4 series', '4 series'),
#     ('5 series', '5 series'),
#     ('6 series', '6 series'),
#     ('7 series', '7 series'),
#     ('8 series', '8 series'),
#     ('X1', 'X1'),
#     ('X2', 'X2'),
#     ('X3', 'X3'),
#     ('X4', 'X4'),
#     ('X5', 'X5'),
#     ('X6', 'X6'),
#     ('X7', 'X7')
# )
#
# MERCEDES_BENZ_MODELS = (
#     ('A class', 'A class'),
#     ('B class', 'B class'),
#     ('C class', 'C class'),
#     ('E class', 'E class'),
#     ('G class', 'G class'),
#     ('S class', 'S class'),
#     ('GLE', 'GLE'),
#     ('GLS', 'GLS')
#
# )

class Car(models.Model):
    mark = models.CharField(
        max_length=30,
        choices=MARKS
    )
    model = models.CharField(max_length=30)
    year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(2000)]
    )
    VIN_code = models.CharField(max_length=50, unique=True)
    description = models.TextField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Enter a brief description of your car'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sales = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.mark} {self.model}"

    class Meta:
        verbose_name = 'Մեքենա'
        verbose_name_plural = 'Մեքենաներ'
