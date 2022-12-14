# Generated by Django 3.2.6 on 2022-09-27 13:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumerSystem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reference', models.CharField(max_length=50, verbose_name='Consumer Reference')),
            ],
            options={
                'verbose_name': 'Consumer System',
                'verbose_name_plural': 'Consumer Systems',
            },
        ),
        migrations.CreateModel(
            name='WhatsappMessage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('to', models.CharField(max_length=15, verbose_name='Recipient Number')),
                ('type', models.CharField(default='text', max_length=5, verbose_name='Message Type')),
                ('message_body', models.CharField(max_length=1000, verbose_name='Message Body')),
                ('date_to_send', models.DateTimeField(auto_now_add=True, verbose_name='Date to Send')),
                ('was_sent', models.BooleanField(default=False, verbose_name='Was Sent?')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wpp_messages.consumersystem')),
            ],
            options={
                'verbose_name': 'Consumer System',
                'verbose_name_plural': 'Consumer Systems',
            },
        ),
    ]
