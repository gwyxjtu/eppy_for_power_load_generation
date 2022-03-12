# eppy_for_power_load_generation
python script for generating power cold and heat load in different building type

本脚本提供：
+ 中国大部分省份城市的epw天气数据，用于后续ep仿真
+ ASHRAE的一部分建筑类型的idf文件，用于后续ep仿真
+ 通过天气数据和建筑文件仿真每年8760的冷热电负荷

```Run_BuildingWeather.py```为原始版本的eppy调用程序，感谢申沅均师兄的技术支持
```weathers/spyder.py```为request爬取energy plus官网天气数据的爬虫文件
```run1124.py```为主程序，仿真脚本

## 配置运行环境

+ 第一步：找到电脑energy plus的安装位置，吧Energy+.idd的路径修改到代码中的iddfile
+ 第二步：修改运行文件和building文件路径，默认可以不修改
+ 第三步：所有天气文件已经通过爬虫爬取到weathers/spyder的文件夹下，将需要仿真的城市的数据复制到epwdir所示的文件夹地下，目前写的是weather/1124
+ 第四步：修改最底部try里面的building类型，具体可选项见building的dict.

## 运行
运行run1124.py，负荷输出到res1124文件夹中
## 附录
可提供建筑类型：
```
buildings = {
    'ApartmentHighRise': "ASHRAE9012016_ApartmentHighRise_Denver",
    'ApartmentMidRise': "ASHRAE9012016_ApartmentMidRise_Denver",
    'Hospital': "ASHRAE9012016_Hospital_Denver",
    'HotelLarge': "ASHRAE9012016_HotelLarge_Denver",
    'HotelSmall': "ASHRAE9012016_HotelSmall_Denver",
    'OfficeLarge': "ASHRAE9012016_OfficeLarge_Denver",
    'OfficeMedium': "ASHRAE9012016_OfficeMedium_Denver",
    'OfficeSmall': "ASHRAE9012016_OfficeSmall_Denver",
    'RestaurantFastFood': "ASHRAE9012016_RestaurantFastFood_Denver",
    'RestaurantSitDown': "ASHRAE9012016_RestaurantSitDown_Denver",
    'RetailStandalone': "ASHRAE9012016_RetailStandalone_Denver",
    'RetailStripmall': "ASHRAE9012016_RetailStripmall_Denver",
    'SchoolPrimary': "ASHRAE9012016_SchoolPrimary_Denver",
    'SchoolSecondary': "ASHRAE9012016_SchoolSecondary_Denver",
    'Warehouse': "ASHRAE9012016_Warehouse_Denver"

}
```

可提供天气数据：

