import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from app.controllers import soalController


#variables and terms
#Parameters
ach = ctrl.Antecedent(np.arange(5,26), 'ACH')
deff = ctrl.Antecedent(np.arange(5,25), 'DEF')
ord =  ctrl.Antecedent(np.arange(4,27), 'ORD')
exh =  ctrl.Consequent(np.arange(4,24), 'EXH')
aut =  ctrl.Antecedent(np.arange(4,26), 'AUT')
aff =  ctrl.Antecedent(np.arange(5,26), 'AFF')
intt =  ctrl.Antecedent(np.arange(4,26), 'INT')
suc =  ctrl.Antecedent(np.arange(1,25), 'SUC')
dom =  ctrl.Antecedent(np.arange(3,28), 'DOM')
aba =  ctrl.Antecedent(np.arange(3,27), 'ABA')
nur =  ctrl.Antecedent(np.arange(5,28), 'NUR')
chg =  ctrl.Antecedent(np.arange(3,27), 'CHG')
end =  ctrl.Antecedent(np.arange(5,29), 'END')
het =  ctrl.Antecedent(np.arange(0,30), 'HET')
agg =  ctrl.Antecedent(np.arange(3,26), 'AGG')
con =  ctrl.Antecedent(np.arange(6,17), 'CON')
#Result
res =  ctrl.Consequent(np.arange(0,30), 'Hasil')

#Membership functions Parameter

ach['Rendah'] = fuzz.trapmf(ach.universe, [4,5,10,11])
ach['RataRata'] = fuzz.trapmf(ach.universe, [10,11,18,19])
ach['Tinggi'] = fuzz.trapmf(ach.universe, [18,19,24,25])

deff['Rendah'] = fuzz.trapmf(deff.universe, [4,5,9,10])
deff['RataRata'] = fuzz.trapmf(deff.universe, [9,10,17,18])
deff['Tinggi'] = fuzz.trapmf(deff.universe, [17,18,23,24])

ord['Rendah'] = fuzz.trapmf(ord.universe, [3,4,9,10])
ord['RataRata'] = fuzz.trapmf(ord.universe, [9,10,19,20])
ord['Tinggi'] = fuzz.trapmf(ord.universe, [19,20,25,26])

exh['Rendah'] = fuzz.trapmf(exh.universe, [3,4,8,9])
exh['RataRata'] = fuzz.trapmf(exh.universe, [8,9,16,17])
exh['Tinggi'] = fuzz.trapmf(exh.universe, [16,17,22,23])

aut['Rendah'] = fuzz.trapmf(aut.universe, [3,4,9,10])
aut['RataRata'] = fuzz.trapmf(aut.universe, [9,10,18,19])
aut['Tinggi'] = fuzz.trapmf(aut.universe, [18,19,24,25])

aff['Rendah'] = fuzz.trapmf(aff.universe, [4,5,9,10])
aff['RataRata'] = fuzz.trapmf(aff.universe, [9,10,18,19])
aff['Tinggi'] = fuzz.trapmf(aff.universe, [18,19,24,25])

intt['Rendah'] = fuzz.trapmf(intt.universe, [3,4,9,10])
intt['RataRata'] = fuzz.trapmf(intt.universe, [9,10,18,19])
intt['Tinggi'] = fuzz.trapmf(intt.universe, [18,19,24,25])

suc['Rendah'] = fuzz.trapmf(suc.universe, [0,1,5,6])
suc['RataRata'] = fuzz.trapmf(suc.universe, [5,6,15,16])
suc['Tinggi'] = fuzz.trapmf(suc.universe, [15,16,23,24])

dom['Rendah'] = fuzz.trapmf(dom.universe, [2,3,8,9])
dom['RataRata'] = fuzz.trapmf(dom.universe, [8,9,19,20])
dom['Tinggi'] = fuzz.trapmf(dom.universe, [19,20,26,27])

aba['Rendah'] = fuzz.trapmf(aba.universe, [2,3,8,9])
aba['RataRata'] = fuzz.trapmf(aba.universe, [8,9,19,20])
aba['Tinggi'] = fuzz.trapmf(aba.universe, [19,20,25,26])

nur['Rendah'] = fuzz.trapmf(nur.universe, [4,5,10,11])
nur['RataRata'] = fuzz.trapmf(nur.universe, [10,11,20,21])
nur['Tinggi'] = fuzz.trapmf(nur.universe, [20,21,26,27])

chg['Rendah'] = fuzz.trapmf(chg.universe, [2,3,8,9])
chg['RataRata'] = fuzz.trapmf(chg.universe, [8,9,18,19])
chg['Tinggi'] = fuzz.trapmf(chg.universe, [18,19,25,26])

end['Rendah'] = fuzz.trapmf(end.universe, [4,5,11,12])
end['RataRata'] = fuzz.trapmf(end.universe, [11,12,21,22])
end['Tinggi'] = fuzz.trapmf(end.universe, [21,22,27,28])

