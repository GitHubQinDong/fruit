# Generated by Django 2.0.1 on 2018-02-02 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttitle', models.CharField(max_length=20)),
                ('scbz', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodinfo',
            name='gadv',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='goodinfo',
            name='gtype',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='goodinfo',
            name='gclick',
            field=models.IntegerField(default=0),
        ),
    ]
