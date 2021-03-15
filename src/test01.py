import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import solve
import copy
import matplotlib
from matplotlib.ticker import (MultipleLocator)

y=[2.00E+00	,
1.96E+00	,
1.92E+00	,
1.88E+00	,
1.84E+00	,
1.80E+00	,
1.76E+00	,
1.72E+00	,
1.68E+00	,
1.64E+00	,
1.60E+00	,
1.56E+00	,
1.52E+00	,
1.47E+00	,
1.43E+00	,
1.39E+00	,
1.35E+00	,
1.31E+00	,
1.27E+00	,
1.23E+00	,
1.19E+00	,
1.15E+00	,
1.11E+00	,
1.07E+00	,
1.03E+00	,
9.90E-01	,
9.49E-01	,
9.09E-01	,
8.69E-01	,
8.28E-01	,
7.88E-01	,
7.47E-01	,
7.07E-01	,
6.67E-01	,
6.26E-01	,
5.86E-01	,
5.45E-01	,
5.05E-01	,
4.65E-01	,
4.24E-01	,
3.84E-01	,
3.43E-01	,
3.03E-01	,
2.63E-01	,
2.22E-01	,
1.82E-01	,
1.41E-01	,
1.01E-01	,
6.06E-02	,
2.02E-02	,
-2.02E-02	,
-6.06E-02	,
-1.01E-01	,
-1.41E-01	,
-1.82E-01	,
-2.22E-01	,
-2.63E-01	,
-3.03E-01	,
-3.43E-01	,
-3.84E-01	,
-4.24E-01	,
-4.65E-01	,
-5.05E-01	,
-5.45E-01	,
-5.86E-01	,
-6.26E-01	,
-6.67E-01	,
-7.07E-01	,
-7.47E-01	,
-7.88E-01	,
-8.28E-01	,
-8.69E-01	,
-9.09E-01	,
-9.49E-01	,
-9.90E-01	,
-1.03E+00	,
-1.07E+00	,
-1.11E+00	,
-1.15E+00	,
-1.19E+00	,
-1.23E+00	,
-1.27E+00	,
-1.31E+00	,
-1.35E+00	,
-1.39E+00	,
-1.43E+00	,
-1.47E+00	,
-1.52E+00	,
-1.56E+00	,
-1.60E+00	,
-1.64E+00	,
-1.68E+00	,
-1.72E+00	,
-1.76E+00	,
-1.80E+00	,
-1.84E+00	,
-1.88E+00	,
-1.92E+00	,
-1.96E+00	,
-2.00E+00	]
# =============================================================================
# 
# =============================================================================
vel1=[
0.001662494	,
0.001665561	,
0.001668628	,
0.001671887	,
0.001675177	,
0.001678467	,
0.001681366	,
0.001683248	,
0.001685325	,
0.001687698	,
0.001687506	,
0.001685993	,
0.00168455	,
0.00168299	,
0.001677557	,
0.001667219	,
0.00165577	,
0.001643178	,
0.001629411	,
0.001614304	,
0.001575591	,
0.001530283	,
0.001481892	,
0.001430338	,
0.001375539	,
0.00129885	,
0.001212405	,
0.001122163	,
0.001029215	,
0.000934185	,
0.00083236	,
0.000730334	,
0.000628104	,
0.000525668	,
0.000432356	,
0.000346206	,
0.000260899	,
0.000176643	,
0.000102236	,
4.38065E-05	,
2.52934E-05	,
8.00801E-05	,
0.000130019	,
0.000164584	,
0.000199052	,
0.000233365	,
0.00025842	,
0.000269564	,
0.000280701	,
0.000291832	,
0.000291832	,
0.000280701	,
0.000269564	,
0.000258422	,
0.000233364	,
0.00019905	,
0.000164583	,
0.000130018	,
8.00778E-05	,
2.52916E-05	,
4.38086E-05	,
0.000102248	,
0.000176621	,
0.000260902	,
0.000346209	,
0.00043236	,
0.000525672	,
0.000628108	,
0.000730338	,
0.000832363	,
0.000934496	,
0.001029219	,
0.001122166	,
0.001212408	,
0.001298853	,
0.001375541	,
0.00143034	,
0.001481894	,
0.001530285	,
0.001575593	,
0.001614305	,
0.001629411	,
0.001643178	,
0.00165577	,
0.00166722	,
0.001677557	,
0.00168299	,
0.001684551	,
0.001685993	,
0.001687506	,
0.001687698	,
0.001685325	,
0.001683248	,
0.001681367	,
0.001678466	,
0.001675177	,
0.001671887	,
0.001668628	,
0.00166556	,
0.001662493	
]
# =============================================================================
# 
# =============================================================================
vel2=[0.001660672	,
0.001663445	,
0.00166627	,
0.001669153	,
0.001672002	,
0.001674786	,
0.001677706	,
0.001681118	,
0.00168415	,
0.001687065	,
0.001690056	,
0.001692316	,
0.001693763	,
0.001694035	,
0.001693038	,
0.001690426	,
0.001686102	,
0.001675583	,
0.001663095	,
0.001639948	,
0.001611726	,
0.00157025	,
0.001522132	,
0.001458604	,
0.001386523	,
0.001301352	,
0.001209374	,
0.001107024	,
0.001001157	,
0.000891945	,
0.000782237	,
0.000675476	,
0.000571448	,
0.000473067	,
0.000380876	,
0.000293413	,
0.000215643	,
0.000141944	,
7.68271E-05	,
2.08117E-05	,
4.21237E-05	,
8.7761E-05	,
0.000130565	,
0.000167728	,
0.000198554	,
0.000225779	,
0.000246239	,
0.000261646	,
0.000273442	,
0.00027753	,
0.00027753	,
0.000273442	,
0.000261645	,
0.000246239	,
0.00022578	,
0.000198553	,
0.000167723	,
0.000130564	,
8.77592E-05	,
4.21217E-05	,
2.08133E-05	,
7.68296E-05	,
0.000141947	,
0.000215646	,
0.000293417	,
0.000380879	,
0.00047307	,
0.000571452	,
0.00067548	,
0.000782241	,
0.00089195	,
0.001001161	,
0.001107028	,
0.001209378	,
0.001301355	,
0.001386526	,
0.001458607	,
0.001522134	,
0.001570252	,
0.001611725	,
0.001639948	,
0.001663095	,
0.001675583	,
0.001686103	,
0.001690426	,
0.001693038	,
0.001694035	,
0.001693763	,
0.001692316	,
0.001690055	,
0.001687065	,
0.00168415	,
0.001681118	,
0.001677705	,
0.001674785	,
0.001672002	,
0.001669152	,
0.00166627	,
0.001663445	,
0.001660672	
]
# =============================================================================
# 
# =============================================================================
vel3=[0.00162683	,
0.001628156	,
0.001629483	,
0.001630811	,
0.001632139	,
0.001633469	,
0.001631641	,
0.0016204	,
0.001609078	,
0.001597678	,
0.001586201	,
0.001574644	,
0.001563013	,
0.001551387	,
0.001540991	,
0.001529905	,
0.001518108	,
0.001505579	,
0.001492294	,
0.001463049	,
0.001422493	,
0.001381605	,
0.001339321	,
0.001295969	,
0.001251524	,
0.001205966	,
0.001159271	,
0.00111142	,
0.001062389	,
0.00101216	,
0.000960712	,
0.000908032	,
0.000854106	,
0.000788343	,
0.000719413	,
0.000649851	,
0.000579689	,
0.000508901	,
0.000437514	,
0.000364846	,
0.000290789	,
0.000217	,
0.000144367	,
7.71734E-05	,
4.85103E-05	,
4.0299E-05	,
3.22462E-05	,
2.44175E-05	,
1.73929E-05	,
1.24765E-05	,
1.24766E-05	,
1.73931E-05	,
2.44178E-05	,
3.21991E-05	,
4.03013E-05	,
4.85639E-05	,
7.71983E-05	,
0.000144499	,
0.000217003	,
0.000290792	,
0.000364849	,
0.000437517	,
0.000508904	,
0.000579692	,
0.000649854	,
0.000719377	,
0.000788257	,
0.000854108	,
0.000907978	,
0.000960714	,
0.001012161	,
0.001062391	,
0.001111422	,
0.001159273	,
0.001205967	,
0.001251526	,
0.00129597	,
0.001339323	,
0.001381606	,
0.001422841	,
0.00146305	,
0.001492295	,
0.001505579	,
0.001518109	,
0.001529906	,
0.001540992	,
0.001551388	,
0.001563017	,
0.001574644	,
0.001586198	,
0.001597677	,
0.001609078	,
0.0016204	,
0.001631642	,
0.001633469	,
0.001632139	,
0.001630811	,
0.001629483	,
0.001628156	,
0.00162683]
# =============================================================================
# 
# =============================================================================
vel4=[0.001660552	,
0.001663325	,
0.001666144	,
0.001669007	,
0.001671913	,
0.001674802	,
0.001677717	,
0.001680882	,
0.001683895	,
0.001686863	,
0.001689715	,
0.00169226	,
0.001694527	,
0.001695651	,
0.001695653	,
0.001693913	,
0.001689586	,
0.001681475	,
0.001667647	,
0.001647035	,
0.00161774	,
0.00157849	,
0.00152801	,
0.001465406	,
0.001391026	,
0.001305109	,
0.001209732	,
0.00110653	,
0.000998429	,
0.000888134	,
0.000777496	,
0.000669648	,
0.000565966	,
0.000467643	,
0.000375404	,
0.000289613	,
0.000210684	,
0.000138907	,
7.37609E-05	,
1.85232E-05	,
4.29582E-05	,
8.94881E-05	,
0.000131166	,
0.000167741	,
0.000199248	,
0.000225014	,
0.000245655	,
0.00026134	,
0.000271865	,
0.000276794	,
0.000276794	,
0.000271864	,
0.000261339	,
0.000245654	,
0.000225013	,
0.000199247	,
0.00016774	,
0.000131164	,
8.94864E-05	,
4.29562E-05	,
1.85247E-05	,
7.37633E-05	,
0.00013891	,
0.000210687	,
0.000289619	,
0.000375408	,
0.000467647	,
0.00056597	,
0.000669652	,
0.000777489	,
0.000887795	,
0.000998432	,
0.001106534	,
0.001209747	,
0.001305113	,
0.001391029	,
0.001465409	,
0.001528012	,
0.001578492	,
0.001617741	,
0.001647037	,
0.001667649	,
0.001681475	,
0.001689585	,
0.001693913	,
0.001695653	,
0.001695651	,
0.001694527	,
0.00169226	,
0.001689715	,
0.001686863	,
0.001683895	,
0.001680882	,
0.001677717	,
0.001674802	,
0.001671913	,
0.001669007	,
0.001666144	,
0.001663324	,
0.001660551	
]
# =============================================================================
# 
# =============================================================================
vel5=[0.001660605	,
0.001663386	,
0.001666208	,
0.001669074	,
0.001671995	,
0.001674867	,
0.00167779	,
0.00168096	,
0.001683986	,
0.001686965	,
0.001689724	,
0.001692364	,
0.001694495	,
0.00169512	,
0.001694762	,
0.001692964	,
0.001687866	,
0.001679767	,
0.001665426	,
0.001644385	,
0.001616093	,
0.001576102	,
0.001525156	,
0.00146428	,
0.001389655	,
0.001303868	,
0.00120981	,
0.001107499	,
0.000999448	,
0.000889555	,
0.000779535	,
0.000671283	,
0.000567759	,
0.000469676	,
0.000377474	,
0.000291491	,
0.000212181	,
0.000139562	,
7.45995E-05	,
1.92813E-05	,
4.19216E-05	,
8.87288E-05	,
0.000130838	,
0.000167727	,
0.000199387	,
0.000225553	,
0.000246126	,
0.000261552	,
0.000271843	,
0.000276988	,
0.000276986	,
0.000271835	,
0.000261547	,
0.000246143	,
0.000225552	,
0.000199374	,
0.000167726	,
0.000130837	,
8.87271E-05	,
4.19775E-05	,
1.92829E-05	,
7.4602E-05	,
0.000139617	,
0.000212173	,
0.000291525	,
0.000377477	,
0.00046968	,
0.000567705	,
0.00067135	,
0.000779539	,
0.000889519	,
0.000999452	,
0.001107563	,
0.001209813	,
0.001303872	,
0.001389639	,
0.001464288	,
0.001525158	,
0.001576104	,
0.001616115	,
0.001644403	,
0.001665427	,
0.001679768	,
0.001687866	,
0.001692964	,
0.001694762	,
0.00169512	,
0.001694495	,
0.001692364	,
0.001689724	,
0.001686965	,
0.001683986	,
0.001680961	,
0.001677789	,
0.001674867	,
0.001671995	,
0.001669074	,
0.001666208	,
0.001663386	,
0.001660605	
]
# =============================================================================
# 
# =============================================================================
vel6=[0.001660615	,
0.001663386	,
0.00166622	,
0.001669093	,
0.001672002	,
0.001674824	,
0.001677747	,
0.001681006	,
0.001684068	,
0.00168697	,
0.001689693	,
0.001692281	,
0.001694207	,
0.001694691	,
0.001694105	,
0.001692046	,
0.001686873	,
0.001678536	,
0.001663685	,
0.001643886	,
0.001613158	,
0.001575613	,
0.001523718	,
0.00146229	,
0.001388769	,
0.00130354	,
0.001210201	,
0.001107356	,
0.001000498	,
0.000890573	,
0.000781026	,
0.000673519	,
0.000568756	,
0.000471193	,
0.000378975	,
0.000292219	,
0.000213352	,
0.000141532	,
7.56604E-05	,
1.91617E-05	,
4.17582E-05	,
8.82602E-05	,
0.000130648	,
0.000168309	,
0.000199022	,
0.00022488	,
0.000245963	,
0.000262281	,
0.000272447	,
0.000277221	,
0.000277221	,
0.000272447	,
0.000262275	,
0.000245962	,
0.000224879	,
0.000199021	,
0.00016828	,
0.000130686	,
8.83489E-05	,
4.17416E-05	,
1.91632E-05	,
7.56628E-05	,
0.000141535	,
0.000213333	,
0.000292225	,
0.000378978	,
0.000471197	,
0.000568788	,
0.000673523	,
0.00078103	,
0.000890986	,
0.001000583	,
0.001107361	,
0.001210227	,
0.001303543	,
0.001388688	,
0.001462249	,
0.00152372	,
0.001575651	,
0.001613147	,
0.001643889	,
0.001663685	,
0.001678536	,
0.001686873	,
0.001692047	,
0.001694108	,
0.001694691	,
0.001694208	,
0.001692282	,
0.001689693	,
0.00168697	,
0.001684068	,
0.001681006	,
0.001677747	,
0.001674824	,
0.001672001	,
0.001669093	,
0.001666219	,
0.001663386	,
0.001660615	
]
# =============================================================================
# 
# =============================================================================
vel7=[0.00166299	,
0.001665884	,
0.001668778	,
0.001671673	,
0.001674567	,
0.001677461	,
0.001679674	,
0.001680088	,
0.001680853	,
0.001681971	,
0.001683445	,
0.001680699	,
0.001672189	,
0.001664341	,
0.001656572	,
0.001648003	,
0.001638612	,
0.001628373	,
0.001603838	,
0.00157032	,
0.001534986	,
0.001497789	,
0.001458681	,
0.001415776	,
0.001365941	,
0.001293311	,
0.001210941	,
0.001126813	,
0.001040833	,
0.000952958	,
0.000863145	,
0.000769947	,
0.000674774	,
0.000579495	,
0.000484115	,
0.000388641	,
0.000293144	,
0.000216132	,
0.00014548	,
7.58236E-05	,
1.61958E-05	,
6.66181E-05	,
0.000123347	,
0.000159165	,
0.000194934	,
0.000230588	,
0.000266098	,
0.00029812	,
0.00029809	,
0.000298075	,
0.000298075	,
0.00029809	,
0.00029812	,
0.000266096	,
0.000230587	,
0.000194932	,
0.000159164	,
0.000123345	,
6.66155E-05	,
1.61965E-05	,
7.58263E-05	,
0.000145452	,
0.000216187	,
0.000293148	,
0.000388644	,
0.000484119	,
0.000579499	,
0.000674777	,
0.000769951	,
0.000863149	,
0.000952962	,
0.001040836	,
0.001126816	,
0.001210944	,
0.001293261	,
0.001365943	,
0.001415778	,
0.001458683	,
0.00149779	,
0.001534987	,
0.001570321	,
0.00160384	,
0.001628374	,
0.001638612	,
0.001648004	,
0.001656572	,
0.001664342	,
0.00167219	,
0.001680698	,
0.001683444	,
0.001681971	,
0.001680853	,
0.001680087	,
0.001679674	,
0.001677461	,
0.001674567	,
0.001671673	,
0.001668778	,
0.001665884	,
0.00166299	
]

