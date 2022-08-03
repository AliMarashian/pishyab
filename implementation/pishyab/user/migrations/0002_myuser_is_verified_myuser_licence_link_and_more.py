# Generated by Django 4.0.6 on 2022-08-02 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='licence_link',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='pic_link',
            field=models.CharField(default='https://www.citypng.com/public/uploads/preview/warranty-ribbon-blue-icon-logo-sign-label-badge-png-11635941164yp8i70hmcb.png', max_length=200),
        ),
    ]