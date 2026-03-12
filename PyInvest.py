import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8 ')

#entrada 

capital = float(input('capital inicial:'))
aporte = float(input('aporte mensal:'))
meses = float(input('prazo (meses):'))
cdi_anual = float(input('cdi anual %:'))/100
perc_cdb = float(input('percentual do cdi-cdb (%):'))/100
perc_lci = float(input('percentual do cdi-lci (%):'))/100
taxa_fii = float(input('rentabilidade do fii (%):'))/100
meta =float(input('meta financeira (R$):'))

#coversão do cdi
cdi_mensal = math.pow((1+cdi_anual),1/12)-1

#total investido
total_investido = capital + (aporte * meses)

#cdb
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb =(capital * math.pow((1+taxa_cdb),meses))+(aporte * meses)
lucro_cdb = montante_cdb- total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#lci/lca
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1+taxa_lci),meses))+(aporte * meses)
 
#poupança
taxa_poupanca =  0.005
montante_poupanca = (capital * math.pow((1+taxa_poupanca),meses))+(aporte * meses)
