# Generated by Django 4.1.2 on 2022-10-29 15:41

import datetime
from django.conf import settings
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('additionalnames', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=10, verbose_name='additional names')),
                ('creationdate', models.DateTimeField(default=datetime.datetime(2022, 10, 29, 15, 41, 18, 501791, tzinfo=datetime.timezone.utc), max_length=20, verbose_name='create date')),
                ('accountid', models.CharField(max_length=50)),
                ('roleid', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='phone number')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
