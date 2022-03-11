from eppy.modeleditor import IDF
from eppy.results import fasthtml
import pandas as pd
import os
from collections import defaultdict
J = 3600000
def get_dict(filePath):
    #filePath = "./"
    for _,d,_ in os.walk(filePath):
        break 
        # 很奇怪为什么是一个迭代对象？难道是迭代打开子目录？
    def addtwodimdict(thedict, key_a, key_b, val): 
        if key_a in thedict:
            thedict[key_a].update({key_b: val})
        else:
            thedict.update({key_a:{key_b: val}})

    main_dic = dict(dict())
    for name in d:
        #print(name.split("."))
        province,city = name.split(".")[0][4:],name.split(".")[-2]
        #print(province,city)
        # if province in main_dic.keys():
        #main_dic[province][city] = name
        addtwodimdict(main_dic,province,city,name)
    return main_dic


# 运行环境配置
iddfile = "D:/energyplus/Energy+.idd"
# epwfile = "CHN_Shaanxi.Xian.570360_CSWD/CHN_Shaanxi.Xian.570360_CSWD.epw"
rundir = "ep_run/"
epsdir = "buildings/"
epwdir = "weathers/spyder/"
buildings = {
    'ApartmentHighRise': "ASHRAE9012016_ApartmentHighRise_Denver",
    'ApartmentMidRise': "ASHRAE9012016_ApartmentMidRise_Denver",
    'Hospital': "ASHRAE9012016_Hospital_Denver",
    'HotelLarge': "ASHRAE9012016_HotelLarge_Denver",
    'HotelSmall': "ASHRAE9012016_HotelSmall_Denver",
    'OfficeLarge': "ASHRAE9012016_OfficeLarge_Denver",
    'OfficeMedium': "ASHRAE9012016_OfficeMedium_Denver",
    'OfficeSmall': "ASHRAE9012016_OfficeSmall_Denver",
    # 'OutPatientHealthCare':"'"ASHRAE9012016_OutPatientHealthCare_Denver"'",
    'RestaurantFastFood': "ASHRAE9012016_RestaurantFastFood_Denver",
    'RestaurantSitDown': "ASHRAE9012016_RestaurantSitDown_Denver",
    'RetailStandalone': "ASHRAE9012016_RetailStandalone_Denver",
    'RetailStripmall': "ASHRAE9012016_RetailStripmall_Denver",
    'SchoolPrimary': "ASHRAE9012016_SchoolPrimary_Denver",
    'SchoolSecondary': "ASHRAE9012016_SchoolSecondary_Denver",
    'Warehouse': "ASHRAE9012016_Warehouse_Denver"

}
weathers = {
    '安徽': {
        '安庆': "CHN_Anhui.Anqing.584240_CSWD",
        '蚌埠': "CHN_Anhui.Bengbu.582210_CSWD",
        "合肥":"CHN_Anhui.Hefei.583210_CSWD"
    },
    '福建': {
        'Congwu': "CHN_Fujian.Congwu.591330_CSWD"
    },
    '陕西': {
        '西安': "CHN_Shaanxi.Xian.570360_CSWD"
    }
}
keys = [
    'Electricity Load [J]',
    'Heating Load [J]',
    'Cooling Load [J]',
    "Environment:Site Direct Solar Radiation Rate per Area [W/m2](Hourly)",
    "Environment:Site Wind Speed [m/s](Hourly)",
    "Environment:Site Wind Speed [m/s](Hourly)"
]


