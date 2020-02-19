import matplotlib.pyplot as plt
import pandas as pd


losses_m1 = [4489.41255277630, 1948.97124134601, 1815.46492164741, 1693.03473604539, 1544.04887332169, 976.617778442428, 1234.09805776434, 1131.90775268320, 882.851571283326, 953.837755278396, 1196.57526455081, 987.393697971591, 1132.16559201314, 804.811557174001, 1023.87836257769, 1039.56776622864, 1076.86804607034, 1026.60808592341, 755.029695052523, 951.937284870297, 654.928509720996, 855.378645022301, 678.741693860372, 591.691020938271, 560.551503447250, 958.397553736115, 649.173026244376, 738.243191028154, 655.925812136789, 444.320849350736] + [444.320849350736] * 70
losses_m4 = [2073.26955297917, 1388.62386284751, 1307.81984281571, 921.347605070989, 758.097082534308, 717.894386504567, 888.105249590512, 836.377861619166, 754.268149446069, 679.974040620475, 669.257337937978, 562.335145958893, 480.055260266122, 340.992734392064, 361.888838268202, 543.708409663288, 692.713761398384, 678.911523161070, 644.314032441998, 638.230722959596, 458.053990716115, 555.747720640369, 563.884262895810, 682.571906702985, 654.222042425573, 518.154133085931, 556.377396827306, 449.991308071228, 512.094284776397, 565.483440375812] + [565.483440375812] * 70
losses_m5 = [2054.53443990443, 956.897756155736, 660.526632853207, 714.416543695435, 472.306731203369, 450.602364905625, 465.019540839029, 532.547532912544, 353.266177820113, 448.076139385534, 260.402411018959, 283.310072303853, 397.847817935597, 287.966172949730, 414.612614451539, 276.598016167308, 252.597758073547, 306.850334658353, 362.772949952947, 268.634098773864, 354.158570660237, 478.557926699175, 335.822781656765, 160.543513048221, 318.582759661476, 272.319655261984, 286.981495779974, 410.566799366501, 220.832930317550, 198.296782155622, 191.276484363171, 311.178228433675, 233.782317788697, 149.852112766465, 251.628960679763, 233.924795595428, 203.990459182719, 190.894436492986, 158.561847959353, 187.450190795111, 139.054660170438, 164.727847076309, 158.763713769673, 235.419145364965, 266.089057769448, 104.515882068384, 141.826060103941, 113.051457716762, 97.2768468175639, 156.402025733797] # + [156.402025733797]*50
losses_m6 = [2213.2816890526, 1177.7160113540, 1175.4917748543, 1096.7655487974, 947.66134449226, 737.27014612806, 689.74113572757, 878.01372138596, 809.62137268662, 567.16167309479, 550.27802565463, 711.30663475518, 757.87294620938, 651.48652196918, 745.19210745882, 569.29387830316, 583.24594917509, 574.18881041765, 512.06075765982, 449.57706580689, 484.78514369206, 453.90877675971, 627.67029327614, 456.96500620742, 458.38373778113, 576.66383583084, 730.51911997827, 582.88787341573, 425.72264916455, 508.43622044665, 360.36363847965, 565.01124880164, 446.30692663318, 421.60169420721, 479.14689742292, 351.46352381231, 371.44046752328, 550.87068734939, 457.73135672571, 411.25728906482, 539.32981558915, 593.04042964154, 415.99321581484, 330.72147888356, 423.29534278752, 405.54213005876, 459.95925341461, 299.31849723692, 297.40464639710, 303.18246195855] + [303.18246195855]*50
losses_m7 = [3449.8314453990, 1439.6053198740, 1223.3000404487, 1142.3521626912, 957.41282402281, 576.10836560015, 496.97806356467, 567.14018568948, 992.56271122959, 525.17403505526, 526.34780348245, 336.53029384808, 408.02567044927, 326.62009662726, 618.55878299568, 385.63562369626, 319.52864105840, 356.57886173877, 390.63461575731, 449.90726285925, 328.29629493954, 477.26113895543, 267.37003014343, 476.73009439123, 736.81106630154, 494.76553484648, 651.03157587358, 391.71837701418, 394.92839264937, 478.95058262417, 517.90778157198, 438.48598957256, 482.00459082207, 465.29741741391, 476.46490187490, 417.88057276143, 368.31439655578, 519.71904903609, 309.92044798284, 227.12681499481, 309.58336504173, 280.57741396905, 463.57721447304, 161.48333767830, 383.34273813451, 265.02867680044, 189.03586370612, 357.85337098658, 447.16992378394, 505.73214710034, 207.13632826344, 249.15786806386, 198.46174082683, 153.01353732068, 171.19543448594, 185.81480990761, 149.87806730470, 240.16287079554, 203.97152560027, 276.68085147259, 299.04782793296, 235.77016863791, 216.75096823902, 446.15479790178, 342.50074764319, 323.01531024893, 230.86611401233, 218.42522776629, 226.17856167356, 391.99376267980, 230.17950565446, 189.78411273121, 196.86345224380, 387.18506711461, 275.63977459662, 213.75648690093, 189.08625217395, 262.71986667349, 231.50102515656, 218.84301213899, 178.49599818292, 96.169918055244, 319.48175471399, 330.40894804470, 210.28250222436, 146.52030794735, 269.26287692926]
losses_m7 = losses_m7 + [269.26287692926]* (100-len(losses_m7))
losses_m8 = [1913.1187070098, 1039.0514437212, 1028.9520007291, 597.89408959043, 742.87972633884, 545.32674727767, 648.25194658212, 552.42866523847, 360.56812387797, 283.33697039836, 301.63293597943, 518.70815077080, 266.40182485266, 397.44081482450, 228.45873716811, 296.00514423095, 298.05853104086, 263.67721609054, 196.71848943285, 141.37132491279, 199.98370414965, 167.08047733159, 271.14777233500, 424.39628347201, 233.03496382078, 203.41285916723, 303.61920683974, 287.64561972142, 191.98977213765, 207.35365974571, 288.04825807584, 297.51318445384, 239.29689313097, 360.28960603898, 263.86173294141, 289.18367156653, 292.41926478186, 352.11183932778, 328.50354538009, 237.99935597789, 331.31921413435, 178.92936791883, 217.54673949627, 214.20538475785, 133.64738955204, 157.82746235342, 233.26180136049, 252.55930123165, 86.577192835733, 139.91938526171, 113.82965008306, 111.56824974837, 209.69173995029, 205.71924362953, 285.83343323773, 136.85667714718, 168.20162750410, 186.05222633511, 188.18272803540, 219.29580682636, 185.48368275450, 188.82771136839, 294.52742913037, 247.15757010671, 118.15531989195, 117.06165262124, 169.78583347433, 233.48487585012, 314.46114083966, 110.71327708892, 91.526132826998, 146.85871141121, 206.61402182675, 147.32019714524, 135.93187732187, 207.39982160489, 129.61092831992, 302.39694781101, 187.71114953149, 129.14707990210, 117.24448690107, 267.63144874741, 209.03136407899, 130.23813792241, 129.98365204057, 215.66752594466, 122.35032974360, 178.66256786468, 167.30338180537, 158.20882245767, 156.96372784829, 113.72417170667, 138.78984822374, 190.82193412888, 149.28930681906, 136.20896438614, 208.87743186218, 74.919212460191, 82.060178730617, 158.56681073414]
losses_m9 = [2681.08407204496, 281.220513015372, 237.478018059851, 64.1701811880434, 99.1839925690353, 129.197997083788, 165.077800734196, 103.840544715992, 173.782147663976, 93.5548561168180, 119.551196752653, 178.884986595700, 246.032488043995, 46.2408468301800, 105.817024806334, 66.4648662783521, 79.5649671809957, 107.579942769895, 128.359501348375, 74.5681759849884, 102.288454723473, 109.693582316185, 36.6684506829047, 53.5299727158932, 143.470323991640, 80.1023665984627, 46.1947769860290, 85.8389022907183, 95.3874125533077, 125.951373842116, 132.012087170003, 108.499004079402, 46.3693385419224, 16.8708368643576, 34.8180177314569, 78.2624103369489, 37.2217335155972, 54.6265647096158, 113.985123543756, 157.596087218944, 36.4509711736472, 93.4952999123246, 103.843612461493, 38.0703011551052, 60.3517619949948, 79.8410854368382, 88.9201562319521, 73.1903583510721, 107.135621841382, 109.784799786648]


