# Generated by Django 3.1.6 on 2021-04-04 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('u_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=500)),
                ('reviews', models.CharField(max_length=1000)),
                ('res_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.restuarantinformation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.review')),
            ],
        ),
    ]