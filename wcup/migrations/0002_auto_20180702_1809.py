# Generated by Django 2.0.7 on 2018-07-02 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wcup', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='name_pinyi',
            new_name='name_pinyin',
        ),
    ]