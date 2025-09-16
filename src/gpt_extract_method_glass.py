import os
import openai
import requests
import json
import copy

openai.api_key = 'your API key'

docpath='D:/glass-total-results/'
f=open(docpath+'data_html.json','r')
doc_dict=json.load(f)
f.close()

text1 = "['Glasses with the composition 60Sb2O3-(40-x) NaPO3-xWO3 (where x\u00a0=\u00a00 to 5\u00a0mol.%) were prepared by a conventional melt-quenching technique from Sb2O3, NaPO3, and WO3 high-purity raw materials (99.6%). The glasses are labelled SNW0, SNW5 according to the molar content of WO3 as mentioned in Table\u00a01. All batch compositions (taken in molar%) were preheated at 300\u00a0\u00b0C for 1\u00a0hour in a silica tube crucible to remove adsorbed water. The glasses were melted at a temperature close to 1000\u00a0\u00b0C in the air under flame heat for 10 to 15\u00a0min until was obtained a homogeneous liquid, then the melt was cast on a stainless steel mould, maintained at 280\u00a0\u00b0C (T \u2248 Tg-10\u00a0\u00b0C). The obtained glasses were annealed for 6\u00a0h at 280 \u00b0C in an electric furnace to eliminate the stresses induced during quenching. Polishing was carried to obtain samples with 1 to 2\u00a0mm parallel faces, and appropriate thickness for optical analysis and elastic measure. The glasses that had an amount of WO3 > 25 was found to be less stable and could not achieve sufficient thickness for optical and mechanical tests.']{\"title\": \"Table 1 Glass composition (mol%), data DSC, density and molar volume of SNWx glasses.\", \"head\": [[\"Sample\", \"Sb2O3\", \"NaPO3\", \"WO3\", \"Tg( \\u00b0C)\\u00b12\\u00a0\\u00b0C\", \"Tx( \\u00b0C)\\u00b12\\u00a0\\u00b0C\", \"Tp( \\u00b0C)\\u00b11\\u00a0\\u00b0C\", \"\\u0394T( \\u00b0C)\", \"D(g/cm3)\", \"Vm(cm3.mol\\u22121)\"]], \"body\": [[\"SNW0\", \"60\", \"40\", \"0\", \"305\", \"442\", \"470\", \"137\", \"4.394\", \"40.16\"], [\"SNW5\", \"60\", \"35\", \"5\", \"309\", \"434\", \"446\", \"125\", \"4.613\", \"38.71\"]], \"legend\": []}{\"title\": \"Table 2 Sound velocities, elastic moduli and micro hardness of SNWx glasses. Results of other tungsten containing glasses are also presented for comparison.\", \"head\": [[\"Glass\", \"VL\", \"VT\", \"L\", \"G\", \"K\", \"E\", \"\\u03bd\", \"HV0.2\", \"Ref\"], [\"\", \"(m/s)\", \"(m/s)\", \"(m/s)\", \"(GPa)\", \"(GPa)\", \"(GPa)\", \"(GPa)\", \"(N/mm2)\", \"\"]], \"body\": [[\"SNW0\", \"3082\", \"1778\", \"41,75\", \"13,89\", \"23,24\", \"34,74\", \"0,251\", \"328\", \"Present work\"], [\"SNW 5\", \"3101\", \"1784\", \"44,36\", \"14,69\", \"24,77\", \"36,79\", \"0,252\", \"345\", \"Present work\"]], \"legend\": []}"
str1 = '{"1":{"O":0.6,"Na":0.08,"P":0.08,"Sb":0.24,"W":0.0,"WO3":0.0,"Sb2O3":60.0,"NaPO3":40.0,"Tg":578.15,"Tmelt":null,"Tliquidus":null,"TLittletons":null,"TAnnealing":null,"Tstrain":null,"Tsoft":null,"TdilatometricSoftening":null,"AbbeNum":null,"RefractiveIndex":null,"MeanDispersion":null,"Permittivity":null,"TangentOfLossAngle":null,"TresistivityIs1MOhm.m":null,"Resistivity273K":null,"YoungModulus":34.74,"ShearModulus":13.89,"Microhardness":0.328,"PoissonRatio":0.251,"Density293K":4.394,"ThermalConductivity":null,"ThermalShockRes":null,"CTEbelowTg":null,"Cp293K":null,"NucleationTemperature":null,"NucleationRate":null,"TMaxGrowthVelocity":null,"MaxGrowthVelocity":null,"CrystallizationPeak":743.15,"CrystallizationOnset":715.15,"SurfaceTensionAboveTg":null,"DielectricConstant":null,"MeltTemperature":1273.15,"MeltTime":0.25,"AnnealTemperature":553.15,"AnnealTime":6},"2":{"O":0.6075,"Na":0.07,"P":0.07,"Sb":0.24,"W":0.0125,"WO3":5.0,"Sb2O3":60.0,"NaPO3":35.0,"Tg":582.15,"Tmelt":null,"Tliquidus":null,"TLittletons":null,"TAnnealing":null,"Tstrain":null,"Tsoft":null,"TdilatometricSoftening":null,"AbbeNum":null,"RefractiveIndex":null,"MeanDispersion":null,"Permittivity":null,"TangentOfLossAngle":null,"TresistivityIs1MOhm.m":null,"Resistivity273K":null,"YoungModulus":36.79,"ShearModulus":14.69,"Microhardness":0.345,"PoissonRatio":0.252,"Density293K":4.613,"ThermalConductivity":null,"ThermalShockRes":null,"CTEbelowTg":null,"Cp293K":null,"NucleationTemperature":null,"NucleationRate":null,"TMaxGrowthVelocity":null,"MaxGrowthVelocity":null,"CrystallizationPeak":719.15,"CrystallizationOnset":707.15,"SurfaceTensionAboveTg":null,"DielectricConstant":null,"MeltTemperature":1273.15,"MeltTime":0.25,"AnnealTemperature":553.15,"AnnealTime":6}}'
text2 = "['The glasses used in the present study were formulated based on the CBS phase diagram [20], as shown in Fig. 1, with the specific compositions listed in Table 1 High-purity (>99.9% pure) SiO2, B2O3, and CaO (reagent grade; Wako Pure Chemical Industries Ltd., Osaka, Japan) were utilized as the raw materials. The CBS glasses were prepared via melting and quenching of the raw materials according to the following procedure. The oxides were mixed in proportion to the weight percentages shown in Table 1, and subsequently milled for 12\\xa0h in a polyethylene jar using a methyl alcohol solution and zirconia balls, and then oven-dried overnight at 80\\xa0\u00b0C. The dried powders were melted in a platinum crucible at 1500\\xa0\u00b0C for 1\\xa0h, and the melt was then quenched in deionized water to prevent devitrification. The quenched melt was crushed and then re-milled in methyl alcohol for 24\\xa0h to produce pulverized glass powders.', 'The phase analyses of the glass powders were performed via X-ray diffraction (XRD; D2 Phaser A26-X1, Bruker AXS GmBH, Karlsruhe, Germany) with Cu K\u03b1 radiation. The glass powders were also subjected to differential thermal analysis (DTA, Pyris Diamond (calorimeter), PerkinElmer, Inc., Massachusetts, USA) to investigate the reactions that occurred during heating.']{\"title\": \"Table 1 Compositions of various CaO\\u2013B2O3\\u2013SiO2 glass-ceramics.\", \"head\": [[\"Formulation\", \"Composites\", \"CaO\", \"CaO\", \"B2O3\", \"B2O3\", \"SiO2\", \"SiO2\"], [\"Formulation\", \"Composites\", \"mol%\", \"wt%\", \"mol%\", \"wt%\", \"mol%\", \"wt%\"]], \"body\": [[\"CBS-1\", \"10.5CaO\\u201222.2B2O3\\u201267.3SiO2\", \"10.5\", \"9.5\", \"22.2\", \"25.0\", \"67.3\", \"65.5\"], [\"CBS-2\", \"40.3CaO-15.5B2O3-44.2SiO2\", \"40.3\", \"37.7\", \"15.5\", \"18.0\", \"44.2\", \"44.3\"], [\"CBS-3\", \"50.1CaO-7.3B2O3-42.6SiO2\", \"50.1\", \"47.8\", \"7.3\", \"8.6\", \"42.6\", \"43.6\"]], \"legend\": []}{\"title\": \"Table 2 Crystalline phases present in various glass-ceramics after sintering.\", \"head\": [[\"No.\", \"Composites\", \"Firing condition\", \"Density (g/cm3)\", \"Major phase\", \"Minor phase\"]], \"body\": [[\"CBS-1\", \"10.5CaO\\u201222.2B2O3\\u201267.3SiO2\", \"1050\\u00a0\\u00b0C/15\\u00a0min\", \"2.39\", \"Quartz (SiO2)-h\", \"Cristobalite (SiO2)-tWollastonite (CaSiO3)\"], [\"CBS-2\", \"40.3CaO-15.5B2O3-44.2SiO2\", \"850\\u00a0\\u00b0C/15\\u00a0min\", \"2.50\", \"Wollastonite (CaSiO3)\", \"Coesite (SiO2)-m\"], [\"CBS-3\", \"50.1CaO-7.3B2O3-42.6SiO2\", \"950\\u00a0\\u00b0C/15\\u00a0min\", \"2.84\", \"Wollastonite (CaSiO3)\", \"Coesite (SiO2)-m\"]], \"legend\": []}{\"title\": \"Table 3 Dielectric and thermal properties of the sintered CBS-1, CBS-2 and CBS-3 glass-ceramics.\", \"head\": [[\"No.\", \"Firing temperature (\\u00b0C)\", \"\\u03b5r (@ 60\\u00a0GHz)\", \"tan\\u03b4 (@ 60\\u00a0GHz)\", \"Eb (kV/mm)\", \"\\u03c1 (\\u03a9-cm)\", \"CTE (ppm/\\u00b0C; 25\\u2013300\\u00a0\\u00b0C)\", \"k (W/mk)\"]], \"body\": [[\"CBS-1\", \"1050\\u00a0\\u00b0C\", \"4.04\", \"0.0029\", \"15.20\\u00a0\\u00b1\\u00a02.55\", \"9.62\\u00a0\\u00d7\\u00a01011\", \"3.2\", \"2.43\"], [\"CBS-2\", \"850\\u00a0\\u00b0C\", \"6.29\", \"0.0020\", \"8.16\\u00a0\\u00b1\\u00a01.31\", \"2.98\\u00a0\\u00d7\\u00a01012\", \"6.6\", \"1.06\"], [\"CBS-3\", \"950\\u00a0\\u00b0C\", \"7.61\", \"0.0012\", \"6.27\\u00a0\\u00b1\\u00a00.97\", \"5.13\\u00a0\\u00d7\\u00a01011\", \"5.9\", \"0.82\"]], \"legend\": []}"
str2 = '{"1":{"B":0.0888,"O":0.634366,"Si":0.224333,"Ca":0.0525,"SiO2":67.3,"CaO":10.5,"B2O3":22.2,"Tg":null,"Tmelt":null,"Tliquidus":null,"TLittletons":null,"TAnnealing":null,"Tstrain":null,"Tsoft":null,"TdilatometricSoftening":null,"AbbeNum":null,"RefractiveIndex":null,"MeanDispersion":null,"Permittivity":null,"TangentOfLossAngle":null,"TresistivityIs1MOhm.m":null,"Resistivity273K":null,"YoungModulus":null,"ShearModulus":null,"Microhardness":null,"PoissonRatio":null,"Density293K":2.39,"ThermalConductivity":null,"ThermalShockRes":null,"CTEbelowTg":3.2e-6,"Cp293K":null,"NucleationTemperature":null,"NucleationRate":null,"TMaxGrowthVelocity":null,"MaxGrowthVelocity":null,"CrystallizationPeak":null,"CrystallizationOnset":null,"SurfaceTensionAboveTg":null,"DielectricConstant":4.04,"MeltTemperature":1773.15,"MeltTime":1,"AnnealTemperature":null,"AnnealTime":null},"2":{"B":0.062,"O":0.589166,"Si":0.147333,"Ca":0.2015,"SiO2":44.2,"CaO":40.3,"B2O3":15.5,"Tg":null,"Tmelt":null,"Tliquidus":null,"TLittletons":null,"TAnnealing":null,"Tstrain":null,"Tsoft":null,"TdilatometricSoftening":null,"AbbeNum":null,"RefractiveIndex":null,"MeanDispersion":null,"Permittivity":null,"TangentOfLossAngle":null,"TresistivityIs1MOhm.m":null,"Resistivity273K":null,"YoungModulus":null,"ShearModulus":null,"Microhardness":null,"PoissonRatio":null,"Density293K":2.50,"ThermalConductivity":null,"ThermalShockRes":null,"CTEbelowTg":6.6e-6,"Cp293K":null,"NucleationTemperature":null,"NucleationRate":null,"TMaxGrowthVelocity":null,"MaxGrowthVelocity":null,"CrystallizationPeak":null,"CrystallizationOnset":null,"SurfaceTensionAboveTg":null,"DielectricConstant":6.29,"MeltTemperature":1773.15,"MeltTime":1,"AnnealTemperature":null,"AnnealTime":null},"3":{"B":0.0292,"O":0.5783,"Si":0.142,"Ca":0.2505,"SiO2":42.6,"CaO":50.1,"B2O3":7.3,"Tg":null,"Tmelt":null,"Tliquidus":null,"TLittletons":null,"TAnnealing":null,"Tstrain":null,"Tsoft":null,"TdilatometricSoftening":null,"AbbeNum":null,"RefractiveIndex":null,"MeanDispersion":null,"Permittivity":null,"TangentOfLossAngle":null,"TresistivityIs1MOhm.m":null,"Resistivity273K":null,"YoungModulus":null,"ShearModulus":null,"Microhardness":null,"PoissonRatio":null,"Density293K":2.84,"ThermalConductivity":null,"ThermalShockRes":null,"CTEbelowTg":5.9e-6,"Cp293K":null,"NucleationTemperature":null,"NucleationRate":null,"TMaxGrowthVelocity":null,"MaxGrowthVelocity":null,"CrystallizationPeak":null,"CrystallizationOnset":null,"SurfaceTensionAboveTg":null,"DielectricConstant":7.61,"MeltTemperature":1773.15,"MeltTime":1,"AnnealTemperature":null,"AnnealTime":null}}'