df = pd.DataFrame({'x': range(1, len(losses_m5)+1), 'y3': losses_m5, 'y7': losses_m9})

#plt.plot( 'x', 'y1', data=df, marker='o', markerfacecolor='blue', markersize=2, color='skyblue', linewidth=1, label="Model 1")
#plt.plot( 'x', 'y2', data=df, marker='o', markerfacecolor='green', markersize=2, color='lightgreen', linewidth=1, label="Model 4")
plt.plot( 'x', 'y3', data=df, marker='o', markerfacecolor='red', markersize=2, color='orange', linewidth=1, label="Model 5")
#plt.plot( 'x', 'y4', data=df, marker='o', markerfacecolor='orange', markersize=2, color='yellow', linewidth=1, label="Model 6")
#plt.plot( 'x', 'y5', data=df, marker='o', markerfacecolor='purple', markersize=2, color='violet', linewidth=1, label="Model 7")
#plt.plot( 'x', 'y6', data=df, marker='o', markerfacecolor='black', markersize=2, color='grey', linewidth=1, label="Model 8")
plt.plot( 'x', 'y7', data=df, marker='o', markerfacecolor='black', markersize=2, color='grey', linewidth=1, label="Model 9")

plt.xlabel('Epochs')
plt.ylabel('NER Losses')
plt.title('Model Training Metric: NER Loss')

plt.legend()
plt.ylim([0, 1500])
plt.savefig("line_chart.png")