#!/usr/bin/env python3
#coding: utf-8



import csv #CSV/TSV File Reading and Writing
#import sys
import os
from os import path

DIALECT='unix-tsv'
csv.register_dialect(DIALECT, delimiter='\t',quoting=csv.QUOTE_NONE,strict=True)

WRN1="WARNING duplicate index:"
ERR1="missing lang code:"
ERR2="missing country code:"


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


def get_flags_files(path_name):
	db={}
	for file_name in os.listdir(path_name) :
		file_path_name=os.path.join(path_name,file_name)
		if path.isfile(file_path_name) :
			code=path.splitext(file_name)[0]
			db[code]=file_path_name
	return db

	
def write_tsv_files(db,output_file,head_fields):
	with open(output_file,'w',newline='') as tsv_file :
		writer = csv.DictWriter(tsv_file,fieldnames=head_fields,dialect=DIALECT)
		for data in db :
			writer.writerow(data)




if __name__ == '__main__':
	
	flags_path="../../data/country-flags/data/flags/"
	flags_file="../../data/sources/unicode_flags.tsv"
	combo_file='../../data/sources/ms_lc.tsv'
	country_file='../../data/sources/wp_iso3166.tsv'
	lang_file='../../data/sources/wp_iso639.tsv'
	dir_file='../../data/sources/wm_dir.tsv'
	output_file='../../data/data.tsv'

	lang_family_field="#Language family"
	lang_code_field="#639-1"
	lang_name_field="#ISO language name"
	lang_endo_field="#Native name (endonym)"
	lang_dir_field="#Directionality"
	code_dir_field="#Code"
	country_code_field="#Alpha-2 code"
	country_name_field="#English short name"
	country_flag_field="#Flag"
	flag_field="#Emoji"
	flag_country_field="#ISO"
	combo_code_field="#Language Culture Name"
	lang_fields=[lang_family_field,lang_code_field,lang_name_field,lang_endo_field,lang_dir_field]
	country_fields=[country_code_field,country_name_field,flag_field,country_flag_field]
	head_fields=[combo_code_field]+lang_fields+country_fields



	code_db=get_tsv_data(combo_file,combo_code_field)
	country_db=get_tsv_data(country_file,country_code_field,fields_list=[country_name_field])
	lang_db=get_tsv_data(lang_file,lang_code_field,fields_list=[lang_family_field,lang_name_field,lang_endo_field])
	dir_db=get_tsv_data(dir_file,code_dir_field,fields_list=[lang_dir_field])
	flags_unicode_db=get_tsv_data(flags_file,flag_country_field,fields_list=[flag_field])
	flags_image_db=get_flags_files(flags_path)
	
	header={}
	header[combo_code_field]=combo_code_field
	header[lang_family_field]=lang_family_field
	header[lang_code_field]=lang_code_field
	header[lang_name_field]=lang_name_field
	header[lang_endo_field]=lang_endo_field
	header[lang_dir_field]=lang_dir_field
	header[country_code_field]=country_code_field
	header[country_name_field]=country_name_field
	header[flag_field]=flag_field
	header[country_flag_field]=country_flag_field
	db=[header]
	for combo_code in code_db :
		lang_code,sep,country_code=combo_code.rpartition('-')
		if not lang_code in lang_db :
			print(ERR1,lang_code)
		elif not lang_code in dir_db :
			print(ERR1,lang_code)
		elif not country_code in country_db :
			print(ERR2,country_code)
		elif not country_code in flags_unicode_db :
			print(ERR2,country_code)
		elif not country_code.lower() in flags_image_db :
			print(ERR2,country_code)
		else :
			flag_image=flags_image_db[country_code.lower()]
			flag_unicode=flags_unicode_db[country_code]
			country=country_db[country_code]
			lang=lang_db[lang_code]
			dir=dir_db[lang_code]


			data={}
			data[combo_code_field]=combo_code
			data[lang_dir_field]=dir[lang_dir_field]
			data[lang_family_field]=lang[lang_family_field]
			data[lang_code_field]=lang_code
			data[lang_name_field]=lang[lang_name_field]
			data[lang_endo_field]=lang[lang_endo_field]
			data[country_name_field]=country[country_name_field]
			data[country_code_field]=country_code
			data[flag_field]=flag_unicode[flag_field]
			data[country_flag_field]=path.relpath(flag_image,path.dirname(output_file))
			db.append(data)
			
	
	write_tsv_files(db,output_file,head_fields)
	