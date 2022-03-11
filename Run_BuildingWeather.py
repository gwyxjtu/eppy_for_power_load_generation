from eppy.modeleditor import IDF
from eppy.results import fasthtml
import pandas as pd

# 运行环境配置
iddfile = "D:/energyplus/Energy+.idd"
# epwfile = "CHN_Shaanxi.Xian.570360_CSWD/CHN_Shaanxi.Xian.570360_CSWD.epw"
rundir = "ep_run/"
epsdir = "buildings/"
epwdir = "weathers/"
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
    'Date/Time',
    'Heating Load [J]',
    'Cooling Load [J]',
    'Electricity Load [J]'
]


def LoadCal(building, area, weather):
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
    site_s = ddyidf.idfobjects["Site:Location"]
    ddy_s = ddyidf.idfobjects["SizingPeriod:DesignDay"]
    site.pop(0)
    idf.copyidfobject(site_s[0])
    for i in range(len(ddy)):
        ddy.pop(0)
    for i in range(len(ddy_s)):
        idf.copyidfobject(ddy_s[i])
    # 运行idf
    idf.run(readvars=True, output_directory=rundir)
    # 读取并修改输出
    filehandle = open(rundir + 'eplustbl.htm', 'r')
    A0 = fasthtml.tablebyname(filehandle, "Building Area")[1][1][1]  # 原建筑面积
    ra = area / A0
    rv = pd.read_csv(rundir + 'eplusout.csv')
    T_begin = rv[rv["Date/Time"] == ' 01/01  01:00:00'].index[0]  # 读取数据的起始时间（跳过DesignDay）
    rv = rv.loc[rv.index >= T_begin, :].reset_index(drop=True)
    a = rv.columns[3]  # InteriorLights:Electricity
    b = rv.columns[4]  # InteriorEquipment:Electricity
    rv["Electricity Load [J]"] = rv[[a, b]].apply(lambda x: x[a] + x[b], axis=1)
    # logP = a + ' + ' + b#验证a和b是否是light和equipment
    rv.rename(columns={'Heating:EnergyTransfer [J](Hourly)': 'Heating Load [J]'}, inplace=True)
    rv.rename(columns={'Cooling:EnergyTransfer [J](Hourly)': 'Cooling Load [J]'}, inplace=True)
    rv = rv[keys]  # 只要时间和3种负荷数据
    rv = rv.apply(lambda x: x * ra if x.name in keys[1:4] else x)  # 面积等比缩放
    rv.to_csv('Load.csv', index=False)#生成csv文件
    return rv


if __name__ == '__main__':
    load = LoadCal(buildings["OfficeSmall"], 1000, weathers['安徽']["合肥"])
