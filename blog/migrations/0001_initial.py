# Generated by Django 3.2.4 on 2021-06-04 10:24

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类名称')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类管理',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
                ('path', models.CharField(max_length=255, verbose_name='链接')),
                ('desc', mdeditor.fields.MDTextField(verbose_name='描述')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '友链',
                'verbose_name_plural': '友链管理',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='文章标题')),
                ('content', mdeditor.fields.MDTextField(verbose_name='文章内容')),
                ('文章状态,1 置顶显示 2正常显示 3 不显示', models.IntegerField(default=1, verbose_name='文章状态')),
                ('reading', models.IntegerField(default=0, verbose_name='阅读量')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章管理',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='网站标题')),
                ('desc', mdeditor.fields.MDTextField(verbose_name='网站描述')),
                ('icon', models.FileField(upload_to='./media/', verbose_name='网站图标')),
                ('start', models.TimeField(auto_now_add=True, verbose_name='网站开始运行时间')),
            ],
            options={
                'verbose_name': '设置',
                'verbose_name_plural': '系统设置',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=60, verbose_name='昵称')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='邮箱')),
                ('cr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.comment')),
                ('pid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pid', to='blog.post')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论管理',
            },
        ),
    ]