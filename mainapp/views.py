from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Player, Formation, Ability, RarityCategory, Skill, PositionCategory, LeagueCategory, PlayerFeature, PlayerCorrection
from .forms import PlayerCreateForm, AbilityFormSet, SkillInlineFormSet, FormationFormSet, SkillInlineAddFormSet, AbilityAddFormSet, FormationAddFormSet, ContactForm, PlayerFeatureFormSet, PlayerCorrectionFormSet, PlayerFeatureAddFormSet, PlayerCorrectionAddFormSet
from django.views import generic
import logging
from django.db.models import Q
from functools import reduce
from operator import and_
from django.core.paginator import Paginator
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = "mainapp/index.html"

def detailview(request, pk):
    player = Player.objects.filter(pk=pk)
    ability = Ability.objects.filter(pk=pk)
    formation = Formation.objects.filter(pk=pk)
    feature = PlayerFeature.objects.filter(pk=pk)
    correction = PlayerCorrection.objects.filter(pk=pk)
    return render(request, 'mainapp/detail.html', {'player': player, 'ability': ability, 'formation': formation, 'feature': feature, 'correction': correction})

def addformview(request):
    form = PlayerCreateForm(request.POST or None, files=request.FILES)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        player = form.save(commit=False)
        skill_formset = SkillInlineAddFormSet(
            request.POST or None, instance=player)
        ability_formset = AbilityAddFormSet(request.POST, instance=player)
        formation_formset = FormationAddFormSet(
            request.POST, files=request.FILES, instance=player)  # 増えた
        feature_formset = PlayerFeatureAddFormSet(request.POST, instance=player)
        correction_formset = PlayerCorrectionAddFormSet(request.POST, instance=player)
        if skill_formset.is_valid() and ability_formset.is_valid() and formation_formset.is_valid() and feature_formset.is_valid() and correction_formset.is_valid():  # image_formset.is_valid()が増えた
            player.save()
            skill_formset.save()
            ability_formset.save()
            formation_formset.save()  # 増えた
            feature_formset.save()  # 増えた
            correction_formset.save()  # 増えた
            return redirect('index')

        # エラーメッセージつきのformsetをテンプレートへ渡すため、contextに格納
        else:
            context['skill_formset'] = skill_formset
            context['ability_formset'] = ability_formset
            context['formation_formset'] = formation_formset  # 増えた
            context['feature_formset'] = feature_formset  # 増えた
            context['correction_formset'] = correction_formset  # 増えた

    # GETのとき
    else:
        # 空のformsetをテンプレートへ渡す
        context['skill_formset'] = SkillInlineAddFormSet()
        context['ability_formset'] = AbilityAddFormSet()
        context['formation_formset'] = FormationAddFormSet()  # 増えた
        context['feature_formset'] = PlayerFeatureAddFormSet()  # 増えた
        context['correction_formset'] = PlayerCorrectionAddFormSet()  # 増えた

    return render(request, 'mainapp/addform.html', context)


def editformview(request, pk):
    player = get_object_or_404(Player, pk=pk)
    form = PlayerCreateForm(request.POST or None,
                            files=request.FILES or None, instance=player)
    skillformset = SkillInlineFormSet(request.POST or None, instance=player)
    abilityformset = AbilityFormSet(request.POST or None, instance=player)
    formationformset = FormationFormSet(
        request.POST or None, files=request.FILES or None, instance=player)
    featureformset = PlayerFeatureFormSet(request.POST or None, instance=player)
    correctionformset = PlayerCorrectionFormSet(request.POST or None, instance=player)
    if request.method == 'POST' and form.is_valid() and skillformset.is_valid() and abilityformset.is_valid() and formationformset.is_valid() and featureformset.is_valid() and correctionformset.is_valid():
        form.save()
        skillformset.save()
        abilityformset.save()
        formationformset.save()
        featureformset.save()
        correctionformset.save()
        return redirect('index')
        
    context = {
        'form': form,
        'skillformset': skillformset,
        'abilityformset': abilityformset,
        'pk': pk,
        'formationformset': formationformset,
        'featureformset': featureformset,
        'correctionformset': correctionformset,
    }

    return render(request, 'mainapp/editform.html', context)


