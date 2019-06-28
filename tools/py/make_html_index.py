#!/usr/bin/env python3
#coding: utf-8



#from html.parser import HTMLParser
import csv #CSV/TSV File Reading and Writing
#import sys
import os
from os import path



DIALECT='unix-tsv'
csv.register_dialect(DIALECT, delimiter='\t',quoting=csv.QUOTE_NONE,strict=True)


def get_tsv_data(tsv_path,field_index,fields_list=[]):
	db={}
	with open(tsv_path,newline='') as tsv_file :
		reader = csv.DictReader(tsv_file,dialect=DIALECT)
		for row in reader:
			index=row[field_index]
			if index in db :
				print(WRN1,index)
			else :
				db[index]={}
			data=db[index]
			for field in fields_list :
				data[field]=row[field]
	return db


def write_html_head(output_file,lang_header,country_header,link_header):
	with open(output_file,'w') as html_file :
		html_file.writelines("<table>\n")
		html_file.writelines("<thead><tr>\n")
		html_file.writelines("<th>{}</th>\n".format(lang_header))
		html_file.writelines("<th>{}</th>\n".format(country_header))
		html_file.writelines("<th>{}</th>\n".format(link_header))
		html_file.writelines("</tr></thead>\n")
		html_file.writelines("<tbody>\n")
def write_html_line(output_file,lang_code,dir,lang,index_path_name,flag,country,links_text):
	with open(output_file,'a') as html_file :
		html_file.writelines("<tr>\n")
		html_file.writelines('<td lang="{}" dir="{}">{}</td>\n'.format(lang_code,dir,lang))
		html_file.writelines('<td title="{}">{}</td>\n'.format(country,flag))
		html_file.writelines('<td><a href="{}" hreflang="{}" type="text/html" rel="next">{}️</a></td>\n'.format(index_path_name,lang_code,links_text))
		html_file.writelines("</tr>\n")
def write_html_foot(output_file):
	with open(output_file,'a') as html_file :
		html_file.writelines("</tbody>")
		html_file.writelines("</table>")
		
		
if __name__ == '__main__':
	
	data_file='../../data/data.tsv'
	output_file='../../data/index.html'
	links_path='../../data/languages'
	
	links_file='index.html'
	links_text="➡"
		
	lang_header="language"
	country_header="country"
	link_header="link"
	
	combo_code_field="#Combo Code"
	lang_code_field="#Language Code"
	lang_endo_field="#Language Endonym"
	lang_dir_field="#Language Direction"
	country_name_field="#Country Name"
	country_flag_field="#Country Flag"

	lang_fields=[lang_code_field,lang_endo_field,lang_dir_field]
	country_fields=[country_name_field,country_flag_field]
	#all_fields=lang_fields+country_fields+[combo_code_field]

	db=get_tsv_data(data_file,combo_code_field,fields_list=lang_fields+country_fields)
	
	write_html_head(output_file,lang_header,country_header,link_header)

	for combo_code in db :
		data=db[combo_code]
		flag=data[country_flag_field]
		country=data[country_name_field]
		lang=data[lang_endo_field]
		lang_code=data[lang_code_field]
		dir=data[lang_dir_field]
				
		link_path_abs=os.path.join(links_path,combo_code.lower(),links_file)
		link_path_rel=path.relpath(link_path_abs,path.dirname(output_file))
		
		write_html_line(output_file,lang_code,dir,lang,link_path_rel,flag,country,links_text)

	write_html_foot(output_file)