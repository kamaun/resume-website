from django.db import models
import datetime, os


# Create your models here.

def get_date(**kwargs):
    if kwargs['date'] == "day":
        return [(d, d) for d in range(0, 32)]
    elif kwargs['date'] == "month":
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'September', 'October', 'November', 'December']
        return [(m, m) for m in months]
    elif kwargs['date'] == "year":
        years = [y for y in range(2006, datetime.date.today().year + 6)]
        return [(y, y) for y in years]


def get_profile_image_url(instance, filename):
    return os.path.join('photos/profile', str(instance.id), filename)


def get_project_image_url(instance, filename):
    return os.path.join('photos/project', str(instance.id), filename)


def application():
    application_base = ["Web Application", "Mobile Application", "Desktop Application", "Raspberry Pi"]
    return [(a, a) for a in application_base]


def category():
    category_base = ["Application Type", "Programming", "Framework", "Cloud Services", "Software", "Operating System"]
    return [(c, c) for c in category_base]


class Profile(models.Model):
    first_name = models.CharField(max_length=20, db_column='FirstName', verbose_name='First Name', default='Kevin')
    last_name = models.CharField(max_length=20, db_column='LastName', verbose_name='Last Name', default='Anderson')
    occupation = models.CharField(max_length=20, default='Software Engineer')
    location_city = models.CharField(max_length=30, default='Deerfield Beach')
    location_state = models.CharField(max_length=10, default='Florida')
    profile_pic = models.ImageField(upload_to=get_profile_image_url, null=True, blank=True)
    email = models.EmailField(max_length=30, default='kevinnjeri@live.com')
    email2 = models.EmailField(max_length=30, default='devkevengineer@gmail.com')
    linkedin = models.URLField(verbose_name='LinkedIn', default='https://www.linkedin.com/in/kelvinnjeri/')
    bitbucket = models.URLField(verbose_name='Bitbucket', default='https://bitbucket.org/knjeri')
    github = models.URLField(verbose_name='Git Hub', default='https://github.com/kamaun')
    age = models.IntegerField(default=26)
    cell_number = models.BigIntegerField(default=9547935283, db_column='CellNumber', verbose_name='Cell Number')
    bio = models.TextField(max_length=600, default='Bio')
    interest = models.TextField(max_length=600, null=True, blank=True)

    class Meta:
        managed = True
        app_label = 'resume'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.occupation}'


class Technology(models.Model):
    # techid = models.AutoField(primary_key=True, db_column='ID')
    category = models.CharField(max_length=20, choices=category(), default="Programming")
    technology = models.CharField(max_length=20)
    proficiency = models.IntegerField(choices=[(i * 10, i * 10) for i in range(11)], default=1)
    years = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        managed = True
        app_label = 'resume'
        db_table = 'Technology'
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.technology


class School(models.Model):
    # schoolid = models.AutoField(primary_key=True, db_column='ID')
    school = models.CharField(max_length=50, db_column='School')
    city = models.CharField(max_length=20, db_column='City')
    state = models.CharField(max_length=10, db_column='State', blank=True)
    country = models.CharField(max_length=20, db_column='Country')
    degree = models.CharField(max_length=50, db_column="Degree", null=True)
    concentration = models.CharField(max_length=20, db_column='Concentration')
    from_month = models.CharField(max_length=10, choices=get_date(date='month'))
    from_year = models.IntegerField(choices=get_date(date='year'))
    current_school = models.BooleanField(default=False)
    end_month = models.CharField(max_length=10, choices=get_date(date='month'), blank=True)
    end_year = models.IntegerField(choices=get_date(date='year'), null=True, blank=True)

    class Meta:
        managed = True
        app_label = 'resume'
        db_table = 'School'

    def __str__(self):
        return f'{self.degree} in {self.concentration}'

    def location(self):
        if self.state is None:
            return f'{self.city}, {self.country}'
        else:
            return f'{self.city}, {self.state}, {self.country}'

    def is_current_school(self):
        return self.current_school

    def start_date(self):
        return f'{self.from_month} {self.from_year}'

    def end_date(self):
        return f'{self.end_month} {self.end_year}'


