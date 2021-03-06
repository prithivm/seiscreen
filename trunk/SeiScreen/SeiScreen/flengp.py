#coding=utf-8
# fleng versión en español
from fleng import FlEngLookup as original_FlEngLookup
sreg_esp = [
    "",
    "ALASKA - ARCO DE LAS ISLAS ALEUTIANAS", "ESTE DE ALASKA A ISLA DE VONCOUVER",
    "CALIFORNIA - AREA DE NEVADA", "BAJA CALIFORNIA Y GOLFO DE CALIFORNIA",
    "AREA MEXICO - GUATEMALA", "AMERICA CENTRAL", "EL CARIBE",
    "SUDAMERICA ANDINA", "EXTREMO DE AMÉRICA DEL SUR", "ANTILLAS DEL SUR",
    "AREA NUEVA ZELANDA", "AREA DE LA CUENCA KERMADAC - TONGA - SAMOA", "AREA DE LAS ISLAS FIYI",
    "ISLAS VANUATU", "BISMARCK Y LAS ISLAS SALOMÓN", "ÁREA DE NUEVA GUINEA",
    "ISLAS CAROLINAS A GUAM", "GUAM A JAPÓN",
    "JAPÓN - ISLAS KURILES - LA PENÍNSULA DE KAMCHATKA",
    "ISLAS RYUKYU, EL SUROESTE DE JAPÓN", "TAIWAN", "FILIPINAS",
    "BORNEO - SULAWESI", "ARCO LA SONDA", "MYANMAR Y ASIA DEL ESTE",
    "INDIA - XIZANG - SICHUAN - YUNNAN", "EL SUR DE XINJIANG A GANSU",
    "LAGO ISSYK-KUL A LAGO BAIKAL", "ASIA OCCIDENTAL",
    "ORIENTE MEDIO - CRIMEA - BALCANES ORIENTALES", "MEDITERRÁNEO OCCIDENTAL AREA",
    "OCÉANO ATLÁNTICO", "EL OCÉANO ÍNDICO", "EL ESTE DE NORTEAMÉRICA",
    "ESTE DE SUDAMÉRICA", "EL NOROESTE DE EUROPA", "ÁFRICA", "AUSTRALIA",
    "CUENCA DEL PACIFICO", "ARCTIC ZONE", "ASIA ORIENTAL",
    "EL NORESTE DE ASIA, EL NORTE DE ALASKA A GROENLANDIA",
    "EL SURESTE Y ANTÁRTICA DEL OCEANO PACIFICO", "ZONA DE GALAPAGOS", "MACQUARIE LOOP",
    "ISLAS ANDAMÁN A SUMATRA", "BALUCHISTÁN", "HINDU KUSH Y PAMIR",
    "EURASIA", "ANTÁRTIDA",
    ]

