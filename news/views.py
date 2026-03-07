from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from .forms import NewsForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .scraper import fetch_google_news
from .article_parser import get_article_content
from .ai_utils import summarize_article
from django.http import JsonResponse
from .article_parser import get_article_content
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def index(request):
    return render(request, 'news/index.html')


def news_list(request):
    news_items = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news': news_items})


def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news_item = form.save(commit=False)
            news_item.user = request.user
            news_item.save()
            return redirect('news_list')
    else:
        form = NewsForm()

    return render(request, 'news/news_create.html', {'form': form})


@login_required
def news_edit(request, news_id):
    news_item = get_object_or_404(News, pk=news_id, user=request.user)

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news_item)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm(instance=news_item)

    return render(request, 'news/news_create.html', {'form': form})


@login_required
def news_delete(request, news_id):
    news_item = get_object_or_404(News, pk=news_id, user=request.user)

    if request.method == 'POST':
        news_item.delete()
        return redirect('news_list')

    return render(request, 'news/news_delete.html', {'news': news_item})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('news_list')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def google_news(request):
    articles = fetch_google_news()
    return render(request, 'news/google_news.html', {'articles': articles})


def article_view(request):

    url = request.GET.get("url")

    article = get_article_content(url)

    return render(request, "news/article.html", {"article": article})


tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")


def summarize_news(request):

    url = request.GET.get("url")

    article = get_article_content(url)

    summary = summarize_article(article["text"])

    return JsonResponse({"summary": summary})


def ask_ai(request):

    url = request.GET.get("url")
    question = request.GET.get("question")

    article = get_article_content(url)

    context = article["text"][:1500]

    prompt = f"Answer the question based on this article:\n{context}\n\nQuestion: {question}"

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(
        inputs["input_ids"],
        max_length=120,
        num_beams=4
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return JsonResponse({"answer": answer})
