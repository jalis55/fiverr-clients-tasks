** Generated for: hspiceD
** Generated on: Mar 22 22:48:39 2022
** Design library name: test
** Design cell name: SRAM_8T_128
** Design view name: schematic


.IC
+    V(q<127>)=1.2
+    V(q<126>)=1.2
+    V(q<125>)=1.2
+    V(q<124>)=1.2
+    V(q<123>)=1.2
+    V(q<122>)=1.2
+    V(q<121>)=1.2
+    V(q<120>)=1.2
+    V(q<119>)=1.2
+    V(q<118>)=1.2
+    V(q<117>)=1.2
+    V(q<116>)=1.2
+    V(q<115>)=1.2
+    V(q<114>)=1.2
+    V(q<113>)=1.2
+    V(q<112>)=1.2
+    V(q<111>)=1.2
+    V(q<110>)=1.2
+    V(q<109>)=1.2
+    V(q<108>)=1.2
+    V(q<107>)=1.2
+    V(q<106>)=1.2
+    V(q<105>)=1.2
+    V(q<104>)=1.2
+    V(q<103>)=1.2
+    V(q<102>)=1.2
+    V(q<101>)=1.2
+    V(q<100>)=1.2
+    V(q<99>)=1.2
+    V(q<98>)=1.2
+    V(q<97>)=1.2
+    V(q<96>)=1.2
+    V(q<95>)=1.2
+    V(q<94>)=1.2
+    V(q<93>)=1.2
+    V(q<92>)=1.2
+    V(q<91>)=1.2
+    V(q<90>)=1.2
+    V(q<89>)=1.2
+    V(q<88>)=1.2
+    V(q<87>)=1.2
+    V(q<86>)=1.2
+    V(q<85>)=1.2
+    V(q<84>)=1.2
+    V(q<83>)=1.2
+    V(q<82>)=1.2
+    V(q<81>)=1.2
+    V(q<80>)=1.2
+    V(q<79>)=1.2
+    V(q<78>)=1.2
+    V(q<77>)=1.2
+    V(q<76>)=1.2
+    V(q<75>)=1.2
+    V(q<74>)=1.2
+    V(q<73>)=1.2
+    V(q<72>)=1.2
+    V(q<71>)=1.2
+    V(q<70>)=1.2
+    V(q<69>)=1.2
+    V(q<68>)=1.2
+    V(q<67>)=1.2
+    V(q<66>)=1.2
+    V(q<65>)=1.2
+    V(q<64>)=1.2
+    V(q<63>)=1.2
+    V(q<62>)=1.2
+    V(q<61>)=1.2
+    V(q<60>)=1.2
+    V(q<59>)=1.2
+    V(q<58>)=1.2
+    V(q<57>)=1.2
+    V(q<56>)=1.2
+    V(q<55>)=1.2
+    V(q<54>)=1.2
+    V(q<53>)=1.2
+    V(q<52>)=1.2
+    V(q<51>)=1.2
+    V(q<50>)=1.2
+    V(q<49>)=1.2
+    V(q<48>)=1.2
+    V(q<47>)=1.2
+    V(q<46>)=1.2
+    V(q<45>)=1.2
+    V(q<44>)=1.2
+    V(q<43>)=1.2
+    V(q<42>)=1.2
+    V(q<41>)=1.2
+    V(q<40>)=1.2
+    V(q<39>)=1.2
+    V(q<38>)=1.2
+    V(q<37>)=1.2
+    V(q<36>)=1.2
+    V(q<35>)=1.2
+    V(q<34>)=1.2
+    V(q<33>)=1.2
+    V(q<32>)=1.2
+    V(q<31>)=1.2
+    V(q<30>)=1.2
+    V(q<29>)=1.2
+    V(q<28>)=1.2
+    V(q<27>)=1.2
+    V(q<26>)=1.2
+    V(q<25>)=1.2
+    V(q<24>)=1.2
+    V(q<23>)=1.2
+    V(q<22>)=1.2
+    V(q<21>)=1.2
+    V(q<20>)=1.2
+    V(q<19>)=1.2
+    V(q<18>)=1.2
+    V(q<17>)=1.2
+    V(q<16>)=1.2
+    V(q<15>)=1.2
+    V(q<14>)=1.2
+    V(q<13>)=1.2
+    V(q<12>)=1.2
+    V(q<11>)=1.2
+    V(q<10>)=1.2
+    V(q<9>)=1.2
+    V(q<8>)=1.2
+    V(q<7>)=1.2
+    V(q<6>)=1.2
+    V(q<5>)=1.2
+    V(q<4>)=1.2
+    V(q<3>)=1.2
+    V(q<2>)=1.2
+    V(q<1>)=1.2
+    V(q<0>)=1.2
.PROBE TRAN
+    V(cwl<0>)
+    V(cbl)
.TRAN 100e-12 10e-9 START=0.0

