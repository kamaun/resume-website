from django.db import models
import datetime

# Create your models here.


def get_date(**kwargs):
    if kwargs['date'] == "day":
        return [(d, d) for d in range(0, 32)]
    elif kwargs['date'] == "month":
        months = ['January', 'February', 'March', 'April',
                  'May', 'June', 'July', 'August',
                  'September', 'October', 'November', 'December']
        return [(m, m) for m in months]
    elif kwargs['date'] == "year":
        return [(y, y) for y in range(2005,  datetime.date.today().year + 4)]


def category():
    CATEGORY_BASE = ["Programming", "Framework", "Cloud Services", "Software", "Operating System"]
    return [(c, c) for c in CATEGORY_BASE]

def development():
    DEV_BASE = ["Web Development", "iOS Development", "Desktop Development"]
    return [(d, d) for d in DEV_BASE]


class profile(models.Model):
    first_name = models.CharField(max_length=20, db_column='FirstName', verbose_name='First Name', default='Kevin')
    last_name = models.CharField(max_length=20, db_column='LastName', verbose_name='Last Name', default='Anderson')
    occupation = models.CharField(max_length=20, default='Software Developer')
    email = models.EmailField(max_length=30, default='kevinnjeri@live.com')
    email2 = models.EmailField(max_length=30, default='devkevengineer@gmail.com')
    age = models.IntegerField(default=26)
    cell_number = models.BigIntegerField(default=9547935283, db_column='CellNumber', verbose_name='Cell Number')
    bio = models.TextField(max_length=600, default='Bio')

    class Meta:
        managed = True
        app_label = 'main'

    def __str__(self):
        fullname = "%s %s" % (self.first_name, self.last_name)
        return fullname


class Technology(models.Model):

    techid = models.AutoField(primary_key=True, db_column='ID')
    category = models.CharField(max_length=20, choices=category(), default="Programming")
    technology = models.CharField(max_length=20)
    proficiency = models.IntegerField(choices=[(i*10, i*10) for i in range(11)], default=1)
    years = models.DecimalField(max_digits=20, decimal_places=1)

    class Meta:
        managed = True
        app_label = 'main'
        db_table = 'Technology'
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.technology


class School(models.Model):
    schoolid = models.AutoField(primary_key=True, db_column='ID')
    school = models.CharField(max_length=50, db_column='School')
    city = models.CharField(max_length=20, db_column='City')
    state = models.CharField(max_length=10, db_column='State', blank=True)
    country = models.CharField(max_length=20, db_column='Country')
    degree = models.CharField(max_length=50, db_column="Degree", null=True)
    major = models.CharField(max_length=20, db_column='Major')
    from_month = models.CharField(max_length=10, choices=get_date(date='month'))
    from_year = models.IntegerField(choices=get_date(date='year'))
    current_school = models.BooleanField(default=False)
    end_month = models.CharField(max_length=10, choices=get_date(date='month'), blank=True)
    end_year = models.IntegerField(choices=get_date(date='year'), null=True, blank=True)
    extra = models.BooleanField(default=False)


    class Meta:
        managed = True
        app_label = 'main'
        db_table = 'School'

    def __str__(self):
        return self.degree

    def is_current_school(self):
        return self.current_school


class WorkPlaces(models.Model):
    jobid = models.AutoField(primary_key=True, db_column='ID')
    work_name = models.CharField(max_length=50, db_column='Company', verbose_name="Company")
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=10, db_column='State', blank=True)
    country = models.CharField(max_length=20)
    position = models.CharField(max_length=50)
    link = models.URLField(max_length=128,  verbose_name='Web Link', blank=True)
    from_month = models.CharField(max_length=10, choices=get_date(date='month'))
    from_year = models.IntegerField(choices=get_date(date='year'))
    current_job = models.BooleanField(default=False)
    end_month = models.CharField(max_length=10, choices=get_date(date='month'), blank=True)
    end_year = models.IntegerField(choices=get_date(date='year'), null=True, blank=True)
    description = models.TextField(max_length=600, default="Enter job description")
    extra = models.BooleanField(default=False)

    class Meta:
        managed = True
        app_label = 'main'
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return self.position


    def is_current_job(self):
        return self.current_job


class Projects(models.Model):
    projectid = models.AutoField(primary_key=True, db_column='ID')
    project_name = models.CharField(max_length=30, db_column='Project')
    link = models.URLField(max_length=128, blank=True, verbose_name='Web Link')
    school = models.ForeignKey('School', models.CASCADE, null=True, blank=True)
    job = models.ForeignKey('WorkPlaces', models.CASCADE, null=True, blank=True)
    personal = models.BooleanField(default=False)
    description = models.TextField(max_length=600, default="Project Description")
    category = models.CharField(max_length=30, choices=development(), blank=True)

    class Meta:
        managed = True
        app_label = 'main'
        verbose_name = 'Project'

    def __str__(self):
        return self.project_name

    def is_personal_project(self):
        return self.personal


class TechUsed(models.Model):
    project = models.ForeignKey('Projects', models.CASCADE)
    technology = models.ForeignKey('Technology', models.CASCADE, null=True)
    # school = models.ForeignKey('School', models.CASCADE, null=True, blank=True)
    # work = models.ForeignKey(WorkPlaces, models.CASCADE, null=True, blank=True)
    purpose = models.CharField(max_length=300, default="Technology use")

    class Meta:
        managed = True
        app_label = 'main'
        verbose_name = 'Tech Use'
        verbose_name_plural = 'Tech Uses'

    def __str__(self):
        return self.technology.technology


class Task(models.Model):
    title = models.CharField(max_length=30)
    work = models.ForeignKey(WorkPlaces, models.CASCADE, null=True, blank=True)
    school = models.ForeignKey(School, models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Projects, models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=800)

    class Meta:
        managed = True
        app_label = 'main'

    def __str__(self):
        return self.title

