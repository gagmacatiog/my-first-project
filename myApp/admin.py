from django.contrib import admin
from .models import User
from .models import student_info
from .models import familyBackground_info
from .models import educationalBackground_Info


admin.site.register(User)
admin.site.register(student_info)
admin.site.register(familyBackground_info)
admin.site.register(educationalBackground_Info)



# Register your models here.
