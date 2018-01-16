import os, glob, time


def pack_copy(originpath, targetpath="/Users/renormalization/Desktop/Transfer/", prename=""):
    print originpath
    print targetpath
    return "cp " + originpath + " " + targetpath + ("." if prename=="" else prename)

def main():
    start_time = time.time()

    plotpath      = "/Users/renormalization/mnt/work/bbbb/MoriondAnalysis/Output/"
    limitplotpath = "/Users/renormalization/mnt/work/bbbb/MoriondAnalysis/StatAnalysis/Plots/"
    smoothsystpath= "/Users/renormalization/mnt/work/bbbb/MoriondAnalysis/MakePlot/Xhh4bUtils/mHH_l/"
    notepath      = "/Users/renormalization/Git/Thesis/"

# ##for Section 5 sigeff
#     lst_dir    = ["Moriond"]
#     lst_region = ["SigEff"]
#     lst_type   = [""]
#     lst_plt    = ["region_2b_lst_Moriond_Efficiency_PreSel.pdf", "region_3b_lst_Moriond_Efficiency_PreSel.pdf", \
#     "region_4b_lst_Moriond_Efficiency_PreSel.pdf", "detail_lst_Moriond_Efficiency_AllTag_Signal.pdf",\
#     "evtsel_Moriond_Efficiency_PreSel.pdf", "evtsel_Moriond_Efficiency_PreSel_rel.pdf",\
#     "region_alltag_lst_Moriond_Efficiency_PreSel.pdf", "region_lst_Moriond_Efficiency_AllTag_Signal.pdf",\
#     ]
#     note_dir   = "figures/boosted/SigEff/"
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for plt in lst_plt:
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))

# ##for Section 5 cutflow
#     lst_dir    = ["Moriond_bkg_9"]
#     lst_region = ["Tables"]
#     lst_type   = [""]
#     lst_plt    = ["cutflow.tex", "SignalEffTable_RSG_c20.tex", "SignalEffTable_RSG_c10.tex", "SignalEffTable_Xhh.tex"]
#     note_dir   = "figures/boosted/tables/"
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for plt in lst_plt:
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))

# ##for Section 6 SBCR definition
#     lst_dir    = ["Moriond"]
#     lst_region = ["Other"]
#     lst_type   = ["Sideband_", "Control_"]
#     lst_plt    = ["OneTag_mH0H1.pdf", "TwoTag_mH0H1.pdf"]
#     note_dir   = "figures/boosted/Other/"
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for plt in lst_plt:
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))

# ##for Section 6 ttbar shape
#     lst_dir    = ["Moriond"]
#     lst_region = ["Other"]
#     lst_type   = [""]
#     lst_plt    = ["ttbar_compare_mHH_l.pdf", "ttbar_compare_mHH_l_1.pdf"]
#     note_dir   = "figures/boosted/Other/"
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for plt in lst_plt:
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))

# ##for Section 6 Fitting for QCD and ttbar
#     lst_dir    = ["Moriond_bkg_9"]
#     lst_region = ["Fit"]
#     lst_type   = [""]
#     lst_plt    = ["fitNorm_FourTag_leadHCand_Mass_s.pdf", "fitNorm_ThreeTag_leadHCand_Mass_s.pdf", "fitNorm_TwoTag_split_leadHCand_Mass_s.pdf"]
#     note_dir   = "figures/boosted/Fit/"
#     note_name  = ["fitNorm_i4.pdf", "fitNorm_i3.pdf", "fitNorm_i2s.pdf"]
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir, prename=note_name[i]))
#     lst_dir    = ["Moriond_bkg_9"]
#     lst_region = ["Tables"]
#     lst_type   = [""]
#     lst_plt    = ["normfit.tex"]
#     note_dir   = "figures/boosted/tables/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))


# ##for Section 6 Reweighting comparison
#     lst_dir    = ["Moriond"]
#     lst_region = ["Sideband", "Control"]
#     lst_type   = ["FourTag_", "ThreeTag_", "TwoTag_split_"]
#     lst_plt    = ["leadHCand_Pt_m.pdf",\
#     "leadHCand_trk0_Pt.pdf", "leadHCand_trk1_Pt.pdf",\
#     "sublHCand_trk0_Pt.pdf", "sublHCand_trk1_Pt.pdf",\
#     "mHH_l_1.pdf",\
#     ]
#     note_dir   = "figures/boosted/Prereweight/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Dir + "_" + Type + region + "_" +  plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))


