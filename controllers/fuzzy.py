import numpy as np
import skfuzzy as fuzz
from app.controllers import soalController
from skfuzzy import control as ctrl
from app.models.percentile import Percentile

# Antecedents
ach = ctrl.Antecedent(np.arange(0, 28, 1), 'ach')
deff = ctrl.Antecedent(np.arange(0, 28, 1), 'deff')
ord  = ctrl.Antecedent(np.arange(0, 28, 1), 'ord')
exh = ctrl.Antecedent(np.arange(0, 28, 1), 'exh')
aut = ctrl.Antecedent(np.arange(0, 28, 1), 'aut')
aff  = ctrl.Antecedent(np.arange(0, 28, 1), 'aff')
intt = ctrl.Antecedent(np.arange(0, 28, 1), 'intt')
suc = ctrl.Antecedent(np.arange(0, 28, 1), 'suc')
dom  = ctrl.Antecedent(np.arange(0, 28, 1), 'dom')
aba = ctrl.Antecedent(np.arange(0, 28, 1), 'aba')
nur = ctrl.Antecedent(np.arange(0, 28, 1), 'nur')
chg  = ctrl.Antecedent(np.arange(0, 28, 1), 'chg')
end = ctrl.Antecedent(np.arange(0, 28, 1), 'end')
het = ctrl.Antecedent(np.arange(0, 28, 1), 'het')
agg  = ctrl.Antecedent(np.arange(0, 28, 1), 'agg')

# Consequents
res = ctrl.Consequent(np.arange(0, 28, 1), 'result')

# ach memberships
ach['Rendah'] = fuzz.trapmf(ach.universe, [5,7,8,11])
ach['Rata-Rata'] = fuzz.trimf(ach.universe, [10,15,19])
ach['Tinggi'] = fuzz.trimf(ach.universe, [18,19,22])
# deff memberships
deff['Rendah'] = fuzz.trimf(deff.universe, [6, 7, 10])
deff['Rata-Rata'] = fuzz.trimf(deff.universe, [9, 14, 18])
deff['Tinggi'] = fuzz.trimf(deff.universe, [17, 18, 21])
# ord memberships
ord['Rendah'] = fuzz.trapmf(ord.universe, [5,7,8,10])
ord['Rata-Rata'] = fuzz.trimf(ord.universe, [9,15,20])
ord['Tinggi'] = fuzz.trapmf(ord.universe, [19,21,22,24])
# exh memberships
exh['Rendah'] = fuzz.trapmf(exh.universe, [3,4,8,9])
exh['Rata-Rata'] = fuzz.trapmf(exh.universe, [8,9,16,17])
exh['Tinggi'] = fuzz.trapmf(exh.universe, [16,17,22,23])
# aut memberships
aut['Rendah'] = fuzz.trapmf(aut.universe, [3,4,9,10])
aut['Rata-Rata'] = fuzz.trapmf(aut.universe, [9,10,18,19])
aut['Tinggi'] = fuzz.trapmf(aut.universe, [18,19,24,25])
# aff memberships
aff['Rendah'] = fuzz.trapmf(aff.universe, [4,5,9,10])
aff['Rata-Rata'] = fuzz.trapmf(aff.universe, [9,10,18,19])
aff['Tinggi'] = fuzz.trapmf(aff.universe, [18,19,24,25])
# int memberships
intt['Rendah'] = fuzz.trapmf(intt.universe, [3,4,9,10])
intt['Rata-Rata'] = fuzz.trapmf(intt.universe, [9,10,18,19])
intt['Tinggi'] = fuzz.trapmf(intt.universe, [18,19,24,25])
# suc memberships
suc['Rendah'] = fuzz.trapmf(suc.universe, [0,1,5,6])
suc['Rata-Rata'] = fuzz.trapmf(suc.universe, [5,6,15,16])
suc['Tinggi'] = fuzz.trapmf(suc.universe, [15,16,23,24])
#dom memberships
dom['Rendah'] = fuzz.trapmf(dom.universe, [2,3,8,9])
dom['Rata-Rata'] = fuzz.trapmf(dom.universe, [8,9,19,20])
dom['Tinggi'] = fuzz.trapmf(dom.universe, [19,20,26,27])
# aba memberships
aba['Rendah'] = fuzz.trapmf(aba.universe, [2,3,8,9])
aba['Rata-Rata'] = fuzz.trapmf(aba.universe, [8,9,19,20])
aba['Tinggi'] = fuzz.trapmf(aba.universe, [19,20,25,26])
# nur memberships
nur['Rendah'] = fuzz.trapmf(nur.universe, [4,5,10,11])
nur['Rata-Rata'] = fuzz.trapmf(nur.universe, [10,11,20,21])
nur['Tinggi'] = fuzz.trapmf(nur.universe, [20,21,26,27])
# chg memberships
chg['Rendah'] = fuzz.trapmf(chg.universe, [2,3,8,9])
chg['Rata-Rata'] = fuzz.trapmf(chg.universe, [8,9,18,19])
chg['Tinggi'] = fuzz.trapmf(chg.universe, [18,19,25,26])
# end memberships
end['Rendah'] = fuzz.trapmf(end.universe, [4,5,11,12])
end['Rata-Rata'] = fuzz.trapmf(end.universe, [11,12,21,22])
end['Tinggi'] = fuzz.trapmf(end.universe, [21,22,27,28])
# het memberships
het['Rendah'] = fuzz.trapmf(het.universe, [0,1,2,3])
het['Rata-Rata'] = fuzz.trapmf(het.universe, [2,3,19,20])
het['Tinggi'] = fuzz.trapmf(het.universe, [19,20,28,29])
# agg memberships
agg['Rendah'] = fuzz.trapmf(agg.universe, [2,3,8,9])
agg['Rata-Rata'] = fuzz.trapmf(agg.universe, [8,9,17,18])
agg['Tinggi'] = fuzz.trapmf(agg.universe, [17,18,24,25])
# result memberships
res['Rekomendasi Pekerjaan'] = fuzz.trimf(ord.universe, [85, 90, 99])
res['Tidak Ada Rekomendasi Pekerjaan'] = fuzz.trimf(ord.universe, [0, 84, 84])