message0 = [
    {"role": "system", "content": "You are an expert in the field of glass materials, and you are skilled at extracting key data and facts from examples and texts provided by the user. You present the extracted information in a JSON structure that follows the format shown in the examples. Below, I will give two examples to show you how to extract data from text and the format in which the data should be returned."},
    {"role": "user", "content": text1},
    {"role": "assistant", "content": str1},
    {"role": "user", "content": text2},
    {"role": "assistant", "content": str2},
]

data=[]
ct=0
dois=list(doc_dict.keys())

# for ii in range(0,len(dois)):
for ii in range(0,len(dois)):
    doi=dois[ii]    
    art=doc_dict[doi]
    for i in range(0,len(art['content'])):
        try:
            ct=ct+1
            print(doi+' para '+str(i)+' total '+str(ct))
            para=art['content'][i]
            msg = copy.deepcopy(message0)
            msg.append({"role": "user", "content": para[0]+para[1]+"Following the two examples and response format above, extract from the provided text the composition, process parameters, and the thermal, mechanical, optical, electrical, and magnetic properties of the glass material. Do not fabricate any data that does not exist in the text, and your task is extraction only. Use kelvin (K) for temperature, hours (h) for time, and mole percent (mol%) for composition; perform unit conversions if necessary. The returned data format must strictly follow the examples given earlier."})
        #rp = openai.Completion.create(
          #model="text-davinci-003",
            rp = openai.ChatCompletion.create(
              model='gpt-4o-2024-08-06',
              messages = msg,
          #prompt=''.join(prompt)+para[0]+para[1]+"\n<data>\n",
              temperature=0.1,
            )
            d={}
            d['doi']=doi
            d['para_id']=i
            d['src']=para
            d['gpt_model']=rp['model']
            d['object']=rp['object']
            d['usage']={'completion_tokens':rp['usage']['completion_tokens'],'prompt_tokens':rp['usage']['prompt_tokens'],'total_tokens':rp['usage']['total_tokens']}
        #d['result']=rp['choices'][0]['text']
            d['result']=rp['choices'][0].message["content"]
            d['finish_reason']=rp['choices'][0]['finish_reason']
            data.append(d)
        
            f=open(docpath+'result_html_20241013.json','w',encoding='utf-8')
            json.dump(data,f)
            f.close()
        except:
            print('error')
        # except:
        #     print('ERROR')