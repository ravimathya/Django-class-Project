from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from.models import Story, Tag

# Create your views here.


def story(request):
    story_list = Story.objects.all()
    tag_list = Tag.objects.all()
    context = {
        # to dispaly in front-end, we first make list and then context by adding like story_list and tag_list
        "story_list": story_list,
        "tag_list": tag_list
    }
    return render(request, 'story/story.html', context)


def story_detail(request, slug=None):
    # Story is model and slug is used for query.
    instance = get_object_or_404(Story, slug=slug)
    context = {
        "instance": instance
    }
    return render(request, 'story/story-detail.html', context)


def story_tag(request, name=None):
    story_list = Story.objects.filter(tag__name=name)
    tag_list = Tag.objects.all()
    context = {
        "story_list": story_list,
        "name": name,
        "tag_list": tag_list

    }
    return render(request, 'story/tag-story.html', context)

    # for the form of Story


@login_required(login_url='/admin/login/')
def story_create(request):
    def storyFormHandle(request):
        received = 0
        if request.method == 'POST':
            received = 1
            form = StoryForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'You have successfully submitted the your message ')
            else:
                messages.error(
                    request, 'Error submitting your message. Please correct you informations'
                )
    context = {
        "form": StoryForm()
    }
    context = {
        "form": storyFormHandle(request)
    }
    return render(request, 'story/story-create.html', context)