# Rule system
rule1 = ctrl.Rule(ach['Tinggi'] and deff['Rendah'] and ord['Rendah'] and exh['Rendah'] and aut['Rendah'] and aff['Rendah'] and intt['Rendah'] and suc['Rendah'] and dom['Rendah'] and aba['Rendah'] and nur['Rendah'] and chg['Rendah'] and end['Rendah'] and het['Rendah'] and agg['Rendah'], res['Rekomendasi Pekerjaan'])
rule2 = ctrl.Rule(ach['Rendah'] and deff['Tinggi'] and ord['Rendah'] and exh['Rendah'] and aut['Rendah'] and aff['Rendah'] and intt['Rendah'] and suc['Rendah'] and dom['Rendah'] and aba['Rendah'] and nur['Rendah'] and chg['Rendah'] and end['Rendah'] and het['Rendah'] and agg['Rendah'], res['Rekomendasi Pekerjaan'])
rule3 = ctrl.Rule(ach['Rendah'] and deff['Rendah'] and ord['Tinggi'] and exh['Rendah'] and aut['Rendah'] and aff['Rendah'] and intt['Rendah'] and suc['Rendah'] and dom['Rendah'] and aba['Rendah'] and nur['Rendah'] and chg['Rendah'] and end['Rendah'] and het['Rendah'] and agg['Rendah'], res['Rekomendasi Pekerjaan'])
rule4 = ctrl.Rule(ach['Rendah'] and deff['Rendah'] and ord['Rendah'] and exh['Tinggi'] and aut['Rendah'] and aff['Rendah'] and intt['Rendah'] and suc['Rendah'] and dom['Rendah'] and aba['Rendah'] and nur['Rendah'] and chg['Rendah'] and end['Rendah'] and het['Rendah'] and agg['Rendah'], res['Rekomendasi Pekerjaan'])
rule5 = ctrl.Rule(ach['Rendah'] and deff['Rendah'] and ord['Rendah'] and exh['Rendah'] and aut['Tinggi'] and aff['Rendah'] and intt['Rendah'] and suc['Rendah'] and dom['Rendah'] and aba['Rendah'] and nur['Rendah'] and chg['Rendah'] and end['Rendah'] and het['Rendah'] and agg['Rendah'], res['Rekomendasi Pekerjaan'])
rule6 = ctrl.Rule(ach['Rendah'] and deff['Rendah'] and ord['Rendah'] and exh['Rendah'] and aut['Rendah'] and aff['Tinggi'] and intt['Rendah'] and suc['Rendah'] and dom['Rendah'] and aba['Rendah'] and nur['Rendah'] and chg['Rendah'] and end['Rendah'] and het['Rendah'] and agg['Rendah'], res['Rekomendasi Pekerjaan'])
rule7 = ctrl.Rule(ach['Rendah'] and deff['Rendah'] and ord['Rendah'] and exh['Rendah'] and aut['Rendah'] and aff['Rendah'] and intt['Tinggi'] and suc['Rendah'] and dom['Rendah'] and aba['Rendah'] and nur['Rendah'] and chg['Rendah'] and end['Rendah'] and het['Rendah'] and agg['Rendah'], res['Rekomendasi Pekerjaan'])
rule8 = ctrl.Rule(ach['Rendah'] and deff['Rendah'] and ord['Rendah'] and exh['Rendah'] and aut['Rendah'] and aff['Rendah'] and intt['Rendah'] and suc['Tinggi'] and dom['Rendah'] and aba['Rendah'] and nur['Rendah'] and chg['Rendah'] and end['Rendah'] and het['Rendah'] and agg['Rendah'], res['Rekomendasi Pekerjaan'])
rule9 = ctrl.Rule(ach['Rendah'] and deff['Rendah'] and ord['Rendah'] and exh['Rendah'] and aut['Rendah'] and aff['Rendah'] and intt['Rendah'] and suc['Rendah'] and dom['Tinggi'] and aba['Rendah'] and nur['Rendah'] and chg['Rendah'] and end['Rendah'] and het['Rendah'] and agg['Rendah'], res['Rekomendasi Pekerjaan'])
rule10 = ctrl.Rule(ach['Rendah'] and deff['Rendah'] and ord['Rendah'] and exh['Rendah'] and aut['Rendah'] and aff['Rendah'] and intt['Rendah'] and suc['Rendah'] and dom['Rendah'] and aba['Tinggi'] and nur['Rendah'] and chg['Rendah'] and end['Rendah'] and het['Rendah'] and agg['Rendah'], res['Rekomendasi Pekerjaan'])
rule11 = ctrl.Rule(ach['Rendah'] and deff['Rendah'] and ord['Rendah'] and exh['Rendah'] and aut['Rendah'] and aff['Rendah'] and intt['Rendah'] and suc['Rendah'] and dom['Rendah'] and aba['Rendah'] and nur['Tinggi'] and chg['Rendah'] and end['Rendah'] and het['Rendah'] and agg['Rendah'], res['Rekomendasi Pekerjaan'])
rule12 = ctrl.Rule(ach['Rendah'] and deff['Rendah'] and ord['Rendah'] and exh['Rendah'] and aut['Rendah'] and aff['Rendah'] and intt['Rendah'] and suc['Rendah'] and dom['Rendah'] and aba['Rendah'] and nur['Rendah'] and chg['Tinggi'] and end['Rendah'] and het['Rendah'] and agg['Rendah'], res['Rekomendasi Pekerjaan'])
rule13 = ctrl.Rule(ach['Rendah'] and deff['Rendah'] and ord['Rendah'] and exh['Rendah'] and aut['Rendah'] and aff['Rendah'] and intt['Rendah'] and suc['Rendah'] and dom['Rendah'] and aba['Rendah'] and nur['Rendah'] and chg['Rendah'] and end['Tinggi'] and het['Rendah'] and agg['Rendah'], res['Rekomendasi Pekerjaan'])
rule14 = ctrl.Rule(ach['Rendah'] and deff['Rendah'] and ord['Rendah'] and exh['Rendah'] and aut['Rendah'] and aff['Rendah'] and intt['Rendah'] and suc['Rendah'] and dom['Rendah'] and aba['Rendah'] and nur['Rendah'] and chg['Rendah'] and end['Rendah'] and het['Tinggi'] and agg['Rendah'], res['Rekomendasi Pekerjaan'])
rule15 = ctrl.Rule(ach['Rendah'] and deff['Rendah'] and ord['Rendah'] and exh['Rendah'] and aut['Rendah'] and aff['Rendah'] and intt['Rendah'] and suc['Rendah'] and dom['Rendah'] and aba['Rendah'] and nur['Rendah'] and chg['Rendah'] and end['Rendah'] and het['Rendah'] and agg['Tinggi'], res['Rekomendasi Pekerjaan'])
rule16 = ctrl.Rule(ach['Rendah'] and deff['Rendah'] and ord['Rendah'] and exh['Rendah'] and aut['Rendah'] and aff['Rendah'] and intt['Rendah'] and suc['Rendah'] and dom['Rendah'] and aba['Rendah'] and nur['Rendah'] and chg['Rendah'] and end['Rendah'] and het['Rendah'] and agg['Rendah'], res['Tidak Ada Rekomendasi Pekerjaan'])
rule17 = ctrl.Rule(ach['Rata-Rata'] and deff['Rata-Rata'] and ord['Rata-Rata'] and exh['Rata-Rata'] and aut['Rata-Rata'] and aff['Rata-Rata'] and intt['Rata-Rata'] and suc['Rata-Rata'] and dom['Rata-Rata'] and aba['Rata-Rata'] and nur['Rata-Rata'] and chg['Rata-Rata'] and end['Rata-Rata'] and het['Rata-Rata'] and agg['Rata-Rata'], res['Tidak Ada Rekomendasi Pekerjaan'])
rule18 = ctrl.Rule(ach['Tinggi'] and deff['Rata-Rata'] and ord['Rata-Rata'] and exh['Rata-Rata'] and aut['Rata-Rata'] and aff['Rata-Rata'] and intt['Rata-Rata'] and suc['Rata-Rata'] and dom['Rata-Rata'] and aba['Rata-Rata'] and nur['Rata-Rata'] and chg['Rata-Rata'] and end['Rata-Rata'] and het['Rata-Rata'] and agg['Rata-Rata'], res['Rekomendasi Pekerjaan'])
rule19 = ctrl.Rule(ach['Rata-Rata'] and deff['Tinggi'] and ord['Rata-Rata'] and exh['Rata-Rata'] and aut['Rata-Rata'] and aff['Rata-Rata'] and intt['Rata-Rata'] and suc['Rata-Rata'] and dom['Rata-Rata'] and aba['Rata-Rata'] and nur['Rata-Rata'] and chg['Rata-Rata'] and end['Rata-Rata'] and het['Rata-Rata'] and agg['Rata-Rata'], res['Rekomendasi Pekerjaan'])
rule20 = ctrl.Rule(ach['Rata-Rata'] and deff['Rata-Rata'] and ord['Tinggi'] and exh['Rata-Rata'] and aut['Rata-Rata'] and aff['Rata-Rata'] and intt['Rata-Rata'] and suc['Rata-Rata'] and dom['Rata-Rata'] and aba['Rata-Rata'] and nur['Rata-Rata'] and chg['Rata-Rata'] and end['Rata-Rata'] and het['Rata-Rata'] and agg['Rata-Rata'], res['Rekomendasi Pekerjaan'])
rule21 = ctrl.Rule(ach['Rata-Rata'] and deff['Rata-Rata'] and ord['Rata-Rata'] and exh['Tinggi'] and aut['Rata-Rata'] and aff['Rata-Rata'] and intt['Rata-Rata'] and suc['Rata-Rata'] and dom['Rata-Rata'] and aba['Rata-Rata'] and nur['Rata-Rata'] and chg['Rata-Rata'] and end['Rata-Rata'] and het['Rata-Rata'] and agg['Rata-Rata'], res['Rekomendasi Pekerjaan'])
rule22 = ctrl.Rule(ach['Rata-Rata'] and deff['Rata-Rata'] and ord['Rata-Rata'] and exh['Rata-Rata'] and aut['Tinggi'] and aff['Rata-Rata'] and intt['Rata-Rata'] and suc['Rata-Rata'] and dom['Rata-Rata'] and aba['Rata-Rata'] and nur['Rata-Rata'] and chg['Rata-Rata'] and end['Rata-Rata'] and het['Rata-Rata'] and agg['Rata-Rata'], res['Rekomendasi Pekerjaan'])
rule23 = ctrl.Rule(ach['Rata-Rata'] and deff['Rata-Rata'] and ord['Rata-Rata'] and exh['Rata-Rata'] and aut['Rata-Rata'] and aff['Tinggi'] and intt['Rata-Rata'] and suc['Rata-Rata'] and dom['Rata-Rata'] and aba['Rata-Rata'] and nur['Rata-Rata'] and chg['Rata-Rata'] and end['Rata-Rata'] and het['Rata-Rata'] and agg['Rata-Rata'], res['Rekomendasi Pekerjaan'])
rule24 = ctrl.Rule(ach['Rata-Rata'] and deff['Rata-Rata'] and ord['Rata-Rata'] and exh['Rata-Rata'] and aut['Rata-Rata'] and aff['Rata-Rata'] and intt['Tinggi'] and suc['Rata-Rata'] and dom['Rata-Rata'] and aba['Rata-Rata'] and nur['Rata-Rata'] and chg['Rata-Rata'] and end['Rata-Rata'] and het['Rata-Rata'] and agg['Rata-Rata'], res['Rekomendasi Pekerjaan'])
rule25 = ctrl.Rule(ach['Rata-Rata'] and deff['Rata-Rata'] and ord['Rata-Rata'] and exh['Rata-Rata'] and aut['Rata-Rata'] and aff['Rata-Rata'] and intt['Rata-Rata'] and suc['Tinggi'] and dom['Rata-Rata'] and aba['Rata-Rata'] and nur['Rata-Rata'] and chg['Rata-Rata'] and end['Rata-Rata'] and het['Rata-Rata'] and agg['Rata-Rata'], res['Rekomendasi Pekerjaan'])
rule26 = ctrl.Rule(ach['Rata-Rata'] and deff['Rata-Rata'] and ord['Rata-Rata'] and exh['Rata-Rata'] and aut['Rata-Rata'] and aff['Rata-Rata'] and intt['Rata-Rata'] and suc['Rata-Rata'] and dom['Tinggi'] and aba['Rata-Rata'] and nur['Rata-Rata'] and chg['Rata-Rata'] and end['Rata-Rata'] and het['Rata-Rata'] and agg['Rata-Rata'], res['Rekomendasi Pekerjaan'])
rule27 = ctrl.Rule(ach['Rata-Rata'] and deff['Rata-Rata'] and ord['Rata-Rata'] and exh['Rata-Rata'] and aut['Rata-Rata'] and aff['Rata-Rata'] and intt['Rata-Rata'] and suc['Rata-Rata'] and dom['Rata-Rata'] and aba['Tinggi'] and nur['Rata-Rata'] and chg['Rata-Rata'] and end['Rata-Rata'] and het['Rata-Rata'] and agg['Rata-Rata'], res['Rekomendasi Pekerjaan'])
rule28 = ctrl.Rule(ach['Rata-Rata'] and deff['Rata-Rata'] and ord['Rata-Rata'] and exh['Rata-Rata'] and aut['Rata-Rata'] and aff['Rata-Rata'] and intt['Rata-Rata'] and suc['Rata-Rata'] and dom['Rata-Rata'] and aba['Rata-Rata'] and nur['Tinggi'] and chg['Rata-Rata'] and end['Rata-Rata'] and het['Rata-Rata'] and agg['Rata-Rata'], res['Rekomendasi Pekerjaan'])
rule29 = ctrl.Rule(ach['Rata-Rata'] and deff['Rata-Rata'] and ord['Rata-Rata'] and exh['Rata-Rata'] and aut['Rata-Rata'] and aff['Rata-Rata'] and intt['Rata-Rata'] and suc['Rata-Rata'] and dom['Rata-Rata'] and aba['Rata-Rata'] and nur['Rata-Rata'] and chg['Tinggi'] and end['Rata-Rata'] and het['Rata-Rata'] and agg['Rata-Rata'], res['Rekomendasi Pekerjaan'])
rule30 = ctrl.Rule(ach['Rata-Rata'] and deff['Rata-Rata'] and ord['Rata-Rata'] and exh['Rata-Rata'] and aut['Rata-Rata'] and aff['Rata-Rata'] and intt['Rata-Rata'] and suc['Rata-Rata'] and dom['Rata-Rata'] and aba['Rata-Rata'] and nur['Rata-Rata'] and chg['Rata-Rata'] and end['Tinggi'] and het['Rata-Rata'] and agg['Rata-Rata'], res['Rekomendasi Pekerjaan'])
rule31 = ctrl.Rule(ach['Rata-Rata'] and deff['Rata-Rata'] and ord['Rata-Rata'] and exh['Rata-Rata'] and aut['Rata-Rata'] and aff['Rata-Rata'] and intt['Rata-Rata'] and suc['Rata-Rata'] and dom['Rata-Rata'] and aba['Rata-Rata'] and nur['Rata-Rata'] and chg['Rata-Rata'] and end['Rata-Rata'] and het['Tinggi'] and agg['Rata-Rata'], res['Rekomendasi Pekerjaan'])
rule32 = ctrl.Rule(ach['Rata-Rata'] and deff['Rata-Rata'] and ord['Rata-Rata'] and exh['Rata-Rata'] and aut['Rata-Rata'] and aff['Rata-Rata'] and intt['Rata-Rata'] and suc['Rata-Rata'] and dom['Rata-Rata'] and aba['Rata-Rata'] and nur['Rata-Rata'] and chg['Rata-Rata'] and end['Rata-Rata'] and het['Rata-Rata'] and agg['Tinggi'], res['Rekomendasi Pekerjaan'])

