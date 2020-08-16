# Generated by Django 3.0.8 on 2020-08-16 06:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='User Name')),
                ('money', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Account Balance')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Customer Name')),
                ('address', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=11, verbose_name='Phone Number')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Employee Name')),
                ('basicSalary', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('bonus', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('isPaid', models.BooleanField(default=False)),
                ('lastSalary', models.DateTimeField(verbose_name='last salary updated date')),
                ('designation', models.CharField(choices=[('Worker', 'Worker'), ('Manager', 'Manager'), ('Superviser', 'Superviser'), ('MarketingHead', 'MarketingHead'), ('Others', 'others')], default='Others', max_length=200)),
                ('address', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=11, verbose_name='Phone Number')),
                ('dob', models.DateTimeField(verbose_name='date of birth')),
                ('doj', models.DateTimeField(verbose_name='date of Joined')),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Others')], default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Product Name')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('wages', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='raw_materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Material Name')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cost of the material')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Currently Available')),
                ('make', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Product Make percentage')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Supplier Name')),
                ('address', models.CharField(max_length=70, verbose_name='Address of the supplier')),
                ('phone', models.CharField(max_length=11, verbose_name='Phone Number')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amt', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Transaction Amount')),
                ('description', models.CharField(max_length=200, verbose_name='Transaction Description')),
                ('type', models.BooleanField(verbose_name='Credit/Debit')),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='date of Transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Employee')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.raw_materials')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Products')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basicSalary', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('bonus', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('paidDate', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Date of paided')),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Odate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of Ordered')),
                ('Ddate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Delivered Date')),
                ('total_amt', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Amount')),
                ('isDelivered', models.BooleanField(default=False)),
                ('cus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Orders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Products')),
            ],
        ),
        migrations.CreateModel(
            name='materials_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.raw_materials')),
                ('sup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Supplier')),
            ],
        ),
    ]
