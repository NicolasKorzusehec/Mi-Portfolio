# Generated by Django 4.1 on 2022-08-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proyectos',
            options={'ordering': ['-created'], 'verbose_name': 'proyecto', 'verbose_name_plural': 'proyectos'},
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects', verbose_name='Imagen'),
        ),
    ]