res_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4,rule5, rule6, rule7, rule8,rule9, rule10, rule11, rule12,rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32])
res_output = ctrl.ControlSystemSimulation(res_ctrl)



# def hasil_klasifikasi():
#     data = Percentile.query.all()
#     for data in data:
#         #nilai hasil tes
#         ach_a = soalController.ach_hasiltes()
#         ach_b = soalController.ach1_hasiltes()
#         ach_fix = ach_a + ach_b
#         DEF_a = soalController.DEF_hasiltes()
#         DEF_b = soalController.DEF1_hasiltes()
#         DEF_fix = DEF_a + DEF_b
#         ord_a = soalController.ord_hasiltes()
#         ord_b = soalController.ord1_hasiltes()
#         ord_fix = ord_a + ord_b
#         exh_a = soalController.exh_hasiltes()
#         exh_b = soalController.exh1_hasiltes()
#         exh_fix = exh_a + exh_b
#         aut_a = soalController.aut_hasiltes()
#         aut_b = soalController.aut1_hasiltes()
#         aut_fix = aut_a + aut_b
#         aff_a = soalController.aff_hasiltes()
#         aff_b = soalController.aff1_hasiltes()
#         aff_fix = aff_a + aff_b
#         int_a = soalController.int_hasiltes()
#         int_b = soalController.int1_hasiltes()
#         int_fix = int_a + int_b
#         suc_a = soalController.suc_hasiltes()
#         suc_b = soalController.suc1_hasiltes()
#         suc_fix = suc_a + suc_b
#         dom_a = soalController.dom_hasiltes()
#         dom_b = soalController.dom1_hasiltes()
#         dom_fix = dom_a + dom_b
#         aba_a = soalController.aba_hasiltes()
#         aba_b = soalController.aba1_hasiltes()
#         aba_fix = aba_a + aba_b
#         nur_a = soalController.nur_hasiltes()
#         nur_b = soalController.nur1_hasiltes()
#         nur_fix = nur_a + nur_b
#         chg_a = soalController.chg_hasiltes()
#         chg_b = soalController.chg1_hasiltes()
#         chg_fix = chg_a + chg_b
#         end_a = soalController.end_hasiltes()
#         end_b = soalController.end1_hasiltes()
#         end_fix = end_a + end_b
#         het_a = soalController.het_hasiltes()
#         het_b = soalController.het1_hasiltes()
#         het_fix = het_a + het_b
#         agg_a = soalController.agg_hasiltes()
#         agg_b = soalController.agg1_hasiltes()
#         agg_fix = agg_a + agg_b

