from app.models.soal import Soal
from app.models.percentile import Percentile
from flask import request
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def index():
    page = request.args.get('page', 1, type=int)
    soal = Soal.query.paginate(page=page, per_page = 255)
    return soal

def ach_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_6 = request.form[str(data[5])]
        soal_11 = request.form[str(data[10])]
        soal_16 = request.form[str(data[15])]
        soal_21 = request.form[str(data[20])]
        soal_26 = request.form[str(data[25])]
        soal_31 = request.form[str(data[30])]
        soal_36 = request.form[str(data[35])]
        soal_41 = request.form[str(data[40])]
        soal_46 = request.form[str(data[45])]
        soal_51 = request.form[str(data[50])]
        soal_56 = request.form[str(data[55])]
        soal_61 = request.form[str(data[60])]
        soal_66 = request.form[str(data[65])]
        soal_71 = request.form[str(data[70])]
            
        ach = [soal_6, soal_11, soal_16, soal_21, soal_26, soal_31, soal_36, soal_41, soal_46, soal_51, soal_56, soal_61, soal_66, soal_71]

        hasil_ach = ach.count('A')

        return hasil_ach

def DEF_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_2 = request.form[str(data[1])]
        soal_12 = request.form[str(data[11])]
        soal_17 = request.form[str(data[16])]
        soal_22 = request.form[str(data[21])]
        soal_27 = request.form[str(data[26])]
        soal_32 = request.form[str(data[31])]
        soal_37 = request.form[str(data[36])]
        soal_42 = request.form[str(data[41])]
        soal_47 = request.form[str(data[46])]
        soal_52 = request.form[str(data[51])]
        soal_57 = request.form[str(data[56])]
        soal_62 = request.form[str(data[61])]
        soal_67 = request.form[str(data[66])]
        soal_72 = request.form[str(data[71])]
            
        DEF = [soal_2, soal_12, soal_17, soal_22, soal_27, soal_32, soal_37, soal_42, soal_47, soal_52, soal_57, soal_62, soal_67, soal_72]

        hasil_DEF = DEF.count('A')

        return hasil_DEF

def ord_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_3 = request.form[str(data[2])]
        soal_8 = request.form[str(data[7])]
        soal_18 = request.form[str(data[17])]
        soal_23 = request.form[str(data[22])]
        soal_28 = request.form[str(data[27])]
        soal_33 = request.form[str(data[32])]
        soal_38 = request.form[str(data[37])]
        soal_43 = request.form[str(data[42])]
        soal_48 = request.form[str(data[47])]
        soal_53 = request.form[str(data[52])]
        soal_58 = request.form[str(data[57])]
        soal_63 = request.form[str(data[62])]
        soal_68 = request.form[str(data[67])]
        soal_73 = request.form[str(data[72])]
            
        ord = [soal_3, soal_8, soal_18, soal_23, soal_28, soal_33, soal_38, soal_43, soal_48, soal_53, soal_58, soal_63, soal_68, soal_73]

        hasil_ord = ord.count('A')

        return hasil_ord

def exh_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_4 = request.form[str(data[3])]
        soal_9 = request.form[str(data[11])]
        soal_14 = request.form[str(data[16])]
        soal_24 = request.form[str(data[21])]
        soal_29 = request.form[str(data[26])]
        soal_34 = request.form[str(data[31])]
        soal_39 = request.form[str(data[36])]
        soal_44 = request.form[str(data[41])]
        soal_49 = request.form[str(data[46])]
        soal_54 = request.form[str(data[51])]
        soal_59 = request.form[str(data[56])]
        soal_64 = request.form[str(data[61])]
        soal_69 = request.form[str(data[66])]
        soal_74 = request.form[str(data[71])]
            
        exh = [soal_4, soal_9, soal_14, soal_24, soal_29, soal_34, soal_39, soal_44, soal_49, soal_54, soal_59, soal_64, soal_69, soal_74]

        hasil_exh = exh.count('A')

        return hasil_exh

def aut_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_5 = request.form[str(data[4])]
        soal_10 = request.form[str(data[9])]
        soal_15 = request.form[str(data[14])]
        soal_20 = request.form[str(data[19])]
        soal_25 = request.form[str(data[24])]
        soal_30 = request.form[str(data[29])]
        soal_35 = request.form[str(data[34])]
        soal_40 = request.form[str(data[39])]
        soal_45 = request.form[str(data[44])]
        soal_50 = request.form[str(data[49])]
        soal_55 = request.form[str(data[54])]
        soal_60 = request.form[str(data[59])]
        soal_65 = request.form[str(data[64])]
        soal_70 = request.form[str(data[69])]
            
        aut = [soal_5, soal_10, soal_15, soal_20, soal_25, soal_30, soal_35, soal_40, soal_45, soal_50, soal_55, soal_60, soal_65, soal_70]

        hasil_aut = aut.count('A')

        return hasil_aut

def aff_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_76 = request.form[str(data[75])]
        soal_81 = request.form[str(data[80])]
        soal_86 = request.form[str(data[85])]
        soal_91 = request.form[str(data[90])]
        soal_96 = request.form[str(data[95])]
        soal_106 = request.form[str(data[105])]
        soal_111 = request.form[str(data[110])]
        soal_116 = request.form[str(data[115])]
        soal_121 = request.form[str(data[120])]
        soal_126 = request.form[str(data[125])]
        soal_131 = request.form[str(data[130])]
        soal_136 = request.form[str(data[135])]
        soal_141 = request.form[str(data[140])]
        soal_146 = request.form[str(data[145])]
            
        aff = [soal_76, soal_81, soal_86, soal_91, soal_96, soal_106, soal_111, soal_116, soal_121, soal_126, soal_131, soal_136, soal_141, soal_146]

        hasil_aff = aff.count('A')

        return hasil_aff