```
{
    "Anhui": {
        "Anqing": "CHN_Anhui.Anqing.584240_CSWD",
        "Bengbu": "CHN_Anhui.Bengbu.582210_CSWD",
        "Boxian": "CHN_Anhui.Boxian.581020_CSWD",
        "Dongcheng": "CHN_Anhui.Dongcheng.583190_CSWD",
        "Hefei": "CHN_Anhui.Hefei.583210_CSWD",
        "Huoshan": "CHN_Anhui.Huoshan.583140_CSWD",
        "Shouxian": "CHN_Anhui.Shouxian.582150_CSWD",
        "Tunxi": "CHN_Anhui.Tunxi.585310_CSWD"
    },
    "Beijing": {
        "Beijing": "CHN_Beijing.Beijing.545110_CSWD",
        "Miyun": "CHN_Beijing.Miyun.544160_CSWD"
    },
    "Chongqing": {
        "Shapingba": "CHN_Chongqing.Chongqing.Shapingba.575160_CSWD",
        "Youyang": "CHN_Chongqing.Youyang.576330_CSWD"
    },
    "Fujian": {
        "Congwu": "CHN_Fujian.Congwu.591330_CSWD",
        "Fuzhou": "CHN_Fujian.Fuzhou.588470_CSWD",
        "Jianou": "CHN_Fujian.Jianou.587370_CSWD",
        "Nanping": "CHN_Fujian.Nanping.588340_CSWD",
        "Shanghang": "CHN_Fujian.Shanghang.589180_CSWD",
        "Xiamen": "CHN_Fujian.Xiamen.591340_CSWD",
        "Yongan": "CHN_Fujian.Yongan.589210_CSWD"
    },
    "Gansu": {
        "Dunhuang": "CHN_Gansu.Dunhuang.524180_CSWD",
        "Hezuo": "CHN_Gansu.Hezuo.560800_CSWD",
        "Jiuquan": "CHN_Gansu.Jiuquan.525330_CSWD",
        "Lanzhou": "CHN_Gansu.Lanzhou.528890_CSWD",
        "Minqin": "CHN_Gansu.Minqin.526810_CSWD",
        "Minxian": "CHN_Gansu.Minxian.560930_CSWD",
        "Pingliang": "CHN_Gansu.Pingliang.539150_CSWD",
        "Tianshui": "CHN_Gansu.Tianshui.570060_CSWD",
        "Wudu": "CHN_Gansu.Wudu.560960_CSWD",
        "Wushaoling": "CHN_Gansu.Wushaoling.527870_CSWD",
        "Xifengzhen": "CHN_Gansu.Xifengzhen.539230_CSWD",
        "Yumenzhen": "CHN_Gansu.Yumenzhen.524360_CSWD",
        "Yuzhong": "CHN_Gansu.Yuzhong.529830_CSWD"
    },
    "Guangdong": {
        "Dianbai": "CHN_Guangdong.Dianbai.596640_CSWD",
        "Guangzhou": "CHN_Guangdong.Guangzhou.592870_CSWD",
        "Heyuan": "CHN_Guangdong.Heyuan.592930_CSWD",
        "Nanxiong": "CHN_Guangdong.Nanxiong.579960_CSWD",
        "Shantou": "CHN_Guangdong.Shantou.593160_CSWD",
        "Shanwei": "CHN_Guangdong.Shanwei.595010_CSWD",
        "Shaoguan": "CHN_Guangdong.Shaoguan.590820_CSWD",
        "Yangjiang": "CHN_Guangdong.Yangjiang.596630_CSWD",
        "Zhengcheng": "CHN_Guangdong.Zhengcheng.592940_CSWD"
    },
    "Guangxi": {
        "Baise": "CHN_Guangxi.Zhuang.Baise.592110_CSWD",
        "Duan": "CHN_Guangxi.Zhuang.Duan.590370_CSWD",
        "Guilin": "CHN_Guangxi.Zhuang.Guilin.579570_CSWD",
        "Guiping": "CHN_Guangxi.Zhuang.Guiping.592540_CSWD",
        "Hechi": "CHN_Guangxi.Zhuang.Hechi.590230_CSWD",
        "Lingshan": "CHN_Guangxi.Zhuang.Lingshan.594460_CSWD",
        "Longzhou": "CHN_Guangxi.Zhuang.Longzhou.594170_CSWD",
        "Nanning": "CHN_Guangxi.Zhuang.Nanning.594310_CSWD",
        "Qinzhou": "CHN_Guangxi.Zhuang.Qinzhou.596320_CSWD",
        "Wuzhou": "CHN_Guangxi.Zhuang.Wuzhou.592650_CSWD"
    },
    "Guizhou": {
        "Bijie": "CHN_Guizhou.Bijie.577070_CSWD",
        "Guiyang": "CHN_Guizhou.Guiyang.578160_CSWD",
        "Sansui": "CHN_Guizhou.Sansui.578320_CSWD",
        "Tongzi": "CHN_Guizhou.Tongzi.576060_CSWD",
        "Weining": "CHN_Guizhou.Weining.566910_CSWD",
        "Xingyi": "CHN_Guizhou.Xingyi.579020_CSWD",
        "Zunyi": "CHN_Guizhou.Zunyi.577130_CSWD"
    },
    "Hainan": {
        "Dongfang": "CHN_Hainan.Dongfang.598380_CSWD",
        "Haikou": "CHN_Hainan.Haikou.597580_CSWD",
        "Qionghai": "CHN_Hainan.Qionghai.598550_CSWD"
    },
    "Hebei": {
        "Chengde": "CHN_Hebei.Chengde.544230_CSWD",
        "Fengning": "CHN_Hebei.Fengning.543080_CSWD",
        "Huailai": "CHN_Hebei.Huailai.544050_CSWD",
        "Leting": "CHN_Hebei.Leting.545390_CSWD",
        "Raoyang": "CHN_Hebei.Raoyang.546060_CSWD",
        "Shijiazhuang": "CHN_Hebei.Shijiazhuang.536980_CSWD",
        "Xingtai": "CHN_Hebei.Xingtai.537980_CSWD",
        "Zhangbei": "CHN_Hebei.Zhangbei.533990_CSWD"
    },
    "Heilongjiang": {
        "Anda": "CHN_Heilongjiang.Anda.508540_CSWD",
        "Fujin": "CHN_Heilongjiang.Fujin.507880_CSWD",
        "Fuyu": "CHN_Heilongjiang.Fuyu.507420_CSWD",
        "Hailun": "CHN_Heilongjiang.Hailun.507560_CSWD",
        "Harbin": "CHN_Heilongjiang.Harbin.509530_CSWD",
        "Huma": "CHN_Heilongjiang.Huma.503530_CSWD",
        "Jiamusi": "CHN_Heilongjiang.Jiamusi.508730_CSWD",
        "Jixi": "CHN_Heilongjiang.Jixi.509780_CSWD",
        "Keshan": "CHN_Heilongjiang.Keshan.506580_CSWD",
        "Mohe": "CHN_Heilongjiang.Mohe.501360_CSWD",
        "Mudanjiang": "CHN_Heilongjiang.Mudanjiang.540940_CSWD",
        "Nenjiang": "CHN_Heilongjiang.Nenjiang.505570_CSWD",
        "Qiqihar": "CHN_Heilongjiang.Qiqihar.507450_CSWD",
        "Shangzhi": "CHN_Heilongjiang.Shangzhi.509680_CSWD",
        "Suifenhe": "CHN_Heilongjiang.Suifenhe.540960_CSWD",
        "Sunwu": "CHN_Heilongjiang.Sunwu.505640_CSWD",
        "Tonghe": "CHN_Heilongjiang.Tonghe.509630_CSWD",
        "Zhaozhou": "CHN_Heilongjiang.Zhaozhou.509500_CSWD"
    },
    "Henan": {
        "Anyang": "CHN_Henan.Anyang.538980_CSWD",
        "Lushi": "CHN_Henan.Lushi.570670_CSWD",
        "Nanyang": "CHN_Henan.Nanyang.571780_CSWD",
        "Shangqiu": "CHN_Henan.Shangqiu.580050_CSWD",
        "Xinyang": "CHN_Henan.Xinyang.572970_CSWD",
        "Zhengzhou": "CHN_Henan.Zhengzhou.570830_CSWD",
        "Zhumadian": "CHN_Henan.Zhumadian.572900_CSWD"
    },
    "Hubei": {
        "Exi": "CHN_Hubei.Exi.574470_CSWD",
        "Laohekou": "CHN_Hubei.Laohekou.572650_CSWD",
        "Macheng": "CHN_Hubei.Macheng.573990_CSWD",
        "Wuhan": "CHN_Hubei.Wuhan.574940_CSWD",
        "Yichang": "CHN_Hubei.Yichang.574610_CSWD",
        "Yunxi": "CHN_Hubei.Yunxi.572510_CSWD",
        "Zhongxiang": "CHN_Hubei.Zhongxiang.573780_CSWD"
    },
    "Hunan": {
        "Changde": "CHN_Hunan.Changde.576620_CSWD",
        "Changning": "CHN_Hunan.Changning.578740_CSWD",
        "Changsha": "CHN_Hunan.Changsha.576870_CSWD",
        "Jishou": "CHN_Hunan.Jishou.576490_CSWD",
        "Lingling": "CHN_Hunan.Lingling.578660_CSWD",
        "Nanxian": "CHN_Hunan.Nanxian.575740_CSWD",
        "Shimen": "CHN_Hunan.Shimen.575620_CSWD",
        "Wugang": "CHN_Hunan.Wugang.578530_CSWD",
        "Zhijiang": "CHN_Hunan.Zhijiang.577450_CSWD",
        "Zhuzhou": "CHN_Hunan.Zhuzhou.577800_CSWD"
    },
    "Jiangsu": {
        "Dongtai": "CHN_Jiangsu.Dongtai.582510_CSWD",
        "Ganyu": "CHN_Jiangsu.Ganyu.580400_CSWD",
        "Huaiyang-Qingjiang": "CHN_Jiangsu.Huaiyang-Qingjiang.581440_CSWD",
        "Lusi": "CHN_Jiangsu.Lusi.582650_CSWD",
        "Nanjing": "CHN_Jiangsu.Nanjing.582380_CSWD",
        "Xuzhou": "CHN_Jiangsu.Xuzhou.580270_CSWD"
    },
    "Jiangxi": {
        "Ganzhou": "CHN_Jiangxi.Ganzhou.579930_CSWD",
        "Jian": "CHN_Jiangxi.Jian.577990_CSWD",
        "Jingdezhen": "CHN_Jiangxi.Jingdezhen.585270_CSWD",
        "Nanchang": "CHN_Jiangxi.Nanchang.586060_CSWD",
        "Nancheng": "CHN_Jiangxi.Nancheng.587150_CSWD",
        "Suichuan": "CHN_Jiangxi.Suichuan.578960_CSWD",
        "Yichun": "CHN_Jiangxi.Yichun.577930_CSWD",
        "Yushan": "CHN_Jiangxi.Yushan.586340_CSWD"
    },
    "Jilin": {
        "Baicheng": "CHN_Jilin.Baicheng.509360_CSWD",
        "Changchun": "CHN_Jilin.Changchun.541610_CSWD",
        "Donggang": "CHN_Jilin.Donggang.542840_CSWD",
        "Dunhua": "CHN_Jilin.Dunhua.541860_CSWD",
        "Linjiang": "CHN_Jilin.Linjiang.543740_CSWD",
        "Gorlos": "CHN_Jilin.Qian.Gorlos.509490_CSWD",
        "Siping": "CHN_Jilin.Siping.541570_CSWD",
        "Yanji": "CHN_Jilin.Yanji.542920_CSWD"
    },
    "Liaoning": {
        "Benxi": "CHN_Liaoning.Benxi.543460_CSWD",
        "Chaoyang": "CHN_Liaoning.Chaoyang.543240_CSWD",
        "Dalian": "CHN_Liaoning.Dalian.546620_CSWD",
        "Dandong": "CHN_Liaoning.Dandong.544970_CSWD",
        "Jinzhou": "CHN_Liaoning.Jinzhou.543370_CSWD",
        "Kuandian": "CHN_Liaoning.Kuandian.544930_CSWD",
        "Shenyang": "CHN_Liaoning.Shenyang.543420_CSWD",
        "Xingcheng": "CHN_Liaoning.Xingcheng.544550_CSWD",
        "Xinmin": "CHN_Liaoning.Xinmin.543330_CSWD",
        "Yingkou": "CHN_Liaoning.Yingkou.544710_CSWD",
        "Zhangwu": "CHN_Liaoning.Zhangwu.542360_CSWD"
    },
    "Nei": {
        "Hot": "CHN_Nei.Mongol.Abag.Qi.Hot.531920_CSWD",
        "Arxan": "CHN_Nei.Mongol.Arxan.507270_CSWD",
        "Bailingmiao": "CHN_Nei.Mongol.Bailingmiao.533520_CSWD",
        "Qi": "CHN_Nei.Mongol.Xi.Ujimqin.Qi.540120_CSWD",
        "Mod": "CHN_Nei.Mongol.Bayan.Mod.524950_CSWD",
        "Bugt": "CHN_Nei.Mongol.Bugt.506320_CSWD",
        "Chifeng": "CHN_Nei.Mongol.Chifeng.542180_CSWD",
        "Dongsheng": "CHN_Nei.Mongol.Dongsheng.535430_CSWD",
        "Duolun": "CHN_Nei.Mongol.Duolun.542080_CSWD",
        "Erenhot": "CHN_Nei.Mongol.Erenhot.530680_CSWD",
        "Hailar": "CHN_Nei.Mongol.Hailar.505270_CSWD",
        "Hailisu": "CHN_Nei.Mongol.Hailisu.532310_CSWD",
        "Haliut": "CHN_Nei.Mongol.Haliut.533360_CSWD",
        "Hohhot": "CHN_Nei.Mongol.Hohhot.534630_CSWD",
        "Huade": "CHN_Nei.Mongol.Huade.533910_CSWD",
        "Jartai": "CHN_Nei.Mongol.Jartai.535020_CSWD",
        "Jurh": "CHN_Nei.Mongol.Jurh.532760_CSWD",
        "Kailu": "CHN_Nei.Mongol.Kailu.541340_CSWD",
        "Linxi": "CHN_Nei.Mongol.Linxi.541150_CSWD",
        "Manzhouli": "CHN_Nei.Mongol.Manzhouli.505140_CSWD",
        "Solon": "CHN_Nei.Mongol.Solon.508340_CSWD",
        "Tongliao": "CHN_Nei.Mongol.Tongliao.541350_CSWD",
        "Tulihe": "CHN_Nei.Mongol.Tulihe.504340_CSWD",
        "Xilinhot": "CHN_Nei.Mongol.Xilinhot.541020_CSWD"
    },
    "Ningxia": {
        "Guyuan": "CHN_Ningxia.Hui.Guyuan.538170_CSWD",
        "Yanchi": "CHN_Ningxia.Hui.Yanchi.537230_CSWD",
        "Yinchuan": "CHN_Ningxia.Hui.Yinchuan.536140_CSWD"
    },
    "Qinghai": {
        "Daqaidam": "CHN_Qinghai.Daqaidam.527130_CSWD",
        "Darlag": "CHN_Qinghai.Darlag.560460_CSWD",
        "Us": "CHN_Qinghai.Dulan.Us.528360_CSWD",
        "Gangca": "CHN_Qinghai.Gangca.527540_CSWD",
        "Golmud": "CHN_Qinghai.Golmud.528180_CSWD",
        "Lenghu": "CHN_Qinghai.Lenghu.526020_CSWD",
        "Madoi": "CHN_Qinghai.Madoi.560330_CSWD",
        "Minhe": "CHN_Qinghai.Minhe.528760_CSWD",
        "Nangqen": "CHN_Qinghai.Nangqen.561250_CSWD",
        "Qumarleb": "CHN_Qinghai.Qumarleb.560210_CSWD",
        "Tuotuohe": "CHN_Qinghai.Tuotuohe.560040_CSWD",
        "Xinghai": "CHN_Qinghai.Xinghai.529430_CSWD",
        "Xining": "CHN_Qinghai.Xining.528660_CSWD",
        "Yushu": "CHN_Qinghai.Yushu.560290_CSWD"
    },
    "Shaanxi": {
        "Ankangan": "CHN_Shaanxi.Ankangan.572450_CSWD",
        "Dingbian": "CHN_Shaanxi.Dingbian.537250_CSWD",
        "Hanzhong": "CHN_Shaanxi.Hanzhong.571270_CSWD",
        "Luochuan": "CHN_Shaanxi.Luochuan.539420_CSWD",
        "Suide": "CHN_Shaanxi.Suide.537540_CSWD",
        "Xian": "CHN_Shaanxi.Xian.570360_CSWD",
        "Yanan": "CHN_Shaanxi.Yanan.538450_CSWD",
        "Yulin": "CHN_Shaanxi.Yulin.536460_CSWD"
    },
    "Shandong": {
        "Chaoyang": "CHN_Shandong.Chaoyang.548080_CSWD",
        "Chengshantou": "CHN_Shandong.Chengshantou.547760_CSWD",
        "Xian": "CHN_Shandong.Huimin.Xian.547250_CSWD",
        "Jinan": "CHN_Shandong.Jinan.548230_CSWD",
        "Juxian": "CHN_Shandong.Juxian.549360_CSWD",
        "Longkou": "CHN_Shandong.Longkou.547530_CSWD",
        "Weifang": "CHN_Shandong.Weifang.548430_CSWD",
        "Yanzhou": "CHN_Shandong.Yanzhou.549160_CSWD"
    },
    "Shanghai": {
        "Shanghai": "CHN_Shanghai.Shanghai.583620_CSWD"
    },
    "Shanxi": {
        "Datong": "CHN_Shanxi.Datong.534870_CSWD",
        "Houma": "CHN_Shanxi.Houma.539630_CSWD",
        "Jiexiu": "CHN_Shanxi.Jiexiu.538630_CSWD",
        "Taiyuan": "CHN_Shanxi.Taiyuan.537720_CSWD",
        "Yuanping": "CHN_Shanxi.Yuanping.536730_CSWD",
        "Yuncheng": "CHN_Shanxi.Yuncheng.539590_CSWD",
        "Yushe": "CHN_Shanxi.Yushe.537870_CSWD"
    },
    "Sichuan": {
        "Barkam": "CHN_Sichuan.Barkam.561720_CSWD",
        "Chengdu": "CHN_Sichuan.Chengdu.562940_CSWD",
        "Garze": "CHN_Sichuan.Garze.561460_CSWD",
        "Hongyuan": "CHN_Sichuan.Hongyuan.561730_CSWD",
        "Huili": "CHN_Sichuan.Huili.566710_CSWD",
        "Jiulong": "CHN_Sichuan.Jiulong.564620_CSWD",
        "Leshan": "CHN_Sichuan.Leshan.563860_CSWD",
        "Litang": "CHN_Sichuan.Litang.562570_CSWD",
        "Luzhou": "CHN_Sichuan.Luzhou.576020_CSWD",
        "Mianyang": "CHN_Sichuan.Mianyang.561960_CSWD",
        "Nanchong": "CHN_Sichuan.Nanchong.574110_CSWD",
        "Songpan": "CHN_Sichuan.Songpan.561820_CSWD",
        "Wanyuan": "CHN_Sichuan.Wanyuan.572370_CSWD",
        "Xichang": "CHN_Sichuan.Xichang.565710_CSWD",
        "Yibin": "CHN_Sichuan.Yibin.564920_CSWD"
    },
    "Tianjin": {
        "Tianjin": "CHN_Tianjin.Tianjin.545270_CSWD"
    },
    "Tibet": {
        "Lhasa": "CHN_Tibet.Lhasa.555910_CSWD",
        "Nyingchi": "CHN_Tibet.Nyingchi.563120_CSWD",
        "Qamdo": "CHN_Tibet.Qamdo.561370_CSWD"
    },
    "Xinjiang": {
        "Aksu": "CHN_Xinjiang.Uygur.Aksu.516280_CSWD",
        "Altay": "CHN_Xinjiang.Uygur.Altay.510760_CSWD",
        "Bachu": "CHN_Xinjiang.Uygur.Bachu.517160_CSWD",
        "Fuyun": "CHN_Xinjiang.Uygur.Fuyun.510870_CSWD",
        "Hami": "CHN_Xinjiang.Uygur.Hami.522030_CSWD",
        "Hoboksar": "CHN_Xinjiang.Uygur.Hoboksar.511560_CSWD",
        "Hotan": "CHN_Xinjiang.Uygur.Hotan.518280_CSWD",
        "Jinghe": "CHN_Xinjiang.Uygur.Jinghe.513340_CSWD",
        "Karamay": "CHN_Xinjiang.Uygur.Karamay.512430_CSWD",
        "Kashi": "CHN_Xinjiang.Uygur.Kashi.517090_CSWD",
        "Kuqa": "CHN_Xinjiang.Uygur.Kuqa.516440_CSWD",
        "Minfeng": "CHN_Xinjiang.Uygur.Minfeng.518390_CSWD",
        "Ruoqiang": "CHN_Xinjiang.Uygur.Ruoqiang.517770_CSWD",
        "Shache": "CHN_Xinjiang.Uygur.Shache.518110_CSWD",
        "Tacheng": "CHN_Xinjiang.Uygur.Tacheng.511330_CSWD",
        "Tikanlik": "CHN_Xinjiang.Uygur.Tikanlik.517650_CSWD",
        "Turpan": "CHN_Xinjiang.Uygur.Turpan.515730_CSWD",
        "Urumqi": "CHN_Xinjiang.Uygur.Urumqi.514630_CSWD",
        "Wusu": "CHN_Xinjiang.Uygur.Wusu.513460_CSWD",
        "Yanqi": "CHN_Xinjiang.Uygur.Yanqi.515670_CSWD",
        "Yining": "CHN_Xinjiang.Uygur.Yining.514310_CSWD"
    },
    "Yunnan": {
        "Chuxiong": "CHN_Yunnan.Chuxiong.567680_CSWD",
        "Deqen": "CHN_Yunnan.Deqen.564440_CSWD",
        "Kunming": "CHN_Yunnan.Kunming.567780_CSWD",
        "Lancang": "CHN_Yunnan.Lancang.569540_CSWD",
        "Lijiang": "CHN_Yunnan.Lijiang.566510_CSWD",
        "Lincang": "CHN_Yunnan.Lincang.569510_CSWD",
        "Mengla": "CHN_Yunnan.Mengla.569690_CSWD",
        "Mengzi": "CHN_Yunnan.Mengzi.569850_CSWD",
        "Simao": "CHN_Yunnan.Simao.569640_CSWD",
        "Tengchong": "CHN_Yunnan.Tengchong.567390_CSWD",
        "Yuanjiang": "CHN_Yunnan.Yuanjiang.569660_CSWD"
    },
    "Zhejiang": {
        "Dinghai": "CHN_Zhejiang.Dinghai.584770_CSWD",
        "Hangzhou": "CHN_Zhejiang.Hangzhou.584570_CSWD",
        "Hongjia": "CHN_Zhejiang.Hongjia.586650_CSWD",
        "Quxian": "CHN_Zhejiang.Quxian.586330_CSWD",
        "Wenzhou": "CHN_Zhejiang.Wenzhou.586590_CSWD"
    }
}
```
