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

class Player(models.Model):
    date = models.DateField('リリース日',default=datetime.now)
    initial = models.IntegerField('初期総合値', blank=True, null=True)
    maximum = models.IntegerField('最大総合値', blank=True, null=True)
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
    gksense = models.IntegerField('GKセンス', blank=True, null=True)
    catching = models.IntegerField('キャッチング', blank=True, null=True)
    clearing = models.IntegerField('クリアリング', blank=True, null=True)
    cobraging = models.IntegerField('コブラシング', blank=True, null=True)
    deflectiveing = models.IntegerField('ディフレクティング', blank=True, null=True)
    reverse_foot_frequency = models.IntegerField('逆足頻度', blank=True, null=True)
    reverse_foot_accuracy = models.IntegerField('逆足精度', blank=True, null=True)
    condition_stability = models.IntegerField('コンディション安定度', blank=True, null=True)
    injury_resistance = models.IntegerField('ケガ耐性', blank=True, null=True)

class Formation(models.Model):
    player = models.ForeignKey(
        Player, verbose_name='紐づき選手',
        blank=True, null=True,
        on_delete=models.SET_NULL
        )
    formation_images = models.ImageField(upload_to='images', verbose_name='フォーメーション画像', null=True, blank=True)