def int_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_77 = request.form[str(data[76])]
        soal_82 = request.form[str(data[81])]
        soal_87 = request.form[str(data[86])]
        soal_92 = request.form[str(data[91])]
        soal_97 = request.form[str(data[96])]
        soal_102 = request.form[str(data[101])]
        soal_112 = request.form[str(data[111])]
        soal_117 = request.form[str(data[116])]
        soal_122 = request.form[str(data[121])]
        soal_127 = request.form[str(data[126])]
        soal_132 = request.form[str(data[131])]
        soal_137 = request.form[str(data[136])]
        soal_142 = request.form[str(data[141])]
        soal_147 = request.form[str(data[146])]
            
        int = [soal_77, soal_82, soal_87, soal_92, soal_97, soal_102, soal_112, soal_117, soal_122, soal_127, soal_132, soal_137, soal_142, soal_147]

        hasil_int = int.count('A')

        return hasil_int

def suc_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_78 = request.form[str(data[77])]
        soal_83 = request.form[str(data[82])]
        soal_88 = request.form[str(data[87])]
        soal_93 = request.form[str(data[92])]
        soal_98 = request.form[str(data[98])]
        soal_103 = request.form[str(data[102])]
        soal_108 = request.form[str(data[107])]
        soal_118 = request.form[str(data[117])]
        soal_123 = request.form[str(data[122])]
        soal_128 = request.form[str(data[127])]
        soal_133 = request.form[str(data[132])]
        soal_138 = request.form[str(data[137])]
        soal_143 = request.form[str(data[142])]
        soal_148 = request.form[str(data[147])]
            
        suc = [soal_78, soal_83, soal_88, soal_93, soal_98, soal_103, soal_108, soal_118, soal_123, soal_128, soal_133, soal_138, soal_143, soal_148]

        hasil_suc = suc.count('A')

        return hasil_suc

def dom_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_79 = request.form[str(data[78])]
        soal_84 = request.form[str(data[83])]
        soal_89 = request.form[str(data[88])]
        soal_94 = request.form[str(data[93])]
        soal_99 = request.form[str(data[98])]
        soal_104 = request.form[str(data[103])]
        soal_109 = request.form[str(data[108])]
        soal_114 = request.form[str(data[113])]
        soal_124 = request.form[str(data[123])]
        soal_129 = request.form[str(data[128])]
        soal_134 = request.form[str(data[133])]
        soal_139 = request.form[str(data[138])]
        soal_144 = request.form[str(data[143])]
        soal_149 = request.form[str(data[148])]
            
        dom = [soal_79, soal_84, soal_89, soal_94, soal_99, soal_104, soal_109, soal_114, soal_124, soal_129, soal_134, soal_139, soal_144, soal_149]

        hasil_dom = dom.count('A')

        return hasil_dom

def aba_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_80 = request.form[str(data[79])]
        soal_85 = request.form[str(data[84])]
        soal_90 = request.form[str(data[89])]
        soal_95 = request.form[str(data[94])]
        soal_100 = request.form[str(data[99])]
        soal_105 = request.form[str(data[104])]
        soal_110 = request.form[str(data[109])]
        soal_115 = request.form[str(data[114])]
        soal_120 = request.form[str(data[119])]
        soal_130 = request.form[str(data[129])]
        soal_135 = request.form[str(data[134])]
        soal_140 = request.form[str(data[139])]
        soal_145 = request.form[str(data[144])]
        soal_150 = request.form[str(data[149])]
            
        aba = [soal_80, soal_85, soal_90, soal_95, soal_100, soal_105, soal_110, soal_115, soal_120, soal_130, soal_135, soal_140, soal_145, soal_150]

        hasil_aba = aba.count('A')

        return hasil_aba

def nur_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_151 = request.form[str(data[150])]
        soal_156 = request.form[str(data[155])]
        soal_161 = request.form[str(data[160])]
        soal_166 = request.form[str(data[165])]
        soal_171 = request.form[str(data[170])]
        soal_176 = request.form[str(data[175])]
        soal_181 = request.form[str(data[180])]
        soal_186 = request.form[str(data[185])]
        soal_191 = request.form[str(data[190])]
        soal_196 = request.form[str(data[195])]
        soal_206 = request.form[str(data[205])]
        soal_211 = request.form[str(data[210])]
        soal_216 = request.form[str(data[215])]
        soal_221 = request.form[str(data[220])]
            
        nur = [soal_151, soal_156, soal_161, soal_166, soal_171, soal_176, soal_181, soal_186, soal_191, soal_196, soal_206, soal_211, soal_216, soal_221]

        hasil_nur = nur.count('A')

        return hasil_nur

def chg_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_152 = request.form[str(data[151])]
        soal_157 = request.form[str(data[156])]
        soal_162 = request.form[str(data[161])]
        soal_167 = request.form[str(data[166])]
        soal_172 = request.form[str(data[171])]
        soal_177 = request.form[str(data[176])]
        soal_182 = request.form[str(data[181])]
        soal_187 = request.form[str(data[186])]
        soal_192 = request.form[str(data[191])]
        soal_197 = request.form[str(data[196])]
        soal_202 = request.form[str(data[201])]
        soal_212 = request.form[str(data[211])]
        soal_217 = request.form[str(data[216])]
        soal_222 = request.form[str(data[221])]
            
        chg = [soal_152, soal_157, soal_162, soal_167, soal_172, soal_177, soal_182, soal_187, soal_192, soal_197, soal_202, soal_212, soal_217, soal_222]

        hasil_chg = chg.count('A')

        return hasil_chg

def end_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_153 = request.form[str(data[152])]
        soal_158 = request.form[str(data[157])]
        soal_163 = request.form[str(data[162])]
        soal_168 = request.form[str(data[167])]
        soal_173 = request.form[str(data[172])]
        soal_178 = request.form[str(data[177])]
        soal_183 = request.form[str(data[182])]
        soal_188 = request.form[str(data[187])]
        soal_193 = request.form[str(data[192])]
        soal_198 = request.form[str(data[197])]
        soal_203 = request.form[str(data[202])]
        soal_208 = request.form[str(data[207])]
        soal_218 = request.form[str(data[217])]
        soal_223 = request.form[str(data[222])]
            
        end = [soal_153, soal_158, soal_163, soal_168, soal_173, soal_178, soal_183, soal_188, soal_193, soal_198, soal_203, soal_208, soal_218, soal_223]

        hasil_end = end.count('A')

        return hasil_end