class RarityCategoryView(generic.ListView):
    model = Player
    paginate_by = 20
    template_name = 'mainapp/list.html'

    def get_queryset(self):
        category = RarityCategory.objects.get(rarity=self.kwargs['rarity'])
        queryset = Player.objects.order_by('-id').filter(rarity_group=category)
        return queryset

    """ アクセスされた値を取得し辞書に格納 """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rarity_key'] = self.kwargs['rarity']
        return context

class PositionCategoryView(generic.ListView):
    model = Player
    paginate_by = 20
    template_name = 'mainapp/list.html'

    def get_queryset(self):
        category = PositionCategory.objects.get(position=self.kwargs['position'])
        queryset = Player.objects.order_by('-id').filter(position_group=category)
        return queryset

    """ アクセスされた値を取得し辞書に格納 """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['position_key'] = self.kwargs['position']
        return context


class LeagueCategoryView(generic.ListView):
    model = Player
    paginate_by = 10
    template_name = 'mainapp/list.html'

    def get_queryset(self):
        category = LeagueCategory.objects.get(leaguename=self.kwargs['leaguename'])
        queryset = Player.objects.order_by('-id').filter(league_group=category)
        return queryset

    """ アクセスされた値を取得し辞書に格納 """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leaguename_key'] = self.kwargs['leaguename']
        return context

def SearchList(request):
    player_list = Player.objects.order_by('-id')
    freeword = request.GET.get('freeword')
    select = request.GET.get('select')

    if select == 'none':
        """ 除外リストを作成 """
        exclusion_list = set([' ', '　'])
        q_list = ''

        for i in freeword:
            """ 全角半角の空文字が含まれていたら無視 """
            if i in exclusion_list:
                pass
            else:
                q_list += i
        
        player_list = Player.objects.filter(Q(player_name__icontains=freeword))
        paginator = Paginator(player_list, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)    

    elif select:
        player_list = Player.objects.filter(rarity_group=select)

        """ 除外リストを作成 """
        exclusion_list = set([' ', '　'])
        q_list = ''

        for i in freeword:
            """ 全角半角の空文字が含まれていたら無視 """
            if i in exclusion_list:
                pass
            else:
                q_list += i
        
        player_list = player_list.filter(Q(player_name__icontains=freeword))
        paginator = Paginator(player_list, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    return render(request, 'mainapp/list.html', {
        'page_obj': page_obj,
        'freeword':freeword,
        'select':select,
        })

class ContactFormView(FormView):
    template_name = 'mainapp/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_result')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ContactResultView(TemplateView):
    template_name = 'mainapp/contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context

class RarityCategoryView(generic.ListView):
    model = Player
    paginate_by = 10
    template_name = 'mainapp/list.html'

    def get_queryset(self):
        category = RarityCategory.objects.get(rarity=self.kwargs['rarity'])
        queryset = Player.objects.order_by('-id').filter(rarity_group=category)
        return queryset

    """ アクセスされた値を取得し辞書に格納 """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rarity_key'] = self.kwargs['rarity']
        return context

def weekly_legenddary_list(request):
    context = {}

    date_list = Player.objects.filter(rarity_group=1).values_list('date', flat=True).reverse().first()
    player_list = Player.objects.filter(rarity_group=1 , date=date_list)

    paginator = Paginator(player_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context['page_obj'] = page_obj

    return render(request, 'mainapp/near_legendary.html' , context)

def weekly_trend_list(request):
    context = {}

    date_list = Player.objects.filter(rarity_group=3).values_list('date', flat=True).first()
    player_list = Player.objects.filter(rarity_group=3 , date=date_list)

    paginator = Paginator(player_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['page_obj'] = page_obj

    return render(request, 'mainapp/near_trend.html' , context)

def weekly_features_list(request):
    context = {}

    date_list = Player.objects.filter(rarity_group=4).values_list('date', flat=True).first()
    player_list = Player.objects.filter(rarity_group=4 , date=date_list)
    
    paginator = Paginator(player_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['page_obj'] = page_obj

    return render(request, 'mainapp/near_features.html' , context)

def weekly_standard_list(request):
    context = {}

    date_list = Player.objects.filter(rarity_group=2).values_list('date', flat=True).first()
    player_list = Player.objects.filter(rarity_group=2 , date=date_list)

    paginator = Paginator(player_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['page_obj'] = page_obj

    return render(request, 'mainapp/near_standard.html' , context)
