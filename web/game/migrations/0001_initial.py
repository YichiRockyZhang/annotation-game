# Generated by Django 5.0.3 on 2024-04-18 06:34

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('group_id', models.IntegerField()),
                ('category', models.TextField(default='Everything')),
                ('content', models.TextField()),
                ('answer', models.TextField()),
                ('difficulty', models.TextField(default='HS')),
                ('subdifficulty', models.TextField(default='regular')),
                ('is_human_written', models.BooleanField()),
                ('generation_method', models.CharField(default='human', max_length=30)),
                ('clue_list', models.JSONField(blank=True, null=True)),
                ('wiki_sents', models.JSONField(blank=True, null=True)),
                ('length', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField(default=0)),
                ('correct', models.IntegerField(default=0)),
                ('negs', models.IntegerField(default=0)),
                ('locked_out', models.BooleanField(default=False)),
                ('banned', models.BooleanField(default=False)),
                ('last_seen', models.FloatField(default=0)),
                ('reported_by', models.ManyToManyField(to='game.player')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.SlugField(unique=True)),
                ('collects_feedback', models.BooleanField(default=False)),
                ('max_players', models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(0)])),
                ('state', models.CharField(choices=[('idle', 'Idle'), ('playing', 'Playing'), ('contest', 'Contest')], default='idle', max_length=9)),
                ('start_time', models.FloatField(default=0)),
                ('end_time', models.FloatField(default=1)),
                ('buzz_start_time', models.FloatField(default=0)),
                ('buzz_end_time', models.FloatField(default=1)),
                ('category', models.CharField(choices=[('Everything', 'Everything'), ('Science', 'Science'), ('History', 'History'), ('Literature', 'Literature'), ('Philosophy', 'Philosophy'), ('Religion', 'Religion'), ('Geography', 'Geography'), ('Fine Arts', 'Fine Arts'), ('Social Science', 'Social Science'), ('Mythology', 'Mythology'), ('Trash', 'Trash')], default='Everything', max_length=30)),
                ('difficulty', models.CharField(choices=[('College', 'College'), ('MS', 'MS'), ('HS', 'HS'), ('Open', 'Open')], default='HS', max_length=10)),
                ('change_locked', models.BooleanField(default=False)),
                ('speed', models.IntegerField(default=200, validators=[django.core.validators.MinValueValidator(60), django.core.validators.MaxValueValidator(600)])),
                ('buzz_player', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buzz_player', to='game.player')),
                ('current_question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='game.question')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='game.room'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, max_length=200, null=True)),
                ('tag', models.CharField(choices=[('join', 'Join'), ('leave', 'Leave'), ('buzz_init', 'Buzz Initiated'), ('buzz_correct', 'Buzz Correct'), ('buzz_wrong', 'Buzz Wrong'), ('buzz_forfeit', 'Buzz Forfeit'), ('set_category', 'Set Category'), ('set_difficulty', 'Set Difficulty'), ('reset_score', 'Reset Score'), ('chat', 'Chat')], max_length=20)),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('visible', models.BooleanField(default=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='game.player')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='game.room')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='game.user'),
        ),
        migrations.CreateModel(
            name='QuestionFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guessed_answer', models.CharField(default='', max_length=30)),
                ('guessed_generation_method', models.CharField(choices=[('human', 'Human-written'), ('ai', 'AI-generated')], max_length=30)),
                ('interestingness_rating', models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])),
                ('submitted_clue_list', models.JSONField(blank=True, null=True)),
                ('submitted_clue_order', models.JSONField(blank=True, null=True)),
                ('submitted_factual_mask_list', models.JSONField(blank=True, null=True)),
                ('inversions', models.IntegerField()),
                ('feedback_text', models.TextField(blank=True, max_length=500)),
                ('improved_question', models.TextField(max_length=500)),
                ('answered_correctly', models.BooleanField()),
                ('buzz_position_word', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('buzz_position_norm', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('buzzed', models.BooleanField(default=False)),
                ('solicit_additional_feedback', models.BooleanField(default=False)),
                ('guessed_gen_method_correctly', models.BooleanField(null=True)),
                ('initial_submission_datetime', models.DateTimeField(null=True)),
                ('additional_submission_datetime', models.DateTimeField(null=True)),
                ('is_submitted', models.BooleanField(default=False)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='game.player')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='game.question')),
            ],
            options={
                'unique_together': {('question', 'player')},
            },
        ),
    ]