def het_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_154 = request.form[str(data[153])]
        soal_159 = request.form[str(data[158])]
        soal_164 = request.form[str(data[163])]
        soal_169 = request.form[str(data[168])]
        soal_174 = request.form[str(data[173])]
        soal_179 = request.form[str(data[178])]
        soal_184 = request.form[str(data[183])]
        soal_189 = request.form[str(data[188])]
        soal_194 = request.form[str(data[193])]
        soal_199 = request.form[str(data[198])]
        soal_204 = request.form[str(data[203])]
        soal_209 = request.form[str(data[208])]
        soal_214 = request.form[str(data[213])]
        soal_224 = request.form[str(data[223])]
            
        het = [soal_154, soal_159, soal_164, soal_169, soal_174, soal_179, soal_184, soal_189, soal_194, soal_199, soal_204, soal_209, soal_214, soal_224]

        hasil_het = het.count('A')

        return hasil_het

def agg_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_155 = request.form[str(data[154])]
        soal_160 = request.form[str(data[159])]
        soal_165 = request.form[str(data[164])]
        soal_170 = request.form[str(data[169])]
        soal_175 = request.form[str(data[174])]
        soal_180 = request.form[str(data[179])]
        soal_185 = request.form[str(data[184])]
        soal_190 = request.form[str(data[189])]
        soal_195 = request.form[str(data[194])]
        soal_200 = request.form[str(data[199])]
        soal_205 = request.form[str(data[204])]
        soal_210 = request.form[str(data[209])]
        soal_215 = request.form[str(data[214])]
        soal_220 = request.form[str(data[219])]
            
        agg = [soal_155, soal_160, soal_165, soal_170, soal_175, soal_180, soal_185, soal_190, soal_195, soal_200, soal_205, soal_210, soal_215, soal_220]

        hasil_agg = agg.count('A')

        return hasil_agg

def ach1_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_2 = request.form[str(data[1])]
        soal_3 = request.form[str(data[2])]
        soal_4 = request.form[str(data[3])]
        soal_5 = request.form[str(data[4])]
        soal_76 = request.form[str(data[75])]
        soal_77 = request.form[str(data[76])]
        soal_78 = request.form[str(data[77])]
        soal_79 = request.form[str(data[78])]
        soal_80 = request.form[str(data[79])]
        soal_151 = request.form[str(data[150])]
        soal_152 = request.form[str(data[151])]
        soal_153 = request.form[str(data[152])]
        soal_154 = request.form[str(data[153])]
        soal_155 = request.form[str(data[154])]
            
        ach1 = [soal_2, soal_3, soal_4, soal_5, soal_76, soal_77, soal_78, soal_79, soal_80, soal_151, soal_152, soal_153, soal_154, soal_155]

        hasil_ach1 = ach1.count('B')

        return hasil_ach1

def DEF1_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_6 = request.form[str(data[5])]
        soal_8 = request.form[str(data[7])]
        soal_9 = request.form[str(data[8])]
        soal_10 = request.form[str(data[9])]
        soal_81 = request.form[str(data[80])]
        soal_82 = request.form[str(data[81])]
        soal_83 = request.form[str(data[82])]
        soal_84 = request.form[str(data[83])]
        soal_85 = request.form[str(data[85])]
        soal_156 = request.form[str(data[155])]
        soal_157 = request.form[str(data[156])]
        soal_158 = request.form[str(data[157])]
        soal_159 = request.form[str(data[158])]
        soal_160 = request.form[str(data[159])]
            
        DEF1 = [soal_6, soal_8, soal_9, soal_10, soal_81, soal_82, soal_83, soal_84, soal_85, soal_156, soal_157, soal_158, soal_159, soal_160]

        hasil_DEF1 = DEF1.count('B')

        return hasil_DEF1

def ord1_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_11 = request.form[str(data[10])]
        soal_12 = request.form[str(data[11])]
        soal_14 = request.form[str(data[13])]
        soal_15 = request.form[str(data[14])]
        soal_86 = request.form[str(data[85])]
        soal_87 = request.form[str(data[86])]
        soal_88 = request.form[str(data[87])]
        soal_89 = request.form[str(data[88])]
        soal_90 = request.form[str(data[89])]
        soal_161 = request.form[str(data[160])]
        soal_162 = request.form[str(data[161])]
        soal_163 = request.form[str(data[162])]
        soal_164 = request.form[str(data[163])]
        soal_165 = request.form[str(data[164])]
            
        ord1 = [soal_11, soal_12, soal_14, soal_15, soal_86, soal_87, soal_88, soal_89, soal_90, soal_161, soal_162, soal_163, soal_164, soal_165]

        hasil_ord1 = ord1.count('B')

        return hasil_ord1

def exh1_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_16 = request.form[str(data[15])]
        soal_17 = request.form[str(data[16])]
        soal_18 = request.form[str(data[17])]
        soal_20 = request.form[str(data[19])]
        soal_91 = request.form[str(data[90])]
        soal_92 = request.form[str(data[91])]
        soal_93 = request.form[str(data[92])]
        soal_94 = request.form[str(data[93])]
        soal_95 = request.form[str(data[94])]
        soal_166 = request.form[str(data[165])]
        soal_167 = request.form[str(data[166])]
        soal_168 = request.form[str(data[167])]
        soal_169 = request.form[str(data[168])]
        soal_170 = request.form[str(data[169])]
            
        exh1 = [soal_16, soal_17, soal_18, soal_20, soal_91, soal_92, soal_93, soal_94, soal_95, soal_166, soal_167, soal_168, soal_169, soal_170]

        hasil_exh1 = exh1.count('B')

        return hasil_exh1

