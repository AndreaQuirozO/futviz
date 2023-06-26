import matplotlib.pyplot as plt
from data.global_stats import global_data

def get_data_lollipop():
    data = global_data()
    graph = data.loc[:,['Equipo', 'GF', 'xG', 'GC', 'xGA']]
    ordered_gf = graph.sort_values(by='GF')
    ordered_gc = graph.sort_values(by='GC', ascending=False)
    ran = range(1,len(graph.index)+1)
    return ordered_gf, ordered_gc, ran

#Comparación entre goles a favor y goles esperados a favor (desempeño ofensivo)
def lollipop_att():
    ordered_gf, ran = get_data_lollipop()
    plt.hlines(y=ran, xmin=ordered_gf['GF'], xmax=ordered_gf['xG'], color='grey', alpha=0.4)
    plt.scatter(ordered_gf['GF'], ran, color='skyblue', alpha=1, label='GF')
    plt.scatter(ordered_gf['xG'], ran, color='green', alpha=0.4 , label='xG')
    plt.legend()
    plt.yticks(ran, ordered_gf['Equipo'])
    plt.title("Comparación  GF vs xG", loc='center')
    plt.xlabel('Número de goles')

#Comparación entre goles en contra y goles esperados en contra (desempeño defensivo)
def lollipop_def():
    ordered_gc, ran = get_data_lollipop()
    plt.hlines(y=ran, xmin=ordered_gc['GC'], xmax=ordered_gc['xGA'], color='grey', alpha=0.4)
    plt.scatter(ordered_gc['GC'], ran, color='red', alpha=1, label='GC')
    plt.scatter(ordered_gc['xGA'], ran, color='grey', alpha=0.4 , label='xGA')
    plt.legend()
    plt.yticks(ran, ordered_gc['Equipo'])
    plt.title("Comparación  GC vs xGA", loc='center')
    plt.xlabel('Número de goles')