cp_x=[0.00172	,
0.0015	,
0.0015	,
0.00172	,
0.00172	
]

cp_y=[1.00E+00	,
1.00E+00	,
2.00E+00	,
2.00E+00	,
1.00E+00	
]

fig = plt.figure(dpi=350, figsize=(10,3.5))
fig.suptitle('Velocity magnitude against distance along Y-axis', fontsize=16)
fig.subplots_adjust(top=0.83)

ax1 = plt.subplot2grid((1, 2), (0, 0))
ax1.set_title('Whole Solution',)
ax1.set_xlabel('Velocity magnitude (m/s)')
ax1.set_ylabel('Distance along Y axis')
ax1.set_ylim(-2,2)
ax1.xaxis.set_major_locator(MultipleLocator(0.0004))

ax2 = plt.subplot2grid((1, 2), (0, 1))
ax2.set_title('Close-up of the whole solution')
ax2.set_xlabel('Velocity magnitude (m/s)')
ax2.set_ylabel('Distance along Y axis')
ax2.set_ylim(1,2)
ax2.set_xlim(0.0015,0.0017)
ax2.xaxis.set_major_locator(MultipleLocator(0.00005))

lw_close=1

ax1.plot(vel3,y, label='1595 el.',lw=lw_close)
ax1.plot(vel7,y, label='6825 el.',lw=lw_close)
ax1.plot(vel1,y, label='22400 el.',lw=lw_close)
ax1.plot(vel2,y, label='58900 el.',lw=lw_close)
ax1.plot(vel6,y, label='94800 el.',lw=lw_close)
ax1.plot(vel5,y, label='136300 el.',lw=lw_close)
ax1.plot(vel4,y, label='235600 el.',lw=lw_close)
ax1.plot(cp_x, cp_y, '--k')

ax2.plot(vel3,y, label='1595 el.',lw=lw_close)
ax2.plot(vel7,y, label='6825 el.',lw=lw_close)
ax2.plot(vel1,y, label='22400 el.',lw=lw_close)
ax2.plot(vel2,y, label='58900 el.',lw=lw_close)
ax2.plot(vel6,y, label='94800 el.',lw=lw_close)
ax2.plot(vel5,y, label='136300 el.',lw=lw_close)
ax2.plot(vel4,y, label='235600 el.',lw=lw_close)

# ax1.legend(loc='upper left')
leg=plt.legend(fontsize=7.9,loc='lower center',ncol = 7, bbox_to_anchor=(-0.155,-0.3))

plt.show()




