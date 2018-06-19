# Generated by Django 2.0.6 on 2018-06-19 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0002_emailtemplate_last_used_date'),
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emails', to='templates.EmailTemplate', verbose_name='email template'),
        ),
        migrations.AddField(
            model_name='email',
            name='template_content',
            field=models.TextField(blank=True, verbose_name='email template content'),
        ),
    ]