.TEMP 25.0
.OPTION
+    ARTIST=2
+    INGOLD=2
+    PARHIER=LOCAL
+    PSF=2
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_bip
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_dio
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_dio_33
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_mim
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_dio_dnw
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_dio_18
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_bip_npn
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_33
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_rfrtmom
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_mos_cap_25
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_18
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_disres
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_res
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_dio_na
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_rfmos_33
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_dio_hvt
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_rfmvar
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_rfmos_18
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_na
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_dio_na33
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_dio_lvt
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_rfres_sa
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_na33
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_dio_esd
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_rfmim
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_dio_25od33
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_25od33
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_mos_cap
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_dio_25
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_dio_25ud18
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_25
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_rfmos
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_25ud18
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_dio_na25od33
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_rfjvar
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_rfmos_25
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_rtmom
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_na25od33
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_dio_na25
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_rfres_rpo
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_hvt
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_rfind
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_rfmvar_25
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_na25
.LIB "/mnt/hgfs/Exchange/tsmc_pdk/TSMC65/pdk/Cadence_OA/tn65cmsp018k3_1_0c/models/hspice/crn65gplus_2d5_lk_v1d0.l" tt_lvt

** Library name: W4M09Y21_4
** Cell name: SRAM
** View name: schematic
.subckt SRAM q wl bl blb vdd_1 gnd_1
m7 qb q vdd_1 vdd_1 pch l=65e-9 w=290e-9 m=1 nf=1 sd=200e-9 ad=50.75e-15 as=50.75e-15 pd=930e-9 ps=930e-9 nrd=344.828e-3 nrs=344.828e-3 sa=175e-9 sb=175e-9 sca=0 scb=0 scc=0
m6 q qb vdd_1 vdd_1 pch l=65e-9 w=290e-9 m=1 nf=1 sd=200e-9 ad=50.75e-15 as=50.75e-15 pd=930e-9 ps=930e-9 nrd=344.828e-3 nrs=344.828e-3 sa=175e-9 sb=175e-9 sca=0 scb=0 scc=0
m4 blb wl qb gnd_1 nch l=65e-9 w=120e-9 m=1 nf=1 sd=350e-9 ad=34.5e-15 as=34.5e-15 pd=800e-9 ps=800e-9 nrd=1.45833 nrs=1.45833 sa=100e-9 sb=100e-9 sca=0 scb=0 scc=0
m1 qb q gnd_1 gnd_1 nch l=65e-9 w=290e-9 m=1 nf=1 sd=200e-9 ad=50.75e-15 as=50.75e-15 pd=930e-9 ps=930e-9 nrd=344.828e-3 nrs=344.828e-3 sa=175e-9 sb=175e-9 sca=0 scb=0 scc=0
m0 q qb gnd_1 gnd_1 nch l=65e-9 w=290e-9 m=1 nf=1 sd=200e-9 ad=50.75e-15 as=50.75e-15 pd=930e-9 ps=930e-9 nrd=344.828e-3 nrs=344.828e-3 sa=175e-9 sb=175e-9 sca=0 scb=0 scc=0
m5 q wl bl gnd_1 nch l=65e-9 w=120e-9 m=1 nf=1 sd=350e-9 ad=34.5e-15 as=34.5e-15 pd=800e-9 ps=800e-9 nrd=1.45833 nrs=1.45833 sa=100e-9 sb=100e-9 sca=0 scb=0 scc=0
.ends SRAM
** End of subcircuit definition.

