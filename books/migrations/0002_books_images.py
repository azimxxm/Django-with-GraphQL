# Generated by Django 3.2.8 on 2022-03-09 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='images',
            field=models.ImageField(default='image', help_text='Kitobni rasmini yuklang', upload_to='Books/%y/%m/'),
            preserve_default=False,
        ),
    ]
