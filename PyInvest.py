import math 
import random 
import datetime 
import statistics
import locale 

locale.setlocale(locale.LC_ALL,"pt_BR.UTF-8")

#Entrada
capital = float(input("Capital Inicial: "))
aporte = float(input("Aporte Mensal: "))
meses = float(input("Prazo (meses): "))
cdi_anual = float(input("CDI anual %: "))/100
perc_cdb = float(input("Percetual CDI - CDB (%): "))/100
perc_lci = float (input("Percetual do CDI  - LCI (%): "))/100
taxa_fii = float(input("Rentabilidade do FII (%): "))/100
meta = float(input("Meta financeira (R$): "))

#conversão CDI
cdi_mensal = math.pow((1+cdi_anual), 1/12) - 1

#total investido
total_investido = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1+taxa_cdb), meses))+(aporte * meses)
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1+taxa_lci),meses))+(aporte * meses)

#poupança
taxa_poupanca = 0.005
montante_poupanca = (capital * math.pow((1+taxa_poupanca),meses))+(aporte*meses)

#FII
fii_base = (capital * math.pow((1 + taxa_fii), meses)) + (aporte * ((math.pow((1 + taxa_fii), meses) - 1) / taxa_fii))

ffi_1 = fii_base * (1+random.uniform(-0.03, 0.03))
ffi_2 = fii_base * (1+random.uniform(-0.03, 0.03))
ffi_3 = fii_base * (1+random.uniform(-0.03, 0.03))
ffi_4 = fii_base * (1+random.uniform(-0.03, 0.03))
ffi_5 = fii_base * (1+random.uniform(-0.03, 0.03))

media_fii = statistics.mean([ffi_1,ffi_2,ffi_3,ffi_4,ffi_5])
mediana_fii = statistics.median([ffi_1,ffi_2,ffi_3,ffi_4,ffi_5])
desvio_fii = statistics.stdev([ffi_1,ffi_2,ffi_3,ffi_4,ffi_5])
montante_fii = media_fii

#data
hoje = datetime.date.today()
data_resgate = hoje + datetime.timedelta(days=30 * meses)

#gráfico
bloco_cdb = "█" * int(montante_cdb_liquido / 1000)
bloco_lci = "█" * int(montante_lci / 1000)
bloco_poup = "█" * int(montante_poupanca / 1000)
bloco_fii = "█" * int(montante_fii / 1000)

#meta
meta_atingida = (montante_cdb_liquido >= meta or montante_lci >= meta or montante_poupanca >= meta or montante_fii >= meta)

#relatório
print("=" * 38)
print("PyInvest - Simulador de Investimentos")
print("=" * 38)
print("Data da simulação:", hoje.strftime('%d/%m/%Y'))
print("Data estimada de resgate:", data_resgate.strftime('%d/%m/%Y'))
print("=" * 38)

print("Total investido:", locale.currency(total_investido, grouping=True))
print("--- RESULTADOS FINANCEIROS ---")

print("CDB:", locale.currency(montante_cdb_liquido, grouping=True))
print(bloco_cdb)

print("LCI/LCA:", locale.currency(montante_lci, grouping=True))
print(bloco_lci)

print("Poupança:", locale.currency(montante_poupanca, grouping=True))
print(bloco_poup)

print("FII (média):", locale.currency(montante_fii, grouping=True))
print(bloco_fii)

print("--- ESTATÍSTICAS FII ---")
print("Mediana:", locale.currency(mediana_fii, grouping=True))
print("Desvio padrão:", locale.currency(desvio_fii, grouping=True))

print("Meta atingida:", meta_atingida)
print("=" * 38)