** Library name: SRAM_8T_128
** Cell name: SRAM_8T
** View name: schematic
.subckt SRAM_8T q cwl cbl wl bl blb vdd_1 gnd_1
xi0 q wl bl blb vdd_1 gnd_1 SRAM
xm1 cbl cwl net12 gnd_1 nch_mac l=65e-9 w=200e-9 multi=1 nf=1 sigma=1 sd=200e-9 ad=35e-15 as=35e-15 pd=750e-9 ps=750e-9 nrd=500e-3 nrs=500e-3 sa=175e-9 sb=175e-9 sca=0 scb=0 scc=0 mismatchflag=1
xm0 net12 q gnd_1 gnd_1 nch_mac l=65e-9 w=200e-9 multi=1 nf=1 sigma=1 sd=200e-9 ad=35e-15 as=35e-15 pd=750e-9 ps=750e-9 nrd=500e-3 nrs=500e-3 sa=175e-9 sb=175e-9 sca=0 scb=0 scc=0 mismatchflag=1
.ends SRAM_8T
** End of subcircuit definition.

** Library name: SRAM_8T_128
** Cell name: SRAM_Array_128
** View name: schematic
.subckt SRAM_Array_128 q<127> q<126> q<125> q<124> q<123> q<122> q<121> q<120> q<119> q<118> q<117> q<116> q<115> q<114> q<113> q<112> q<111> q<110> q<109> q<108> q<107> q<106> q<105> q<104> q<103> q<102> q<101> q<100> q<99> q<98> q<97> q<96> q<95> q<94> q<93> q<92> q<91> q<90> q<89> q<88> q<87> q<86> q<85> q<84> q<83> q<82> q<81> q<80> q<79> q<78> q<77> q<76> q<75> q<74> q<73> q<72> q<71> q<70> q<69> q<68> q<67> q<66> q<65> q<64> q<63> q<62> q<61> q<60> q<59> q<58> q<57> q<56> q<55> q<54> q<53> q<52> q<51> q<50> q<49> q<48> q<47> q<46> q<45> q<44> q<43> q<42> q<41> q<40> q<39> q<38> q<37> q<36> q<35> q<34> q<33> q<32> q<31> q<30> q<29> q<28> q<27> q<26> q<25> q<24> q<23> q<22> q<21> q<20> q<19> q<18> q<17> q<16> q<15> q<14> q<13> q<12> q<11> q<10> q<9> q<8> q<7> q<6> q<5> q<4> q<3> q<2> q<1> q<0> cwl<127> cwl<126> cwl<125> cwl<124> cwl<123> cwl<122> cwl<121> cwl<120> cwl<119> cwl<118> cwl<117> cwl<116> cwl<115> cwl<114> cwl<113> cwl<112> cwl<111> cwl<110> cwl<109> cwl<108> cwl<107> cwl<106> cwl<105>
+cwl<104> cwl<103> cwl<102> cwl<101> cwl<100> cwl<99> cwl<98> cwl<97> cwl<96> cwl<95> cwl<94> cwl<93> cwl<92> cwl<91> cwl<90> cwl<89> cwl<88> cwl<87> cwl<86> cwl<85> cwl<84> cwl<83> cwl<82> cwl<81> cwl<80> cwl<79> cwl<78> cwl<77> cwl<76> cwl<75> cwl<74> cwl<73> cwl<72> cwl<71> cwl<70> cwl<69> cwl<68> cwl<67> cwl<66> cwl<65> cwl<64> cwl<63> cwl<62> cwl<61> cwl<60> cwl<59> cwl<58> cwl<57> cwl<56> cwl<55> cwl<54> cwl<53> cwl<52> cwl<51> cwl<50> cwl<49> cwl<48> cwl<47> cwl<46> cwl<45> cwl<44> cwl<43> cwl<42> cwl<41> cwl<40> cwl<39> cwl<38> cwl<37> cwl<36> cwl<35> cwl<34> cwl<33> cwl<32> cwl<31> cwl<30> cwl<29> cwl<28> cwl<27> cwl<26> cwl<25> cwl<24> cwl<23> cwl<22> cwl<21> cwl<20> cwl<19> cwl<18> cwl<17> cwl<16> cwl<15> cwl<14> cwl<13> cwl<12> cwl<11> cwl<10> cwl<9> cwl<8> cwl<7> cwl<6> cwl<5> cwl<4> cwl<3> cwl<2> cwl<1> cwl<0> cbl wl<127> wl<126> wl<125> wl<124> wl<123> wl<122> wl<121> wl<120> wl<119> wl<118> wl<117> wl<116> wl<115> wl<114> wl<113> wl<112> wl<111> wl<110> wl<109> wl<108> wl<107> wl<106> wl<105> 
+wl<104> wl<103> wl<102> wl<101> wl<100> wl<99> wl<98> wl<97> wl<96> wl<95> wl<94> wl<93> wl<92> wl<91> wl<90> wl<89> wl<88> wl<87> wl<86> wl<85> wl<84> wl<83> wl<82> wl<81> wl<80> wl<79> wl<78> wl<77> wl<76> wl<75> wl<74> wl<73> wl<72> wl<71> wl<70> wl<69> wl<68> wl<67> wl<66> wl<65> wl<64> wl<63> wl<62> wl<61> wl<60> wl<59> wl<58> wl<57> wl<56> wl<55> wl<54> wl<53> wl<52> wl<51> wl<50> wl<49> wl<48> wl<47> wl<46> wl<45> wl<44> wl<43> wl<42> wl<41> wl<40> wl<39> wl<38> wl<37> wl<36> wl<35> wl<34> wl<33> wl<32> wl<31> wl<30> wl<29> wl<28> wl<27> wl<26> wl<25> wl<24> wl<23> wl<22> wl<21> wl<20> wl<19> wl<18> wl<17> wl<16> wl<15> wl<14> wl<13> wl<12> wl<11> wl<10> wl<9> wl<8> wl<7> wl<6> wl<5> wl<4> wl<3> wl<2> wl<1> wl<0> bl blb vdd_1 gnd_1
xi127 q<127> cwl<127> cbl wl<127> bl blb vdd_1 gnd_1 SRAM_8T
xi126 q<126> cwl<126> cbl wl<126> bl blb vdd_1 gnd_1 SRAM_8T
xi125 q<125> cwl<125> cbl wl<125> bl blb vdd_1 gnd_1 SRAM_8T
xi124 q<124> cwl<124> cbl wl<124> bl blb vdd_1 gnd_1 SRAM_8T
xi123 q<123> cwl<123> cbl wl<123> bl blb vdd_1 gnd_1 SRAM_8T
xi122 q<122> cwl<122> cbl wl<122> bl blb vdd_1 gnd_1 SRAM_8T
xi121 q<121> cwl<121> cbl wl<121> bl blb vdd_1 gnd_1 SRAM_8T
xi120 q<120> cwl<120> cbl wl<120> bl blb vdd_1 gnd_1 SRAM_8T
xi119 q<119> cwl<119> cbl wl<119> bl blb vdd_1 gnd_1 SRAM_8T
xi118 q<118> cwl<118> cbl wl<118> bl blb vdd_1 gnd_1 SRAM_8T
xi117 q<117> cwl<117> cbl wl<117> bl blb vdd_1 gnd_1 SRAM_8T
xi116 q<116> cwl<116> cbl wl<116> bl blb vdd_1 gnd_1 SRAM_8T
xi115 q<115> cwl<115> cbl wl<115> bl blb vdd_1 gnd_1 SRAM_8T
xi114 q<114> cwl<114> cbl wl<114> bl blb vdd_1 gnd_1 SRAM_8T
xi113 q<113> cwl<113> cbl wl<113> bl blb vdd_1 gnd_1 SRAM_8T
xi112 q<112> cwl<112> cbl wl<112> bl blb vdd_1 gnd_1 SRAM_8T
xi111 q<111> cwl<111> cbl wl<111> bl blb vdd_1 gnd_1 SRAM_8T
xi110 q<110> cwl<110> cbl wl<110> bl blb vdd_1 gnd_1 SRAM_8T
xi109 q<109> cwl<109> cbl wl<109> bl blb vdd_1 gnd_1 SRAM_8T
xi108 q<108> cwl<108> cbl wl<108> bl blb vdd_1 gnd_1 SRAM_8T
xi107 q<107> cwl<107> cbl wl<107> bl blb vdd_1 gnd_1 SRAM_8T
xi106 q<106> cwl<106> cbl wl<106> bl blb vdd_1 gnd_1 SRAM_8T
xi105 q<105> cwl<105> cbl wl<105> bl blb vdd_1 gnd_1 SRAM_8T
xi104 q<104> cwl<104> cbl wl<104> bl blb vdd_1 gnd_1 SRAM_8T
xi103 q<103> cwl<103> cbl wl<103> bl blb vdd_1 gnd_1 SRAM_8T
xi102 q<102> cwl<102> cbl wl<102> bl blb vdd_1 gnd_1 SRAM_8T
xi101 q<101> cwl<101> cbl wl<101> bl blb vdd_1 gnd_1 SRAM_8T
xi100 q<100> cwl<100> cbl wl<100> bl blb vdd_1 gnd_1 SRAM_8T
xi99 q<99> cwl<99> cbl wl<99> bl blb vdd_1 gnd_1 SRAM_8T
xi98 q<98> cwl<98> cbl wl<98> bl blb vdd_1 gnd_1 SRAM_8T
xi97 q<97> cwl<97> cbl wl<97> bl blb vdd_1 gnd_1 SRAM_8T
xi96 q<96> cwl<96> cbl wl<96> bl blb vdd_1 gnd_1 SRAM_8T
xi95 q<95> cwl<95> cbl wl<95> bl blb vdd_1 gnd_1 SRAM_8T
xi94 q<94> cwl<94> cbl wl<94> bl blb vdd_1 gnd_1 SRAM_8T
xi93 q<93> cwl<93> cbl wl<93> bl blb vdd_1 gnd_1 SRAM_8T
xi92 q<92> cwl<92> cbl wl<92> bl blb vdd_1 gnd_1 SRAM_8T
xi91 q<91> cwl<91> cbl wl<91> bl blb vdd_1 gnd_1 SRAM_8T
xi90 q<90> cwl<90> cbl wl<90> bl blb vdd_1 gnd_1 SRAM_8T
xi89 q<89> cwl<89> cbl wl<89> bl blb vdd_1 gnd_1 SRAM_8T
xi88 q<88> cwl<88> cbl wl<88> bl blb vdd_1 gnd_1 SRAM_8T
xi87 q<87> cwl<87> cbl wl<87> bl blb vdd_1 gnd_1 SRAM_8T
xi86 q<86> cwl<86> cbl wl<86> bl blb vdd_1 gnd_1 SRAM_8T
xi85 q<85> cwl<85> cbl wl<85> bl blb vdd_1 gnd_1 SRAM_8T
xi84 q<84> cwl<84> cbl wl<84> bl blb vdd_1 gnd_1 SRAM_8T
xi83 q<83> cwl<83> cbl wl<83> bl blb vdd_1 gnd_1 SRAM_8T
xi82 q<82> cwl<82> cbl wl<82> bl blb vdd_1 gnd_1 SRAM_8T
xi81 q<81> cwl<81> cbl wl<81> bl blb vdd_1 gnd_1 SRAM_8T
xi80 q<80> cwl<80> cbl wl<80> bl blb vdd_1 gnd_1 SRAM_8T
xi79 q<79> cwl<79> cbl wl<79> bl blb vdd_1 gnd_1 SRAM_8T
xi78 q<78> cwl<78> cbl wl<78> bl blb vdd_1 gnd_1 SRAM_8T
xi77 q<77> cwl<77> cbl wl<77> bl blb vdd_1 gnd_1 SRAM_8T
xi76 q<76> cwl<76> cbl wl<76> bl blb vdd_1 gnd_1 SRAM_8T
xi75 q<75> cwl<75> cbl wl<75> bl blb vdd_1 gnd_1 SRAM_8T
xi74 q<74> cwl<74> cbl wl<74> bl blb vdd_1 gnd_1 SRAM_8T
xi73 q<73> cwl<73> cbl wl<73> bl blb vdd_1 gnd_1 SRAM_8T
xi72 q<72> cwl<72> cbl wl<72> bl blb vdd_1 gnd_1 SRAM_8T
xi71 q<71> cwl<71> cbl wl<71> bl blb vdd_1 gnd_1 SRAM_8T
xi70 q<70> cwl<70> cbl wl<70> bl blb vdd_1 gnd_1 SRAM_8T
xi69 q<69> cwl<69> cbl wl<69> bl blb vdd_1 gnd_1 SRAM_8T
xi68 q<68> cwl<68> cbl wl<68> bl blb vdd_1 gnd_1 SRAM_8T
xi67 q<67> cwl<67> cbl wl<67> bl blb vdd_1 gnd_1 SRAM_8T
xi66 q<66> cwl<66> cbl wl<66> bl blb vdd_1 gnd_1 SRAM_8T
xi65 q<65> cwl<65> cbl wl<65> bl blb vdd_1 gnd_1 SRAM_8T
xi64 q<64> cwl<64> cbl wl<64> bl blb vdd_1 gnd_1 SRAM_8T
xi63 q<63> cwl<63> cbl wl<63> bl blb vdd_1 gnd_1 SRAM_8T
xi62 q<62> cwl<62> cbl wl<62> bl blb vdd_1 gnd_1 SRAM_8T
xi61 q<61> cwl<61> cbl wl<61> bl blb vdd_1 gnd_1 SRAM_8T
xi60 q<60> cwl<60> cbl wl<60> bl blb vdd_1 gnd_1 SRAM_8T
xi59 q<59> cwl<59> cbl wl<59> bl blb vdd_1 gnd_1 SRAM_8T
xi58 q<58> cwl<58> cbl wl<58> bl blb vdd_1 gnd_1 SRAM_8T
xi57 q<57> cwl<57> cbl wl<57> bl blb vdd_1 gnd_1 SRAM_8T
xi56 q<56> cwl<56> cbl wl<56> bl blb vdd_1 gnd_1 SRAM_8T
xi55 q<55> cwl<55> cbl wl<55> bl blb vdd_1 gnd_1 SRAM_8T
xi54 q<54> cwl<54> cbl wl<54> bl blb vdd_1 gnd_1 SRAM_8T
xi53 q<53> cwl<53> cbl wl<53> bl blb vdd_1 gnd_1 SRAM_8T
xi52 q<52> cwl<52> cbl wl<52> bl blb vdd_1 gnd_1 SRAM_8T
xi51 q<51> cwl<51> cbl wl<51> bl blb vdd_1 gnd_1 SRAM_8T
xi50 q<50> cwl<50> cbl wl<50> bl blb vdd_1 gnd_1 SRAM_8T
xi49 q<49> cwl<49> cbl wl<49> bl blb vdd_1 gnd_1 SRAM_8T
xi48 q<48> cwl<48> cbl wl<48> bl blb vdd_1 gnd_1 SRAM_8T
xi47 q<47> cwl<47> cbl wl<47> bl blb vdd_1 gnd_1 SRAM_8T
xi46 q<46> cwl<46> cbl wl<46> bl blb vdd_1 gnd_1 SRAM_8T
xi45 q<45> cwl<45> cbl wl<45> bl blb vdd_1 gnd_1 SRAM_8T
xi44 q<44> cwl<44> cbl wl<44> bl blb vdd_1 gnd_1 SRAM_8T
xi43 q<43> cwl<43> cbl wl<43> bl blb vdd_1 gnd_1 SRAM_8T
xi42 q<42> cwl<42> cbl wl<42> bl blb vdd_1 gnd_1 SRAM_8T
xi41 q<41> cwl<41> cbl wl<41> bl blb vdd_1 gnd_1 SRAM_8T
xi40 q<40> cwl<40> cbl wl<40> bl blb vdd_1 gnd_1 SRAM_8T
xi39 q<39> cwl<39> cbl wl<39> bl blb vdd_1 gnd_1 SRAM_8T
xi38 q<38> cwl<38> cbl wl<38> bl blb vdd_1 gnd_1 SRAM_8T
xi37 q<37> cwl<37> cbl wl<37> bl blb vdd_1 gnd_1 SRAM_8T
xi36 q<36> cwl<36> cbl wl<36> bl blb vdd_1 gnd_1 SRAM_8T
xi35 q<35> cwl<35> cbl wl<35> bl blb vdd_1 gnd_1 SRAM_8T
xi34 q<34> cwl<34> cbl wl<34> bl blb vdd_1 gnd_1 SRAM_8T
xi33 q<33> cwl<33> cbl wl<33> bl blb vdd_1 gnd_1 SRAM_8T
xi32 q<32> cwl<32> cbl wl<32> bl blb vdd_1 gnd_1 SRAM_8T
xi31 q<31> cwl<31> cbl wl<31> bl blb vdd_1 gnd_1 SRAM_8T
xi30 q<30> cwl<30> cbl wl<30> bl blb vdd_1 gnd_1 SRAM_8T
xi29 q<29> cwl<29> cbl wl<29> bl blb vdd_1 gnd_1 SRAM_8T
xi28 q<28> cwl<28> cbl wl<28> bl blb vdd_1 gnd_1 SRAM_8T
xi27 q<27> cwl<27> cbl wl<27> bl blb vdd_1 gnd_1 SRAM_8T
xi26 q<26> cwl<26> cbl wl<26> bl blb vdd_1 gnd_1 SRAM_8T
xi25 q<25> cwl<25> cbl wl<25> bl blb vdd_1 gnd_1 SRAM_8T
xi24 q<24> cwl<24> cbl wl<24> bl blb vdd_1 gnd_1 SRAM_8T
xi23 q<23> cwl<23> cbl wl<23> bl blb vdd_1 gnd_1 SRAM_8T
xi22 q<22> cwl<22> cbl wl<22> bl blb vdd_1 gnd_1 SRAM_8T
xi21 q<21> cwl<21> cbl wl<21> bl blb vdd_1 gnd_1 SRAM_8T
xi20 q<20> cwl<20> cbl wl<20> bl blb vdd_1 gnd_1 SRAM_8T
xi19 q<19> cwl<19> cbl wl<19> bl blb vdd_1 gnd_1 SRAM_8T
xi18 q<18> cwl<18> cbl wl<18> bl blb vdd_1 gnd_1 SRAM_8T
xi17 q<17> cwl<17> cbl wl<17> bl blb vdd_1 gnd_1 SRAM_8T
xi16 q<16> cwl<16> cbl wl<16> bl blb vdd_1 gnd_1 SRAM_8T
xi15 q<15> cwl<15> cbl wl<15> bl blb vdd_1 gnd_1 SRAM_8T
xi14 q<14> cwl<14> cbl wl<14> bl blb vdd_1 gnd_1 SRAM_8T
xi13 q<13> cwl<13> cbl wl<13> bl blb vdd_1 gnd_1 SRAM_8T
xi12 q<12> cwl<12> cbl wl<12> bl blb vdd_1 gnd_1 SRAM_8T
xi11 q<11> cwl<11> cbl wl<11> bl blb vdd_1 gnd_1 SRAM_8T
xi10 q<10> cwl<10> cbl wl<10> bl blb vdd_1 gnd_1 SRAM_8T
xi9 q<9> cwl<9> cbl wl<9> bl blb vdd_1 gnd_1 SRAM_8T
xi8 q<8> cwl<8> cbl wl<8> bl blb vdd_1 gnd_1 SRAM_8T
xi7 q<7> cwl<7> cbl wl<7> bl blb vdd_1 gnd_1 SRAM_8T
xi6 q<6> cwl<6> cbl wl<6> bl blb vdd_1 gnd_1 SRAM_8T
xi5 q<5> cwl<5> cbl wl<5> bl blb vdd_1 gnd_1 SRAM_8T
xi4 q<4> cwl<4> cbl wl<4> bl blb vdd_1 gnd_1 SRAM_8T
xi3 q<3> cwl<3> cbl wl<3> bl blb vdd_1 gnd_1 SRAM_8T
xi2 q<2> cwl<2> cbl wl<2> bl blb vdd_1 gnd_1 SRAM_8T
xi1 q<1> cwl<1> cbl wl<1> bl blb vdd_1 gnd_1 SRAM_8T
xi0 q<0> cwl<0> cbl wl<0> bl blb vdd_1 gnd_1 SRAM_8T
.ends SRAM_Array_128
** End of subcircuit definition.