# ##for Section 6 Reweighting demonstration
#     lst_dir    = ["Moriond"]
#     lst_region = [""]
#     lst_type   = [""]
#     lst_plt    = ["2bs_directcompare_sublHCand_trk1_Pt_1.pdf",\
#     "2bs_directcompare_sublHCand_trk0_Pt_1.pdf",\
#     "2bs_directcompare_leadHCand_trk1_Pt_1.pdf",\
#     "2bs_directcompare_leadHCand_trk0_Pt_1.pdf",\
#     ]
#     note_dir   = "figures/boosted/Prereweight/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + "Other_study" + "/" +  plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))


# ##for Section 6 Reweighting fits
#     lst_dir    = ["Moriond", "Moriond_bkg_0", "Moriond_bkg_3", "Moriond_bkg_9"]
#     lst_region = ["/Plot_r0/Incl/", "/Plot_r1/Incl/", "/Plot_r4/Incl/", "/Plot_r10/Incl/"]
#     lst_type   = ["2Trk_split_", "3Trk_", "4Trk_"]
#     lst_plt    = [
#     "lead_Incl_sublHCand_Pt_m_1.pdf",\
#     "lead_Incl_sublHCand_trk0_Pt.pdf",\
#     "lead_Incl_sublHCand_trk1_Pt.pdf",\
#     "subl_Incl_leadHCand_Pt_m_1.pdf",\
#     "subl_Incl_leadHCand_trk0_Pt.pdf",\
#     "subl_Incl_leadHCand_trk1_Pt.pdf",\
#     ]
#     note_dir   = "figures/boosted/Reweight/Fits/"
#     note_name  = []
#     for j, Dir in enumerate(lst_dir):
#         for Type in lst_type:
#             for i, plt in enumerate(lst_plt):
#                 originpath = plotpath + Dir + lst_region[j] + Dir + "_NoTag_" + Type + plt
#                 os.system(pack_copy(originpath, targetpath=notepath + note_dir))

# #for Section 6 Sideband and Control Regions
#     lst_dir    = ["Moriond_bkg_9"]
#     lst_region = ["Sideband", "Control"]
#     lst_type   = ["FourTag_", "ThreeTag_", "TwoTag_split_"]
#     # lst_plt    = ["leadHCand_Pt_m.pdf", "leadHCand_Pt_m_1.pdf", "leadHCand_Mass_s.pdf", "leadHCand_Eta.pdf", "leadHCand_Phi.pdf",\
#     # "sublHCand_Pt_m.pdf", "sublHCand_Pt_m_1.pdf", "sublHCand_Mass_s.pdf", "sublHCand_Eta.pdf", "sublHCand_Phi.pdf",\
#     # "leadHCand_trk0_Pt.pdf", "leadHCand_trk1_Pt.pdf",\
#     # "sublHCand_trk0_Pt.pdf", "sublHCand_trk1_Pt.pdf",\
#     # "leadHCand_trk_dr.pdf",  "sublHCand_trk_dr.pdf",\
#     # "mHH_l_1.pdf", "hCandDr.pdf", "hCandDeta.pdf", "hCandDphi.pdf",\
#     # ]
#     lst_plt    = ["leadHCand_ntrk.pdf", "sublHCand_ntrk.pdf"]
#     note_dir   = "figures/boosted/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Dir + "_" + Type + region + "_" +  plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir + region + "/", prename=str("b77_" + Type + region + "_" +  plt)))

# ##for Section 6 Blinded Signal Regions
#     lst_dir    = ["Moriond_bkg_9"]
#     lst_region = ["Signal"]
#     lst_type   = ["FourTag_", "ThreeTag_", "TwoTag_split_"]
#     lst_plt    = ["leadHCand_Pt_m_blind.pdf", "leadHCand_Mass_s_blind.pdf", "leadHCand_Eta_blind.pdf", "leadHCand_Phi_blind.pdf",\
#     "sublHCand_Pt_m_blind.pdf", "sublHCand_Mass_s_blind.pdf", "sublHCand_Eta_blind.pdf", "sublHCand_Phi_blind.pdf",\
#     "leadHCand_trk0_Pt_blind.pdf", "leadHCand_trk1_Pt_blind.pdf",\
#     "sublHCand_trk0_Pt_blind.pdf", "sublHCand_trk1_Pt_blind.pdf",\
#     "leadHCand_trk_dr_blind.pdf",  "sublHCand_trk_dr_blind.pdf",\
#     "mHH_l_1_blind.pdf", "hCandDr_blind.pdf", "hCandDeta_blind.pdf", "hCandDphi_blind.pdf",\
#     ]
#     note_dir   = "figures/boosted/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Dir + "_" + Type + region + "_" +  plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir + region + "/", prename=str("b77_" + Type + region + "_" +  plt)))

