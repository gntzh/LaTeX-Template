# 字体
## fontconfig
Linux下管理字体的软件，Windows下亦有适配（TeX发行版、miniconda都带有）。
参考
- 查找系统字体
```shell
fc-list -f "%{file}、%{family}、%{style}\n" :lang=zh
```
- 刷新字体缓存
```shell
fc-cache -fv
```
