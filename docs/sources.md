# SOURCES


## use

 - wp_iso639.tsv
   Source: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
   Title: "List of ISO 639-1 codes."
   Description: ISO 639 is a standardized nomenclature used to classify languages. Each language is assigned a two-letter (639-1) and three-letter (639-2 and 639-3), lowercase abbreviation, amended in later versions of the nomenclature.

 - wp_iso3166.tsv
   Source: https://en.wikipedia.org/wiki/ISO_3166-1
   Title: ISO 3166-1 - Wikipedia
   Description: a complete ISO 3166-1 encoding list of the countries which are assigned official codes

 - ms_lc.tsv
   Source: http://msdn.microsoft.com/en-us/library/ee825488(v=cs.20).aspx
   Title: Table of Language Culture Names, Codes, and ISO Values Method C++
   Description: contains values for Language Culture Names, Display Names, Culture Codes, and ISO 639x Values that are used by Commerce Server.
	Note: Microsoft is not the most reliable source, then the necessary adaptations and fix are made on this file
		- remove zh-CHS Chinese (Simplified) 0x0004 and zh-CHT Chinese (Traditional) 0x7C04
		  because its not lang-country combo and because zh-CHS and zh-CHT are not included in the official ISO 639-1 languages listing.
		- remove en-CB English - Caribbean 0x2409 
		  because Caribbean is not a country and its not in the official ISO 3166-1 countries listing.
		- remove Lt-sr-SP Serbian (Latin) - Serbia 0x081A
			and change Cy-sr-SP Serbian (Cyrillic) - Serbia 0x0C1A to sr-RS Serbian (Cyrillic) - Serbia 0x0C1A
			because only sr  Serbian Cyrillic is referenced in the official ISO 639-1 languages listing.
			and because RS is the new Alpha-2 code in the official ISO 3166-1 languages listing.
		- remove Cy-az-AZ	Azeri (Cyrillic) - Azerbaijan	0x082C
			and change Lt-az-AZ Azeri (Latin) - Azerbaijan	0x042C to az-AZ Azerbaijani- Azerbaijan	0x042C	
			because only az Azerbaijani is referenced in the official ISO 639-1 languages listing.
		- remove Cy-uz-UZ	Uzbek (Cyrillic) - Uzbekistan	0x0843
			and change Lt-uz-UZ	Uzbek (Latin) - Uzbekistan	0x0443 to uz-UZ Uzbek - Uzbekistan	0x0443
			because only uz Uzbek  is referenced in the official ISO 639-1 languages listing.
		- remove kok-IN	Konkani - India	0x0457
			because no ISO 639-1 code in the official languages listing.
		- remove syr-SY	Syriac - Syria	0x045A	 
			because no ISO 639-1 code in the official languages listing and there is already ar-SY Arabic - Syria	0x2801 ARS 
      - 	change div-MV	Dhivehi - Maldives	0x0465 to dv-MV	Dhivehi - Maldives	0x0465
		   because dv is the ISO 639-1 code for Dhivehi in the official languages listing



## others

 - Source: http://www.loc.gov/standards/iso639-2/php/code_list.php
   Title: "Library of Congress: Codes for the Representation of Names of Languages")
   Description: Complete listing of ISO 639.2 languages

 - Source: https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes
   Title: "List of ISO 3166 country codes"
   Description: The International Organization for Standardization (ISO) created and maintains the ISO 3166 standard – Codes for the representation of names of countries and their subdivisions.

 - Source: http://en.wikipedia.org/wiki/Right-to-left
   Title: "Right-to-left"
   Description: Languages with Right-to-Left writing scripts

 - Source: http://en.wikipedia.org/wiki/List_of_official_languages
   Title: List of official languages
   Description: List of languages along with the countries where each language is official.

 - Source: https://www.w3.org/International/articles/language-tags/
   Title: "Language tags in HTML and XML"
   Description: Language tags are used to indicate the language of text or other items in HTML and XML documents.

