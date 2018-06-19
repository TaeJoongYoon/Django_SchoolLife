from django import forms
from django.contrib.auth.models import User

from .models import Department,Instructor,Course,Category,LecturePost,MarketPost,FreePost,LectureComment,MarketComment,FreeComment

class SignupForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    # 비밀번호 확인을 위한 필드
    password_Confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    # username필드의 검증에 username이 이미 사용중인지 여부 검사
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('아이디가 이미 사용중입니다')
        return username

    # password1와 password2의 값이 일치하는지 유효성 검사
    def clean_password2(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['password_Confirm']
        if password1 != password2:
            raise forms.ValidationError('비밀번호와 비밀번호 확인란의 값이 일치하지 않습니다')
        return password2

    def signup(self):
        if self.is_valid():
            return User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password']
            )


class SigninForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )


class SigninForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

class LecturePostForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        )
    )

    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
    )


    def post(self,cur_user):
        if self.is_valid():
            return LecturePost.objects.create(
                title = self.cleaned_data['title'],
                author = cur_user,
                content = self.cleaned_data['content'],
                course = self.cleaned_data['course'],
            )

class MarketPostForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        )
    )

    photo = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )


    def post(self,cur_user):
        if self.is_valid():
            return MarketPost.objects.create(
                title = self.cleaned_data['title'],
                author = cur_user,
                content = self.cleaned_data['content'],
                photo = self.cleaned_data['photo'],
            )

class FreePostForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def post(self,cur_user):
        if self.is_valid():
            return FreePost.objects.create(
                title = self.cleaned_data['title'],
                author = cur_user,
                content = self.cleaned_data['content'],
            )