het['Rendah'] = fuzz.trapmf(het.universe, [0,1,2,3])
het['RataRata'] = fuzz.trapmf(het.universe, [2,3,19,20])
het['Tinggi'] = fuzz.trapmf(het.universe, [19,20,28,29])

agg['Rendah'] = fuzz.trapmf(agg.universe, [2,3,8,9])
agg['RataRata'] = fuzz.trapmf(agg.universe, [8,9,17,18])
agg['Tinggi'] = fuzz.trapmf(agg.universe, [17,18,24,25])

con['Rendah'] = fuzz.trapmf(con.universe, [5,6,8,9])
con['RataRata'] = fuzz.trapmf(con.universe, [8,9,12,13])
con['Tinggi'] = fuzz.trapmf(con.universe, [12,13,15,16])

#Membership functions Score
res['ach'] = fuzz.trapmf(res.universe, [4,5,24,25])
res['def'] = fuzz.trapmf(res.universe, [4,5,23,24])
res['ord'] = fuzz.trapmf(res.universe, [3,4,25,26])
res['exh'] = fuzz.trapmf(res.universe, [3,4,22,23])
res['aut'] = fuzz.trapmf(res.universe, [3,4,24,25])
res['aff'] = fuzz.trapmf(res.universe, [4,5,24,25])
res['int'] = fuzz.trapmf(res.universe, [3,4,24,25])
res['suc'] = fuzz.trapmf(res.universe, [0,1,23,24])
res['dom'] = fuzz.trapmf(res.universe, [2,3,26,27])
res['aba'] = fuzz.trapmf(res.universe, [2,3,25,26])
res['nur'] = fuzz.trapmf(res.universe, [4,5,26,27])
res['chg'] = fuzz.trapmf(res.universe, [2,3,25,26])
res['end'] = fuzz.trapmf(res.universe, [4,5,27,28])
res['het'] = fuzz.trapmf(res.universe, [0,1,28,29])
res['agg'] = fuzz.trapmf(res.universe, [2,3,24,25])
res['con'] = fuzz.trapmf(res.universe, [5,6,15,16])

# Rule system
# Rules for ACH Job
ruleAch = ctrl.Rule(
    (ach['Tinggi'] and deff['RataRata']) |
    (ach['Tinggi'] and deff['Tinggi']) |
    (ach['Tinggi'] and ord['RataRata'] and ord['Rendah'] and ord['RataRata'])|
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Rendah'] and exh['RataRata']), res['ach'])

# Rule system
# Rules for DEF Job
ruleDef = ctrl.Rule(
    (ach['Tinggi'] and deff['Tinggi']) |
    (ach['Tinggi'] and deff['Tinggi'] and ord['Rendah'] and ord['RataRata']) , res['def'])

# Rule system
# Rules for ORD Job
ruleOrd = ctrl.Rule(
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi']) |
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Rendah'] and exh['RataRata']), res['ord'])

# Rule system
# Rules for EXH Job
ruleExh = ctrl.Rule(
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi']) |
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Rendah'] and aut['RataRata']), res['exh'])

# Rule system
# Rules for AUT Job
ruleAut = ctrl.Rule(
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi']and aut['Tinggi']) |
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Rendah'] and aff['RataRata']), res['aut'])


# Rule system
# Rules for AFF Job
ruleAff = ctrl.Rule(
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi']and aut['Tinggi'] and aff['Tinggi']) |
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Rendah'] and intt['RataRata']), res['aff'])


# Rule system
# Rules for INT Job
ruleInt = ctrl.Rule(
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi']) |
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi'] and suc['Rendah'] and suc['RataRata']), res['int'])


# Rule system
# Rules for SUC Job
ruleSuc = ctrl.Rule(
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi'] and suc['Tinggi']) |
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi'] and suc['Tinggi'] and dom['Rendah'] and dom['RataRata']), res['suc'])

# Rule system
# Rules for DOM Job
ruleDom = ctrl.Rule(
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi']and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi'] and suc['Tinggi'] and dom['Tinggi']) |
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi'] and suc['Tinggi'] and dom['Tinggi'] 
    and aba['Rendah'] and aba['RataRata']), res['dom'])


# Rule system
# Rules for ABA Job
ruleAba = ctrl.Rule(
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi'] and suc['Tinggi'] and dom['Tinggi'] 
    and aba['Tinggi']) |
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi'] and suc['Tinggi'] and dom['Tinggi'] 
    and aba['Tinggi'] and nur['Rendah'] and nur['RataRata']), res['aba'])


# Rule system
# Rules for NUR Job
ruleNur = ctrl.Rule(
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi'] and suc['Tinggi'] and dom['Tinggi'] 
    and aba['Tinggi'] and nur['Tinggi']) |
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi'] and suc['Tinggi'] and dom['Tinggi'] 
    and aba['Tinggi'] and nur['Tinggi'] and chg['Rendah'] and chg['RataRata']), res['nur'])