** Library name: test
** Cell name: SRAM_8T_128
** View name: schematic
xi0 q<127> q<126> q<125> q<124> q<123> q<122> q<121> q<120> q<119> q<118> q<117> q<116> q<115> q<114> q<113> q<112> q<111> q<110> q<109> q<108> q<107> q<106> q<105> q<104> q<103> q<102> q<101> q<100> q<99> q<98> q<97> q<96> q<95> q<94> q<93> q<92> q<91> q<90> q<89> q<88> q<87> q<86> q<85> q<84> q<83> q<82> q<81> q<80> q<79> q<78> q<77> q<76> q<75> q<74> q<73> q<72> q<71> q<70> q<69> q<68> q<67> q<66> q<65> q<64> q<63> q<62> q<61> q<60> q<59> q<58> q<57> q<56> q<55> q<54> q<53> q<52> q<51> q<50> q<49> q<48> q<47> q<46> q<45> q<44> q<43> q<42> q<41> q<40> q<39> q<38> q<37> q<36> q<35> q<34> q<33> q<32> q<31> q<30> q<29> q<28> q<27> q<26> q<25> q<24> q<23> q<22> q<21> q<20> q<19> q<18> q<17> q<16> q<15> q<14> q<13> q<12> q<11> q<10> q<9> q<8> q<7> q<6> q<5> q<4> q<3> q<2> q<1> q<0> cwl<127> cwl<126> cwl<125> cwl<124> cwl<123> cwl<122> cwl<121> cwl<120> cwl<119> cwl<118> cwl<117> cwl<116> cwl<115> cwl<114> cwl<113> cwl<112> cwl<111> cwl<110> cwl<109> cwl<108> cwl<107> cwl<106> cwl<105> cwl<104> cwl<103> cwl<102> 
+cwl<101> cwl<100> cwl<99> cwl<98> cwl<97> cwl<96> cwl<95> cwl<94> cwl<93> cwl<92> cwl<91> cwl<90> cwl<89> cwl<88> cwl<87> cwl<86> cwl<85> cwl<84> cwl<83> cwl<82> cwl<81> cwl<80> cwl<79> cwl<78> cwl<77> cwl<76> cwl<75> cwl<74> cwl<73> cwl<72> cwl<71> cwl<70> cwl<69> cwl<68> cwl<67> cwl<66> cwl<65> cwl<64> cwl<63> cwl<62> cwl<61> cwl<60> cwl<59> cwl<58> cwl<57> cwl<56> cwl<55> cwl<54> cwl<53> cwl<52> cwl<51> cwl<50> cwl<49> cwl<48> cwl<47> cwl<46> cwl<45> cwl<44> cwl<43> cwl<42> cwl<41> cwl<40> cwl<39> cwl<38> cwl<37> cwl<36> cwl<35> cwl<34> cwl<33> cwl<32> cwl<31> cwl<30> cwl<29> cwl<28> cwl<27> cwl<26> cwl<25> cwl<24> cwl<23> cwl<22> cwl<21> cwl<20> cwl<19> cwl<18> cwl<17> cwl<16> cwl<15> cwl<14> cwl<13> cwl<12> cwl<11> cwl<10> cwl<9> cwl<8> cwl<7> cwl<6> cwl<5> cwl<4> cwl<3> cwl<2> cwl<1> cwl<0> cbl wl<127> wl<126> wl<125> wl<124> wl<123> wl<122> wl<121> wl<120> wl<119> wl<118> wl<117> wl<116> wl<115> wl<114> wl<113> wl<112> wl<111> wl<110> wl<109> wl<108> wl<107> wl<106> wl<105> wl<104> wl<103> wl<102>
+wl<101> wl<100> wl<99> wl<98> wl<97> wl<96> wl<95> wl<94> wl<93> wl<92> wl<91> wl<90> wl<89> wl<88> wl<87> wl<86> wl<85> wl<84> wl<83> wl<82> wl<81> wl<80> wl<79> wl<78> wl<77> wl<76> wl<75> wl<74> wl<73> wl<72> wl<71> wl<70> wl<69> wl<68> wl<67> wl<66> wl<65> wl<64> wl<63> wl<62> wl<61> wl<60> wl<59> wl<58> wl<57> wl<56> wl<55> wl<54> wl<53> wl<52> wl<51> wl<50> wl<49> wl<48> wl<47> wl<46> wl<45> wl<44> wl<43> wl<42> wl<41> wl<40> wl<39> wl<38> wl<37> wl<36> wl<35> wl<34> wl<33> wl<32> wl<31> wl<30> wl<29> wl<28> wl<27> wl<26> wl<25> wl<24> wl<23> wl<22> wl<21> wl<20> wl<19> wl<18> wl<17> wl<16> wl<15> wl<14> wl<13> wl<12> wl<11> wl<10> wl<9> wl<8> wl<7> wl<6> wl<5> wl<4> wl<3> wl<2> wl<1> wl<0> bl blb vdd_1 gnd_1 SRAM_Array_128
v2 cwl<0> 0 DC=1.2
v1 gnd_1 0 DC=0
v0 vdd_1 0 DC=1.2
c0 cbl 0 5e-12
.END