def aut1_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_21 = request.form[str(data[20])]
        soal_22 = request.form[str(data[21])]
        soal_23 = request.form[str(data[22])]
        soal_24 = request.form[str(data[23])]
        soal_96 = request.form[str(data[95])]
        soal_97 = request.form[str(data[96])]
        soal_98 = request.form[str(data[97])]
        soal_99 = request.form[str(data[98])]
        soal_100 = request.form[str(data[99])]
        soal_171 = request.form[str(data[170])]
        soal_172 = request.form[str(data[171])]
        soal_173 = request.form[str(data[172])]
        soal_174 = request.form[str(data[173])]
        soal_175 = request.form[str(data[174])]
            
        aut1 = [soal_21, soal_22, soal_23, soal_24, soal_96, soal_97, soal_98, soal_99, soal_100, soal_171, soal_172, soal_173, soal_174, soal_175]

        hasil_aut1 = aut1.count('B')

        return hasil_aut1

def aff1_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_26 = request.form[str(data[25])]
        soal_27 = request.form[str(data[26])]
        soal_28 = request.form[str(data[27])]
        soal_29 = request.form[str(data[28])]
        soal_30 = request.form[str(data[29])]
        soal_102 = request.form[str(data[101])]
        soal_103 = request.form[str(data[102])]
        soal_104 = request.form[str(data[103])]
        soal_105 = request.form[str(data[104])]
        soal_176 = request.form[str(data[175])]
        soal_177 = request.form[str(data[176])]
        soal_178 = request.form[str(data[177])]
        soal_179 = request.form[str(data[178])]
        soal_180 = request.form[str(data[179])]
            
        aff1 = [soal_26, soal_27, soal_28, soal_29, soal_30, soal_102, soal_103, soal_104, soal_105, soal_176, soal_177, soal_178, soal_179, soal_180]

        hasil_aff1 = aff1.count('B')

        return hasil_aff1

def int1_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_31 = request.form[str(data[30])]
        soal_32 = request.form[str(data[31])]
        soal_33 = request.form[str(data[32])]
        soal_34 = request.form[str(data[33])]
        soal_35 = request.form[str(data[34])]
        soal_106 = request.form[str(data[105])]
        soal_108 = request.form[str(data[107])]
        soal_109 = request.form[str(data[108])]
        soal_110 = request.form[str(data[109])]
        soal_181 = request.form[str(data[180])]
        soal_182 = request.form[str(data[181])]
        soal_183 = request.form[str(data[182])]
        soal_184 = request.form[str(data[183])]
        soal_185 = request.form[str(data[184])]
            
        int1 = [soal_31, soal_32, soal_33, soal_34, soal_35, soal_106, soal_108, soal_109, soal_110, soal_181, soal_182, soal_183, soal_184, soal_185]

        hasil_int1 = int1.count('B')

        return hasil_int1

def suc1_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_36 = request.form[str(data[35])]
        soal_37 = request.form[str(data[36])]
        soal_38 = request.form[str(data[37])]
        soal_39 = request.form[str(data[38])]
        soal_40 = request.form[str(data[39])]
        soal_111 = request.form[str(data[110])]
        soal_112 = request.form[str(data[111])]
        soal_114 = request.form[str(data[113])]
        soal_115 = request.form[str(data[114])]
        soal_186 = request.form[str(data[185])]
        soal_187 = request.form[str(data[186])]
        soal_188 = request.form[str(data[187])]
        soal_189 = request.form[str(data[188])]
        soal_190 = request.form[str(data[189])]
            
        suc1 = [soal_36, soal_37, soal_38, soal_39, soal_40, soal_111, soal_112, soal_114, soal_115, soal_186, soal_187, soal_188, soal_189, soal_190]

        hasil_suc1 = suc1.count('B')

        return hasil_suc1

def dom1_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_41 = request.form[str(data[40])]
        soal_42 = request.form[str(data[41])]
        soal_43 = request.form[str(data[42])]
        soal_44 = request.form[str(data[43])]
        soal_45 = request.form[str(data[44])]
        soal_116 = request.form[str(data[115])]
        soal_117 = request.form[str(data[116])]
        soal_118 = request.form[str(data[117])]
        soal_120 = request.form[str(data[119])]
        soal_191 = request.form[str(data[190])]
        soal_192 = request.form[str(data[191])]
        soal_193 = request.form[str(data[192])]
        soal_194 = request.form[str(data[193])]
        soal_195 = request.form[str(data[194])]
            
        dom1 = [soal_41, soal_42, soal_43, soal_44, soal_45, soal_116, soal_117, soal_118, soal_120, soal_191, soal_192, soal_193, soal_194, soal_195]

        hasil_dom1 = dom1.count('B')

        return hasil_dom1

def aba1_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_46 = request.form[str(data[45])]
        soal_47 = request.form[str(data[46])]
        soal_48 = request.form[str(data[47])]
        soal_49 = request.form[str(data[48])]
        soal_50 = request.form[str(data[49])]
        soal_121 = request.form[str(data[120])]
        soal_122 = request.form[str(data[121])]
        soal_123 = request.form[str(data[122])]
        soal_124 = request.form[str(data[123])]
        soal_196 = request.form[str(data[195])]
        soal_197 = request.form[str(data[196])]
        soal_198 = request.form[str(data[197])]
        soal_199 = request.form[str(data[198])]
        soal_200 = request.form[str(data[199])]
            
        aba1 = [soal_46, soal_47, soal_48, soal_49, soal_50, soal_121, soal_122, soal_123, soal_124, soal_196, soal_197, soal_198, soal_199, soal_200]

        hasil_aba1 = aba1.count('B')

        return hasil_aba1

def nur1_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_51 = request.form[str(data[50])]
        soal_52 = request.form[str(data[51])]
        soal_53 = request.form[str(data[52])]
        soal_54 = request.form[str(data[53])]
        soal_55 = request.form[str(data[54])]
        soal_126 = request.form[str(data[125])]
        soal_127 = request.form[str(data[126])]
        soal_128 = request.form[str(data[127])]
        soal_129 = request.form[str(data[128])]
        soal_130 = request.form[str(data[129])]
        soal_202 = request.form[str(data[201])]
        soal_203 = request.form[str(data[202])]
        soal_204 = request.form[str(data[203])]
        soal_205 = request.form[str(data[204])]
            
        nur1 = [soal_51, soal_52, soal_53, soal_54, soal_55, soal_126, soal_127, soal_128, soal_129, soal_130, soal_202, soal_203, soal_204, soal_205]

        hasil_nur1 = nur1.count('B')

        return hasil_nur1

