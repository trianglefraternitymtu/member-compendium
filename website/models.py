from django.db import models

class Member(models.Model):
    ACTIVE = 'AC'
    REMOTE_ALUMNUS = 'RA'
    LOCAL_ALUMNUS = 'LA'
    PLEDGE = 'PL'
    NOT_INITIATED = 'NI'
    DISASSOCIATE = 'DS'

    MEMBER_STATES = (
        (ACTIVE, 'Active Member'),
        (REMOTE_ALUMNUS, 'Alumnus'),
        (LOCAL_ALUMNUS, 'Local Alumnus'),
        (PLEDGE, 'Pledge'),
        (NOT_INITIATED, 'Not Initiated'),
        (DISASSOCIATE, 'Disassociated')
    )

    member_status = models.CharField(
        max_length=2,
        choices=MEMBER_STATES,
        default=PLEDGE,
    )
    user_id = models.CharField(editable=False, primary_key=True, max_length=21)
    started_school = models.CharField(max_length=11)
    email = models.EmailField()
    initiated = models.DateField()
    seniority_points = models.PositiveIntegerField(default=0)
    pin = models.PositiveIntegerField(default=0)
    # pledge_father = models.ForeignKey('self', on_delete=models.CASCADE)

class Webhook(models.Model):
    nonce = models.CharField(editable=False, primary_key=True, unique=True, max_length=128)
    channel = models.CharField(max_length=21)
