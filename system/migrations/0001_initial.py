# Generated by Django 3.0.6 on 2020-08-02 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('linkToRegister', models.CharField(max_length=255)),
                ('image', models.ImageField(default='event_images/event_placeholder.png', upload_to='event_images/')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='EventGoer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatName', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('numOfRecommended', models.IntegerField(default=0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Event')),
                ('eventBuddy', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.EventGoer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=1000)),
                ('quantity', models.IntegerField(default=0)),
                ('pointsNeeded', models.IntegerField(default=1)),
                ('image', models.ImageField(default='rewards_images/reward_placeholder.svg', upload_to='rewards_images/')),
            ],
        ),
        migrations.CreateModel(
            name='RewardWithdrawer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fulfilled', models.BooleanField(default=False)),
                ('reward', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.Reward')),
                ('withdrawer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='RecommendedPerson',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('ipAddress', models.CharField(max_length=40)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('recommendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.EventGoer')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('chatName', models.CharField(max_length=255)),
                ('timeSent', models.DateTimeField(auto_now_add=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
