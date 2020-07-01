# 路径配置
$out_dir = "out";
#$jobname = "main";

# 编译配置
$pdf_mode = 5;
$xelatex = "xelatex -file-line-error -halt-on-error -interaction=nonstopmode --synctex=1 %O --shell-escape %S";
$xdvipdfmx = "xdvipdfmx -E -o %D %O %S";

# PDF预览
#$preview_mode = 0;
#$pdf_previewer = "SumatraPDF -reuse-instance -inverse-search -a %O %S";

# 连续编译模式
#$preview_continuous_mode = 0;
#$pdf_update_method = 0;

# 其他配置
#$clean_ext = "synctex.gz acn acr alg aux bbl bcf blg brf fdb_latexmk glg glo gls idx ilg ind ist lof log lot out run.xml toc dvi";
