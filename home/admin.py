from django.contrib import admin
from home.models import Department,Instructor,Course,Category,LecturePost,MarketPost,FreePost,LectureComment,MarketComment,FreeComment

# Register your models here.
admin.site.register(Department)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(LecturePost)
admin.site.register(MarketPost)
admin.site.register(FreePost)
admin.site.register(LectureComment)
admin.site.register(MarketComment)
admin.site.register(FreeComment)