# ## for Section 6, Smoothing
#     lst_dir    = ["Moriond_bkg_9"]
#     lst_region = ["Other"]
#     lst_type   = [""]
#     lst_plt    = ["FourTag_Signal_compare_scale_mHH_1.pdf", "ThreeTag_Signal_compare_scale_mHH_1.pdf", "TwoTag_split_Signal_compare_scale_mHH_1.pdf"]
#     note_dir   = "figures/boosted/Other/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))

#     lst_dir    = ["Moriond_bkg_9"]
#     lst_region = ["Tables"]
#     lst_type   = [""]
#     lst_plt    = ["smoothfit_l.tex", "smoothfit_pole.tex"]
#     note_dir   = "figures/boosted/tables/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))
    
#     lst_dir    = ["Moriond_bkg_9"]
#     lst_region = ["Smooth"]
#     lst_type   = ["TwoTag_split_", "ThreeTag_", "FourTag_"]
#     lst_plt    = ["Signal_mHH_l.pdf", "Signal_mHH_l_l.pdf", "Signal_mHH_pole.pdf", "Signal_mHH_pole_l.pdf"]
#     note_dir   = "figures/boosted/Smooth/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     for pretype in ["qcd_est_", "ttbar_est_"]:
#                         originpath = plotpath + Dir + "/Plot/" + region + "/" + pretype + Type + plt
#                         os.system(pack_copy(originpath, targetpath=notepath + note_dir))

#     lst_dir    = ["Moriond_bkg_9"]
#     lst_region = ["Smooth"]
#     lst_type   = ["TwoTag_split_", "ThreeTag_", "FourTag_"]
#     lst_plt    = ["l_smoothed.pdf ", "pole_smoothed.pdf "]
#     note_dir   = "figures/boosted/Smooth/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))

#     lst_dir    = ["Moriond_bkg_9"]
#     lst_region = ["Smooth"]
#     lst_type   = ["TwoTag_split_pole_", "ThreeTag_pole_", "FourTag_pole_"]
#     lst_plt    = ["Signal_mHH_pole_1_blind.pdf"]
#     note_dir   = "figures/boosted/Smooth/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Dir + "_" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))

# # for Section 7, yields
#     lst_dir    = ["Moriond_bkg_9"]
#     lst_region = ["Tables"]
#     lst_type   = [""]
#     lst_plt    = ["FourTag_yield.tex", "ThreeTag_yield.tex", "TwoTag_split_yield.tex"]
#     note_dir   = "figures/boosted/tables/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))


# ## for Section 8, CR/SB Variation systematics
#     lst_dir    = ["Moriond_CR_High", "Moriond_CR_Low", "Moriond_CR_Small", \
#     "Moriond_SB_Large", "Moriond_SB_Small", "Moriond_SB_High", "Moriond_SB_Low"]
#     lst_region = ["Tables"]
#     lst_type   = [""]
#     lst_plt    = ["FourTag_yield.tex", "ThreeTag_yield.tex", "TwoTag_split_yield.tex"]
#     note_dir   = "figures/boosted/tables/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir, prename=Dir.replace("Moriond_", "") + "_" + plt))
#     lst_region = ["Other"]
#     lst_type   = [""]
#     lst_plt    = ["Sideband_OneTag_mH0H1.pdf", "Control_OneTag_mH0H1.pdf"]
#     note_dir   = "figures/boosted/Syst_CRSB/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir, prename=Dir.replace("Moriond_", "") + "_" + plt))
#     ##this is the CR varaition tex
#     lst_dir    = ["Moriond"]
#     lst_region = ["Tables"]
#     lst_type   = ["FourTag_", "ThreeTag_", "TwoTag_split_"]
#     lst_plt    = ["CR_Varations.tex", "SR_Varations.tex"]
#     note_dir   = "figures/boosted/tables/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))