# Rule system
# Rules for CHG Job
ruleChg = ctrl.Rule(
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi'] and suc['Tinggi'] and dom['Tinggi'] 
    and aba['Tinggi'] and nur['Tinggi'] and chg['Tinggi']) |
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi'] and suc['Tinggi'] and dom['Tinggi'] 
    and aba['Tinggi'] and nur['Tinggi'] and chg['Tinggi'] and end['Rendah'] and end['RataRata']), res['chg'])

# Rule system
# Rules for END Job
ruleEnd = ctrl.Rule(
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi'] and suc['Tinggi'] and dom['Tinggi'] 
    and aba['Tinggi'] and nur['Tinggi'] and chg['Tinggi'] and end['Tinggi'])|
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi'] and suc['Tinggi'] and dom['Tinggi'] 
    and aba['Tinggi'] and nur['Tinggi'] and chg['Tinggi'] and end['Tinggi'] and het['Rendah'] and het['Tinggi']), res['end'])

# Rule system
# Rules for HET Job
ruleHet = ctrl.Rule(
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi'] and suc['Tinggi'] and dom['Tinggi'] 
    and aba['Tinggi'] and nur['Tinggi'] and chg['Tinggi'] and end['Tinggi'] and het['Tinggi'])|
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi'] and suc['Tinggi'] and dom['Tinggi'] 
    and aba['Tinggi'] and nur['Tinggi'] and chg['Tinggi'] and end['Tinggi'] and het['Tinggi'] and agg['Rendah'] and agg['RataRata']), res['het'])


# Rule system
# Rules for AGG Job
ruleAgg = ctrl.Rule(
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi'] and suc['Tinggi'] and dom['Tinggi'] 
    and aba['Tinggi'] and nur['Tinggi'] and chg['Tinggi'] and end['Tinggi'] and het['Tinggi'] and agg['Tinggi'])|
    (ach['Tinggi'] and deff['Tinggi'] and ord['Tinggi'] and exh['Tinggi'] and aut['Tinggi'] and aff['Tinggi'] and intt['Tinggi'] and suc['Tinggi'] and dom['Tinggi'] 
    and aba['Tinggi'] and nur['Tinggi'] and chg['Tinggi'] and end['Tinggi'] and het['Tinggi'] and agg['Tinggi'] and con['Rendah'] and con['RataRata']), res['con'])

# Control System Creation and Simulation
res_ctrl = ctrl.ControlSystem([ruleAch and ruleDef and ruleOrd and ruleExh and ruleAut and ruleAff and ruleInt and ruleSuc and ruleDom and ruleAba and ruleNur and ruleChg and ruleEnd and ruleHet and ruleAgg])
res_output = ctrl.ControlSystemSimulation(res_ctrl)



persentil_ach = soalController.hitung_persentil_ach()
persentil_DEF = soalController.hitung_persentil_DEF()
persentil_ord = soalController.hitung_persentil_ord()
persentil_exh = soalController.hitung_persentil_exh()
persentil_aut = soalController.hitung_persentil_aut()
persentil_aff = soalController.hitung_persentil_aff()
persentil_int = soalController.hitung_persentil_int()
persentil_suc = soalController.hitung_persentil_suc()
persentil_dom = soalController.hitung_persentil_dom()
persentil_aba = soalController.hitung_persentil_aba()
persentil_nur = soalController.hitung_persentil_nur()
persentil_chg = soalController.hitung_persentil_chg()
persentil_end = soalController.hitung_persentil_end()
persentil_het = soalController.hitung_persentil_het()
persentil_agg = soalController.hitung_persentil_agg()




res_output.output['ach'] = float(persentil_ach[2])
res_output.output['deff'] = float(persentil_DEF[2])
res_output.output['ord'] = float(persentil_ord[2])
res_output.output['exh'] = float(persentil_exh[2])
res_output.output['aut'] = float(persentil_aut[2])
res_output.output['aff'] = float(persentil_aff[2])
res_output.output['intt'] = float(persentil_int[2])
res_output.output['suc'] = float(persentil_suc[2])
res_output.output['dom'] = float(persentil_dom[2])
res_output.output['aba'] = float(persentil_aba[2])
res_output.output['nur'] = float(persentil_nur[2])
res_output.output['chg'] = float(persentil_chg[2])
res_output.output['end'] = float(persentil_end[2])
res_output.output['het'] = float(persentil_het[2])
res_output.output['agg'] = float(persentil_agg[2])

# Print output result
# print(res_output.output['Rekomendasi Pekerjaan'])

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

def hasil_klasifikasi():
    hasil = posisi
    return hasil