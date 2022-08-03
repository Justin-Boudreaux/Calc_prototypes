#info: flare burning (80 kj/hr) fuel of Propanol (62 wt%), Octane (36 wt%), and Benzene (balence); air as the oxidizer (excess)
#Rxns (balenced)
 #   1 [C3H8O + (9/2)O2 -> 3CO2 + 4H2O] ----complete combustion 
 #   2 [C3H8O + 3O2 -> 3CO + 4H2O]-----------partial combustion
 #   3 [C8H18 + (25/2)O2 -> 8CO2 + 9H2O]-----complete combustion
 #   4 [C8H18 + (17/2)O2 -> 8CO + 9H2O]------partial combustion
 #   5 [C6H6 + (15/2) O2 -> 6CO2 + 3H2O]-----complete combustion
 #   6 [C6H6 + (9/2) O2 -> 6CO + 3H2O]-------partial combustion
#HF info: [ Propanol(g)=-238.6, Octane(g)=-208.5, Benezne(l)= 49.1, CO(g)=-110.5, CO2(g)=-393.5, O2=0 ]
#efficiency info: Propanol [96% convered via complete], Octane [73.5% and 26.5% convered via complete and partial respectively], benzene [99.9% via complete combustion].
#getting info 
#======================fuels 
mw_prop = 60.01
hf_pro = -238.6
mw_oct = 114.23
hf_oct = -208.5
mw_ben = 78.11
hf_ben = 49.1
# ==================CO/ CO2 / H2O / air 
hf_CO = -110.5
mw_CO = 28.01
hf_CO2 = -393.5
mw_CO2 = 44.01
hf_H2O = -241.8
mw_H2O = 18.02
hf_O2= 0
mw_air = 28.96
# =========================rxns
rxn_1_eff = .96
rxn_2_eff = 0
rxn_3_eff = .735
rxn_4_eff = .265
rxn_5_eff = .999
rxn_6_eff = 0

rxn_1_sto = [1,4.5,-3,-4]
rxn_1_spe = [hf_pro,hf_O2,hf_CO2,hf_H2O]
rxn_2_sto = [1,3,-3,-4]
rxn_2_spe = [hf_pro,hf_O2,hf_CO,hf_H2O]
rxn_3_sto = [1,12.5,-8,-9]
rxn_3_spe = [hf_oct,hf_O2,hf_CO2,hf_H2O]
rxn_4_sto = [1,8.5,-8,-9]
rxn_4_spe = [hf_oct,hf_O2,hf_CO,hf_H2O]
rxn_5_sto = [1,12.5,-6,-3]
rxn_5_spe = [hf_ben,hf_O2,hf_CO2,hf_H2O]
rxn_6_sto = [1,4.5,-6,-3]
rxn_6_spe = [hf_ben,hf_O2,hf_CO,hf_H2O]

def weightflow_to_moleflow(totalflow_by_weight,fuel_1_wtpercent,fuel_1_MW, fuel_2_wtpercent, fuel_2_MW, fuel_3_wtpercent,fuel_3_MW):
    MW_avg = (fuel_1_MW + fuel_2_MW + fuel_3_MW)/3
    total_molar_flow = MW_avg * totalflow_by_weight
    mf_fuel_1 = totalflow_by_weight * (fuel_1_wtpercent/ fuel_1_MW) 
    mf_fuel_2 = totalflow_by_weight * (fuel_2_wtpercent/ fuel_2_MW) 
    mf_fuel_3 = totalflow_by_weight * (fuel_3_wtpercent/ fuel_3_MW) 
    return total_molar_flow, mf_fuel_1, mf_fuel_2,mf_fuel_3
(total_molar_flowrate, Prop_molar_flowrate, Oct_molar_flowrate, Benz_molar_flowrate) = weightflow_to_moleflow(80,62,60,36,114.23,2,78.11)

def change_in_enthalpy(rxn_stoichiometry,rxn_species):
    H = 0
    H += rxn_stoichiometry[0]*rxn_species[0]
    H += rxn_stoichiometry[1]*rxn_species[1]
    H += rxn_stoichiometry[2]*rxn_species[2]
    H += rxn_stoichiometry[3]*rxn_species[3]
    return H 

H_1 = change_in_enthalpy(rxn_1_sto,rxn_1_spe)
H_2 = change_in_enthalpy(rxn_2_sto,rxn_2_spe)
H_3 = change_in_enthalpy(rxn_3_sto,rxn_3_spe)
H_4 = change_in_enthalpy(rxn_4_sto,rxn_4_spe)
H_5 = change_in_enthalpy(rxn_5_sto,rxn_5_spe)
H_6 = change_in_enthalpy(rxn_6_sto,rxn_6_spe)
H_total = Prop_molar_flowrate*(rxn_1_eff*H_1 + rxn_2_eff*H_2)+ Oct_molar_flowrate*(rxn_3_eff*H_3 + rxn_4_eff*H_4) + Benz_molar_flowrate*(rxn_5_eff*H_5+ rxn_6_eff*H_6)
print('heat of combustion {} in kj/hr'.format(round(H_total,2)))