#     lst_dir    = ["Moriond"]
#     lst_region = ["FourTag_", "ThreeTag_", "TwoTag_split_"]
#     lst_type   = ["CR_High", "CR_Low", "CR_Small", "SB_Large", "SB_Small", "SB_High", "SB_Low"]
#     lst_plt    = ["qcd_hh.pdf"]
#     note_dir   = "figures/boosted/Syst_CRSB/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + "Syst" + "/" + Type + "_compare_" + region + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))

# ## For Section 8, smoothing systematics
#     lst_type   = ["QCDSysfitSmooth"]
#     lst_plt    = ["22.pdf", "33.pdf", "44.pdf", \
#     "ratio_22.pdf", "ratio_33.pdf", "ratio_44.pdf"]
#     note_dir   = "figures/boosted/Syst_Shape/"
#     note_name  = []
#     for Type in lst_type:
#         for i, plt in enumerate(lst_plt):
#             originpath = smoothsystpath + "/" + Type + "_" + plt
#             os.system(pack_copy(originpath, targetpath=notepath + note_dir))

#     lst_type   = ["smoothFuncCompare", "smoothFuncRangeCompare"]
#     lst_plt    = ["22_comp.pdf", "33_comp.pdf", "44_comp.pdf", \
#     "22_comp_ratio.pdf", "33_comp_ratio.pdf", "44_comp_ratio.pdf"]
#     note_dir   = "figures/boosted/Syst_Smooth/"
#     note_name  = []
#     for Type in lst_type:
#         for i, plt in enumerate(lst_plt):
#             originpath = smoothsystpath + "/" + Type + "_" + plt
#             os.system(pack_copy(originpath, targetpath=notepath + note_dir))

# ## For Section 8, 4b ttbar systematics    
#     lst_plt    = ["TopShapeSRSysfitSmooth_sig33_comp22_ratio.pdf",\
#     "TopShapeSRSysfitSmooth_sig33_comp22.pdf"]
#     note_dir   = "figures/boosted/Syst_Smooth/"
#     note_name  = []
#     for i, plt in enumerate(lst_plt):
#         originpath = smoothsystpath + "/" + plt
#         os.system(pack_copy(originpath, targetpath=notepath + note_dir))

# ## For Section 8, ZZ/TT systematics 
#     lst_dir    = ["Moriond_ZZ"]
#     lst_region = ["Signal"]
#     lst_type   = ["TwoTag_split_", "ThreeTag_", "FourTag_"]
#     lst_plt    = ["mHH_l_1.pdf", "leadHCand_Mass_s.pdf"]
#     note_dir   = "figures/boosted/ZZ/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Dir + "_" + Type + region + "_" + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))
#     lst_dir    = ["Moriond_ZZ"]
#     lst_region = ["Other"]
#     lst_plt    = ["Compare_NoTag_mH0H1.pdf"]
#     note_dir   = "figures/boosted/ZZ/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for i, plt in enumerate(lst_plt):
#                 originpath = plotpath + Dir + "/Plot/" + region + "/" + plt
#                 os.system(pack_copy(originpath, targetpath=notepath + note_dir))

#     lst_dir    = ["Moriond"]
#     lst_region = ["Tables"]
#     lst_type   = [""]
#     lst_plt    = ["ZZ_Signal_Region.tex"]
#     note_dir   = "figures/boosted/tables/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))

#     lst_dir    = ["Moriond_ZZ"]
#     lst_region = ["Tables"]
#     lst_type   = [""]
#     lst_plt    = ["FourTag_yield.tex", "ThreeTag_yield.tex", "TwoTag_split_yield.tex"]
#     note_dir   = "figures/boosted/tables/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir, prename=Dir + "_" + plt))

#     lst_dir    = ["Moriond_TT"]
#     lst_region = ["Signal"]
#     lst_type   = ["TwoTag_split_", "ThreeTag_", "FourTag_"]
#     lst_plt    = ["mHH_l_1.pdf", "leadHCand_Mass_s.pdf"]
#     note_dir   = "figures/boosted/TT/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Dir + "_" + Type + region + "_" + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))
#     lst_dir    = ["Moriond_TT"]
#     lst_region = ["Other"]
#     lst_plt    = ["Compare_NoTag_mH0H1.pdf"]
#     note_dir   = "figures/boosted/TT/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for i, plt in enumerate(lst_plt):
#                 originpath = plotpath + Dir + "/Plot/" + region + "/" + plt
#                 os.system(pack_copy(originpath, targetpath=notepath + note_dir))

