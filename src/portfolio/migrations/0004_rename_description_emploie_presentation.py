# Generated by Django 4.2.2 on 2023-06-30 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_emploie_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emploie',
            old_name='description',
            new_name='presentation',
        ),
    ]
