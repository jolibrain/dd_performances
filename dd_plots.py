import numpy as np
import matplotlib.pyplot as plt

######data_area

gtx = np.matrix\
('\
37.2	12.2	19.8	35.8	44.4	16.6	45.6	69	8.4	8.6	14	14.6	15;\
36.3	6.2	14.1	22.5	27.8	9.8	24	38.6	4.1	5.5	9.9	11.2	9.1;\
22.1	4.3	8.8	13.8	18.5	5.25	16.5	25.9	2.6	3.55	6.95	8.2	6.95;\
21.2	3.52	7.27	10.4	14.6	3.93	11.92	18.5	2.38	2.33	5.7	6.25	4.55;\
19.5	3.73	6.33	8.63	11.6	3.18	9.06	13.7	2.16	1.97	5.18	6.21	4.71;\
18.2	3.23	5.9	7.82	-1	3.3	-1	-1	2.59	2.96	5.15	6.05	3.49;\
19.3	3.12	-1	-1	-1	3.13	-1	-1	2.5	2.33	4.82	5.63	3.26;\
16.8	2.63	-1	-1	-1	3.05	-1	-1	2.2	2.2	4.97	5.57	2.87\
')

tx1 = np.matrix\
('\
171	33.8	89	142	195	43.6	134	248	33.4	30.2	133	152	60;\
173	29.2	77.7	122	180	29.6	98.5	159	23.7	17.9	165	187	38.8;\
164	27	69.6	112	-1	24	93.7	-1	20.7	14.2	127	149	21.7;\
155	26.1	66.7	-1	-1	21.8	-1	-1	18.6	12.1	110	130	20.6;\
-1	25.6	-1	-1	-1	20.2	-1	-1	17.7	11.8	100	120	21.8;\
-1	25.5	-1	-1	-1	19.7	-1	-1	17.5	11.8	-1	-1	22.9;\
-1	-1	-1	-1	-1	20	-1	-1	17.6	11.5	-1	-1	-1;\
-1	-1	-1	-1	-1	-1	-1	-1	-1	11.6	-1	-1	-1\
')

tk1 = np.matrix\
('\
464	336	203	283	400	197	294	637	119	90.2	-1	-1	82.8;\
462	210	231	351	477	127	225	-1	88	71.3	-1	-1	63.8;\
453	135	234	-1	-1	87.2	-1	-1	70.8	50.9	-1	-1	53.4;\
441	141	-1	-1	-1	78.8	-1	-1	62.9	53.6	-1	-1	52;\
452	137	-1	-1	-1	87.8	-1	-1	67	40	-1	-1	51.3;\
-1	-1	-1	-1	-1	93	-1	-1	81	46.8	-1	-1	-1;\
-1	-1	-1	-1	-1	-1	-1	-1	-1	45.2	-1	-1	-1;\
-1	-1	-1	-1	-1	-1	-1	-1	-1	-1	-1	-1	-1\
')

raspi = np.matrix\
('\
1246.0	1443	3560	-1	-1	7980	-1	-1	1492	910	-1	-1	1115;\
1230	1370	-1	-1	-1	8008	-1	-1	1478	917	-1	-1	1067;\
-1	1372	-1	-1	-1	7943	-1	-1	1493	919	-1	-1	1047;\
-1	1401	-1	-1	-1	8015	-1	-1	1444	913	-1	-1	1046;\
-1	-1	-1	-1	-1	-1	-1	-1	1456	909	-1	-1	-1;\
-1	-1	-1	-1	-1	-1	-1	-1	-1	-1	-1	-1	-1;\
-1	-1	-1	-1	-1	-1	-1	-1	-1	-1	-1	-1	-1;\
-1	-1	-1	-1	-1	-1	-1	-1	-1	-1	-1	-1	-1\
')

#model flops and params matrix
#giga flops, million params
cost = np.matrix\
('\
0.5687  0.5514  3.8580  7.5702  11.2825 1.5826  3.0631  4.7727  0.8475  0.3491  15.4702 19.6320 0.1234;\
4.2309  4.2309  25.5560 44.5481 60.1918 6.9902  7.9778  20.0129 1.2444  1.2315  138.344 143.652 1.8137\
')

small_cost = np.matrix\
('\
0.564	1.58	0.847	0.349	0.123;\
4.23	6.99	1.24	1.231	1.813\
')

small_name = ['mobilenet', 'googlenet', 'Squeezenetv1.0', 'Squeezenetv1.1', 'shufflenet']

#####add NaN to make sure the data is not being plotted
gtx[gtx < 0] = np.nan
tx1[tx1 < 0] = np.nan
tk1[tk1 < 0] = np.nan
raspi[raspi < 0] = np.nan

####plot config
x_dd = [1,2,4,8,16,32,64,128]
y_dd = ['mobilenet','mobilenet_depthwise','res50','res101','res152','googlenet','dense121','dense201','squeezenet_v1.0','squeezenet_v1.1','vgg16','vgg19','shufflenet']
platform_dd = ['GTX1080Ti','TX1','TK1','RasPi3']