greg_esp = ["",
    "Central Alaska, Estados Unidos", "El sur de Alaska, Estados Unidos",
    "Mar de Bering", "Islas Komandorsky, Rusia, la regi'on",
    "Cerca de las Islas, Islas Aleutianas, Estados Unidos",
    "Rat Islas, Islas Aleutianas, Estados Unidos",
    "Andreanof, Islas Aleutianas, Estados Unidos",
    "Pribilof, Alaska, Estados Unidos",
    "Fox, Islas Aleutianas, Estados Unidos",
    "Isla Unimak, Alaska, Estados Unidos, la regi'on",
    "Bristol Bay, Alaska, Estados Unidos", "la Pen'insula de Alaska, Estados Unidos",
    "La isla de Kodiak, Alaska, Estados Unidos, la regi'on",
    "Pen'insula de Kenai, Alaska, Estados Unidos", "Golfo de Alaska",
    "Al sur de las Islas Aleutianas", "Al sur de Alaska",
    "El sur de Territorio del Yuk'on, Canad'a", "Sureste de Alaska, Estados Unidos",
    "Frente a la costa del sureste de Alaska, Estados Unidos", "Al oeste de la isla de Vancouver",
    "Queen Charlotte Islands, Canad'a, la regi'on", "British Columbia, Canad'a",
    "Alberta, Canad'a", "Isla de Vancouver, Canad'a, la regi'on",
    "Frente a la costa de Washington, Estados Unidos",
    "Cerca de la costa de Washington, Estados Unidos", "Washington-Oregon regi'on fronteriza",
    "Washington, Estados Unidos", "Frente a la costa de Oregon, Estados Unidos",
    "Cerca de la costa de Oregon, Estados Unidos", "Oregon, Estados Unidos",
    "Western Idaho, Estados Unidos",
    "Frente a la costa del norte de California, Estados Unidos",
    "Cerca de la costa del norte de California, Estados Unidos",
    "El norte de California, Estados Unidos", "Nevada, Estados Unidos",
    "Frente a la costa de California, Estados Unidos", "Centro de California, Estados Unidos",
    "California y Nevada, en la regi'on fronteriza", "El sur de Nevada, Estados Unidos",
    "Oeste de Arizona, Estados Unidos", "el sur de California, Estados Unidos",
    "California-Arizona en la regi'on fronteriza",
    "California-Baja California regi'on fronteriza",
    "Oeste de Arizona-Sonora en la regi'on fronteriza",
    "Fuera de la costa oeste de Baja California, M'exico", "Baja California, M'exico",
    "Golfo de California, M'exico", "Sonora, M'exico", "Frente a la costa del centro de M'exico",
    "Cerca de la costa del centro de M'exico", "Islas Revillagigedo, M'exico, la regi'on",
    "Frente a la costa de Jalisco, M'exico", "Cerca de la costa de Jalisco, M'exico",
    "Cerca de la costa de Michoac'an, M'exico", "Michoac'an, M'exico",
    "Cerca de la costa de Guerrero, M'exico", "Guerrero, M'exico", "Oaxaca, M'exico",
    "Chiapas, M'exico", "M'exico-Guatemala en la regi'on fronteriza", "Frente a la costa de M'exico",
    "Frente a la costa de Michoac'an, M'exico", "Frente a la costa de Guerrero, M'exico",
    "Cerca de la costa de Oaxaca, M'exico", "Frente a la costa de Oaxaca, M'exico",
    "Frente a la costa de Chiapas, M'exico", "Cerca de la costa de Chiapas, M'exico", "Guatemala",
    "Cerca de la costa de Guatemala", "Honduras", "El Salvador", "Cerca de la costa de Nicaragua",
    "Nicaragua", "Frente a la costa de Am'erica Central", "Frente a la costa de Costa Rica",
    "Costa Rica", "al norte de Panam'a", "Panam'a-Costa Rica Regi'on fronteriza", "Panam'a",
    "Panam'a-Colombia en la regi'on fronteriza", "Al sur de Panam'a",
    "Pen'insula de Yucat'an, M'exico", "regi'on de Cuba", "regi'on de Jamaica", "regi'on de Hait'i",
    "Rep'ublica Dominicana regi'on", "Canal de la Mona", "Puerto Rico regi'on",
    "Islas V'irgenes", "Islas de Sotavento", "Belice", "Mar Caribe",
    "Islas de Barlovento", "Cerca de la costa norte de Colombia", "Cerca de la costa de Venezuela",
    "Trinidad", "el norte de Colombia", "Lago de Maracaibo, Venezuela", "Venezuela",
    "Cerca de la costa occidental de Colombia", "Colombia", "Frente a la costa de Ecuador",
    "Cerca de la costa de Ecuador", "Colombia-Ecuador en la regi'on fronteriza", "Ecuador",
    "Frente a la costa del norte del Per'u", "Cerca de la costa del norte del Per'u",
    "El Per'u-Ecuador en la regi'on fronteriza", "el norte del Per'u", "Per'u-Brasil regi'on fronteriza",
    "Western Brasil", "Frente a la costa del Per'u", "Cerca de la costa del Per'u", "Centro del Per'u",
    "El sur de Per'u", "Per'u-Bolivia regi'on fronteriza", "El norte de Bolivia",
    "Central de Bolivia", "Frente a la costa del norte de Chile",
    "Cerca de la costa del norte de Chile", "el norte de Chile",
    "Chile-Bolivia en la regi'on fronteriza", "El sur de Bolivia", "Paraguay",
    "Chile-Argentina en la regi'on fronteriza", "Provincia de Jujuy, Argentina",
    "Provincia de Salta, Argentina", "Provincia de Catamarca, Argentina",
    "Provincia de Tucum'an, Argentina", "Santiago del Estero, Argentina",
    "Nordeste de Argentina", "Frente a la costa de Chile central",
    "Cerca de la costa de Chile central", "Central de Chile", "Provincia de San Juan, Argentina",
    "La Rioja, Argentina", "Provincia de Mendoza, Argentina",
    "Provincia de San Luis, Argentina", "la provincia de C'ordoba, Argentina", "Uruguay",
    "Frente a la costa del sur de Chile", "El sur de Chile",
    "El sur de Chile y Argentina en la regi'on fronteriza", "El sur de Argentina",
    "Tierra del Fuego", "regi'on de las Islas Malvinas", "Paso de Drake", "Mar de Scotia",
    "Isla Georgia del Sur la regi'on", "Sur subida Georgia",
    "Islas Sandwich del Sur regi'on", "Islas Shetland del Sur",
    "Pen'insula Ant'artica", "al sudoeste del Oc'eano Atl'antico", "Mar de Weddell",
    "Fuera de la costa oeste de la Isla Norte, Nueva Zelanda", "Isla Norte, Nueva Zelanda",
    "Fuera de la costa este de la Isla Norte, Nueva Zelanda",
    "Fuera de la costa oeste de la Isla Sur, Nueva Zelanda", "Isla Sur, Nueva Zelanda",
    "Estrecho de Cook, Nueva Zelanda", "Fuera de la costa este de la Isla Sur, Nueva Zelanda",
    "Al norte de la isla Macquarie", "Islas Auckland, Nueva Zelanda, la regi'on",
    "Isla Macquarie, Australia, la regi'on", "Sur de Nueva Zelanda",
    "Islas Samoa regi'on", "Islas Samoa", "Al sur de las Islas Fiyi",
    "Al oeste de las Islas Tonga (REGIÓN NO EN USO)", "Islas Tonga",
    "Islas Tonga regi'on", "Al sur de las Islas Tonga", "Norte de Nueva Zelanda",
    "Islas Kermadec regi'on", "Islas Kermadec, Nueva Zelanda",
    "Al sur de las Islas Kermadec", "Al norte de las Islas Fiyi", "regi'on de las Islas Fiyi",
    "Islas Fiyi", "Santa Cruz regi'on de las Islas", "Islas Santa Cruz",
    "Vanuatu Islas regi'on", "Islas Vanuatu", "Nueva Caledonia", "Islas de la Lealtad",
    "Al sureste de Islas de la Lealtad", "New Ireland, Papua Nueva Guinea, la regi'on",
    "Al norte de las Islas Salom'on", "Gran Bretaña, Papua Nueva Guinea, la regi'on",
    "Bougainville - regi'on de las Islas Salom'on",
    "D'Entrecasteaux Islas, Papua Nueva Guinea, la regi'on",
    "Al sur de las Islas Salom'on", "regi'on de Irian Jaya, Indonesia,",
    "Cerca de la costa norte de Irian Jaya, Indonesia",
    "Ninigo Islas, Papua Nueva Guinea, la regi'on",
    "Islas del Almirantazgo, Papua Nueva Guinea, la regi'on",
    "Cerca de la costa norte de Nueva Guinea, Papua Nueva Guinea", "Irian Jaya, Indonesia",
    "Nueva Guinea, Papua Nueva Guinea", "Mar de Bismarck",
    "Islas Aru, Indonesia, la regi'on", "Cerca de la costa sur de Irian Jaya, Indonesia",
    "Cerca de la costa sur de Nueva Guinea, Papua Nueva Guinea",
    "Este Nueva Guinea, Papua Nueva Guinea, la regi'on", "mar de Arafura",
    "Western Islas Carolinas, Micronesia", "Al sur de las Islas Marianas",
    "Al sureste de Honshu, Jap'on", "Islas Bonin, Jap'on, la regi'on",
    "Volc'an de las Islas, Jap'on, la regi'on", "Al oeste de las Islas Marianas",
    "Islas Marianas regi'on", "Mariana Islands", "la pen'insula de Kamchatka, Rusia",
    "Cerca de la costa este de la pen'insula de Kamchatka, Rusia",
    "Fuera de la costa este de la pen'insula de Kamchatka, Rusia",
    "Al noroeste de las Islas Kuriles, Rusia", "las islas Kuriles, Rusia",
    "Al este de las Islas Kuriles, Rusia", "Este mar de Jap'on",
    "Hokkaido, Jap'on, la regi'on", "Fuera costa sureste de Hokkaido, Jap'on",
    "Cerca de la costa oeste del este de Honshu, Jap'on", "oriental de Honshu, Jap'on",
    "Cerca de la costa este del este de Honshu, Jap'on", "Fuera de la costa este de Honshu, Jap'on",
    "Cerca de la costa sur del este de Honshu, Jap'on", "Corea del Sur",
    "Occidental de Honshu, Jap'on", "Cerca de la costa sur del oeste de Honshu, Jap'on",
    "Al noroeste de las Islas Ryukyu, Jap'on", "Kyushu, Jap'on", "Shikoku, Jap'on",
    "Al sureste de Shikoku, Jap'on", "Islas Ryukyu, Jap'on",
    "Al sureste de las islas Ryukyu, Jap'on", "Al oeste de las Islas Bonin, Jap'on",
    "Mar de Filipinas", "Cerca de la costa del sureste de China", "la regi'on de Taiw'an", "Taiwan",
    "El nordeste de Taiwan", "Southwestern Islas Ryukyu, Jap'on",
    "Al sureste de Taiwan", "regi'on de las Islas Filipinas",
    "Luzon, Islas Filipinas", "Mindoro, Filipinas Islas",
    "Samar, Islas Filipinas", "Palawan, Filipinas Islas", "Mar de Sulu",
    "Panay, Islas Filipinas", "Cebu, Filipinas, Islas",
    "Leyte, Islas Filipinas", "Negros, las Islas Filipinas",
    "Archipi'elago Sulu, Islas Filipinas", "Mindanao, Filipinas, Islas",
    "Al este de las Islas Filipinas", "Borneo", "Mar de C'elebes",
    "Islas Talaud, Indonesia", "Al norte de Halmahera, Indonesia",
    "Minahassa Pen'insula, Sulawesi, Indonesia", "El norte de las Molucas del Mar",
    "Halmahera, Indonesia", "Sulawesi, Indonesia", "El sur de las Molucas del Mar",
    "Ceram Sea", "Buru, Indonesia", "Seram, Indonesia",
    "Al suroeste de Sumatra, Indonesia", "El sur de Sumatra, Indonesia", "Mar de Java",
    "Estrecho de la Sonda, Indonesia", "Jawa, Indonesia", "Bali Sea", "Flores del Mar",
    "Banda Sea", "Tanimbar Islands, Indonesia, la regi'on", "Al sur de Jawa, Indonesia",
    "Bali, Indonesia, la regi'on", "Al sur de Bali, Indonesia",
    "Sumbawa, Indonesia, la regi'on", "Flores, Indonesia, la regi'on",
    "Sumba, Indonesia, la regi'on", "Savu Mar", "Timor, Indonesia, la regi'on", "Mar de Timor",
    "Al sur de Sumbawa, Indonesia", "Al sur de Sumba, Indonesia",
    "Al sur de Timor, Indonesia", "Myanmar-India regi'on fronteriza",
    "Myanmar-Bangladesh en la regi'on fronteriza", "Myanmar", "Myanmar-China Regi'on fronteriza",
    "Cerca de la costa sur de Myanmar", "Sudeste de Asia (regi'on no en uso)",
    "La isla de Hainan, China", "Mar de China Meridional", "Eastern Cachemira",
    "Cachemira-India en la regi'on fronteriza", "Kashmir-Xizang regi'on fronteriza",
    "Western Xizang-India en la regi'on fronteriza", "Xizang", "Sichuan, China",
    "El norte de la India", "Nepal-India en la regi'on fronteriza", "Nepal", "Sikkim, India",
    "But'an", "Eastern Xizang-India regi'on fronteriza", "El sur de la India",
    "India y Bangladesh en la regi'on fronteriza", "Bangladesh", "Noreste de la India",
    "Yunnan, China", "Bah'ia de Bengala", "Kirguist'an-Xinjiang regi'on fronteriza",
    "El sur de Xinjiang, China", "Gansu, China", "Western Mongolia Interior, China",
    "Cachemira-Xinjiang en la regi'on fronteriza", "Qinghai, China",
    "Suroeste de Siberia, Rusia", "El Lago Baikal, Rusia, la regi'on",
    "Al este del lago Baikal, Rusia", "Kazajst'an oriental",
    "El lago Issyk-Kul, Kirguist'an, la regi'on", "Kazajst'an-Xinjiang regi'on fronteriza",
    "El norte de Xinjiang, China", "Tuva y Mongolia-Buriatia regi'on fronteriza", "Mongolia",
    "Las montañas de los Urales, Rusia, la regi'on", "regi'on de Kazajst'an occidental", "Eastern C'aucaso",
    "Mar Caspio", "el noroeste de Uzbekist'an", "Turkmenist'an",
    "Ir'an y Turkmenist'an en la regi'on fronteriza", "Turkmenist'an-Afganist'an regi'on fronteriza",
    "Turqu'ia e Ir'an en la regi'on fronteriza", "Ir'an-Armenia-Azerbaiy'an regi'on fronteriza",
    "El noroeste de Ir'an", "Ir'an-Irak en la regi'on fronteriza", "el oeste de Ir'an",
    "El norte y el centro de Ir'an", "el noroeste de Afganist'an",
    "El suroeste de Afganist'an", "Eastern Pen'insula Ar'abiga", "Golfo P'ersico",
    "El sur de Ir'an", "el suroeste de Pakist'an", "Golfo de Om'an",
    "Frente a la costa de Pakist'an", "Ucrania - Moldavia - suroeste de Rusia, la regi'on",
    "Ruman'ia", "Bulgaria", "Mar Negro", "Crimea, Ucrania, la regi'on",
    "Western C'aucaso", "Grecia-Bulgaria regi'on fronteriza", "Grecia", "Mar Egeo",
    "Turqu'ia", "Turqu'ia-Georgia-Armenia regi'on fronteriza", "El sur de Grecia",
    "Islas del Dodecaneso, Grecia", "Creta, Grecia", "Mediterr'aneo oriental",
    "Chipre regi'on", "regi'on del Mar Muerto", "Jordania - Siria regi'on", "Irak", "Portugal",
    "España", "Pirineos", "Cerca de la costa sur de Francia", "C'orcega, Francia",
    "El centro de Italia", "Mar Adri'atico", "Noroeste Pen'insula Balc'anica",
    "Al oeste de Gibraltar", "Estrecho de Gibraltar", "Islas Baleares, España",
    "Mediterr'aneo occidental", "Cerdeña, Italia", "Mar Tirreno",
    "El sur de Italia", "Albania", "Grecia-Albania regi'on fronteriza",
    "Madeira, Portugal, la regi'on", "Islas Canarias, España, la regi'on",
    "Marruecos", "El norte de Argelia", "T'unez", "Sicilia, Italia", "Mar J'onico",
    "Central Mar Mediterr'aneo", "Cerca de la costa de Libia", "Atl'antico Norte",
    "El norte de Cordillera del Atl'antico", "Islas Azores regi'on",
    "Islas Azores, Portugal", "Central Cordillera del Atl'antico",
    "Al norte de la isla de Ascensi'on", "regi'on de la isla Ascensi'on", "Atl'antico Sur",
    "Southern Cordillera del Atl'antico", "Tristan da Cunha regi'on",
    "Isla Bouvet regi'on", "Al suroeste de África", "del sudeste del Oc'eano Atl'antico",
    "Este del Golfo de Ad'en", "regi'on de Socotra", "Mar de Arabia",
    "Lakshadweep, India, la regi'on", "el noreste de Somalia", "al norte del Oc'eano Índico",
    "Carlsberg Ridge", "regi'on de las islas Maldivas", "Mar Laquedivas", "Sri Lanka",
    "Sur del Oc'eano Índico", "regi'on archipi'elago de Chagos",
    "Mauricio - regi'on de Reunion", "Southwest Indian Ridge", "Mid-Indian Ridge",
    "Al sur de África", "Isla del Pr'incipe Eduardo, South Africa, la regi'on",
    "Islas Crozet regi'on", "regi'on de las islas Kerguelen", "Ridge rotos",
    "Sudeste Indian Ridge", "El sur de la meseta Kerguelen", "Al sur de Australia",
    "Saskatchewan, Canad'a", "Manitoba, Canad'a", "Hudson Bay", "Ontario, Canad'a",
    "Estrecho de Hudson, Canad'a, la regi'on", "El norte de Quebec, Canad'a", "Estrecho de Davis",
    "Labrador, Canad'a", "Mar de Labrador", "El sur de Quebec, Canad'a",
    "Gaspe Pen'insula, Canad'a", "Eastern Quebec, Canad'a",
    "Anticosti Island, Canad'a", "New Brunswick, Canad'a", "Nova Scotia, Canad'a",
    "Isla del Pr'incipe Eduardo, Canad'a", "Golfo de San Lorenzo, Canad'a",
    "Terranova, Canad'a", "Montana, Estados Unidos",
    "Eastern Idaho, Estados Unidos", "Hebgen Lake, Montana, Estados Unidos, la regi'on",
    "Yellowstone, Estados Unidos, la regi'on", "Wyoming, Estados Unidos",
    "Dakota del Norte, Estados Unidos", "Dakota del Sur, Estados Unidos",
    "Nebraska, Estados Unidos", "Minnesota, Estados Unidos", "Iowa, Estados Unidos",
    "Wisconsin, Estados Unidos", "Illinois, Estados Unidos",
    "Michigan, Estados Unidos", "Indiana, Estados Unidos",
    "El sur de Ontario, Canad'a", "New York, Estados Unidos", "New York, Estados Unidos",
    "Pennsylvania, Estados Unidos",
    "Vermont - New Hampshire, Estados Unidos, la regi'on", "estado de Maine, Estados Unidos",
    "El sur de Nueva Inglaterra, Estados Unidos", "Golfo de Maine, Estados Unidos",
    "Utah, Estados Unidos", "Colorado, Estados Unidos", "Kansas, Estados Unidos",
    "Iowa, Missouri en la regi'on fronteriza", "Missouri-Kansas regi'on fronteriza",
    "Missouri, Estados Unidos", "Missouri y Arkansas en la regi'on fronteriza",
    "Missouri-Illinois de la regi'on fronteriza",
    "New Madrid, Missouri, Estados Unidos, la regi'on",
    "Cape Girardeau, Missouri, Estados Unidos, la regi'on",
    "El sur de Illinois, Estados Unidos", "El sur de Indiana, Estados Unidos",
    "De Kentucky, Estados Unidos", "Virginia Occidental, Estados Unidos",
    "Virginia, Estados Unidos", "Bah'ia de Chesapeake, Estados Unidos, la regi'on",
    "Nueva Jersey, Estados Unidos", "Eastern Arizona, Estados Unidos",
    "Nuevo M'exico, Estados Unidos", "el noroeste de Texas y Oklahoma regi'on fronteriza",
    "Oeste de Texas, Estados Unidos", "Oklahoma, Estados Unidos",
    "El centro de Texas, Estados Unidos", "Texas-Oklahoma regi'on fronteriza",
    "Arkansas, Estados Unidos", "Louisiana-Texas regi'on fronteriza",
    "Louisiana, Estados Unidos", "Mississippi, Estados Unidos",
    "Tennessee, Estados Unidos", "Alabama, Estados Unidos",
    "Western Florida, Estados Unidos", "Georgia, Estados Unidos",
    "Florida y Georgia en la regi'on fronteriza", "Carolina del Sur, Estados Unidos",
    "Carolina del Norte, Estados Unidos", "Fuera de la costa este de Estados Unidos",
    "Pen'insula de la Florida, Estados Unidos", "Antillas Neerlandesas",
    "Eastern Arizona-Sonora en la regi'on fronteriza", "Nuevo M'exico-Chihuahua regi'on fronteriza",
    "Texas-M'exico en la regi'on fronteriza", "El sur de Texas, Estados Unidos",
    "Cerca de la costa de Texas, Estados Unidos", "Chihuahua, M'exico", "el norte de M'exico",
    "El centro de M'exico", "Jalisco, M'exico", "Veracruz, M'exico", "Golfo de M'exico",
    "Bah'ia de Campeche", "Brazil", "Guyana", "Surinam", "French Guiana", "Eire",
    "Reino Unido", "Mar del Norte", "El sur de Noruega", "Suecia", "Mar B'altico",
    "Francia", "Golfo de Vizcaya", "Pa'ises Bajos", "B'elgica", "Dinamarca", "Alemania",
    "Suiza", "el norte de Italia", "Austria", "Rep'ublica Checa y Eslovaquia",
    "Polonia", "Hungr'ia", "el noroeste de África (regi'on no en uso)", "El sur de Argelia",
    "Libia", "Egipto", "Mar Rojo", "Western Pen'insula Ar'abiga", "regi'on de Chad", "Sud'an",
    "Etiop'ia", "Oeste del Golfo de Ad'en", "el noroeste de Somalia",
    "Sur de la costa del noroeste de África", "Camer'un", "Guinea Ecuatorial",
    "Rep'ublica Centroafricana", "Gab'on", "Congo", "Zaire", "Uganda",
    "Regi'on del Lago Victoria", "Kenia", "El sur de Somalia", "la regi'on del Lago Tanganika",
    "Tanzania", "el noroeste de Madagascar", "Angola", "Zambia", "Malawi", "Namibia",
    "Botsuana", "Zimbabwe", "Mozambique", "Canal de Mozambique", "Madagascar",
    "Sud'africa", "Lesotho", "Suazilandia", "Frente a la costa de África del Sur",
    "Al noroeste de Australia", "Al oeste de Australia", "Australia Occidental",
    "Territorio del Norte, Australia", "Australia del Sur",
    "Golfo de Carpentaria, Australia", "Queensland, Australia", "Coral",
    "Al noroeste de Nueva Caledonia", "regi'on de Nueva Caledonia", "Al suroeste de Australia",
    "Fuera de la costa sur de Australia", "Cerca de la costa de Australia del Sur",
    "New South Wales, Australia", "Victoria, Australia",
    "Cerca de la costa sureste de Australia", "Cerca de la costa este de Australia",
    "Al este de Australia", "Isla Norfolk, Australia, la regi'on",
    "Al noroeste de Nueva Zelanda", "el Estrecho de Bass, Australia",
    "Tasmania, Australia, la regi'on", "el sudeste de Australia", "Oc'eano Pac'ifico del Norte",
    "Islas de Hawai regi'on", "Islas de Hawai, Estados Unidos",
    "Este Islas Carolinas, Micronesia, la regi'on", "regi'on de las Islas Marshall",
    "Enewetak Atoll, Islas Marshall, de la regi'on",
    "Bikini Atoll, Islas Marshall, de la regi'on", "Gilbert Islands, Kiribati, la regi'on",
    "La isla de Johnston regi'on", "Islas de la L'inea, Kiribati, la regi'on",
    "Palmyra Isla, Kiribati, la regi'on", "Kiritimati, Kiribati, la regi'on",
    "Tuvalu regi'on", "Islas Phoenix, de Kiribati, en la regi'on", "regi'on de las Islas Tokelau",
    "El norte de las Islas Cook", "Cook regi'on de las Islas", "Sociedad de la regi'on de las islas",
    "Islas Tubuai regi'on", "regi'on de las Islas Marquesas",
    "Archipi'elago Tuamotu regi'on", "Pac'ifico Sur", "Lomonosov Ridge",
    "Oc'eano Ártico", "Cerca de la costa norte de Kalaallit Nunaat",
    "Este Kalaallit Nunaat", "Islandia regi'on", "Islandia",
    "Isla de Jan Mayen regi'on", "Mar de Groenlandia", "Al norte de Svalbard",
    "Mar de Noruega", "Svalbard, Noruega, la regi'on", "al norte de la Tierra de Francisco Jos'e",
    "Tierra de Francisco Jos'e, Rusia", "el norte de Noruega", "Mar de Barents",
    "Novaya Zemlya, Rusia", "Mar de Kara",
    "Cerca de la costa del noroeste de Siberia, Rusia", "Al norte de Severnaya Zemlya",
    "Severnaya Zemlya, Rusia", "Cerca de la costa del norte de Siberia, Rusia",
    "Este de Severnaya Zemlya", "Mar de Laptev", "del sudeste de Siberia, Rusia",
    "Priamurye-noreste de China Regi'on fronteriza", "el noreste de China",
    "Corea del Norte", "Mar del Jap'on", "Primorye, Rusia", "la isla de Sakhalin, Rusia",
    "Mar de Okhotsk", "Sudeste de China", "Mar Amarillo",
    "Fuera de la costa este del sureste de China", "al norte de las Islas de Nueva Siberia",
    "Islas de Nueva Siberia, Rusia", "Mar de Siberia Oriental",
    "Cerca de la costa norte del este de Siberia, Rusia", "Siberia Oriental, Rusia",
    "Chukchi Sea", "Estrecho de Bering", "la isla San Lorenzo, Estados Unidos, la regi'on",
    "Mar de Beaufort", "el norte de Alaska, Estados Unidos",
    "El norte de Territorio del Yuk'on, Canad'a", "Queen Elizabeth Islands, Canad'a",
    "Territorios del Noroeste, Canad'a", "Western Kalaallit Nunaat", "la bah'ia de Baffin",
    "La isla de Baffin, Canad'a, la regi'on", "Southeastcentral Oc'eano Pac'ifico",
    "El sur del Pac'ifico Oriental Rise", "regi'on de la isla de Pascua", "West Dorsal de Chile",
    "Archipi'elago Juan Fern'andez, Chile, la regi'on", "Oriente de la Isla Norte, Nueva Zelanda",
    "Islas Chatham, Nueva Zelanda, la regi'on", "Al sur de las Islas Chatham",
    "Pac'ifico-Ant'artico Ridge", "El sur del oc'eano Pac'ifico",
    "Eastcentral Oc'eano Pac'ifico", "Central y del Este auge del Pac'ifico",
    "Al oeste de las Islas Gal'apagos", "regi'on de las Islas Gal'apagos",
    "Islas Gal'apagos, Ecuador", "Al suroeste de las Islas Gal'apagos",
    "Al sureste de las Islas Gal'apagos", "Al sur de Tasmania",
    "Al oeste de la isla Macquarie", "regi'on de las Islas Balleny",
    "Islas Andam'an, India, la regi'on", "Islas Nicobar, India, la regi'on",
    "Fuera de la costa oeste del norte de Sumatra, Indonesia",
    "El norte de Sumatra, Indonesia", "Pen'insula Malaya", "Golfo de Tailandia",
    "El sudeste de Afganist'an", "Pakist'an", "al sudoeste de Cachemira",
    "India y Pakist'an en la regi'on fronteriza", "Central de Kazajst'an",
    "Sudeste de Uzbekist'an", "Tayikist'an", "Kirguist'an",
    "Afganist'an y Tayikist'an en la regi'on fronteriza", "Hindu Kush, en Afganist'an, la regi'on",
    "Tayikist'an-Xinjiang en la regi'on fronteriza", "Noroeste de Cachemira", "Finlandia",
    "Noruega-Murmansk en la regi'on fronteriza", "Finlandia, Karelia regi'on fronteriza",
    "Estados b'alticos - Bielorrusia - Regi'on del Noroeste de Rusia",
    "Del noroeste de Siberia, Rusia", "Norte y Siberia central, Rusia",
    "Tierra de Victoria, en la Ant'artida", "Mar de Ross", "Ant'artida",
    "El norte del Pac'ifico Oriental Rise", "Al norte de Honduras",
    "Al este de las Islas Sandwich del Sur", "Tailandia", "Laos", "Kampuchea", "Vietnam",
    "Golfo de Tongking", "Reykjanes Ridge", "Azores-Cabo de San Vicente Ridge",
    "Fractura de Owen Zona regi'on", "Triple Junction Oc'eano Índico",
    "Indico Occidental de la Ant'artida Ridge", "S'ahara Occidental", "Mauritania", "Mali",
    "Senegal - Gambia regi'on", "regi'on de Guinea", "Sierra Leona", "regi'on de Liberia",
    "Cote d'Ivoire", "Burkina Faso", "Ghana", "Benin - regi'on de Togo", "N'iger",
    "Nigeria", "Sudeste de la Isla de Pascua", "Gal'apagos regi'on Triple Junction",
    ]
def FlEngLookup(lat, lng):
    return original_FlEngLookup(lat,lng,greg_esp,sreg_esp)