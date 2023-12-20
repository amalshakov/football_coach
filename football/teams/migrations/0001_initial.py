# Generated by Django 3.2 on 2023-12-20 08:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formation_home', models.CharField(choices=[('a', '4-4-2'), ('b', '3-5-2'), ('c', '3-4-3'), ('d', '4-5-1')], max_length=1)),
                ('tactics_home', models.CharField(choices=[('з', 'защитная'), ('н', 'нормальная'), ('а', 'атакующая')], max_length=1)),
                ('style_home', models.CharField(choices=[('нрм', 'нормальный'), ('ббг', 'бей-беги'), ('брт', 'британский'), ('ктч', 'катеначчо'), ('спк', 'спартаковский'), ('брз', 'бразильский'), ('ттк', 'тики-така')], max_length=3)),
                ('protection_home', models.CharField(choices=[('и', 'по игроку'), ('з', 'зональный')], max_length=1)),
                ('mood_home', models.CharField(choices=[('о', 'отдых'), ('с', 'супер')], max_length=1)),
                ('score', models.CharField(max_length=255)),
                ('formation_guest', models.CharField(choices=[('a', '4-4-2'), ('b', '3-5-2'), ('c', '3-4-3'), ('d', '4-5-1')], max_length=1)),
                ('tactics_guest', models.CharField(choices=[('з', 'защитная'), ('н', 'нормальная'), ('а', 'атакующая')], max_length=1)),
                ('style_guest', models.CharField(choices=[('нрм', 'нормальный'), ('ббг', 'бей-беги'), ('брт', 'британский'), ('ктч', 'катеначчо'), ('спк', 'спартаковский'), ('брз', 'бразильский'), ('ттк', 'тики-така')], max_length=3)),
                ('protection_guest', models.CharField(choices=[('и', 'по игроку'), ('з', 'зональный')], max_length=1)),
                ('mood_guest', models.CharField(choices=[('о', 'отдых'), ('с', 'супер')], max_length=1)),
                ('position1_home', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position2_home', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position3_home', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position4_home', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position5_home', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position6_home', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position7_home', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position8_home', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position9_home', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position10_home', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position11_home', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position1_guest', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position2_guest', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position3_guest', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position4_guest', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position5_guest', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position6_guest', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position7_guest', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position8_guest', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position9_guest', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position10_guest', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
                ('position11_guest', models.CharField(choices=[('GK', 'вратарь'), ('LD', 'левый защитник'), ('CD', 'центральный защитник'), ('RD', 'правый защитник'), ('LM', 'левый полузащитник'), ('CM', 'центральный полузащитник'), ('RM', 'правый полузащитник'), ('CF', 'центральный нападающий')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Футболист')),
                ('age', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(40, 'Сделай помоложе'), django.core.validators.MinValueValidator(16, 'Сделай постарше')], verbose_name='Возраст футболиста')),
                ('power', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(50, 'Слишком сильный'), django.core.validators.MinValueValidator(10, 'Слишком слабый')], verbose_name='Сила футболиста')),
                ('cost', models.PositiveIntegerField(verbose_name='Цена футболиста')),
                ('position', models.CharField(choices=[('ВР', 'Вратарь'), ('ЗЩ', 'Защитник'), ('ПЗ', 'Полузащитник'), ('НП', 'Нападающий')], max_length=2)),
                ('country', models.CharField(choices=[('RU', 'Россия'), ('EN', 'Англия')], max_length=2)),
                ('fatigue', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='Усталость футболиста')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название команды')),
                ('city', models.CharField(max_length=255, verbose_name='Команда из города')),
                ('emblem', models.ImageField(blank=True, null=True, upload_to='teams/', verbose_name='Эмблема клуба')),
                ('stadium', models.CharField(max_length=255, verbose_name='Название стадиона команды')),
                ('capacity', models.PositiveIntegerField(default=3500, verbose_name='Вместимость стадиона')),
            ],
        ),
    ]