#     if ach_fix == data.score:

#         if ach_fix >= 19 and DEF_fix < 18 and ord_fix < 20 and exh_fix < 17 and aut_fix < 19 and aff_fix < 19 and int_fix < 19 and suc_fix < 16 and dom_fix < 20 and aba_fix < 19 and nur_fix < 21 and chg_fix < 19 and end_fix < 22 and het_fix < 20 and agg_fix < 18:
#             posisi = "Manager"
#         if ach_fix < 19 and DEF_fix >= 18 and ord_fix < 20 and exh_fix < 17 and aut_fix < 19 and aff_fix < 19 and int_fix < 19 and suc_fix < 16 and dom_fix < 20 and aba_fix < 19 and nur_fix < 21 and chg_fix < 19 and end_fix < 22 and het_fix < 20 and agg_fix < 18:
#             posisi = "Personal Staff"
#         if ach_fix < 19 and DEF_fix < 18 and ord_fix >= 20 and exh_fix < 17 and aut_fix < 19 and aff_fix < 19 and int_fix < 19 and suc_fix < 16 and dom_fix < 20 and aba_fix < 19 and nur_fix < 21 and chg_fix < 19 and end_fix < 22 and het_fix < 20 and agg_fix < 18:
#             posisi = "Office Staff"
#         if ach_fix < 19 and DEF_fix < 18 and ord_fix < 20 and exh_fix >= 17 and aut_fix < 19 and aff_fix < 19 and int_fix < 19 and suc_fix < 16 and dom_fix < 20 and aba_fix < 19 and nur_fix < 21 and chg_fix < 19 and end_fix < 22 and het_fix < 20 and agg_fix < 18:
#             posisi = "Sales Management"
#         if ach_fix < 19 and DEF_fix < 18 and ord_fix < 20 and exh_fix < 17 and aut_fix >= 19 and aff_fix < 19 and int_fix < 19 and suc_fix < 16 and dom_fix < 20 and aba_fix < 19 and nur_fix < 21 and chg_fix < 19 and end_fix < 22 and het_fix < 20 and agg_fix < 18:
#             posisi = "Sales Management"
#         if ach_fix < 19 and DEF_fix < 18 and ord_fix < 20 and exh_fix < 17 and aut_fix < 19 and aff_fix >= 19 and int_fix < 19 and suc_fix < 16 and dom_fix < 20 and aba_fix < 19 and nur_fix < 21 and chg_fix < 19 and end_fix < 22 and het_fix < 20 and agg_fix < 18:
#             posisi = "Team Leader"
#         if ach_fix < 19 and DEF_fix < 18 and ord_fix < 20 and exh_fix < 17 and aut_fix < 19 and aff_fix < 19 and int_fix >= 19 and suc_fix < 16 and dom_fix < 20 and aba_fix < 19 and nur_fix < 21 and chg_fix < 19 and end_fix < 22 and het_fix < 20 and agg_fix < 18:
#             posisi = "Team Leader"
#         if ach_fix < 19 and DEF_fix < 18 and ord_fix < 20 and exh_fix < 17 and aut_fix < 19 and aff_fix < 19 and int_fix < 19 and suc_fix >= 16 and dom_fix < 20 and aba_fix < 19 and nur_fix < 21 and chg_fix < 19 and end_fix < 22 and het_fix < 20 and agg_fix < 18:
#             posisi = "Management Personalia"
#         if ach_fix < 19 and DEF_fix < 18 and ord_fix < 20 and exh_fix < 17 and aut_fix < 19 and aff_fix < 19 and int_fix < 19 and suc_fix < 16 and dom_fix >= 20 and aba_fix < 19 and nur_fix < 21 and chg_fix < 19 and end_fix < 22 and het_fix < 20 and agg_fix < 18:
#             posisi = "Sales Management"
#         if ach_fix < 19 and DEF_fix < 18 and ord_fix < 20 and exh_fix < 17 and aut_fix < 19 and aff_fix < 19 and int_fix < 19 and suc_fix < 16 and dom_fix < 20 and aba_fix >= 19 and nur_fix < 21 and chg_fix < 19 and end_fix < 22 and het_fix < 20 and agg_fix < 18:
#             posisi = "Regional Staff"
#         if ach_fix < 19 and DEF_fix < 18 and ord_fix < 20 and exh_fix < 17 and aut_fix < 19 and aff_fix < 19 and int_fix < 19 and suc_fix < 16 and dom_fix < 20 and aba_fix < 19 and nur_fix >= 21 and chg_fix < 19 and end_fix < 22 and het_fix < 20 and agg_fix < 18:
#             posisi = "Office Staff / Customer Service"
#         if ach_fix < 19 and DEF_fix < 18 and ord_fix < 20 and exh_fix < 17 and aut_fix < 19 and aff_fix < 19 and int_fix < 19 and suc_fix < 16 and dom_fix < 20 and aba_fix < 19 and nur_fix < 21 and chg_fix >= 19 and end_fix < 22 and het_fix < 20 and agg_fix < 18:
#             posisi = "Sales Management / Customer Service"
#         if ach_fix < 19 and DEF_fix < 18 and ord_fix < 20 and exh_fix < 17 and aut_fix < 19 and aff_fix < 19 and int_fix < 19 and suc_fix < 16 and dom_fix < 20 and aba_fix < 19 and nur_fix < 21 and chg_fix < 19 and end_fix >= 22 and het_fix < 20 and agg_fix < 18:
#             posisi = "Team Leader"
#         if ach_fix < 19 and DEF_fix < 18 and ord_fix < 20 and exh_fix < 17 and aut_fix < 19 and aff_fix < 19 and int_fix < 19 and suc_fix < 16 and dom_fix < 20 and aba_fix < 19 and nur_fix < 21 and chg_fix < 19 and end_fix < 22 and het_fix >= 20 and agg_fix < 18:
#             posisi = "Sales Management"
#         if ach_fix < 19 and DEF_fix < 18 and ord_fix < 20 and exh_fix < 17 and aut_fix < 19 and aff_fix < 19 and int_fix < 19 and suc_fix < 16 and dom_fix < 20 and aba_fix < 19 and nur_fix < 21 and chg_fix < 19 and end_fix < 22 and het_fix < 20 and agg_fix >= 18:
#             posisi = "Regional Staff"
#         else:
#             posisi = "Tidak Ada Rekomendasi"
#         pekerjaan = [ach_fix, posisi]
#         return pekerjaan



