# Generated by Django 4.0.6 on 2022-08-02 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_myuser_is_verified_myuser_licence_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='licence_link',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='pic_link',
            field=models.CharField(default='https://www.citypng.com/public/uploads/preview/warranty-ribbon-blue-icon-logo-sign-label-badge-png-11635941164yp8i70hmcb.png', max_length=400),
        ),
    ]