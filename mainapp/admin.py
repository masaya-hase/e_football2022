from django.contrib import admin
from .models import RarityCategory, Player, Ability, Formation, PositionCategory, ClubCategory, LeagueCategory, Skill, PlayStyleCategory, RarityCategory, PlayStyleCategory
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from import_export.fields import Field

# Shopモデルに統合する為にModelResourceを継承したクラスを作成
class PositionCategoryResource(resources.ModelResource):
    class Meta:
        model = PositionCategory

# Costモデルに統合する為にModelResourceを継承したクラスを作成
class ClubCategoryResource(resources.ModelResource):
    league_group = Field(attribute='league_group', column_name='league_group_id',widget=ForeignKeyWidget(LeagueCategory))
    class Meta:
        model = ClubCategory
        fields = ('id','league_group' ,'clubname')
        export_order = fields

class LeagueCategoryResource(resources.ModelResource):
    class Meta:
        model = LeagueCategory

class RarityCategoryResource(resources.ModelResource):
    class Meta:
        model = RarityCategory

# Shopモデルに統合する為にModelResourceを継承したクラスを作成
class PlayStyleCategoryResource(resources.ModelResource):
    class Meta:
        model = PlayStyleCategory

# Costモデルに統合する為にModelResourceを継承したクラスを作成
class SkillResource(resources.ModelResource):
    class Meta:
        model = Skill

class PlayerResource(resources.ModelResource):
    position_group = Field(attribute='position_group', column_name='position_group_id',widget=ForeignKeyWidget(PositionCategory))
    rarity_group = Field(attribute='rarity_group', column_name='rarity_group_id',widget=ForeignKeyWidget(RarityCategory))
    club_group = Field(attribute='club_group', column_name='club_group_id',widget=ForeignKeyWidget(ClubCategory))
    league_group = Field(attribute='league_group', column_name='league_group_id',widget=ForeignKeyWidget(LeagueCategory))
    playstyle_group = Field(attribute='playstyle_group', column_name='playstyle_group_id',widget=ForeignKeyWidget(PlayStyleCategory))
    skill = Field(widget=ManyToManyWidget(Skill, field='player_skill'))

    class Meta:
        model = Player
        skip_unchanged = True
        fields = ('id', 'date', 'initial', 'maximum', 'level', 'player_name', 'country', 'age', 'height', 'dominant_foot', 'player_image', 'position_group', 'rarity_group', 'club_group', 'league_group', 'playstyle_group', 'skill')
        export_order = fields

# Shopモデルに統合する為にModelResourceを継承したクラスを作成
class AbilityResource(resources.ModelResource):
    player = Field(
        column_name='player',
        attribute='player',
        widget=ForeignKeyWidget(Player, 'player_name'))
    
    class Meta:
        model = Ability
        fields = ('id','player', 'offense_sense', 'ball_control', 'dribble', 'ball_keep', 'grander_pass', 'fly_pass', 'determining_power', 'heading', 'place_kick', 'curve', 'speed', 'instantaneous_power', 'kick_power', 'jumping', 'physical_contact', 'body_control', 'physical_fitness', 'defense_sense', 'take_the_ball', 'aggressiveness', 'gksense', 'catching', 'clearing', 'cobraging', 'deflectiveing', 'reverse_foot_frequency', 'reverse_foot_accuracy', 'condition_stability', 'injury_resistance')
        export_order = fields

# Costモデルに統合する為にModelResourceを継承したクラスを作成
class FormationResource(resources.ModelResource):
    class Meta:
        model = Formation

@admin.register(RarityCategory)
# ImportExportModelAdminを継承したadminクラスを作成
class RarityCategoryAdmin(ImportExportModelAdmin):
    ordering = ['id']
    list_display=('id', 'rarity')

    # resource_classにModelResourceを継承したクラスを設定
    resource_class = RarityCategoryResource


@admin.register(PositionCategory)
# ImportExportModelAdminを継承したadminクラスを作成
class PositionCategoryAdmin(ImportExportModelAdmin):
    ordering = ['id']
    list_display=('id', 'position')

    # resource_classにModelResourceを継承したクラスを設定
    resource_class = PositionCategoryResource


@admin.register(ClubCategory)
# ImportExportModelAdminを継承したadminクラスを作成
class ClubCategoryAdmin(ImportExportModelAdmin):
    ordering = ['id']
    list_display=('id', 'clubname')

    # resource_classにModelResourceを継承したクラスを設定
    resource_class = ClubCategoryResource

@admin.register(LeagueCategory)
# ImportExportModelAdminを継承したadminクラスを作成
class LeagueCategoryAdmin(ImportExportModelAdmin):
    ordering = ['id']
    list_display=('id', 'leaguename')

    # resource_classにModelResourceを継承したクラスを設定
    resource_class = LeagueCategoryResource


@admin.register(PlayStyleCategory)
# ImportExportModelAdminを継承したadminクラスを作成
class PlayStyleCategoryAdmin(ImportExportModelAdmin):
    ordering = ['id']
    list_display=('id', 'playstyle')

    # resource_classにModelResourceを継承したクラスを設定
    resource_class = PlayStyleCategoryResource


@admin.register(Skill)
# ImportExportModelAdminを継承したadminクラスを作成
class SkillAdmin(ImportExportModelAdmin):
    ordering = ['id']
    list_display=('id', 'player_skill')

    # resource_classにModelResourceを継承したクラスを設定
    resource_class = SkillResource

@admin.register(Player)
# ImportExportModelAdminを継承したadminクラスを作成
class PlayerImportAdmin(ImportExportModelAdmin):
    ordering = ['id']
    list_display=('id', 'date','player_name','rarity_group')
    filter_horizontal = ('skill',)
    # resource_classにModelResourceを継承したクラスを設定
    resource_class = PlayerResource



@admin.register(Ability)
# ImportExportModelAdminを継承したadminクラスを作成
class AbilityAdmin(ImportExportModelAdmin):
    ordering = ['player']
    list_display=('player', 'offense_sense', 'ball_control', 'dribble', 'ball_keep', 'grander_pass', 'fly_pass', 'determining_power', 'heading', 'place_kick', 'curve', 'speed', 'instantaneous_power', 'kick_power', 'jumping', 'physical_contact', 'body_control', 'physical_fitness', 'defense_sense', 'take_the_ball', 'aggressiveness', 'gksense', 'catching', 'clearing', 'cobraging', 'deflectiveing', 'reverse_foot_frequency', 'reverse_foot_accuracy', 'condition_stability', 'injury_resistance')

    # resource_classにModelResourceを継承したクラスを設定
    resource_class = AbilityResource


@admin.register(Formation)
# ImportExportModelAdminを継承したadminクラスを作成
class FormationAdmin(ImportExportModelAdmin):
    ordering = ['id']
    list_display=('id', 'player', 'formation_images')

    # resource_classにModelResourceを継承したクラスを設定
    resource_class = FormationResource