21# Enter values to test
def hasil_klasifikasi():
    ach_value = soalController.hitung_persentil_ach()
    deff_value = soalController.hitung_persentil_DEF()
    ord_value = soalController.hitung_persentil_ord()
    exh_value = soalController.hitung_persentil_exh()
    aut_value = soalController.hitung_persentil_aut()
    aff_value = soalController.hitung_persentil_aff()
    intt_value = soalController.hitung_persentil_int()
    suc_value = soalController.hitung_persentil_suc()
    dom_value = soalController.hitung_persentil_dom()
    aba_value = soalController.hitung_persentil_aba()
    nur_value = soalController.hitung_persentil_nur()
    chg_value = soalController.hitung_persentil_chg()
    end_value = soalController.hitung_persentil_end()
    het_value = soalController.hitung_persentil_het()
    agg_value = soalController.hitung_persentil_agg()



    res_output.output['ach'] = ach_value
    res_output.output['deff'] = deff_value
    res_output.output['ord'] = ord_value
    res_output.output['exh'] = exh_value
    res_output.output['aut'] = aut_value
    res_output.output['aff'] = aff_value
    res_output.output['intt'] = intt_value
    res_output.output['suc'] = suc_value
    res_output.output['dom'] = dom_value
    res_output.output['aba'] = aba_value
    res_output.output['nur'] = nur_value
    res_output.output['chg'] = chg_value
    res_output.output['end'] = end_value
    res_output.output['het'] = het_value
    res_output.output['agg'] = agg_value

