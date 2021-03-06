# Generated by Django 3.0.8 on 2020-07-30 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('addrress', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'MALE'), ('F', 'FEMALE'), ('O', 'OTHERS')], max_length=1, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(blank=True, choices=[('1', '10:00am - 10:15am'), ('2', '10:15am - 10:30am'), ('3', '10:30am - 10:45am'), ('4', '10:45am - 11:00am'), ('5', '11:00am - 11:15am'), ('6', '11:15am - 11:30am'), ('7', '11:30am - 11:45am'), ('8', '11:45am - 12:00pm'), ('9', '12:00pm - 12:15pm'), ('10', '12:15pm - 12:30pm'), ('11', '12:30pm - 12:45pm'), ('12', '12:45pm - 1:00pm'), ('13', '1:00pm - 1:15pm'), ('14', '1:15pm - 1:30pm'), ('15', '1:30pm - 1:45pm'), ('16', '1:45pm - 2:00pm'), ('17', '2:00pm - 2:15pm'), ('18', '2:15pm - 2:30pm'), ('19', '2:30pm - 2:45pm'), ('20', '2:45pm - 3:00pm')], max_length=2, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