#     lst_dir    = ["Moriond"]
#     lst_region = ["Tables"]
#     lst_type   = [""]
#     lst_plt    = ["TT_Signal_Region.tex"]
#     note_dir   = "figures/boosted/tables/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))

#     lst_dir    = ["Moriond_TT"]
#     lst_region = ["Tables"]
#     lst_type   = [""]
#     lst_plt    = ["FourTag_yield.tex", "ThreeTag_yield.tex", "TwoTag_split_yield.tex"]
#     note_dir   = "figures/boosted/tables/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir, prename=Dir + "_" + plt))

# ## For Section 8, systematcs summary

#     lst_dir    = ["Moriond_bkg_9"]
#     lst_region = ["Tables"]
#     lst_type   = ["TwoTag_split_", "ThreeTag_", "FourTag_"]
#     lst_plt    = ["fullsyst.tex"]
#     note_dir   = "figures/boosted/tables/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))

#     lst_dir    = ["Moriond_bkg_9"]
#     lst_region = ["Syst"]
#     lst_type   = ["TwoTag_split_", "ThreeTag_", "FourTag_"]
#     lst_plt    = ["RSG_syst.pdf"]
#     note_dir   = "figures/boosted/Syst_MC/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))

#     lst_dir    = ["Moriond_bkg_9"]
#     lst_region = ["Signal_Syst"]
#     lst_type   = ["TwoTag_split_", "ThreeTag_", "FourTag_"]
#     lst_plt    = ["Signal_mHH_pole_1_blind.pdf", "Signal_mHH_l_1_blind.pdf", "Signal_mHH_pole_blind.pdf", "Signal_mHH_l_blind.pdf"]
#     note_dir   = "figures/boosted/Signal_Syst/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Dir + "_" + Type + plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir))

# ## for Section 9, Limits; notice the date
#     lst_dir    = ["Moriond_bkg_9"]
#     lst_region = [""]
#     lst_type   = [""]
#     lst_plt    = [
#     # "BrazilPlot_Asymptotic_RSGC10_merged_2b.pdf", \
#     # "BrazilPlot_Asymptotic_RSGC10_merged_3b.pdf", \
#     # "BrazilPlot_Asymptotic_RSGC10_merged_4b.pdf", \
#     "BrazilPlot_Asymptotic_RSGC10_merged.pdf", \
#     "BrazilPlot_Asymptotic_RSGC20_merged.pdf", \
#     "BrazilPlot_Asymptotic_2HDM_merged.pdf"]
#     note_dir   = "figures/boosted/Limit_Stat/"
#     note_name  = []
#     for Dir in lst_dir:
#         for i, plt in enumerate(lst_plt):
#             originpath = limitplotpath + plt.replace(".pdf", "_test_TEST_2017-07-04.pdf")
#             os.system(pack_copy(originpath, targetpath=notepath + note_dir, prename=plt))