def chg1_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_56 = request.form[str(data[55])]
        soal_57 = request.form[str(data[56])]
        soal_58 = request.form[str(data[57])]
        soal_59 = request.form[str(data[58])]
        soal_60 = request.form[str(data[59])]
        soal_131 = request.form[str(data[130])]
        soal_132 = request.form[str(data[131])]
        soal_133 = request.form[str(data[132])]
        soal_134 = request.form[str(data[133])]
        soal_135 = request.form[str(data[134])]
        soal_206 = request.form[str(data[205])]
        soal_208 = request.form[str(data[207])]
        soal_209 = request.form[str(data[208])]
        soal_210 = request.form[str(data[209])]
            
        chg1 = [soal_56, soal_57, soal_58, soal_59, soal_60, soal_131, soal_132, soal_133, soal_134, soal_135, soal_206, soal_208, soal_209, soal_210]

        hasil_chg1 = chg1.count('B')

        return hasil_chg1

def end1_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_61 = request.form[str(data[60])]
        soal_62 = request.form[str(data[61])]
        soal_63 = request.form[str(data[62])]
        soal_64 = request.form[str(data[63])]
        soal_65 = request.form[str(data[64])]
        soal_136 = request.form[str(data[135])]
        soal_137 = request.form[str(data[136])]
        soal_138 = request.form[str(data[137])]
        soal_139 = request.form[str(data[138])]
        soal_140 = request.form[str(data[139])]
        soal_211 = request.form[str(data[210])]
        soal_212 = request.form[str(data[211])]
        soal_214 = request.form[str(data[213])]
        soal_215 = request.form[str(data[214])]
            
        end1 = [soal_61, soal_62, soal_63, soal_64, soal_65, soal_136, soal_137, soal_138, soal_139, soal_140, soal_211, soal_212, soal_214, soal_215]

        hasil_end1 = end1.count('B')

        return hasil_end1

def het1_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_66 = request.form[str(data[153])]
        soal_67 = request.form[str(data[158])]
        soal_68 = request.form[str(data[163])]
        soal_69 = request.form[str(data[168])]
        soal_70 = request.form[str(data[173])]
        soal_141 = request.form[str(data[178])]
        soal_142 = request.form[str(data[183])]
        soal_143 = request.form[str(data[188])]
        soal_144 = request.form[str(data[193])]
        soal_145 = request.form[str(data[198])]
        soal_216 = request.form[str(data[203])]
        soal_217 = request.form[str(data[208])]
        soal_218 = request.form[str(data[213])]
        soal_220 = request.form[str(data[223])]
            
        het1 = [soal_66, soal_67, soal_68, soal_69, soal_70, soal_141, soal_142, soal_143, soal_144, soal_145, soal_216, soal_217, soal_218, soal_220]

        hasil_het1 = het1.count('B')

        return hasil_het1

def agg1_hasiltes():
    data = [Soal.query.order_by(Soal.id_soal).all()]
    for data in data:

        soal_71 = request.form[str(data[154])]
        soal_72 = request.form[str(data[159])]
        soal_73 = request.form[str(data[164])]
        soal_74 = request.form[str(data[169])]
        soal_75 = request.form[str(data[174])]
        soal_146 = request.form[str(data[179])]
        soal_147 = request.form[str(data[184])]
        soal_148 = request.form[str(data[189])]
        soal_149 = request.form[str(data[194])]
        soal_150 = request.form[str(data[199])]
        soal_221 = request.form[str(data[204])]
        soal_222 = request.form[str(data[209])]
        soal_223 = request.form[str(data[214])]
        soal_224 = request.form[str(data[219])]
            
        agg1 = [soal_71, soal_72, soal_73, soal_74, soal_75, soal_146, soal_147, soal_148, soal_149, soal_150, soal_221, soal_222, soal_223, soal_224]

        hasil_agg1 = agg1.count('B')

        return hasil_agg1


def hitung_persentil_ach():
    data = Percentile.query.all()
    for data in data:
        # ACH
        ach_a = ach_hasiltes()
        ach_b = ach1_hasiltes()
        ach_fix = ach_a + ach_b
        if ach_fix == data.score:
            persentil = data.ach
            if persentil >= 97:
                persentil_kategori = "Sangat Tinggi"
            elif persentil <= 96 and persentil >= 85:
                persentil_kategori = "Tinggi"
            elif persentil <= 84 and persentil >= 17:
                persentil_kategori = "Rata-Rata"
            elif persentil <= 16 and persentil >= 4:
                persentil_kategori = "Rendah"
            else:
                persentil_kategori = "Sangat Rendah"
            persentil_hasil_ach = [persentil, persentil_kategori, ach_fix]
            return persentil_hasil_ach
def hitung_persentil_DEF():
    data = Percentile.query.all()
    for data in data:
        # DEF
        DEF_a = DEF_hasiltes()
        DEF_b = DEF1_hasiltes()
        DEF_fix = DEF_a + DEF_b
        if DEF_fix == data.score:
            persentil = data.DEF
            if persentil >= 97:
                persentil_kategori = "Sangat Tinggi"
            elif persentil <= 96 and persentil >= 85:
                persentil_kategori = "Tinggi"
            elif persentil <= 84 and persentil >= 17:
                persentil_kategori = "Rata - Rata"
            elif persentil <= 16 and persentil >= 4:
                persentil_kategori = "Rendah"
            else:
                persentil_kategori = "Sangat Rendah"
            persentil_hasil_DEF = [persentil, persentil_kategori, DEF_fix]
            return persentil_hasil_DEF
