from django import template

register = template.Library()


@register.filter
def of_df_fig_css(ability_point):
    if ability_point >= 95:
        return "NF"
    elif 95 > ability_point >= 85:
        return "EF"
    elif 85 > ability_point >= 75:
        return "SF"
    else:
        return "default"


@register.filter
def reverse_css(ability_point):
    if ability_point == 4:
        return "NF"
    elif ability_point == 3:
        return "EF"
    elif ability_point == 2:
        return "SF"
    else:
        return "default"


@register.filter
def condi_css(ability_point):
    if ability_point == 8:
        return "NF"
    elif 8 > ability_point >= 5:
        return "EF"
    elif 5 > ability_point >= 4:
        return "SF"
    else:
        return "default"


@register.filter
def list_css(ability_point):
    if ability_point >= 95:
        return "list_NF"
    elif 95 > ability_point >= 85:
        return "list_EF"
    elif 85 > ability_point >= 75:
        return "list_SF"
    else:
        return "list_default"

@register.filter
def list_condi_css(ability_point):
    if ability_point == 8:
        return "reverse_condi_NF"
    elif 8 > ability_point >= 5:
        return "reverse_condi_EF"
    elif 5 > ability_point >= 4:
        return "reverse_condi_SF"
    else:
        return "reverse_condi_default"

@register.filter
def list_reverse_css(ability_point):
    if ability_point == 4:
        return "reverse_condi_NF"
    elif ability_point == 3:
        return "reverse_condi_EF"
    elif ability_point == 2:
        return "reverse_condi_SF"
    else:
        return "reverse_condi_default"

@register.filter
def list_posi(position):
    if position == 'CF' or position == 'ST' or position == 'LWG' or position == 'RWG':
        return "list_CF"
    elif position == 'LSB' or position == 'CB' or position == 'RSB':
        return "list_DF"
    elif position == 'GK':
        return "list_GK"
    else:
        return "list_MF"