def LoadCal(building, area, weather,name):
    # 初始化idf
    IDF.setiddname(iddfile)
    idfname = epsdir + building + ".idf"
    epwfile = epwdir + weather + "/" + weather + ".epw"
    ddyfile = epwdir + weather + "/" + weather + ".ddy"
    idf = IDF(idfname, epwfile)
    # 修改idf的site和ddy
    site = idf.idfobjects["Site:Location"]
    ddy = idf.idfobjects["SizingPeriod:DesignDay"]
    ddyidf = IDF(ddyfile)
    #idf.printidf()
    #idf.idfobjects["SizingPeriod:DesignDay"].Name
    #exit(0)
    site_s = ddyidf.idfobjects["Site:Location"]
    ddy_s = ddyidf.idfobjects["SizingPeriod:DesignDay"]
    site.pop(0)
    #print(ddyidf.idfobjects["SizingPeriod:DesignDay"])
    idf.copyidfobject(site_s[0])
    for i in range(len(ddy)):
        ddy.pop(0)
    for i in range(len(ddy_s)):
        idf.copyidfobject(ddy_s[i])
    # output=ddyidf.idfobjects["Output:Variable"]
    # idf.copyidfobject(output[0])
    output = idf.newidfobject("Output:Variable")
    output["Variable_Name"] = "Site Direct Solar Radiation Rate per Area"
    output1 = idf.newidfobject("Output:Variable")
    output1["Variable_Name"] = "Site Wind Speed"
    # solar = """
    # Output:Variable,
    # *,                       !- Key Value
    # Site Direct Solar Radiation Rate per Area,  !- Variable Name
    # Hourly;                  !- Reporting Frequency
    # """
    #
    # output=idf.idfobjects["Output:Variable"]
    # output.append(solar)
    # 运行idf
    idf.run(readvars=True, output_directory=rundir)
    #exit(0)
    # 读取并修改输出
    filehandle = open(rundir + 'eplustbl.htm', 'r')
    A0 = fasthtml.tablebyname(filehandle, "Building Area")[1][1][1]  # 原建筑面积
    ra = area / A0
    rv = pd.read_csv(rundir + 'eplusout.csv')
    T_begin = rv[rv["Date/Time"] == ' 01/01  01:00:00'].index[0]  # 读取数据的起始时间（跳过DesignDay）
    rv = rv.loc[rv.index >= T_begin, :].reset_index(drop=True)
    #name=['']
    a = rv.columns[5]  # InteriorLights:Electricity
    b = rv.columns[6]  # InteriorEquipment:Electricity
    rv["Electricity Load [J]"] = rv[[a, b]].apply(lambda x: (x[a] + x[b]), axis=1)
    # logP = a + ' + ' + b#验证a和b是否是light和equipment
    rv.rename(columns={'Heating:EnergyTransfer [J](Hourly)': 'Heating Load [J]'}, inplace=True)
    rv.rename(columns={'Cooling:EnergyTransfer [J](Hourly)': 'Cooling Load [J]'}, inplace=True)
    rv = rv[keys]  # 只要时间和3种负荷数据
    rv = rv.apply(lambda x: x * ra/J if x.name in keys[0:3] else x)  # 面积等比缩放
    rv = rv.apply(lambda x: x /1000 if x.name == keys[3] else x)# 光照千瓦变瓦
    rv.to_csv("warehouse_result/"+name+'.csv', index=None)#生成csv文件
    return rv


if __name__ == '__main__':
    main_dic = get_dict("./weathers/spyder/")
    #print(list(main_dic.keys()))
    ans = []
    # for c in list(main_dic.keys()):
    #     print("------")
    #     print(c)
    #     province = c
    #     city = list(main_dic[c].keys())[0]
    #     filename = main_dic[c].get(list(main_dic[c].keys())[0])
    #     #break
    #     #print(list(main_dic[c].keys())[0])
    #     #print(main_dic[c].get(list(main_dic[c].keys())[0]))
    #     try:
    #         load = LoadCal(buildings["Warehouse"], 1000, filename,province)
    #     except:
    #         ans.append((filename,province))
    #         print("error "+province)
    #     #break

    err = [('CHN_Fujian.Congwu.591330_CSWD', 'Fujian'), ('CHN_Guangdong.Dianbai.596640_CSWD', 'Guangdong'), ('CHN_Jilin.Baicheng.509360_CSWD', 'Jilin'), ('CHN_Ningxia.Hui.Guyuan.538170_CSWD', 'Ningxia'), ('CHN_Xinjiang.Uygur.Aksu.516280_CSWD', 'Xinjiang')]
    for _,c in err:
        filename = main_dic[c].get(list(main_dic[c].keys())[1])
        try:
            load = LoadCal(buildings["Warehouse"], 1000, filename,c)
        except:
            ans.append(c)
            print("error "+province)

    print(ans)
#[('CHN_Fujian.Congwu.591330_CSWD', 'Fujian'), ('CHN_Guangdong.Dianbai.596640_CSWD', 'Guangdong'), ('CHN_Jilin.Baicheng.509360_CSWD', 'Jilin'), ('CHN_Ningxia.Hui.Guyuan.538170_CSWD', 'Ningxia'), ('CHN_Xinjiang.Uygur.Aksu.516280_CSWD', 'Xinjiang')]