# #for Section 10 unBlinded Signal Regions
#     lst_dir    = ["Moriond_bkg_9"]
#     lst_region = ["Tables"]
#     lst_type   = [""]
#     lst_plt    = ["SR_summary.tex",\
#     ]
#     note_dir   = "figures/boosted/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" +  plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir + region + "/"))

    # lst_dir    = ["Moriond_bkg_9"]
    # lst_region = ["Tables"]
    # lst_type   = ["FourTag", "ThreeTag", "TwoTag_split"]
    # lst_plt    = ["Signal_mHH_l_SR_region_compare.tex", "Signal_mHH_pole_SR_region_compare.tex"\
    # ]
    # note_dir   = "figures/boosted/"
    # note_name  = []
    # for Dir in lst_dir:
    #     for region in lst_region:
    #         for Type in lst_type:
    #             for i, plt in enumerate(lst_plt):
    #                 originpath = plotpath + Dir + "/Plot/" + region + "/" + Type + "_" +  plt
    #                 os.system(pack_copy(originpath, targetpath=notepath + note_dir + region + "/"))

    # lst_dir    = ["Moriond_bkg_9"]
    # lst_region = ["Signal_Syst"]
    # lst_type   = ["TwoTag_split_", "ThreeTag_", "FourTag_"]
    # lst_plt    = ["Signal_mHH_pole_1.pdf", "Signal_mHH_l_1.pdf", "Signal_mHH_pole.pdf", "Signal_mHH_l.pdf"]
    # note_dir   = "figures/boosted/Signal_Syst/"
    # note_name  = []
    # for Dir in lst_dir:
    #     for region in lst_region:
    #         for Type in lst_type:
    #             for i, plt in enumerate(lst_plt):
    #                 originpath = plotpath + Dir + "/Plot/" + region + "/" + Dir + "_" + Type + plt
    #                 os.system(pack_copy(originpath, targetpath=notepath + note_dir))

    # lst_dir    = ["Moriond_bkg_9"]
    # lst_region = ["Signal"]
    # lst_type   = ["FourTag_", "ThreeTag_", "TwoTag_split_"]
    # # lst_plt    = ["leadHCand_ntrk.pdf", "sublHCand_ntrk.pdf"]
    # lst_plt    = ["leadHCand_Pt_m.pdf", "leadHCand_Mass_s.pdf", "leadHCand_Eta.pdf", "leadHCand_Phi.pdf",\
    # "sublHCand_Pt_m.pdf", "sublHCand_Mass_s.pdf", "sublHCand_Eta.pdf", "sublHCand_Phi.pdf",\
    # "leadHCand_trk0_Pt.pdf", "leadHCand_trk1_Pt.pdf",\
    # "sublHCand_trk0_Pt.pdf", "sublHCand_trk1_Pt.pdf",\
    # "leadHCand_trk_dr.pdf",  "sublHCand_trk_dr.pdf",\
    # "mHH_l_1.pdf", "hCandDr.pdf", "hCandDeta.pdf", "hCandDphi.pdf",\
    # # ]
    # note_dir   = "figures/boosted/"
    # note_name  = []
    # for Dir in lst_dir:
    #     for region in lst_region:
    #         for Type in lst_type:
    #             for i, plt in enumerate(lst_plt):
    #                 originpath = plotpath + Dir + "/Plot/" + region + "/" + Dir + "_" + Type + region + "_" +  plt
    #                 os.system(pack_copy(originpath, targetpath=notepath + note_dir + region + "/", prename=str("b77_" + Type + region + "_" +  plt)))


# # ## for Appendix, Signal distributions
#     lst_dir    = ["Moriond"]
#     lst_region = ["Truth"]
#     lst_type   = ["FourTag_", "ThreeTag_", "TwoTag_split_"]
#     lst_plt    = ["leadHCand_Pt_m.pdf", "leadHCand_Mass_s.pdf",\
#     "sublHCand_Pt_m.pdf", "sublHCand_Mass_s.pdf",\
#     "leadHCand_trk0_Pt.pdf", "leadHCand_trk1_Pt.pdf",\
#     "sublHCand_trk0_Pt.pdf", "sublHCand_trk1_Pt.pdf",\
#     "mHH_l.pdf", "hCandDr.pdf",\
#     ]
#     note_dir   = "figures/boosted/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + region + "/" + Dir + "_comp_0_" + Type + "Signal" + "_" +  plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir + region + "/"))

# # ## for Appendix, Reweighting weights
#     lst_dir    = ["Moriond_bkg_9"]
#     lst_region = ["Signal", "Sideband"]
#     lst_type   = ["4Trk", "3Trk", "2Trk_split"]
#     lst_plt    = ["leadHCand_Pt_m_weight_projy.pdf", \
#     # "mHH_l_weight.pdf", "mHH_l_weight_profy.pdf", "mHH_l_weight_profx.pdf",\
#     # "leadHCand_Pt_m_weight.pdf", "leadHCand_Pt_m_weight_profy.pdf", "leadHCand_Pt_m_weight_profx.pdf",\
#     # "leadHCand_trk0_Pt_weight.pdf", "leadHCand_trk0_Pt_weight_profy.pdf", "leadHCand_trk0_Pt_weight_profx.pdf",\
#     "sublHCand_trk1_Pt_weight.pdf", "sublHCand_trk1_Pt_weight_profy.pdf", "sublHCand_trk1_Pt_weight_profx.pdf",\
#     ]
#     note_dir   = "figures/boosted/Appendix-Reweight/Weights/"
#     note_name  = []
#     for Dir in lst_dir:
#         for region in lst_region:
#             for Type in lst_type:
#                 for i, plt in enumerate(lst_plt):
#                     originpath = plotpath + Dir + "/Plot/" + "Other" + "/" + Type + "_" + region + "_" +  plt
#                     os.system(pack_copy(originpath, targetpath=notepath + note_dir + "/"))



    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__': 
    main()