class WorkPlaces(models.Model):
    # jobid = models.AutoField(primary_key=True, db_column='ID')
    work_name = models.CharField(max_length=50, db_column='Company', verbose_name="Company")
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=10, db_column='State', blank=True)
    country = models.CharField(max_length=20)
    position = models.CharField(max_length=50)
    link = models.URLField(max_length=128, verbose_name='Url', blank=True)
    from_month = models.CharField(max_length=10, choices=get_date(date='month'))
    from_year = models.IntegerField(choices=get_date(date='year'))
    current_job = models.BooleanField(default=False)
    end_month = models.CharField(max_length=10, choices=get_date(date='month'), blank=True)
    end_year = models.IntegerField(choices=get_date(date='year'), null=True, blank=True)
    description = models.TextField(max_length=600, default="Enter job description")
    extra = models.BooleanField(default=False)

    class Meta:
        managed = True
        app_label = 'resume'
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return self.position

    def is_current_job(self):
        return self.current_job

    def start_date(self):
        return f'{self.from_month} {self.from_year}'

    def end_date(self):
        return f'{self.end_month} {self.end_year}'


class Projects(models.Model):
    # projectid = models.AutoField(primary_key=True, db_column='ID')
    project_image = models.ImageField(upload_to=get_project_image_url, null=True, blank=True)
    project_name = models.CharField(max_length=50, db_column='Project')
    link = models.URLField(max_length=128, blank=True, verbose_name='Url')
    role = models.CharField(max_length=30, null=True)
    school = models.ForeignKey('School', models.CASCADE, null=True, blank=True)
    job = models.ForeignKey('WorkPlaces', models.CASCADE, null=True, blank=True)
    from_month = models.CharField(max_length=10, choices=get_date(date='month'), blank=True, null=True)
    from_year = models.IntegerField(choices=get_date(date='year'), blank=True, null=True)
    in_progress = models.BooleanField(default=False)
    end_month = models.CharField(max_length=10, choices=get_date(date='month'), blank=True, null=True)
    end_year = models.IntegerField(choices=get_date(date='year'), null=True, blank=True)
    personal = models.BooleanField(default=False)
    description = models.TextField(max_length=600, default="Project Description")

    class Meta:
        managed = True
        app_label = 'resume'
        verbose_name = 'Project'

    def __str__(self):
        return self.project_name

    def is_personal_project(self):
        return self.personal

    def is_in_progress(self):
        return self.in_progress

    def start_date(self):
        return f'{self.from_month} {self.from_year}'

    def end_date(self):
        return f'{self.end_month} {self.end_year}'


class ProjectImages(models.Model):
    project = models.ForeignKey('Projects', models.CASCADE)
    image = models.ImageField(upload_to=get_project_image_url)

    class Meta:
        managed = True
        app_label = 'resume'
        verbose_name = 'Project Image'

    def __str__(self):
        return self.project


class ProjectType(models.Model):
    project = models.ForeignKey('Projects', models.CASCADE, null=True, blank=True)
    technology = models.ForeignKey('Technology', models.CASCADE, null=True, blank=True)

    class Meta:
        managed = True
        app_label = 'resume'
        verbose_name = 'Project Type'
        verbose_name_plural = 'Project Types'

    def __str__(self):
        return self.technology


class TechUsed(models.Model):
    project = models.ForeignKey('Projects', models.CASCADE)
    technology = models.ForeignKey('Technology', models.CASCADE, null=True)
    purpose = models.TextField(max_length=200, default="Technology use")

    class Meta:
        managed = True
        app_label = 'resume'
        verbose_name = 'Tech Use'
        verbose_name_plural = 'Tech Uses'

    def __str__(self):
        return self.technology.technology


class Task(models.Model):
    title = models.CharField(max_length=50)
    project = models.ForeignKey(Projects, models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=800)

    class Meta:
        managed = True
        app_label = 'resume'

    def __str__(self):
        return f'{self.title} - {self.project}:\t {self.description[:50]}...'


class Certification(models.Model):
    # cert_type = models.CharField(max_length=50, verbose_name="Type")
    name = models.CharField(max_length=50, verbose_name="Name")
    cert_number = models.CharField(max_length=20, verbose_name="Certificate Number")
    source = models.CharField(max_length=30, verbose_name="Provider")
    cert_month = models.CharField(max_length=10, choices=get_date(date='month'), verbose_name='Certificate Month', null=True, blank=True)
    cert_year = models.IntegerField(choices=get_date(date='year'), verbose_name='Certificate Year', null=True, blank=True)

    class Meta:
        managed = True
        app_label = 'resume'

    def __str__(self):
        return f'{self.source} - {self.name}'

    def issue_date(self):
        return f'{self.cert_month} {self.cert_year}'
