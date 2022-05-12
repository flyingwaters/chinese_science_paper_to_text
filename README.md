# chinese_science_paper_to_text
读取多层级目录下的pdf文件，通常是爬虫爬下来的，将其中摘要和正文抽取出来。可以初步结构化pdf，快速抽取，并且简单清洗数据，得到想要的文本内容，得到（1）摘要（2）正文
保留了pdf的阅读顺序（左上右下）. PyMuPDF中自带的sort 排序失效.自己重排了一遍.为了保证速度，使用了python 多进程加速程序，适用大规模pdf抽取。 
40个进程，18825个pdf文件，在服务器上大概3分钟。 

结果文件中,是dict 的list.
#### 每个dict:
 {"pdf_name":pdf全局path, "whole_content": 所有内容文本, "abstract":abstract, "content_split_list":断句结果}

## 用法
```Python3
python main.py --lang chinese --pdf_dir_pth ./test_pdf --result_json_file ./reult.json --num 40
```
上面例子可以直接, 运行. 如果这个小项目帮助到了您工作或者学习。希望您可以star此项目，感谢。


----------

## 参数说明
1. --lang 选择pdf语言 有 chinese 和 english 两个选项
2. --pdf_dir_pth  pdf所在目录,可任意深度,只要pdf 在最深层
3. --result_json_file 结果
4. --num 并发进程数目

----------
### Author Contact:  
wechat: 343123814
