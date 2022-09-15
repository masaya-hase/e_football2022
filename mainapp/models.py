from django.db import migrations,models
from datetime import datetime

class RarityCategory(models.Model):
  rarity = models.CharField('レアリティ',max_length=100, blank=True, null=True)

  def __str__(self):
        return self.rarity

class PositionCategory(models.Model):
  position = models.CharField('ポジショングループ',max_length=100, blank=True, null=True)

  def __str__(self):
        return self.position

class LeagueCategory(models.Model):
  leaguename = models.CharField('リーググループ',max_length=100, blank=True, null=True)

  def __str__(self):
        return self.leaguename

class PlayStyleCategory(models.Model):
  playstyle = models.CharField('プレースタイルグループ', max_length=30, blank=True, null=True)

  def __str__(self):
        return self.playstyle

class Skill(models.Model):
    player_skill = models.CharField('スキル名', max_length=20, blank=True, null=True)

    def __str__(self):
        return self.player_skill

class ClubCategory(models.Model):
    clubname = models.CharField('クラブグループ',max_length=100, blank=True, null=True)

    def __str__(self):
            return self.clubname

class ReverseCategory(models.Model):
    reverse_level = models.CharField('逆足レベル',max_length=100, blank=True, null=True)

    def __str__(self):
            return self.reverse_level

class ConditionCategory(models.Model):
    condition_level = models.CharField('コンディションレベル',max_length=100, blank=True, null=True)

    def __str__(self):
            return self.condition_level

class InjuryCategory(models.Model):
    injury_resistance_level = models.CharField('怪我耐性レベル',max_length=100, blank=True, null=True)

    def __str__(self):
            return self.injury_resistance_level

class GradeCategory(models.Model):
    grade_level = models.CharField('グレードレベル',max_length=100, blank=True, null=True)

    def __str__(self):
            return self.grade_level

class Player(models.Model):
    date = models.DateField('リリース日',default=datetime.now)
    initial = models.IntegerField('初期総合値', blank=True, null=True)
    level = models.IntegerField('最大レベル', blank=True, null=True)
    player_name = models.CharField('選手名', max_length=50, blank=True, null=True)
    country = models.CharField('国名', max_length=30, blank=True, null=True)
    age = models.IntegerField('年齢', blank=True, null=True)
    height = models.IntegerField('身長', blank=True, null=True)
    dominant_foot = models.CharField('利き足', max_length=2, blank=True, null=True)
    player_image = models.ImageField(upload_to='images', verbose_name='プレイヤー画像', null=True, blank=True)
    position_group = models.ForeignKey(PositionCategory, verbose_name='ポジショングループ' ,on_delete=models.PROTECT, null=True)
    rarity_group = models.ForeignKey(RarityCategory, verbose_name='レアリティ' ,on_delete=models.PROTECT, null=True)
    league_group = models.ForeignKey(LeagueCategory, verbose_name='リーググループ' ,on_delete=models.PROTECT, null=True)
    club_group = models.ForeignKey(ClubCategory,verbose_name='クラブグループ',on_delete=models.PROTECT, null=True)
    playstyle_group = models.ForeignKey(PlayStyleCategory, verbose_name='プレースタイルグループ' ,on_delete=models.PROTECT, null=True)
    grade_group = models.ForeignKey(GradeCategory, verbose_name='グレードグループ' ,on_delete=models.PROTECT, null=True)
    skill = models.ManyToManyField(Skill, verbose_name='スキル', blank=True)

    def __str__(self):
        return self.player_name
    

class Ability(models.Model):
    player = models.ForeignKey(
        Player, verbose_name='紐づき選手',
        blank=True, null=True,
        on_delete=models.SET_NULL
        )
    offense_sense = models.IntegerField('OFセンス', blank=True, null=True)
    ball_control = models.IntegerField('ボールコントロール', blank=True, null=True)
    dribble = models.IntegerField('ドリブル', blank=True, null=True)
    ball_keep = models.IntegerField('ボールキープ', blank=True, null=True)
    grander_pass = models.IntegerField('グランダーパス', blank=True, null=True)
    fly_pass = models.IntegerField('フライパス', blank=True, null=True)
    determining_power = models.IntegerField('決定力', blank=True, null=True)
    heading = models.IntegerField('ヘディング', blank=True, null=True)
    place_kick = models.IntegerField('プレースキック', blank=True, null=True)
    curve = models.IntegerField('カーブ', blank=True, null=True)
    speed = models.IntegerField('スピード', blank=True, null=True)
    instantaneous_power = models.IntegerField('瞬発力', blank=True, null=True)
    kick_power = models.IntegerField('キック力', blank=True, null=True)
    jumping = models.IntegerField('ジャンプ', blank=True, null=True)
    physical_contact = models.IntegerField('フィジカルコンタクト', blank=True, null=True)
    body_control = models.IntegerField('ボディコントロール', blank=True, null=True)
    physical_fitness = models.IntegerField('体力', blank=True, null=True)
    defense_sense = models.IntegerField('ディフェンスセンス', blank=True, null=True)
    take_the_ball = models.IntegerField('ボール奪取', blank=True, null=True)
    aggressiveness = models.IntegerField('アグレッシブネス', blank=True, null=True)
    defensive_consciousness = models.IntegerField('守備意識', blank=True, null=True)
    gksense = models.IntegerField('GKセンス', blank=True, null=True)
    catching = models.IntegerField('キャッチング', blank=True, null=True)
    clearing = models.IntegerField('クリアリング', blank=True, null=True)
    cobraging = models.IntegerField('コブラシング', blank=True, null=True)
    deflectiveing = models.IntegerField('ディフレクティング', blank=True, null=True)

