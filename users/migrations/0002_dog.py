# Generated by Django 4.0.6 on 2022-07-07 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=127, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.animal')),
            ],
        ),
    ]