# res_output.compute()


# Print output result
    if (res_output.output['ach'] >= 85 and res_output.output['deff'] < 85 and res_output.output['ord'] < 85 and res_output.output['exh'] < 85 and res_output.output['aut'] < 85 and res_output.output['aff'] < 85 and res_output.output['intt'] < 85 and res_output.output['suc'] < 85 and res_output.output['dom'] < 85 and res_output.output['aba'] < 85 and res_output.output['nur'] < 85 and res_output.output['chg'] < 85 and res_output.output['end'] < 85 and res_output.output['het'] < 85 and res_output.output['agg'] < 85):
        posisi = 'Manager'
    elif (res_output.output['ach'] < 85 and res_output.output['deff'] >= 85 and res_output.output['ord'] < 85 and res_output.output['exh'] < 85 and res_output.output['aut'] < 85 and res_output.output['aff'] < 85 and res_output.output['intt'] < 85 and res_output.output['suc'] < 85 and res_output.output['dom'] < 85 and res_output.output['aba'] < 85 and res_output.output['nur'] < 85 and res_output.output['chg'] < 85 and res_output.output['end'] < 85 and res_output.output['het'] < 85 and res_output.output['agg'] < 85):
        posisi = 'Personal Staff'
    elif (res_output.output['ach'] < 85 and res_output.output['deff'] < 85 and res_output.output['ord'] >= 85 and res_output.output['exh'] < 85 and res_output.output['aut'] < 85 and res_output.output['aff'] < 85 and res_output.output['intt'] < 85 and res_output.output['suc'] < 85 and res_output.output['dom'] < 85 and res_output.output['aba'] < 85 and res_output.output['nur'] < 85 and res_output.output['chg'] < 85 and res_output.output['end'] < 85 and res_output.output['het'] < 85 and res_output.output['agg'] < 85):
        posisi = 'Office Staff'
    elif (res_output.output['ach'] < 85 and res_output.output['deff'] < 85 and res_output.output['ord'] < 85 and res_output.output['exh'] >= 85 and res_output.output['aut'] < 85 and res_output.output['aff'] < 85 and res_output.output['intt'] < 85 and res_output.output['suc'] < 85 and res_output.output['dom'] < 85 and res_output.output['aba'] < 85 and res_output.output['nur'] < 85 and res_output.output['chg'] < 85 and res_output.output['end'] < 85 and res_output.output['het'] < 85 and res_output.output['agg'] < 85):
        posisi = 'Sales Management'
    elif (res_output.output['ach'] < 85 and res_output.output['deff'] < 85 and res_output.output['ord'] < 85 and res_output.output['exh'] < 85 and res_output.output['aut'] >= 85 and res_output.output['aff'] < 85 and res_output.output['intt'] < 85 and res_output.output['suc'] < 85 and res_output.output['dom'] < 85 and res_output.output['aba'] < 85 and res_output.output['nur'] < 85 and res_output.output['chg'] < 85 and res_output.output['end'] < 85 and res_output.output['het'] < 85 and res_output.output['agg'] < 85):
        posisi = 'Sales Management'
    elif (res_output.output['ach'] < 85 and res_output.output['deff'] < 85 and res_output.output['ord'] < 85 and res_output.output['exh'] < 85 and res_output.output['aut'] < 85 and res_output.output['aff'] >= 85 and res_output.output['intt'] < 85 and res_output.output['suc'] < 85 and res_output.output['dom'] < 85 and res_output.output['aba'] < 85 and res_output.output['nur'] < 85 and res_output.output['chg'] < 85 and res_output.output['end'] < 85 and res_output.output['het'] < 85 and res_output.output['agg'] < 85):
        posisi = 'Team Leader'
    elif (res_output.output['ach'] < 85 and res_output.output['deff'] < 85 and res_output.output['ord'] < 85 and res_output.output['exh'] < 85 and res_output.output['aut'] < 85 and res_output.output['aff'] < 85 and res_output.output['intt'] >= 85 and res_output.output['suc'] < 85 and res_output.output['dom'] < 85 and res_output.output['aba'] < 85 and res_output.output['nur'] < 85 and res_output.output['chg'] < 85 and res_output.output['end'] < 85 and res_output.output['het'] < 85 and res_output.output['agg'] < 85):
        posisi = 'Team Leader'
    elif (res_output.output['ach'] < 85 and res_output.output['deff'] < 85 and res_output.output['ord'] < 85 and res_output.output['exh'] < 85 and res_output.output['aut'] < 85 and res_output.output['aff'] < 85 and res_output.output['intt'] < 85 and res_output.output['suc'] >= 85 and res_output.output['dom'] < 85 and res_output.output['aba'] < 85 and res_output.output['nur'] < 85 and res_output.output['chg'] < 85 and res_output.output['end'] < 85 and res_output.output['het'] < 85 and res_output.output['agg'] < 85):
        posisi = 'Management Personalia'
    elif (res_output.output['ach'] < 85 and res_output.output['deff'] < 85 and res_output.output['ord'] < 85 and res_output.output['exh'] < 85 and res_output.output['aut'] < 85 and res_output.output['aff'] < 85 and res_output.output['intt'] < 85 and res_output.output['suc'] < 85 and res_output.output['dom'] >= 85 and res_output.output['aba'] < 85 and res_output.output['nur'] < 85 and res_output.output['chg'] < 85 and res_output.output['end'] < 85 and res_output.output['het'] < 85 and res_output.output['agg'] < 85):
        posisi = 'Sales Management'
    elif (res_output.output['ach'] < 85 and res_output.output['deff'] < 85 and res_output.output['ord'] < 85 and res_output.output['exh'] < 85 and res_output.output['aut'] < 85 and res_output.output['aff'] < 85 and res_output.output['intt'] < 85 and res_output.output['suc'] < 85 and res_output.output['dom'] < 85 and res_output.output['aba'] >= 85 and res_output.output['nur'] < 85 and res_output.output['chg'] < 85 and res_output.output['end'] < 85 and res_output.output['het'] < 85 and res_output.output['agg'] < 85):
        posisi = 'Regional Staff'
    elif (res_output.output['ach'] < 85 and res_output.output['deff'] < 85 and res_output.output['ord'] < 85 and res_output.output['exh'] < 85 and res_output.output['aut'] < 85 and res_output.output['aff'] < 85 and res_output.output['intt'] < 85 and res_output.output['suc'] < 85 and res_output.output['dom'] < 85 and res_output.output['aba'] < 85 and res_output.output['nur'] >= 85 and res_output.output['chg'] < 85 and res_output.output['end'] < 85 and res_output.output['het'] < 85 and res_output.output['agg'] < 85):
        posisi = 'Personal Staff/Customer Service'
    elif (res_output.output['ach'] < 85 and res_output.output['deff'] < 85 and res_output.output['ord'] < 85 and res_output.output['exh'] < 85 and res_output.output['aut'] < 85 and res_output.output['aff'] < 85 and res_output.output['intt'] < 85 and res_output.output['suc'] < 85 and res_output.output['dom'] < 85 and res_output.output['aba'] < 85 and res_output.output['nur'] < 85 and res_output.output['chg'] >= 85 and res_output.output['end'] < 85 and res_output.output['het'] < 85 and res_output.output['agg'] < 85):
        posisi = 'Personal Staff/Customer Service'
    elif (res_output.output['ach'] < 85 and res_output.output['deff'] < 85 and res_output.output['ord'] < 85 and res_output.output['exh'] < 85 and res_output.output['aut'] < 85 and res_output.output['aff'] < 85 and res_output.output['intt'] < 85 and res_output.output['suc'] < 85 and res_output.output['dom'] < 85 and res_output.output['aba'] < 85 and res_output.output['nur'] < 85 and res_output.output['chg'] < 85 and res_output.output['end'] >= 85 and res_output.output['het'] < 85 and res_output.output['agg'] < 85):
        posisi = 'Team Leader'
    elif (res_output.output['ach'] < 85 and res_output.output['deff'] < 85 and res_output.output['ord'] < 85 and res_output.output['exh'] < 85 and res_output.output['aut'] < 85 and res_output.output['aff'] < 85 and res_output.output['intt'] < 85 and res_output.output['suc'] >= 85 and res_output.output['dom'] < 85 and res_output.output['aba'] < 85 and res_output.output['nur'] < 85 and res_output.output['chg'] < 85 and res_output.output['end'] < 85 and res_output.output['het'] >= 85 and res_output.output['agg'] < 85):
        posisi = 'Sales Management'
    elif (res_output.output['ach'] < 85 and res_output.output['deff'] < 85 and res_output.output['ord'] < 85 and res_output.output['exh'] < 85 and res_output.output['aut'] < 85 and res_output.output['aff'] < 85 and res_output.output['intt'] < 85 and res_output.output['suc'] < 85 and res_output.output['dom'] >= 85 and res_output.output['aba'] < 85 and res_output.output['nur'] < 85 and res_output.output['chg'] < 85 and res_output.output['end'] < 85 and res_output.output['het'] < 85 and res_output.output['agg'] >= 85):
        posisi = 'Regional Staff'
    elif (res_output.output['ach'] >= 85 and res_output.output['deff'] >= 85 and res_output.output['ord'] < 85 and res_output.output['exh'] < 85 and res_output.output['aut'] < 85 and res_output.output['aff'] < 85 and res_output.output['intt'] < 85 and res_output.output['suc'] < 85 and res_output.output['dom'] < 85 and res_output.output['aba'] < 85 and res_output.output['nur'] < 85 and res_output.output['chg'] < 85 and res_output.output['end'] < 85 and res_output.output['het'] < 85 and res_output.output['agg'] < 85):
        posisi = 'Manager & Personal Staff'
    elif (res_output.output['ach'] >= 85 and res_output.output['deff'] < 85 and res_output.output['ord'] >= 85 and res_output.output['exh'] < 85 and res_output.output['aut'] < 85 and res_output.output['aff'] < 85 and res_output.output['intt'] < 85 and res_output.output['suc'] < 85 and res_output.output['dom'] < 85 and res_output.output['aba'] < 85 and res_output.output['nur'] < 85 and res_output.output['chg'] < 85 and res_output.output['end'] < 85 and res_output.output['het'] < 85 and res_output.output['agg'] < 85):
        posisi = 'Manager & Office Staff'
    elif (res_output.output['ach'] >= 85 and res_output.output['deff'] < 85 and res_output.output['ord'] < 85 and res_output.output['exh'] >= 85 and res_output.output['aut'] < 85 and res_output.output['aff'] < 85 and res_output.output['intt'] < 85 and res_output.output['suc'] < 85 and res_output.output['dom'] < 85 and res_output.output['aba'] < 85 and res_output.output['nur'] < 85 and res_output.output['chg'] < 85 and res_output.output['end'] < 85 and res_output.output['het'] < 85 and res_output.output['agg'] < 85):
        posisi = 'Manager & Sales Management'
    else:
        posisi = 'Tidak Ada Rekomendasi Pekerjaan'

        hasil = [posisi]
        return print("Rekomendasi Posisi Pekerjaan",hasil)

# ach.view()
# deff.view()
# ord.view()