def hitung_persentil_ord():
    data = Percentile.query.all()
    for data in data:
        # ORD
        ord_a = ord_hasiltes()
        ord_b = ord1_hasiltes()
        ord_fix = ord_a + ord_b
        if ord_fix == data.score:
            persentil = data.ord
            if persentil >= 97:
                persentil_kategori = "Sangat Tinggi"
            elif persentil <= 96 and persentil >= 85:
                persentil_kategori = "Tinggi"
            elif persentil <= 84 and persentil >= 17:
                persentil_kategori = "Rata - Rata"
            elif persentil <= 16 and persentil >= 4:
                persentil_kategori = "Rendah"
            else:
                persentil_kategori = "Sangat Rendah"
            persentil_hasil_ord = [persentil, persentil_kategori, ord_fix]
            return persentil_hasil_ord
def hitung_persentil_exh():
    data = Percentile.query.all()
    for data in data:
        # EXH
        exh_a = exh_hasiltes()
        exh_b = exh1_hasiltes()
        exh_fix = exh_a + exh_b
        if exh_fix == data.score:
            persentil = data.exh
            if persentil >= 97:
                persentil_kategori = "Sangat Tinggi"
            elif persentil <= 96 and persentil >= 85:
                persentil_kategori = "Tinggi"
            elif persentil <= 84 and persentil >= 17:
                persentil_kategori = "Rata - Rata"
            elif persentil <= 16 and persentil >= 4:
                persentil_kategori = "Rendah"
            else:
                persentil_kategori = "Sangat Rendah"
            persentil_hasil_exh = [persentil, persentil_kategori, exh_fix]
            return persentil_hasil_exh
def hitung_persentil_aut():
    data = Percentile.query.all()
    for data in data:
        # AUT
        aut_a = aut_hasiltes()
        aut_b = aut1_hasiltes()
        aut_fix = aut_a + aut_b
        if aut_fix == data.score:
            persentil = data.aut
            if persentil >= 97:
                persentil_kategori = "Sangat Tinggi"
            elif persentil <= 96 and persentil >= 85:
                persentil_kategori = "Tinggi"
            elif persentil <= 84 and persentil >= 17:
                persentil_kategori = "Rata - Rata"
            elif persentil <= 16 and persentil >= 4:
                persentil_kategori = "Rendah"
            else:
                persentil_kategori = "Sangat Rendah"
            persentil_hasil_aut = [persentil, persentil_kategori, aut_fix]
            return persentil_hasil_aut
def hitung_persentil_aff():
    data = Percentile.query.all()
    for data in data:
        # AFF
        aff_a = aff_hasiltes()
        aff_b = aff1_hasiltes()
        aff_fix = aff_a + aff_b
        if aff_fix == data.score:
            persentil = data.aff
            if persentil >= 97:
                persentil_kategori = "Sangat Tinggi"
            elif persentil <= 96 and persentil >= 85:
                persentil_kategori = "Tinggi"
            elif persentil <= 84 and persentil >= 17:
                persentil_kategori = "Rata - Rata"
            elif persentil <= 16 and persentil >= 4:
                persentil_kategori = "Rendah"
            else:
                persentil_kategori = "Sangat Rendah"
            persentil_hasil_aff = [persentil, persentil_kategori, aff_fix]
            return persentil_hasil_aff
def hitung_persentil_int():
    data = Percentile.query.all()
    for data in data:
        # INT
        int_a = int_hasiltes()
        int_b = int1_hasiltes()
        int_fix = int_a + int_b
        if int_fix == data.score:
            persentil = data.int
            if persentil >= 97:
                persentil_kategori = "Sangat Tinggi"
            elif persentil <= 96 and persentil >= 85:
                persentil_kategori = "Tinggi"
            elif persentil <= 84 and persentil >= 17:
                persentil_kategori = "Rata - Rata"
            elif persentil <= 16 and persentil >= 4:
                persentil_kategori = "Rendah"
            else:
                persentil_kategori = "Sangat Rendah"
            persentil_hasil_int = [persentil, persentil_kategori, int_fix]
            return persentil_hasil_int
def hitung_persentil_suc():
    data = Percentile.query.all()
    for data in data:
        # SUC
        suc_a = suc_hasiltes()
        suc_b = suc1_hasiltes()
        suc_fix = suc_a + suc_b
        if suc_fix == data.score:
            persentil = data.suc
            if persentil >= 97:
                persentil_kategori = "Sangat Tinggi"
            elif persentil <= 96 and persentil >= 85:
                persentil_kategori = "Tinggi"
            elif persentil <= 84 and persentil >= 17:
                persentil_kategori = "Rata - Rata"
            elif persentil <= 16 and persentil >= 4:
                persentil_kategori = "Rendah"
            else:
                persentil_kategori = "Sangat Rendah"
            persentil_hasil_suc = [persentil, persentil_kategori, suc_fix]
            return persentil_hasil_suc
def hitung_persentil_dom():
    data = Percentile.query.all()
    for data in data:
        # DOM
        dom_a = dom_hasiltes()
        dom_b = dom1_hasiltes()
        dom_fix = dom_a + dom_b
        if dom_fix == data.score:
            persentil = data.dom
            if persentil >= 97:
                persentil_kategori = "Sangat Tinggi"
            elif persentil <= 96 and persentil >= 85:
                persentil_kategori = "Tinggi"
            elif persentil <= 84 and persentil >= 17:
                persentil_kategori = "Rata - Rata"
            elif persentil <= 16 and persentil >= 4:
                persentil_kategori = "Rendah"
            else:
                persentil_kategori = "Sangat Rendah"
            persentil_hasil_dom = [persentil, persentil_kategori, dom_fix]
            return persentil_hasil_dom
def hitung_persentil_aba():
    data = Percentile.query.all()
    for data in data:
        # ABA
        aba_a = aba_hasiltes()
        aba_b = aba1_hasiltes()
        aba_fix = aba_a + aba_b
        if aba_fix == data.score:
            persentil = data.aba
            if persentil >= 97:
                persentil_kategori = "Sangat Tinggi"
            elif persentil <= 96 and persentil >= 85:
                persentil_kategori = "Tinggi"
            elif persentil <= 84 and persentil >= 17:
                persentil_kategori = "Rata - Rata"
            elif persentil <= 16 and persentil >= 4:
                persentil_kategori = "Rendah"
            else:
                persentil_kategori = "Sangat Rendah"
            persentil_hasil_aba = [persentil, persentil_kategori, aba_fix]
            return persentil_hasil_aba
