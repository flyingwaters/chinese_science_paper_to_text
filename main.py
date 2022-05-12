#fenglongyu 
#2022-5-12
#chengdu
#start this to get the content from pdf
import argparse
from extract import Process

def main():
    parser = argparse.ArgumentParser(description="parse pdf into words, notice:design for chinese academic pdf in zhiwang")
    parser.add_argument("--lang", type=str, default="english",)
    parser.add_argument("--pdf_dir_pth", type=str, default="/tmp/result/experiment")
    parser.add_argument("--result_json_file", type=str, default="/tmp/result/pdf_content.json")
    parser.add_argument("--num", type=int, default=40)
    args = parser.parse_args()
    language = args.lang    
    dir_pth = args.pdf_dir_pth
    file_pth = args.result_json_file
    num = args.num
    import os
    if not os.path.isdir(dir_pth):
        print("wrong pdf path")
        return 
    proc = Process(num)
    if language.lower()=="chinese":
        
        list_names = proc.all_filename_list(dir_pth)
        proc.parallel_excute(list_names, file_pth, proc.parse_pdf)
        print("sucess!")
    elif language.lower()=="english":
        
        list_names = proc.all_filename_list(dir_pth)
        proc.parallel_excute(list_names, file_pth, proc.extract_abstract_from_pdf_en)
        print("success!")

if __name__ == "__main__":
    main()