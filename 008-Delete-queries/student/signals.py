# from django.db.models.signals import pre_delete, post_delete
# from .models import Student
# from django.dispatch import receiver

# @receiver(pre_delete,sender=Student)
# def pre_delete_profile(sender,instance,**kwargs):
#         print("You are just about to delete a student!!!")
        
# @receiver(post_delete,sender=Student)
# def delete_profile(sender,instance,*args,**kwargs):
#     print("Yep, you deleted a student!!!")