def hitung_persentil_nur():
    data = Percentile.query.all()
    for data in data:
        # NUR
        nur_a = nur_hasiltes()
        nur_b = nur1_hasiltes()
        nur_fix = nur_a + nur_b
        if nur_fix == data.score:
            persentil = data.nur
            if persentil >= 97:
                persentil_kategori = "Sangat Tinggi"
            elif persentil <= 96 and persentil >= 85:
                persentil_kategori = "Tinggi"
            elif persentil <= 84 and persentil >= 17:
                persentil_kategori = "Rata - Rata"
            elif persentil <= 16 and persentil >= 4:
                persentil_kategori = "Rendah"
            else:
                persentil_kategori = "Sangat Rendah"
            persentil_hasil_nur = [persentil, persentil_kategori, nur_fix]
            return persentil_hasil_nur
def hitung_persentil_chg():
    data = Percentile.query.all()
    for data in data:
        # CHG
        chg_a = chg_hasiltes()
        chg_b = chg1_hasiltes()
        chg_fix = chg_a + chg_b
        if chg_fix == data.score:
            persentil = data.chg
            if persentil >= 97:
                persentil_kategori = "Sangat Tinggi"
            elif persentil <= 96 and persentil >= 85:
                persentil_kategori = "Tinggi"
            elif persentil <= 84 and persentil >= 17:
                persentil_kategori = "Rata - Rata"
            elif persentil <= 16 and persentil >= 4:
                persentil_kategori = "Rendah"
            else:
                persentil_kategori = "Sangat Rendah"
            persentil_hasil_chg = [persentil, persentil_kategori, chg_fix]
            return persentil_hasil_chg
def hitung_persentil_end():
    data = Percentile.query.all()
    for data in data:
        # END
        end_a = end_hasiltes()
        end_b = end1_hasiltes()
        end_fix = end_a + end_b
        if end_fix == data.score:
            persentil = data.end
            if persentil >= 97:
                persentil_kategori = "Sangat Tinggi"
            elif persentil <= 96 and persentil >= 85:
                persentil_kategori = "Tinggi"
            elif persentil <= 84 and persentil >= 17:
                persentil_kategori = "Rata - Rata"
            elif persentil <= 16 and persentil >= 4:
                persentil_kategori = "Rendah"
            else:
                persentil_kategori = "Sangat Rendah"
            persentil_hasil_end = [persentil, persentil_kategori, end_fix]
            return persentil_hasil_end
def hitung_persentil_het():
    data = Percentile.query.all()
    for data in data:
        # HET
        het_a = het_hasiltes()
        het_b = het1_hasiltes()
        het_fix = het_a + het_b
        if het_fix == data.score:
            persentil = data.het
            if persentil >= 97:
                persentil_kategori = "Sangat Tinggi"
            elif persentil <= 96 and persentil >= 85:
                persentil_kategori = "Tinggi"
            elif persentil <= 84 and persentil >= 17:
                persentil_kategori = "Rata - Rata"
            elif persentil <= 16 and persentil >= 4:
                persentil_kategori = "Rendah"
            else:
                persentil_kategori = "Sangat Rendah"
            persentil_hasil_het = [persentil, persentil_kategori, het_fix]
            return persentil_hasil_het
def hitung_persentil_agg():
    data = Percentile.query.all()
    for data in data:
        # AGG
        agg_a = agg_hasiltes()
        agg_b = agg1_hasiltes()
        agg_fix = agg_a + agg_b
        if agg_fix == data.score:
            persentil = data.agg
            if persentil >= 97:
                persentil_kategori = "Sangat Tinggi"
            elif persentil <= 96 and persentil >= 85:
                persentil_kategori = "Tinggi"
            elif persentil <= 84 and persentil >= 17:
                persentil_kategori = "Rata - Rata"
            elif persentil <= 16 and persentil >= 4:
                persentil_kategori = "Rendah"
            else:
                persentil_kategori = "Sangat Rendah"
            persentil_hasil_agg = [persentil, persentil_kategori, agg_fix]
            return persentil_hasil_agg


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

def hasil_klasifikasi_ach():
    data = Percentile.query.all()
    for data in data:
        # ACH
        ach_a = ach_hasiltes()
        ach_b = ach1_hasiltes()
        ach_fix = ach_a + ach_b
        if ach_fix == data.score:
            klasifikasi = data.ach
            if klasifikasi >= 85:
                klasifikasi_kategori = "Manager"
            else:
                klasifikasi_kategori = "-"
            hasil_ach = [klasifikasi, klasifikasi_kategori, ach_fix]
            return hasil_ach

def hasil_klasifikasi_DEF():
    data = Percentile.query.all()
    for data in data:
        # ACH
        DEF_a = DEF_hasiltes()
        DEF_b = DEF1_hasiltes()
        DEF_fix = DEF_a + DEF_b
        if DEF_fix == data.score:
            klasifikasi = data.DEF
            if klasifikasi >= 85:
                klasifikasi_kategori = "Personal Staff"
            else:
                klasifikasi_kategori = "-"
            hasil_DEF = [klasifikasi, klasifikasi_kategori, DEF_fix]
            return hasil_DEF

def hasil_klasifikasi_ord():
    data = Percentile.query.all()
    for data in data:
        # ord
        ord_a = ord_hasiltes()
        ord_b = ord1_hasiltes()
        ord_fix = ord_a + ord_b
        if ord_fix == data.score:
            klasifikasi = data.ord
            if klasifikasi >= 85:
                klasifikasi_kategori = "Office Staff"
            else:
                klasifikasi_kategori = "-"
            hasil_ord = [klasifikasi, klasifikasi_kategori, ord_fix]
            return hasil_ord

def hasil_klasifikasi_exh():
    data = Percentile.query.all()
    for data in data:
        # ACH
        exh_a = exh_hasiltes()
        exh_b = exh1_hasiltes()
        exh_fix = exh_a + exh_b
        if exh_fix == data.score:
            klasifikasi = data.exh
            if klasifikasi >= 85:
                klasifikasi_kategori = "Sales Management"
            else:
                klasifikasi_kategori = "-"
            hasil_exh = [klasifikasi, klasifikasi_kategori, exh_fix]
            return hasil_exh

