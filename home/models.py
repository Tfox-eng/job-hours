from django.db import models
#from django.contrib.auth.models import User


class UserPost(models.Model):
    part_number = models.CharField(max_length=500, default='')
    email = models.CharField(max_length=500)
    panel_holes_punch_qty = models.DecimalField(decimal_places=0, max_digits=500)
    panel_holes_cut_qty = models.DecimalField(decimal_places=0, max_digits=500)
    # User = models.ForeignKey('User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    panel_size_choices = [
    ('NO_PANEL', 'No Panel'),
    ('SMALL', 'Small'),
    ('MEDIUM', 'Medium'),
    ('LARGE', 'Large')]
    
    panel_size = models.CharField(max_length=10, choices=panel_size_choices, default='No Panel')

    

    
    
#class user_input(models.Model):
    
    
# class Friend(models.Model):
    # users = models.ManyToManyField(User)
    # current_user = models.ForeignKey(User, related_name='owner', null=True)

    # @classmethod
    # def make_friend(cls, current_user, new_friend):
        # friend, created = cls.objects.get_or_create(
            # current_user=current_user
        # )
        # friend.users.add(new_friend)

    # @classmethod
    # def lose_friend(cls, current_user, new_friend):
        # friend, created = cls.objects.get_or_create(
            # current_user=current_user
        # )
        # friend.users.remove(new_friend)
