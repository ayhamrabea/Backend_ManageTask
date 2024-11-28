from django.db import models
from django.utils.translation import gettext as _
from django.conf.global_settings import AUTH_USER_MODEL
# Create your models here.


class ProjectStatus(models.IntegerChoices):
    PENDING = 1 , 'pending'
    COMPLETED = 2 , 'completed'
    postponed = 3 , 'postponed'
    canceled = 4 , 'canceled'


class Category(models.Model):

    name = models.CharField(_("name"), max_length=150)    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")

    def __str__(self):
        return self.name


class Project(models.Model):

    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"))
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    update_at = models.DateTimeField(_("update_at"), auto_now=True)
    status = models.IntegerField(_("status") , choices=ProjectStatus.choices , default=ProjectStatus.PENDING)
    category = models.ForeignKey(Category, verbose_name=_("project_category"), on_delete=models.PROTECT)
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_("project_user"), on_delete=models.CASCADE , null=True)
    

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.title



class Task(models.Model):

    description = models.TextField(_("description"))
    is_completed = models.BooleanField(_("is_completed") , default=False)
    project = models.ForeignKey(Project, verbose_name=_("task_project"), on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return self.is_completed