def gen_platform():
  #concat array to compare each platform
  x = [1,2,3,4] #4 platforms place holder 
  for i in range(13):#13models currently
    a1 = gtx[:,i]
    a2 = tx1[:,i]
    a3 = tk1[:,i]
    a4 = raspi[:,i]

    out = np.concatenate((a1,a2,a3,a4),axis = 1)
    out = out.transpose()

  #plot formatting
    #uncomment for custom dimension
    #plt.figure(figsize=(10,6))
    plt.ylabel('log time per image(ms)') 
    plt.yscale('log')
    plt.xticks(x,platform_dd)
    plt.xlabel('platform')
    plt.title(y_dd[i])
    plt.ylim([1,10000])

    lines = plt.plot(x,out,'--o')

    ## mask to prevent adding of legend with no data based on the gtx1080Ti
    filtre = np.asarray(np.isnan(gtx[:,i])).transpose()[0]
    temp = len(lines)
    for k in reversed(range(temp)):
      if filtre[k]:
        lines.remove(lines[k])
     
    x_dd_masked = np.asarray(x_dd)
    x_dd_masked[filtre] = np.ma.masked
    #adding lengends
    legend = plt.legend(lines,[x_dd_masked[j] for j in range(len(lines))])

    ## uncomment to generate image files##
    plt.savefig(y_dd[i]+'.png', bbox_inches='tight')
    plt.clf()
    # plt.show()
    plt.close()
def gen_cost():
  n_groups = 13

  fig, ax = plt.subplots()
  index = np.arange(n_groups)
  bar_width = 0.35
  opacity = 0.8

  first_bar =  np.asarray(cost[0])[0]
  second_bar =  np.asarray(cost[1])[0]
 
  ax2 = ax.twinx()
  rects1 = ax.bar(index, first_bar, bar_width,
                 alpha=opacity,
                 color='b',
                 label='flops')

  rects2 = ax2.bar(index + bar_width, second_bar, bar_width,
                 alpha=opacity,
                 color='g',
                 label='params')

  ax.set_ylabel('Giga flops')
  ax2.set_ylabel('million params')
  ax.set_ylim([0,25])
  ax2.set_ylim([0,160])
  plt.title('Computational cost by model')
  plt.xticks(index + bar_width, y_dd)
  ax.legend(loc=2)
  ax2.legend(loc=1)
  plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')


  plt.tight_layout()
  #plt.show()
  plt.savefig('cost.png', bbox_inches='tight')
  plt.clf()
  plt.close()
 
def gen_small_cost():
  n_groups = 5

  fig, ax = plt.subplots()
  index = np.arange(n_groups)
  bar_width = 0.35
  opacity = 0.8

  first_bar =  np.asarray(small_cost[0])[0]
  second_bar =  np.asarray(small_cost[1])[0]

  ax2 = ax.twinx()
  rects1 = ax.bar(index, first_bar, bar_width,
                 alpha=opacity,
                 color='b',
                 label='flops')

  rects2 = ax2.bar(index + bar_width, second_bar, bar_width,
                 alpha=opacity,
                 color='g',
                 label='params')

  ax.set_ylabel('Giga flops')
  ax2.set_ylabel('million params')
  ax.set_ylim([0,2])
  plt.title('Computational cost by model')
  plt.xticks(index + bar_width, np.asarray(small_name))
  ax.legend(loc=2)  
  ax2.legend(loc=1)
  plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')


  plt.tight_layout()
  #plt.show()
  plt.savefig('small_cost.png', bbox_inches='tight')
  plt.clf()
  plt.close()

def gen_depthwise():
  gtx_ = np.asarray(gtx[:,0:2]).transpose()
  tx1_ = np.asarray(tx1[:,0:2]).transpose()
  tk1_ = np.asarray(tk1[:,0:2]).transpose()
  raspi_ = np.asarray(raspi[:,0:2]).transpose()

  out = [gtx_, tx1_, tk1_, raspi_] 
  
  for i in range(len(platform_dd)):
    plt.ylabel('log time per image(ms)')
    plt.yscale('log')
    plt.ylim([0.5, 300*10**(i+1) + 8**(i+1)]) #manipulating axis
    plt.xlabel('batch size')
    plt.xscale('log')
    plt.xlim([0.5,256])
    plt.xticks(x_dd,x_dd)
    plt.figtext(.5,.93,platform_dd[i], fontsize=18, ha='center')
    plt.figtext(.5,.9,'mobilenet improvement by depthwise convolution',fontsize=10,ha='center')        
    plt.minorticks_off()

    line = plt.plot(x_dd,out[i][0],'--o', label='mobilenet')
    line1 = plt.plot(x_dd,out[i][1],'--o', label='mobilenet depthwise')
   
    plt.legend()      
    #plt.show()
    plt.savefig('mobilenet_'+platform_dd[i]+'.png', bbox_inches='tight')
    plt.clf()
    plt.close()

##run stuff here
#gen_platform()
#gen_cost()
#gen_small_cost()
#gen_depthwise()
