from django.urls import path
from mainapp import views
from .views import detailview, addformview, editformview, RarityCategoryView, SearchList, ContactFormView, ContactResultView, weekly_legenddary_list, weekly_trend_list, weekly_features_list, weekly_standard_list, weekly_highlight_list, weekly_epic_list

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', detailview, name='detail'),
    path('detail/<int:pk>/editform/', editformview, name='editform'),
    path('addform/', addformview, name='addform'),
    path('search', SearchList, name='search'),
    path('raritycategory/<str:rarity>/', views.RarityCategoryView.as_view(), name='rarity'),
    path('positioncategory/<str:position>/', views.PositionCategoryView.as_view(), name='position'),
    path('leaguecategory/<str:leaguename>/', views.LeagueCategoryView.as_view(), name='league'),
    path('contact/', ContactFormView.as_view(), name='contact_form'),
    path('contact/result/', ContactResultView.as_view(), name='contact_result'),
    path('weekly_legendary/', weekly_legenddary_list, name='weekly_legendary'),
    path('weekly_trend/', weekly_trend_list, name='weekly_trend'),
    path('weekly_features/', weekly_features_list, name='weekly_features'),
    path('weekly_standard/', weekly_standard_list, name='weekly_standard'),
    path('weekly_highlight/', weekly_highlight_list, name='weekly_highlight'),
    path('weekly_epic/', weekly_epic_list, name='weekly_epic'),
]