class ColorCategory(models.Model):
    color = models.CharField('カラー', max_length=30, blank=True, null=True)
    def __str__(self):
        return self.color

class FormationColor(models.Model):
    player = models.ForeignKey(
        Player, verbose_name='紐づき選手',
        blank=True, null=True,
        on_delete=models.SET_NULL
        )
    lwg_position_color = models.ForeignKey(ColorCategory, verbose_name='LWGポジションカラー' ,on_delete=models.PROTECT, blank=True, null=True, related_name="lwg_position")
    lwg_opacity = models.FloatField('LWG透明度', blank=True, null=True)
    cf_position_color = models.ForeignKey(ColorCategory, verbose_name='CFポジションカラー' ,on_delete=models.PROTECT, blank=True, null=True, related_name="cf_position")
    cf_opacity = models.FloatField('CF透明度', blank=True, null=True)
    st_position_color = models.ForeignKey(ColorCategory, verbose_name='STポジションカラー' ,on_delete=models.PROTECT, blank=True, null=True, related_name="st_position")
    st_opacity = models.FloatField('ST透明度', blank=True, null=True)
    rwg_position_color = models.ForeignKey(ColorCategory, verbose_name='RWGポジションカラー' ,on_delete=models.PROTECT, blank=True, null=True, related_name="rwg_position")
    rwg_opacity = models.FloatField('RWG透明度', blank=True, null=True)
    lmf_position_color = models.ForeignKey(ColorCategory, verbose_name='LMFポジションカラー' ,on_delete=models.PROTECT, blank=True, null=True, related_name="lmf_position")
    lmf_opacity = models.FloatField('LMF透明度', blank=True, null=True)
    omf_position_color = models.ForeignKey(ColorCategory, verbose_name='OMFポジションカラー' ,on_delete=models.PROTECT, blank=True, null=True, related_name="omf_position")
    omf_opacity = models.FloatField('OMF透明度', blank=True, null=True)
    cmf_position_color = models.ForeignKey(ColorCategory, verbose_name='CMFポジションカラー' ,on_delete=models.PROTECT, blank=True, null=True, related_name="cmf_position")
    cmf_opacity = models.FloatField('CMF透明度', blank=True, null=True)
    dmf_position_color = models.ForeignKey(ColorCategory, verbose_name='DMFポジションカラー' ,on_delete=models.PROTECT, blank=True, null=True, related_name="dmf_position")
    dmf_opacity = models.FloatField('DMF透明度', blank=True, null=True)
    rmf_position_color = models.ForeignKey(ColorCategory, verbose_name='RMFポジションカラー' ,on_delete=models.PROTECT, blank=True, null=True, related_name="rmf_position")
    rmf_opacity = models.FloatField('RMF透明度', blank=True, null=True)
    lsb_position_color = models.ForeignKey(ColorCategory, verbose_name='LSBポジションカラー' ,on_delete=models.PROTECT, blank=True, null=True, related_name="lsb_position")
    lsb_opacity = models.FloatField('LSB透明度', blank=True, null=True)
    cb_position_color = models.ForeignKey(ColorCategory, verbose_name='CBポジションカラー' ,on_delete=models.PROTECT, blank=True, null=True, related_name="cb_position")
    cb_opacity = models.FloatField('CB透明度', blank=True, null=True)
    rsb_position_color = models.ForeignKey(ColorCategory, verbose_name='RSBポジションカラー' ,on_delete=models.PROTECT, blank=True, null=True, related_name="rsb_position")
    rsb_opacity = models.FloatField('RSB透明度', blank=True, null=True)
    gk_position_color = models.ForeignKey(ColorCategory, verbose_name='GKポジションカラー' ,on_delete=models.PROTECT, blank=True, null=True, related_name="gk_position")
    gk_opacity = models.FloatField('GK透明度', blank=True, null=True)

class PlayerFeature(models.Model):
    player = models.ForeignKey(
        Player, verbose_name='紐づき選手',
        blank=True, null=True,
        on_delete=models.SET_NULL
        )

    frequency_choice = models.ForeignKey(ReverseCategory, verbose_name='逆足頻度' ,on_delete=models.PROTECT, null=True, related_name="frequency_item")
    accuracy_choice = models.ForeignKey(ReverseCategory, verbose_name='逆足精度' ,on_delete=models.PROTECT, null=True, related_name="accuracy_item")
    condition_choice = models.ForeignKey(ConditionCategory, verbose_name='コンディションの波' ,on_delete=models.PROTECT, null=True)
    injury_resistance_choice = models.ForeignKey(InjuryCategory, verbose_name='怪我耐性' ,on_delete=models.PROTECT, null=True)

class PlayerCorrection(models.Model):
    player = models.ForeignKey(
        Player, verbose_name='紐づき選手',
        blank=True, null=True,
        on_delete=models.SET_NULL
        )
    position_correction = models.IntegerField('ポジション', blank=True, null=True)
    short_counter_correction = models.IntegerField('ショートカウンター', blank=True, null=True)
    long_counter_correction = models.IntegerField('ロングカウンター', blank=True, null=True)
    side_attack_correction = models.IntegerField('サイドアタック', blank=True, null=True)
    long_ball_correction = models.IntegerField('ロングボール', blank=True, null=True)