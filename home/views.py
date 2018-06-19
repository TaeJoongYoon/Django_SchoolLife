from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from home.forms import SignupForm, SigninForm, LecturePostForm, MarketPostForm, FreePostForm
from home.models import Category, LecturePost, MarketPost, FreePost, LectureComment, MarketComment, FreeComment


def index(request):
    categories = Category.objects.all()
    """
    SELECT *
    FROM Category
    """

    return render(request, 'home/index.html', {'categories': categories})

def lecture(request):
    posts = LecturePost.objects.all().order_by('-created_at')
    """
    SELECT *
    FROM LecturePost
    """

    return render(request, 'home/lecture.html', {'posts': posts})


def market(request):
    posts = MarketPost.objects.all().order_by('-created_at')
    """
    SELECT *
    FROM MarketPost
    """


    return render(request, 'home/market.html', {'posts': posts})


def free(request):
    posts = FreePost.objects.all().order_by('-created_at')
    """
    SELECT *
    FROM FreePost
    """


    return render(request, 'home/free.html', {'posts': posts})

def register(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.signup()
            login(request, new_user)
            """
            INSERT INTO User VALUES(...)
            """

            return redirect('home:main')
        else:
            return HttpResponse('회원가입 실패. 다시 시도 해보세요.')


    else:
        form = SignupForm()
        context = {
            'form' : form,
        }
    return render(request, "home/register.html", context)

def signin(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:main')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')

    else:
        form = SigninForm()
        context = {
            'form' : form,
        }
    return render(request, "home/login.html", context)

def signout(request):
    logout(request)
    return redirect('home:main')

def lecturePost(request):
    if not request.user.is_authenticated:
        return redirect('home:signin')

    else:
        if request.method == "POST":
            form = LecturePostForm(request.POST)
            if form.is_valid():
                cur_user = request.user
                new_post = form.post(cur_user)
                """
                INSERT INTO LecturePost VALUES(...)
                """

                return redirect('home:lecture')
            else:
                return HttpResponse('실패. 다시 시도 해보세요.')

        else:
            form = LecturePostForm()
            context = {
                'form': form,
            }
        return render(request, "home/lecturePost.html", context)

def marketPost(request):

    if not request.user.is_authenticated:
        return redirect('home:signin')

    else:
        if request.method == "POST":
            form = MarketPostForm(request.POST)
            if form.is_valid():
                cur_user = request.user
                new_post = form.post(cur_user)
                """
                INSERT INTO MarketPost VALUES(...)
                """

                return redirect('home:market')
            else:
                return HttpResponse('실패. 다시 시도 해보세요.')

        else:
            form = MarketPostForm()
            context = {
                'form': form,
            }
        return render(request, "home/marketPost.html", context)

def freePost(request):

    if not request.user.is_authenticated:
        return redirect('home:signin')

    else:
        if request.method == "POST":
            form = FreePostForm(request.POST)
            if form.is_valid():
                cur_user = request.user
                new_post = form.post(cur_user)
                """
                INSERT INTO FreePost VALUES(...)
                """

                return redirect('home:free')
            else:
                return HttpResponse('실패. 다시 시도 해보세요.')

        else:
            form = FreePostForm()
            context = {
                'form': form,
            }
        return render(request, "home/freePost.html", context)

def lectureDetail(request,l_id):
    lectureContent = LecturePost.objects.filter(id = l_id)
    comments = LectureComment.objects.filter(post = l_id)
    """
    SELECT *
    FROM LecturePost, LectureComment
    WHERE LecturePost.id = l_id, LectureComment.post_id = l_id
    """

    context = {
        'lectures' : lectureContent,
        'comments' : comments
    }
    return render(request, "home/lectureDetail.html", context)

def marketDetail(request,l_id):
    marketContent = MarketPost.objects.filter(id = l_id)
    comments = MarketComment.objects.filter(post=l_id)
    """
    SELECT *
    FROM MarketPost, MarketComment
    WHERE MarketPost.id = l_id, MarketComment.post_id = l_id
    """

    context = {
        'markets': marketContent,
        'comments': comments
    }
    return render(request, "home/marketDetail.html", context)

def freeDetail(request,l_id):
    freeContent = FreePost.objects.filter(id = l_id)
    comments = FreeComment.objects.filter(post=l_id)
    """
    SELECT *
    FROM FreePost, FreeComment
    WHERE FreePost.id = l_id, FreeComment.post_id = l_id
    """

    context = {
        'frees': freeContent,
        'comments': comments
    }
    return render(request, "home/freeDetail.html", context)

def lectureComment(request):
    l_id = request.POST['post_id']
    lecture = LecturePost.objects.get(id=l_id)
    author = request.user
    content = request.POST['content']

    new_comment = LectureComment(post=lecture, author=author, content=content)
    new_comment.save()
    """
    INSERT INTO LectureComment VALUES(...) 
    """

    return redirect('home:lectureDetail',l_id = l_id)

def marketComment(request):
    l_id = request.POST['post_id']
    market = MarketPost.objects.get(id=l_id)
    author = request.user
    content = request.POST['content']

    new_comment = MarketComment(post=market, author=author, content=content)
    new_comment.save()
    """
    INSERT INTO MarketComment VALUES(...) 
    """

    return redirect('home:marketDetail', l_id=l_id)

def freeComment(request):
    l_id = request.POST['post_id']
    free = FreePost.objects.get(id=l_id)
    author = request.user
    content = request.POST['content']

    new_comment = FreeComment(post=free, author=author, content=content)
    new_comment.save()
    """
    INSERT INTO FreeCommet VALUES(...) 
    """

    return redirect('home:freeDetail', l_id=l_id)

def lectureSearch(request):
    lectureTitle = request.POST['lecture']
    lectures = LecturePost.objects.filter(course__title__icontains=lectureTitle)
    """
    SELECT *
    FROM LecturePost, Course
    WHERE LecturePost.course_id = Course.id and Course.title LIKE '%lectureTitle%';
    """

    return render(request, 'home/lecture.html', {'posts': lectures})