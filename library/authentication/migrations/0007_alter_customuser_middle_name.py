# Generated by Django 4.1 on 2024-03-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_customuser_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
