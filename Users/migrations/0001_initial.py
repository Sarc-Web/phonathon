# Generated by Django 2.2 on 2020-12-04 13:04

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.IntegerField()),
                ('year', models.IntegerField()),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_supervisor', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='worksheet',
            fields=[
                ('increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('worksh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Sheet')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ldap', models.CharField(max_length=9)),
                ('department', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('sheets', models.ManyToManyField(blank=True, related_name='allocated_sheets', to='Users.Sheet')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Alum_Detail',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=55)),
                ('contactno1', models.IntegerField()),
                ('contactno2', models.IntegerField(blank=True, null=True)),
                ('contactno3', models.IntegerField(blank=True, null=True)),
                ('contactno4', models.IntegerField(blank=True, null=True)),
                ('contactno5', models.IntegerField(blank=True, null=True)),
                ('email1', models.EmailField(max_length=60)),
                ('email2', models.EmailField(blank=True, max_length=60, null=True)),
                ('email3', models.EmailField(blank=True, max_length=60, null=True)),
                ('email4', models.EmailField(blank=True, max_length=60, null=True)),
                ('email5', models.EmailField(blank=True, max_length=60, null=True)),
                ('ilp', models.CharField(blank=True, max_length=60, null=True)),
                ('core_talks', models.CharField(blank=True, max_length=60, null=True)),
                ('MI_GD', models.CharField(blank=True, max_length=60, null=True)),
                ('Sarc_Blog', models.CharField(blank=True, max_length=60, null=True)),
                ('newsletter', models.CharField(blank=True, max_length=60, null=True)),
                ('newsletter_feedback', models.CharField(blank=True, max_length=600, null=True)),
                ('permanent_address', models.CharField(blank=True, max_length=1000, null=True)),
                ('temporary_address', models.CharField(blank=True, max_length=1000, null=True)),
                ('class_of', models.IntegerField(blank=True, null=True)),
                ('degree', models.CharField(blank=True, max_length=100, null=True)),
                ('hostelno', models.IntegerField(blank=True, null=True)),
                ('dept', models.CharField(blank=True, max_length=100, null=True)),
                ('Organization_name', models.CharField(blank=True, max_length=200, null=True)),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('working_place', models.CharField(blank=True, max_length=200, null=True)),
                ('remark', models.CharField(blank=True, max_length=600, null=True)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
                ('extra1', models.CharField(blank=True, max_length=60, null=True)),
                ('extra2', models.CharField(blank=True, max_length=60, null=True)),
                ('extra3', models.CharField(blank=True, max_length=60, null=True)),
                ('extra4', models.CharField(blank=True, max_length=60, null=True)),
                ('extra5', models.CharField(blank=True, max_length=60, null=True)),
                ('extra6', models.CharField(blank=True, max_length=60, null=True)),
                ('Alum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.worksheet')),
            ],
        ),
    ]
