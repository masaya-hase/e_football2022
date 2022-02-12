from .models import RarityCategory, PositionCategory, ClubCategory, LeagueCategory, PlayStyleCategory, Skill

def related(request):
  rarity_data = RarityCategory.objects.all()
  position_data = PositionCategory.objects.all()
  club_data = ClubCategory.objects.all()
  league_data = LeagueCategory.objects.all()
  playstyle_data = PlayStyleCategory.objects.all()
  skill_data = Skill.objects.all()
  
  context = {
    'rarity_data' : rarity_data, 
    'position_data' : position_data,
    'club_data' : club_data,
    'league_data' : league_data,
    'playstyle_data' : playstyle_data,
    'skill_data' : skill_data,
  }
  
  return context