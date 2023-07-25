# Generated by Django 4.2.1 on 2023-06-12 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsapp', '0003_author_student_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('Students', models.ManyToManyField(to='petsapp.student')),
            ],
        ),
    ]