def hasil_klasifikasi_aut():
    data = Percentile.query.all()
    for data in data:
        # aut
        aut_a = aut_hasiltes()
        aut_b = aut1_hasiltes()
        aut_fix = aut_a + aut_b
        if aut_fix == data.score:
            klasifikasi = data.aut
            if klasifikasi >= 85:
                klasifikasi_kategori = "Sales Management"
            else:
                klasifikasi_kategori = "-"
            hasil_aut = [klasifikasi, klasifikasi_kategori, aut_fix]
            return hasil_aut

def hasil_klasifikasi_aff():
    data = Percentile.query.all()
    for data in data:
        # ACH
        aff_a = aff_hasiltes()
        aff_b = aff1_hasiltes()
        aff_fix = aff_a + aff_b
        if aff_fix == data.score:
            klasifikasi = data.aff
            if klasifikasi >= 85:
                klasifikasi_kategori = "Team Leader"
            else:
                klasifikasi_kategori = "-"
            hasil_aff = [klasifikasi, klasifikasi_kategori, aff_fix]
            return hasil_aff

def hasil_klasifikasi_int():
    data = Percentile.query.all()
    for data in data:
        # int
        int_a = int_hasiltes()
        int_b = int1_hasiltes()
        int_fix = int_a + int_b
        if int_fix == data.score:
            klasifikasi = data.int
            if klasifikasi >= 85:
                klasifikasi_kategori = "Team Leader"
            else:
                klasifikasi_kategori = "-"
            hasil_int = [klasifikasi, klasifikasi_kategori, int_fix]
            return hasil_int

def hasil_klasifikasi_suc():
    data = Percentile.query.all()
    for data in data:
        # ACH
        suc_a = suc_hasiltes()
        suc_b = suc1_hasiltes()
        suc_fix = suc_a + suc_b
        if suc_fix == data.score:
            klasifikasi = data.suc
            if klasifikasi >= 85:
                klasifikasi_kategori = "Management Personalia"
            else:
                klasifikasi_kategori = "-"
            hasil_suc = [klasifikasi, klasifikasi_kategori, suc_fix]
            return hasil_suc

def hasil_klasifikasi_dom():
    data = Percentile.query.all()
    for data in data:
        # ACH
        dom_a = dom_hasiltes()
        dom_b = dom1_hasiltes()
        dom_fix = dom_a + dom_b
        if dom_fix == data.score:
            klasifikasi = data.dom
            if klasifikasi >= 85:
                klasifikasi_kategori = "Sales Management"
            else:
                klasifikasi_kategori = "-"
            hasil_dom = [klasifikasi, klasifikasi_kategori, dom_fix]
            return hasil_dom

def hasil_klasifikasi_aba():
    data = Percentile.query.all()
    for data in data:
        # aba
        aba_a = aba_hasiltes()
        aba_b = aba1_hasiltes()
        aba_fix = aba_a + aba_b
        if aba_fix == data.score:
            klasifikasi = data.aba
            if klasifikasi >= 85:
                klasifikasi_kategori = "Regional Staff"
            else:
                klasifikasi_kategori = "-"
            hasil_aba = [klasifikasi, klasifikasi_kategori, aba_fix]
            return hasil_aba

def hasil_klasifikasi_nur():
    data = Percentile.query.all()
    for data in data:
        # ACH
        nur_a = nur_hasiltes()
        nur_b = nur1_hasiltes()
        nur_fix = nur_a + nur_b
        if nur_fix == data.score:
            klasifikasi = data.nur
            if klasifikasi >= 85:
                klasifikasi_kategori = "Personal Staff / Customer Service"
            else:
                klasifikasi_kategori = "-"
            hasil_nur = [klasifikasi, klasifikasi_kategori, nur_fix]
            return hasil_nur

def hasil_klasifikasi_chg():
    data = Percentile.query.all()
    for data in data:
        # chg
        chg_a = chg_hasiltes()
        chg_b = chg1_hasiltes()
        chg_fix = chg_a + chg_b
        if chg_fix == data.score:
            klasifikasi = data.chg
            if klasifikasi >= 85:
                klasifikasi_kategori = "Personal Staff / Customer Service"
            else:
                klasifikasi_kategori = "-"
            hasil_chg = [klasifikasi, klasifikasi_kategori, chg_fix]
            return hasil_chg

def hasil_klasifikasi_end():
    data = Percentile.query.all()
    for data in data:
        # ACH
        end_a = end_hasiltes()
        end_b = end1_hasiltes()
        end_fix = end_a + end_b
        if end_fix == data.score:
            klasifikasi = data.end
            if klasifikasi >= 85:
                klasifikasi_kategori = "Team Leader"
            else:
                klasifikasi_kategori = "-"
            hasil_end = [klasifikasi, klasifikasi_kategori, end_fix]
            return hasil_end

def hasil_klasifikasi_het():
    data = Percentile.query.all()
    for data in data:
        # het
        het_a = het_hasiltes()
        het_b = het1_hasiltes()
        het_fix = het_a + het_b
        if het_fix == data.score:
            klasifikasi = data.het
            if klasifikasi >= 85:
                klasifikasi_kategori = "Sales Management"
            else:
                klasifikasi_kategori = "-"
            hasil_het = [klasifikasi, klasifikasi_kategori, het_fix]
            return hasil_het

def hasil_klasifikasi_agg():
    data = Percentile.query.all()
    for data in data:
        # ACH
        agg_a = agg_hasiltes()
        agg_b = agg1_hasiltes()
        agg_fix = agg_a + agg_b
        if agg_fix == data.score:
            klasifikasi = data.agg
            if klasifikasi >= 85:
                klasifikasi_kategori = "Regional Staff"
            else:
                klasifikasi_kategori = "-"
            hasil_agg = [klasifikasi, klasifikasi_kategori, agg_fix]
            return hasil_agg