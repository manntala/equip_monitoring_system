# Generated by Django 4.1.5 on 2023-08-04 17:11

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=30)),
                ('serial_number', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('Laptop', 'Laptop'), ('Desktop', 'Desktop'), ('Mobile', 'Mobile'), ('Tablet', 'Tablet')], max_length=20)),
                ('status', models.CharField(choices=[('Assigned', 'Assigned'), ('Unassigned', 'Unassigned'), ('For Repair', 'For Repair')], default='Unassigned', max_length=20)),
                ('condition', models.CharField(choices=[('New', 'New'), ('Used', 'Used'), ('Refurbished', 'Refurbished')], default='New', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
