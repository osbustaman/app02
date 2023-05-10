from django.db import models
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel

from applications.base.models import Client


# Create your models here.
class Inquist(TimeStampedModel):

    OPTIONS = (
        (1, 'active'),
        (2, 'off'),
    )

    IS = (
        (1, 'yes'),
        (2, 'no'),
    )

    inq_id = models.AutoField("Key", primary_key=True)
    inq_code = models.CharField("code survey", max_length=25)
    inq_title = models.CharField("title inquist", max_length=150)
    inq_name = models.CharField("name inquist", max_length=150)
    inq_initdate = models.DateTimeField("date start inquist")
    inq_finishdate = models.DateTimeField("date finish inquist")
    client = models.ForeignKey(Client, verbose_name="Client", on_delete=models.PROTECT, db_column="inq_client_id")
    inq_status = models.IntegerField("status inquist", choices=OPTIONS, default=0)
    inq_tokens = models.IntegerField("inquist from login?", choices=IS, default=1)
    inq_languaje = models.CharField("language inquist", max_length=150, null=True, blank=True)
    inq_private = models.IntegerField("inquist is private?", choices=IS, default=1)
    inq_timelimit = models.IntegerField("time limit in minutes", default=0)
    inq_responseporcentage = models.IntegerField("percentage survey carried out", default=0)

    def __int__(self):
        return self.inq_id

    def save(self, *args, **kwargs):
        super(Inquist, self).save(*args, **kwargs)

    class Meta:
        db_table = 'inq_inquist'
        ordering = ['inq_id']

class GroupQuestions(TimeStampedModel):

    gq_id = models.AutoField("Key", primary_key=True)
    gq_title = models.CharField("title group questions", max_length=150)
    gq_description = models.TextField("description group questions")

    def __int__(self):
        return self.gq_id

    def save(self, *args, **kwargs):
        super(GroupQuestions, self).save(*args, **kwargs)

    class Meta:
        db_table = 'inq_group_questions'
        ordering = ['gq_id']

class TypeQuestion(TimeStampedModel):

    tq_id = models.AutoField("Key", primary_key=True)
    tq_nametype = models.CharField("type questions", max_length=150)

    def __int__(self):
        return self.tq_id

    def save(self, *args, **kwargs):
        super(TypeQuestion, self).save(*args, **kwargs)

    class Meta:
        db_table = 'inq_type_question'
        ordering = ['tq_id']

class InquistUser(TimeStampedModel):

    OPTIONS = (
        (1, 'active'),
        (2, 'off'),
    )

    inus_id = models.AutoField("Key", primary_key=True)
    user = models.ForeignKey(User, verbose_name="User", db_column="inus_user", on_delete=models.PROTECT)
    inquist = models.ForeignKey(Inquist, verbose_name="Inquist", on_delete=models.PROTECT, db_column="inus_inquist_id")
    inus_status = models.IntegerField("status user in the survey", choices=OPTIONS, default=0)
    inus_initdate = models.DateTimeField("date start inquist user", null=True, blank=True)
    inus_finishdate = models.DateTimeField("date finish inquist user", null=True, blank=True)

    def __int__(self):
        return self.inus_id

    def save(self, *args, **kwargs):
        super(InquistUser, self).save(*args, **kwargs)

    class Meta:
        db_table = 'inq_inquist_user'
        ordering = ['inus_id']

class Question(TimeStampedModel):

    OPTIONS = (
        (1, 'active'),
        (2, 'off'),
    )

    IS = (
        (1, 'yes'),
        (2, 'no'),
    )

    qt_id = models.AutoField("Key", primary_key=True)
    qt_question = models.TextField("question")
    qt_score = models.FloatField("score question", blank=True, null=True, default=0)
    inquist = models.ForeignKey(Inquist, verbose_name="Inquist", on_delete=models.PROTECT, db_column="qt_inquist_id")
    groupQuestions = models.ForeignKey(GroupQuestions, verbose_name="GroupQuestions", on_delete=models.PROTECT, db_column="qt_group_questions_id")
    typeQuestion = models.ForeignKey(TypeQuestion, verbose_name="TypeQuestion", on_delete=models.PROTECT, db_column="qt_type_question_id")
    qt_notlikely = models.CharField("not like (only for questions of the rating scale, Likert scale, differential semantic scale and dichotomous type)", max_length=255, blank=True, null=True)
    qt_verlikely = models.CharField("very like (only for questions of the rating scale, Likert scale, differential semantic scale and dichotomous type)", max_length=255, blank=True, null=True)
    qt_helpquestion = models.IntegerField("question have help?", choices=IS, default=2)
    qt_helpquestiontext = models.TextField("help questions", blank=True, null=True)
    
    def __int__(self):
        return self.qt_id

    def save(self, *args, **kwargs):
        super(Question, self).save(*args, **kwargs)

    class Meta:
        db_table = 'inq_question'
        ordering = ['qt_id']

class AnswerQuestion(TimeStampedModel):

    IS = (
        (1, 'yes'),
        (2, 'no'),
    )

    aq_id = models.AutoField("Key", primary_key=True)
    question = models.ForeignKey(Question, verbose_name="Question", on_delete=models.PROTECT, db_column="aq_questions_id")
    aq_number = models.IntegerField("number question")
    aq_description = models.TextField("descriptions answer questions")
    aq_other = models.TextField("have textbox", choices=IS, default=2)

    def __int__(self):
        return self.aq_id

    def save(self, *args, **kwargs):
        super(AnswerQuestion, self).save(*args, **kwargs)

    class Meta:
        db_table = 'inq_answer_question'
        ordering = ['aq_id']

class AnswerUser(TimeStampedModel):

    IS = (
        (1, 'yes'),
        (2, 'no'),
    )

    aq_id = models.AutoField("Key", primary_key=True)
    client = models.ForeignKey(Client, verbose_name="Client", on_delete=models.PROTECT, db_column="au_client_id")
    user = models.ForeignKey(User, verbose_name="User", db_column="au_user_id", on_delete=models.PROTECT)
    question = models.ForeignKey(Question, verbose_name="Question", on_delete=models.PROTECT, db_column="au_questions_id")
    typeQuestion = models.ForeignKey(TypeQuestion, verbose_name="TypeQuestion", on_delete=models.PROTECT, db_column="au_type_question_id")
    answerQuestion = models.ForeignKey(AnswerQuestion, verbose_name="AnswerQuestion", on_delete=models.PROTECT, db_column="au_answer_question_id")
    au_answeruserother = models.TextField("response answer questions others")

    def __int__(self):
        return self.aq_id

    def save(self, *args, **kwargs):
        super(AnswerQuestion, self).save(*args, **kwargs)

    class Meta:
        db_table = 'inq_answer_user'
        ordering = ['aq_id']