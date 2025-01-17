# Generated by Django 3.0.6 on 2020-05-10 01:02

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20200509_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bodylog',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='cardiovascularlog',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='checkuplog',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='dietlog',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='exerciselog',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='medicationlog',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='naturalremedieslog',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='sleeplog',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='stresslog',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='symptomslog',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='toiletlog',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='vicelog',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='user',
            name='cnp',
            field=models.CharField(blank=True, max_length=13, verbose_name='numeric personal code'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='phone number'),
        ),
    ]
