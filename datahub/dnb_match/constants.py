# Countries in the DnB Worldbase record are represented as numbers.
# The mapping below can be used to determine the related iso_alpha2_code.
# Not all countries have an iso_alpha2_code but this should not be a problem
# as Data Hub only cares about the countries that do.
# Names are not currently used but make the related codes more readable
# and easier to process.
DNB_COUNTRY_CODE_MAPPING = {
    '897': {'iso_alpha2_code': None, 'name': 'ABU DHABI'},
    '901': {'iso_alpha2_code': None, 'name': 'ADMIRALTY ISLANDS'},
    '005': {'iso_alpha2_code': 'AF', 'name': 'AFGHANISTAN'},
    '898': {'iso_alpha2_code': None, 'name': 'AJMAN'},
    '009': {'iso_alpha2_code': 'AL', 'name': 'ALBANIA'},
    '013': {'iso_alpha2_code': 'DZ', 'name': 'ALGERIA'},
    '021': {'iso_alpha2_code': 'AD', 'name': 'ANDORRA'},
    '025': {'iso_alpha2_code': 'AO', 'name': 'ANGOLA'},
    '027': {'iso_alpha2_code': 'AI', 'name': 'ANGUILLA'},
    '028': {'iso_alpha2_code': 'AG', 'name': 'ANTIGUA & BARBUDA'},
    '033': {'iso_alpha2_code': 'AR', 'name': 'ARGENTINA'},
    '900': {'iso_alpha2_code': 'AM', 'name': 'ARMENIA'},
    '034': {'iso_alpha2_code': 'AW', 'name': 'ARUBA'},
    '035': {'iso_alpha2_code': 'AC', 'name': 'ASCENSION ISLAND'},
    '037': {'iso_alpha2_code': 'AU', 'name': 'AUSTRALIA'},
    '041': {'iso_alpha2_code': 'AT', 'name': 'AUSTRIA'},
    '905': {'iso_alpha2_code': 'AZ', 'name': 'AZERBAIJAN'},
    '049': {'iso_alpha2_code': 'BS', 'name': 'BAHAMAS'},
    '053': {'iso_alpha2_code': 'BH', 'name': 'BAHRAIN'},
    '061': {'iso_alpha2_code': 'BD', 'name': 'BANGLADESH'},
    '065': {'iso_alpha2_code': 'BB', 'name': 'BARBADOS'},
    '915': {'iso_alpha2_code': 'BY', 'name': 'BELARUS'},
    '069': {'iso_alpha2_code': 'BE', 'name': 'BELGIUM'},
    '071': {'iso_alpha2_code': 'BZ', 'name': 'BELIZE'},
    '072': {'iso_alpha2_code': 'BJ', 'name': 'BENIN'},
    '073': {'iso_alpha2_code': 'BM', 'name': 'BERMUDA'},
    '077': {'iso_alpha2_code': 'BT', 'name': 'BHUTAN'},
    '081': {'iso_alpha2_code': 'BO', 'name': 'BOLIVIA'},
    '083': {'iso_alpha2_code': 'BQ', 'name': 'BONAIRE ST EUST SABA'},
    '910': {'iso_alpha2_code': 'BA', 'name': 'BOSNIA-HERZEGOVINA'},
    '085': {'iso_alpha2_code': 'BW', 'name': 'BOTSWANA'},
    '089': {'iso_alpha2_code': 'BR', 'name': 'BRAZIL'},
    '091': {'iso_alpha2_code': 'IO', 'name': 'BRITISH INDIAN OCEAN'},
    '096': {'iso_alpha2_code': 'BN', 'name': 'BRUNEI'},
    '100': {'iso_alpha2_code': 'BG', 'name': 'BULGARIA'},
    '101': {'iso_alpha2_code': 'BF', 'name': 'BURKINA FASO'},
    '113': {'iso_alpha2_code': 'BI', 'name': 'BURUNDI'},
    '379': {'iso_alpha2_code': 'KH', 'name': 'CAMBODIA'},
    '117': {'iso_alpha2_code': 'CM', 'name': 'CAMEROON'},
    '121': {'iso_alpha2_code': 'CA', 'name': 'CANADA'},
    '127': {'iso_alpha2_code': 'CV', 'name': 'CAPE VERDE'},
    '135': {'iso_alpha2_code': None, 'name': 'CAROLINE ISLANDS'},
    '131': {'iso_alpha2_code': 'KY', 'name': 'CAYMAN ISLANDS'},
    '141': {'iso_alpha2_code': 'CF', 'name': 'CENTRAL AFRICAN REP'},
    '149': {'iso_alpha2_code': 'TD', 'name': 'CHAD'},
    '153': {'iso_alpha2_code': 'CL', 'name': 'CHILE'},
    '157': {'iso_alpha2_code': 'CN', 'name': 'CHINA'},
    '916': {'iso_alpha2_code': '', 'name': 'CHRISTMAS ISLAND'},
    '165': {'iso_alpha2_code': 'CO', 'name': 'COLOMBIA'},
    '169': {'iso_alpha2_code': 'KM', 'name': 'COMOROS'},
    '173': {'iso_alpha2_code': 'CG', 'name': 'CONGO'},
    '865': {'iso_alpha2_code': 'CD', 'name': 'CONGO DEMOCRATIC REP'},
    '175': {'iso_alpha2_code': 'CK', 'name': 'COOK ISLANDS'},
    '177': {'iso_alpha2_code': 'CR', 'name': 'COSTA RICA'},
    '179': {'iso_alpha2_code': 'HR', 'name': 'CROATIA'},
    '181': {'iso_alpha2_code': 'CU', 'name': 'CUBA'},
    '183': {'iso_alpha2_code': 'CW', 'name': 'CURACAO'},
    '185': {'iso_alpha2_code': 'CY', 'name': 'CYPRUS'},
    '190': {'iso_alpha2_code': 'CZ', 'name': 'CZECH REPUBLIC'},
    '197': {'iso_alpha2_code': 'DK', 'name': 'DENMARK'},
    '198': {'iso_alpha2_code': 'DJ', 'name': 'DJIBOUTI'},
    '199': {'iso_alpha2_code': 'DM', 'name': 'DOMINICA'},
    '201': {'iso_alpha2_code': 'DO', 'name': 'DOMINICAN REPUBLIC'},
    '917': {'iso_alpha2_code': None, 'name': 'DUBAI'},
    '205': {'iso_alpha2_code': 'TL', 'name': 'EAST TIMOR'},
    '209': {'iso_alpha2_code': 'EC', 'name': 'ECUADOR'},
    '029': {'iso_alpha2_code': 'EG', 'name': 'EGYPT'},
    '213': {'iso_alpha2_code': 'SV', 'name': 'EL SALVADOR'},
    '785': {'iso_alpha2_code': 'GB', 'name': 'ENGLAND'},
    '217': {'iso_alpha2_code': 'GQ', 'name': 'EQUATORIAL GUINEA'},
    '919': {'iso_alpha2_code': 'ER', 'name': 'ERITREA'},
    '219': {'iso_alpha2_code': 'EE', 'name': 'ESTONIA'},
    '221': {'iso_alpha2_code': 'ET', 'name': 'ETHIOPIA'},
    '229': {'iso_alpha2_code': 'FK', 'name': 'FALKLAND ISLANDS'},
    '225': {'iso_alpha2_code': 'FO', 'name': 'FAROE ISLANDS'},
    '233': {'iso_alpha2_code': 'FJ', 'name': 'FIJI'},
    '237': {'iso_alpha2_code': 'FI', 'name': 'FINLAND'},
    '241': {'iso_alpha2_code': 'FR', 'name': 'FRANCE'},
    '245': {'iso_alpha2_code': 'GF', 'name': 'FRENCH GUIANA'},
    '249': {'iso_alpha2_code': 'PF', 'name': 'FRENCH POLYNESIA'},
    '918': {'iso_alpha2_code': None, 'name': 'FUJAIRAH'},
    '253': {'iso_alpha2_code': 'GA', 'name': 'GABON'},
    '261': {'iso_alpha2_code': 'GM', 'name': 'GAMBIA'},
    '920': {'iso_alpha2_code': 'GE', 'name': 'GEORGIA'},
    '269': {'iso_alpha2_code': 'DE', 'name': 'GERMANY'},
    '273': {'iso_alpha2_code': 'GH', 'name': 'GHANA'},
    '277': {'iso_alpha2_code': 'GI', 'name': 'GIBRALTAR'},
    '285': {'iso_alpha2_code': 'GR', 'name': 'GREECE'},
    '289': {'iso_alpha2_code': 'GL', 'name': 'GREENLAND'},
    '291': {'iso_alpha2_code': 'GD', 'name': 'GRENADA'},
    '293': {'iso_alpha2_code': 'GP', 'name': 'GUADELOUPE'},
    '297': {'iso_alpha2_code': 'GU', 'name': 'GUAM'},
    '301': {'iso_alpha2_code': 'GT', 'name': 'GUATEMALA'},
    '302': {'iso_alpha2_code': 'GG', 'name': 'GUERNSEY'},
    '305': {'iso_alpha2_code': 'GN', 'name': 'GUINEA'},
    '303': {'iso_alpha2_code': 'GW', 'name': 'GUINEA-BISSAU'},
    '309': {'iso_alpha2_code': 'GY', 'name': 'GUYANA'},
    '313': {'iso_alpha2_code': 'HT', 'name': 'HAITI'},
    '317': {'iso_alpha2_code': 'HN', 'name': 'HONDURAS'},
    '321': {'iso_alpha2_code': 'HK', 'name': 'HONG KONG'},
    '325': {'iso_alpha2_code': 'HU', 'name': 'HUNGARY'},
    '329': {'iso_alpha2_code': 'IS', 'name': 'ICELAND'},
    '333': {'iso_alpha2_code': 'IN', 'name': 'INDIA'},
    '337': {'iso_alpha2_code': 'ID', 'name': 'INDONESIA'},
    '341': {'iso_alpha2_code': 'IR', 'name': 'IRAN'},
    '345': {'iso_alpha2_code': 'IQ', 'name': 'IRAQ'},
    '349': {'iso_alpha2_code': 'IE', 'name': 'IRELAND'},
    '351': {'iso_alpha2_code': 'IM', 'name': 'ISLE OF MAN'},
    '353': {'iso_alpha2_code': 'IL', 'name': 'ISRAEL'},
    '357': {'iso_alpha2_code': 'IT', 'name': 'ITALY'},
    '361': {'iso_alpha2_code': 'CI', 'name': 'IVORY COAST'},
    '365': {'iso_alpha2_code': 'JM', 'name': 'JAMAICA'},
    '369': {'iso_alpha2_code': 'JP', 'name': 'JAPAN'},
    '374': {'iso_alpha2_code': 'JE', 'name': 'JERSEY'},
    '377': {'iso_alpha2_code': 'JO', 'name': 'JORDAN'},
    '925': {'iso_alpha2_code': 'KZ', 'name': 'KAZAKHSTAN'},
    '381': {'iso_alpha2_code': 'KE', 'name': 'KENYA'},
    '387': {'iso_alpha2_code': 'KI', 'name': 'KIRIBATI'},
    '389': {'iso_alpha2_code': 'KP', 'name': 'KOREA NORTH'},
    '393': {'iso_alpha2_code': 'KR', 'name': 'KOREA REP OF'},
    '392': {'iso_alpha2_code': 'XK', 'name': 'KOSOVO'},
    '397': {'iso_alpha2_code': 'KW', 'name': 'KUWAIT'},
    '930': {'iso_alpha2_code': 'KG', 'name': 'KYRGYZSTAN'},
    '401': {'iso_alpha2_code': 'LA', 'name': 'LAOS'},
    '935': {'iso_alpha2_code': 'LV', 'name': 'LATVIA'},
    '405': {'iso_alpha2_code': 'LB', 'name': 'LEBANON'},
    '409': {'iso_alpha2_code': 'LS', 'name': 'LESOTHO'},
    '413': {'iso_alpha2_code': 'LR', 'name': 'LIBERIA'},
    '417': {'iso_alpha2_code': 'LY', 'name': 'LIBYA'},
    '421': {'iso_alpha2_code': 'LI', 'name': 'LIECHTENSTEIN'},
    '425': {'iso_alpha2_code': 'LT', 'name': 'LITHUANIA'},
    '429': {'iso_alpha2_code': 'LU', 'name': 'LUXEMBOURG'},
    '433': {'iso_alpha2_code': 'MO', 'name': 'MACAO'},
    '965': {'iso_alpha2_code': 'MK', 'name': 'MACEDONIA'},
    '441': {'iso_alpha2_code': 'MG', 'name': 'MADAGASCAR'},
    '445': {'iso_alpha2_code': 'MW', 'name': 'MALAWI'},
    '449': {'iso_alpha2_code': 'MY', 'name': 'MALAYSIA'},
    '453': {'iso_alpha2_code': 'MV', 'name': 'MALDIVES'},
    '457': {'iso_alpha2_code': 'ML', 'name': 'MALI'},
    '461': {'iso_alpha2_code': 'MT', 'name': 'MALTA'},
    '469': {'iso_alpha2_code': 'MH', 'name': 'MARSHALL ISLANDS'},
    '473': {'iso_alpha2_code': 'MQ', 'name': 'MARTINIQUE'},
    '477': {'iso_alpha2_code': 'MR', 'name': 'MAURITANIA'},
    '481': {'iso_alpha2_code': 'MU', 'name': 'MAURITIUS'},
    '937': {'iso_alpha2_code': 'YT', 'name': 'MAYOTTE'},
    '489': {'iso_alpha2_code': 'MX', 'name': 'MEXICO'},
    '491': {'iso_alpha2_code': 'FM', 'name': 'MICRONESIA FED ST'},
    '938': {'iso_alpha2_code': 'MI', 'name': 'MIDWAY ISLAND'},
    '940': {'iso_alpha2_code': 'MD', 'name': 'MOLDOVA'},
    '497': {'iso_alpha2_code': 'MC', 'name': 'MONACO'},
    '499': {'iso_alpha2_code': 'MN', 'name': 'MONGOLIA'},
    '498': {'iso_alpha2_code': 'ME', 'name': 'MONTENEGRO'},
    '501': {'iso_alpha2_code': 'MS', 'name': 'MONTSERRAT'},
    '505': {'iso_alpha2_code': 'MA', 'name': 'MOROCCO'},
    '509': {'iso_alpha2_code': 'MZ', 'name': 'MOZAMBIQUE'},
    '510': {'iso_alpha2_code': 'MM', 'name': 'MYANMAR'},
    '511': {'iso_alpha2_code': 'NA', 'name': 'NAMIBIA'},
    '513': {'iso_alpha2_code': 'NR', 'name': 'NAURU'},
    '517': {'iso_alpha2_code': 'NP', 'name': 'NEPAL'},
    '521': {'iso_alpha2_code': 'NL', 'name': 'NETHERLANDS'},
    '525': {'iso_alpha2_code': 'AN', 'name': 'NETHERLANDS ANTILLES'},
    '529': {'iso_alpha2_code': 'NC', 'name': 'NEW CALEDONIA'},
    '537': {'iso_alpha2_code': 'NZ', 'name': 'NEW ZEALAND'},
    '541': {'iso_alpha2_code': 'NI', 'name': 'NICARAGUA'},
    '545': {'iso_alpha2_code': 'NE', 'name': 'NIGER'},
    '549': {'iso_alpha2_code': 'NG', 'name': 'NIGERIA'},
    '570': {'iso_alpha2_code': 'NU', 'name': 'NIUE'},
    '552': {'iso_alpha2_code': 'NF', 'name': 'NORFOLK ISLAND'},
    '793': {'iso_alpha2_code': 'GB', 'name': 'NORTHERN IRELAND'},
    '551': {'iso_alpha2_code': 'MP', 'name': 'NORTHERN MARIANA IS'},
    '553': {'iso_alpha2_code': 'NO', 'name': 'NORWAY'},
    '561': {'iso_alpha2_code': 'OM', 'name': 'OMAN'},
    '565': {'iso_alpha2_code': 'PK', 'name': 'PAKISTAN'},
    '567': {'iso_alpha2_code': 'PW', 'name': 'PALAU'},
    '568': {'iso_alpha2_code': 'PS', 'name': 'PALESTINIAN TERR'},
    '569': {'iso_alpha2_code': 'PA', 'name': 'PANAMA'},
    '573': {'iso_alpha2_code': 'PG', 'name': 'PAPUA NEW GUINEA'},
    '581': {'iso_alpha2_code': 'PY', 'name': 'PARAGUAY'},
    '585': {'iso_alpha2_code': 'PE', 'name': 'PERU'},
    '589': {'iso_alpha2_code': 'PH', 'name': 'PHILIPPINES'},
    '593': {'iso_alpha2_code': 'PN', 'name': 'PITCAIRN ISLAND'},
    '597': {'iso_alpha2_code': 'PL', 'name': 'POLAND'},
    '601': {'iso_alpha2_code': 'PT', 'name': 'PORTUGAL'},
    '613': {'iso_alpha2_code': 'QA', 'name': 'QATAR'},
    '942': {'iso_alpha2_code': None, 'name': 'RAS AL-KHAIMAH'},
    '617': {'iso_alpha2_code': 'RE', 'name': 'REUNION'},
    '620': {'iso_alpha2_code': 'RO', 'name': 'ROMANIA'},
    '622': {'iso_alpha2_code': 'RU', 'name': 'RUSSIAN FEDERATION'},
    '623': {'iso_alpha2_code': 'RW', 'name': 'RWANDA'},
    '641': {'iso_alpha2_code': 'WS', 'name': 'SAMOA'},
    '017': {'iso_alpha2_code': 'AS', 'name': 'SAMOA AMERICAN'},
    '649': {'iso_alpha2_code': 'SM', 'name': 'SAN MARINO'},
    '653': {'iso_alpha2_code': 'ST', 'name': 'SAO TOME & PRINCIPE'},
    '657': {'iso_alpha2_code': 'SA', 'name': 'SAUDI ARABIA'},
    '797': {'iso_alpha2_code': 'GB', 'name': 'SCOTLAND'},
    '661': {'iso_alpha2_code': 'SN', 'name': 'SENEGAL'},
    '663': {'iso_alpha2_code': 'RS', 'name': 'SERBIA'},
    '861': {'iso_alpha2_code': 'YU', 'name': 'YUGOSLAVIA'},
    '665': {'iso_alpha2_code': 'SC', 'name': 'SEYCHELLES'},
    '943': {'iso_alpha2_code': None, 'name': 'SHARJAH'},
    '669': {'iso_alpha2_code': 'SL', 'name': 'SIERRA LEONE'},
    '677': {'iso_alpha2_code': 'SG', 'name': 'SINGAPORE'},
    '680': {'iso_alpha2_code': 'SK', 'name': 'SLOVAKIA'},
    '678': {'iso_alpha2_code': 'SI', 'name': 'SLOVENIA'},
    '679': {'iso_alpha2_code': 'SB', 'name': 'SOLOMON ISLANDS'},
    '681': {'iso_alpha2_code': 'SO', 'name': 'SOMALIA'},
    '685': {'iso_alpha2_code': 'ZA', 'name': 'SOUTH AFRICA'},
    '944': {'iso_alpha2_code': 'GS', 'name': 'SOUTH GEORGIA'},
    '947': {'iso_alpha2_code': 'GS', 'name': 'SOUTH SANDWICH IS'},
    '690': {'iso_alpha2_code': 'SS', 'name': 'SOUTH SUDAN'},
    '693': {'iso_alpha2_code': 'ES', 'name': 'SPAIN'},
    '701': {'iso_alpha2_code': 'LK', 'name': 'SRI LANKA'},
    '625': {'iso_alpha2_code': 'BL', 'name': 'ST BARTHELEMY'},
    '626': {'iso_alpha2_code': 'SH', 'name': 'ST HELENA'},
    '629': {'iso_alpha2_code': 'KN', 'name': 'ST KITTS-NEVIS'},
    '633': {'iso_alpha2_code': 'LC', 'name': 'ST LUCIA'},
    '634': {'iso_alpha2_code': 'SX', 'name': 'ST MAARTEN'},
    '644': {'iso_alpha2_code': 'MF', 'name': 'ST MARTIN'},
    '635': {'iso_alpha2_code': 'PM', 'name': 'ST PIERRE MIQUELON'},
    '637': {'iso_alpha2_code': 'VC', 'name': 'ST VINCENT'},
    '705': {'iso_alpha2_code': 'SD', 'name': 'SUDAN'},
    '709': {'iso_alpha2_code': 'SR', 'name': 'SURINAME'},
    '713': {'iso_alpha2_code': 'SZ', 'name': 'SWAZILAND'},
    '717': {'iso_alpha2_code': 'SE', 'name': 'SWEDEN'},
    '721': {'iso_alpha2_code': 'CH', 'name': 'SWITZERLAND'},
    '725': {'iso_alpha2_code': 'SY', 'name': 'SYRIA'},
    '161': {'iso_alpha2_code': 'TW', 'name': 'TAIWAN'},
    '945': {'iso_alpha2_code': 'TJ', 'name': 'TAJIKISTAN'},
    '729': {'iso_alpha2_code': 'TZ', 'name': 'TANZANIA'},
    '733': {'iso_alpha2_code': 'TH', 'name': 'THAILAND'},
    '741': {'iso_alpha2_code': 'TG', 'name': 'TOGO'},
    '946': {'iso_alpha2_code': '', 'name': 'TOKELAU'},
    '745': {'iso_alpha2_code': 'TO', 'name': 'TONGA'},
    '749': {'iso_alpha2_code': 'TT', 'name': 'TRINIDAD & TOBAGO'},
    '757': {'iso_alpha2_code': 'TN', 'name': 'TUNISIA'},
    '761': {'iso_alpha2_code': 'TR', 'name': 'TURKEY'},
    '763': {'iso_alpha2_code': None, 'name': 'TURKISH REP N CYPRUS'},
    '950': {'iso_alpha2_code': 'TM', 'name': 'TURKMENISTAN'},
    '765': {'iso_alpha2_code': 'TC', 'name': 'TURKS & CAICOS IS'},
    '767': {'iso_alpha2_code': 'TV', 'name': 'TUVALU'},
    '769': {'iso_alpha2_code': 'UG', 'name': 'UGANDA'},
    '771': {'iso_alpha2_code': 'UA', 'name': 'UKRAINE'},
    '952': {'iso_alpha2_code': None, 'name': 'UMM AL-QUWAIN'},
    '777': {'iso_alpha2_code': 'AE', 'name': 'UNITED ARAB EMIRATES'},
    '790': {'iso_alpha2_code': 'GB', 'name': 'UNITED KINGDOM'},
    '813': {'iso_alpha2_code': 'UY', 'name': 'URUGUAY'},
    '814': {'iso_alpha2_code': 'UM', 'name': 'US MINOR OUTLYING IS'},
    '805': {'iso_alpha2_code': 'US', 'name': 'USA'},
    '955': {'iso_alpha2_code': 'UZ', 'name': 'UZBEKISTAN'},
    '816': {'iso_alpha2_code': 'VU', 'name': 'VANUATU'},
    '819': {'iso_alpha2_code': 'VA', 'name': 'VATICAN CITY'},
    '821': {'iso_alpha2_code': 'VE', 'name': 'VENEZUELA'},
    '829': {'iso_alpha2_code': 'VN', 'name': 'VIETNAM'},
    '093': {'iso_alpha2_code': 'VG', 'name': 'VIRGIN ISLANDS UK'},
    '970': {'iso_alpha2_code': 'UM', 'name': 'WAKE ISLAND'},
    '801': {'iso_alpha2_code': 'GB', 'name': 'WALES'},
    '841': {'iso_alpha2_code': 'WF', 'name': 'WALLIS & FUTUNA IS'},
    '853': {'iso_alpha2_code': 'YE', 'name': 'YEMEN'},
    '857': {'iso_alpha2_code': 'YD', 'name': 'YEMEN SOUTH'},
    '869': {'iso_alpha2_code': 'ZM', 'name': 'ZAMBIA'},
    '873': {'iso_alpha2_code': 'ZW', 'name': 'ZIMBABWE'},
    '000': {'iso_alpha2_code': None, 'name': 'Unknown'},
}
