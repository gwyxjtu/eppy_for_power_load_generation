# eppy_for_power_load_generation
python script for generating power cold and heat load in different building type
## 配置运行环境

+ 第一步：找到电脑energy plus的安装位置，吧Energy+.idd的路径修改到代码中的iddfile
+ 第二步：修改运行文件和building文件路径，默认可以不修改
+ 第三步：所有天气文件已经通过爬虫爬取到weathers/spyder的文件夹下，将需要仿真的城市的数据复制到epwdir所示的文件夹地下，目前写的是weather/1124
+ 第四步：修改最底部try里面的building类型，具体可选项见building的dict.
