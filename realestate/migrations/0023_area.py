# Generated by Django 3.0.3 on 2020-04-14 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0022_zipcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('area_id', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=30)),
                ('zipcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.Zipcode')),
            ],
        ),
    ]
