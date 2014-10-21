'use strict';
var surveyApp = angular.module('surveyApp',['ngRoute', 'ngTable']);

surveyApp.factory('surveyFactory',['$http',function($http){
	/*var factory = {};*/
	return {

		get : function() {
			return $http.get('');
		},
		
		create : function(val) {
			return $http.post('',val);
		},

		delete : function(id) {
			return $http.delete('' + id);
		},
			user : 
				{
					fName: 'Mike',
					lName: 'Olson',
					eMail: 'mike@olson.com',
					Phone: '123654789',
					HouseNumber: 'A-1/72',
					Street: 'West Lane',
					City:'London',
					State:'London',
					Country: 'England',
					accountType: 'Admin'
				},

			surveys : [
				{
					ID: "1",
					"Type": "Fringilla Incorporated",
					"Sections": [
						{
							"name": "Section A", "Question" : [
								{
									"ID": "1",
									"Content": "What is your name?"
								},
								{
									"ID": "2",
									"Content": "What is your other name?"
								},
								{
									"ID": "3",
									"Content": "Any other question?"
								}
							]
						}
					]
				},
				{
					ID: "2",
					Type: "Leo Morbi Associates",
					Section: [
						{
							name: "Section A", Question : [
								{
									ID: "1",
									Content: "What is your name?"
								}
							]
						},
						{
							name: "Section A",
							
						}
					]
				},
				{
					ID: "3",
					Type: "Id Libero Donec Associates",
					"Section": [
						{
							"name": "Section A", "Question" : [
								{
									"ID": "1",
									"Content": "What is your name?"
								}
							]
						},
						{
							"name": "Section A",
							
						}
					]
				}
		],

			researchers : [
				{
					'Name': 'Scientist'
				},
				{
					'Name': 'Teacher'
				},
				{
					'Name': 'Foundation',
				},
				{
					'Name': 'Labs'
				}
		],
			managers : [
				{	
					'ID' : '1',
					'Name': 'Allen',
					'Project' : 'Education'
				},
				{	
					'ID' : '2',
					'Name': 'Rajan',
					'Project' : 'Poverty'
				},
				{	
					'ID' : '3',
					'Name': 'Wendy',
					'Project' : 'Africa'
				},
				{	
					'ID' : '4',
					'Name': 'Stephen',
					'Project' : 'UNO'
				}	
		],
			projects : [
				{	
					'ID' : '12',
					'Name': 'Nigeria'
				},
				{	
					'ID' : '43',
					'Name': 'Egypt'
				},
				{	
					'ID' : '48',
					'Name': 'Nigeria 2'
				},
				{	
					'ID' : '4',
					'Name': 'Africa'
				}	
		],
		data2 : [
	{
		"ID": 1,
		"ScheduleName": "Bangladesh",
		"Date": "ThuThu/MayMay/2014201420142014",
		"Time": 1601,
		"ProjectID": "X3K 7R9",
		"Batch": "78F060E7-4CC5-98AB-9417-4A00F162698B",
		"Language": "LU",
		"Status": "Not-Started"
	},
	{
		"ID": 2,
		"ScheduleName": "Namibia",
		"Date": "WedWed/NovNov/2014201420142014",
		"Time": 1941,
		"ProjectID": "T8W 2Z5",
		"Batch": "17420BCC-114B-3E6A-E55F-7EDF36470DD5",
		"Language": "SL",
		"Status": "Not-Started"
	},
	{
		"ID": 3,
		"ScheduleName": "Russian Federation",
		"Date": "WedWed/AprApr/2016201620162016",
		"Time": 1960,
		"ProjectID": "L5U 5F2",
		"Batch": "CE9FDE92-38EE-DABF-18F9-31088FCCAD35",
		"Language": "Ontario",
		"Status": "Started"
	},
	{
		"ID": 4,
		"ScheduleName": "Switzerland",
		"Date": "FriFri/AprApr/2015201520152015",
		"Time": 871,
		"ProjectID": "V6D 2V4",
		"Batch": "25624B26-2074-4B34-834C-ECC0CF8BF11A",
		"Language": "NS",
		"Status": "Not-Started"
	},
	{
		"ID": 5,
		"ScheduleName": "Congo, the Democratic Republic of the",
		"Date": "SatSat/OctOct/2014201420142014",
		"Time": 1969,
		"ProjectID": "T7B 4C3",
		"Batch": "5E54F231-254B-AEC4-743F-0502D03293D5",
		"Language": "Maharastra",
		"Status": "Not-Started"
	},
	{
		"ID": 6,
		"ScheduleName": "Burundi",
		"Date": "FriFri/NovNov/2014201420142014",
		"Time": 575,
		"ProjectID": "J6M 3N9",
		"Batch": "2E6C008E-1739-BCB7-0E30-F60098D7960C",
		"Language": "Opolskie",
		"Status": "Started"
	},
	{
		"ID": 7,
		"ScheduleName": "Belgium",
		"Date": "MonMon/JunJun/2016201620162016",
		"Time": 1476,
		"ProjectID": "S2G 7L5",
		"Batch": "6D09D231-735D-C03D-5410-0FB755594C6B",
		"Language": "Bahia",
		"Status": "Not-Started"
	},
	{
		"ID": 8,
		"ScheduleName": "Cuba",
		"Date": "FriFri/DecDec/2013201320132013",
		"Time": 2245,
		"ProjectID": "H4W 6Y9",
		"Batch": "E0544489-3B8D-C35B-D52D-323766EBD86C",
		"Language": "VI",
		"Status": "Started"
	},
	{
		"ID": 9,
		"ScheduleName": "Uganda",
		"Date": "SunSun/NovNov/2013201320132013",
		"Time": 1877,
		"ProjectID": "S3E 0U3",
		"Batch": "8187D81C-AFC5-06F5-5941-7DF545AC6C9F",
		"Language": "Uttar Pradesh",
		"Status": "Started"
	},
	{
		"ID": 10,
		"ScheduleName": "Sint Maarten",
		"Date": "ThuThu/MayMay/2015201520152015",
		"Time": 1864,
		"ProjectID": "F0I 1M7",
		"Batch": "C0A8EB13-A3C5-5A62-D5F5-ACB62F69790B",
		"Language": "West Bengal",
		"Status": "Not-Started"
	},
	{
		"ID": 11,
		"ScheduleName": "Sweden",
		"Date": "MonMon/OctOct/2015201520152015",
		"Time": 1862,
		"ProjectID": "B7E 0T6",
		"Batch": "CF56178F-3155-D874-67F6-29D41B4ED741",
		"Language": "BE",
		"Status": "Not-Started"
	},
	{
		"ID": 12,
		"ScheduleName": "Bahrain",
		"Date": "ThuThu/MayMay/2014201420142014",
		"Time": 1617,
		"ProjectID": "V0Y 8H8",
		"Batch": "16C7D84A-327E-0130-F690-AAB6747883C7",
		"Language": "Burgenland",
		"Status": "Started"
	},
	{
		"ID": 13,
		"ScheduleName": "Guyana",
		"Date": "MonMon/SepSep/2016201620162016",
		"Time": 203,
		"ProjectID": "T7H 0C7",
		"Batch": "B75B4D0E-3AC7-01D8-A4A0-297C61CF1365",
		"Language": "Limburg",
		"Status": "Started"
	},
	{
		"ID": 14,
		"ScheduleName": "French Guiana",
		"Date": "SatSat/JunJun/2016201620162016",
		"Time": 736,
		"ProjectID": "L5W 5H0",
		"Batch": "A47304DE-82DF-5E8C-271D-307807BB0C90",
		"Language": "Ontario",
		"Status": "Not-Started"
	},
	{
		"ID": 15,
		"ScheduleName": "French Southern Territories",
		"Date": "SatSat/MayMay/2015201520152015",
		"Time": 1540,
		"ProjectID": "F5G 4M5",
		"Batch": "F50CA71A-8238-17F9-DC81-594E845414B5",
		"Language": "Luik",
		"Status": "Not-Started"
	},
	{
		"ID": 16,
		"ScheduleName": "Marshall Islands",
		"Date": "SatSat/MarMar/2014201420142014",
		"Time": 2339,
		"ProjectID": "Y9V 3I8",
		"Batch": "D3472AD0-E7A1-22B1-4375-068FC8A4DB0C",
		"Language": "Oost-Vlaanderen",
		"Status": "Started"
	},
	{
		"ID": 17,
		"ScheduleName": "Czech Republic",
		"Date": "MonMon/DecDec/2013201320132013",
		"Time": 2340,
		"ProjectID": "M8C 1Z3",
		"Batch": "8AB374D2-5EEF-B486-89B4-933D82927DD7",
		"Language": "Vienna",
		"Status": "Started"
	},
	{
		"ID": 18,
		"ScheduleName": "Estonia",
		"Date": "ThuThu/NovNov/2013201320132013",
		"Time": 967,
		"ProjectID": "Z7T 4N6",
		"Batch": "B7540CD2-2DC5-50E3-0BCA-E0CFCBC406CD",
		"Language": "KD",
		"Status": "Started"
	},
	{
		"ID": 19,
		"ScheduleName": "Tonga",
		"Date": "ThuThu/AprApr/2016201620162016",
		"Time": 1266,
		"ProjectID": "A6J 9X1",
		"Batch": "4461D306-A2AC-64AD-0D9F-6C39E1F6293E",
		"Language": "CA",
		"Status": "Not-Started"
	},
	{
		"ID": 20,
		"ScheduleName": "Mali",
		"Date": "SunSun/JunJun/2016201620162016",
		"Time": 2303,
		"ProjectID": "F2F 0G2",
		"Batch": "54E68A9D-3E26-4418-5E2C-A55BCE4F3F79",
		"Language": "Wielkopolskie",
		"Status": "Not-Started"
	},
	{
		"ID": 21,
		"ScheduleName": "Vanuatu",
		"Date": "TueTue/MarMar/2014201420142014",
		"Time": 1452,
		"ProjectID": "K0M 9O1",
		"Batch": "01E087D4-1195-4AAD-C744-999E9D2A498D",
		"Language": "Limburg",
		"Status": "Not-Started"
	},
	{
		"ID": 22,
		"ScheduleName": "Syria",
		"Date": "MonMon/SepSep/2016201620162016",
		"Time": 1944,
		"ProjectID": "N2L 9D6",
		"Batch": "40F6E34F-A7EE-9B57-34A5-B85105268BA5",
		"Language": "HB",
		"Status": "Not-Started"
	},
	{
		"ID": 23,
		"ScheduleName": "Dominica",
		"Date": "TueTue/MarMar/2016201620162016",
		"Time": 1958,
		"ProjectID": "J3V 5R6",
		"Batch": "CA872545-FC2E-F1E3-2186-D7522DCF11FC",
		"Language": "Karnataka",
		"Status": "Started"
	},
	{
		"ID": 24,
		"ScheduleName": "Lithuania",
		"Date": "FriFri/NovNov/2013201320132013",
		"Time": 1070,
		"ProjectID": "O8A 3U2",
		"Batch": "F0A661B7-54F8-04F9-7ED6-30C71727D03B",
		"Language": "A",
		"Status": "Started"
	},
	{
		"ID": 25,
		"ScheduleName": "Germany",
		"Date": "ThuThu/AugAug/2015201520152015",
		"Time": 1148,
		"ProjectID": "C0M 5X4",
		"Batch": "93904522-A3E1-A82A-7FE0-CE791CF1865C",
		"Language": "LA",
		"Status": "Not-Started"
	},
	{
		"ID": 26,
		"ScheduleName": "Armenia",
		"Date": "MonMon/DecDec/2015201520152015",
		"Time": 1639,
		"ProjectID": "H8N 8C9",
		"Batch": "41A712A0-8A0E-4883-8A24-0DAD9C56AEF8",
		"Language": "CA",
		"Status": "Not-Started"
	},
	{
		"ID": 27,
		"ScheduleName": "Sudan",
		"Date": "SunSun/AugAug/2014201420142014",
		"Time": 2182,
		"ProjectID": "P1Q 6I7",
		"Batch": "1C2E9D59-A6E8-D178-AF62-D2DD10690AA4",
		"Language": "West Lothian",
		"Status": "Not-Started"
	},
	{
		"ID": 28,
		"ScheduleName": "Aruba",
		"Date": "MonMon/AugAug/2015201520152015",
		"Time": 1766,
		"ProjectID": "O6G 4Y8",
		"Batch": "6D084255-BDA7-9A13-D58E-E0B3BE4F2410",
		"Language": "Quebec",
		"Status": "Started"
	},
	{
		"ID": 29,
		"ScheduleName": "Ukraine",
		"Date": "SatSat/AprApr/2014201420142014",
		"Time": 1435,
		"ProjectID": "A6P 2T2",
		"Batch": "A59A892F-B3B0-1D3E-25F9-9B081A7CD54C",
		"Language": "OV",
		"Status": "Not-Started"
	},
	{
		"ID": 30,
		"ScheduleName": "United Arab Emirates",
		"Date": "SunSun/MarMar/2015201520152015",
		"Time": 1133,
		"ProjectID": "I5C 0T8",
		"Batch": "9C035C16-2985-9E0D-FEA0-25E5F52E3012",
		"Language": "JK",
		"Status": "Started"
	},
	{
		"ID": 31,
		"ScheduleName": "Belarus",
		"Date": "SunSun/JulJul/2016201620162016",
		"Time": 1955,
		"ProjectID": "I0M 9O2",
		"Batch": "1103F8FC-0069-60D4-E0EB-90AE37542D30",
		"Language": "Nord-Pas-de-Calais",
		"Status": "Started"
	},
	{
		"ID": 32,
		"ScheduleName": "Guam",
		"Date": "WedWed/NovNov/2015201520152015",
		"Time": 95,
		"ProjectID": "M6N 1F0",
		"Batch": "9267BC3C-3FF3-7682-4E68-60987BF426A1",
		"Language": "NW",
		"Status": "Started"
	},
	{
		"ID": 33,
		"ScheduleName": "Congo (Brazzaville)",
		"Date": "WedWed/DecDec/2014201420142014",
		"Time": 250,
		"ProjectID": "Z8V 6Q5",
		"Batch": "E61BE20A-76EA-BB77-F098-7ED050898780",
		"Language": "Vienna",
		"Status": "Started"
	},
	{
		"ID": 34,
		"ScheduleName": "Sri Lanka",
		"Date": "MonMon/AugAug/2014201420142014",
		"Time": 2077,
		"ProjectID": "C2X 3Z7",
		"Batch": "9B46B551-D2ED-F8AB-8474-E8FF50901D2F",
		"Language": "Leicestershire",
		"Status": "Started"
	},
	{
		"ID": 35,
		"ScheduleName": "New Caledonia",
		"Date": "ThuThu/FebFeb/2015201520152015",
		"Time": 1479,
		"ProjectID": "C8B 0R7",
		"Batch": "AE0A6B76-7EA0-84E3-E55A-ED5FBC34757D",
		"Language": "LA",
		"Status": "Started"
	},
	{
		"ID": 36,
		"ScheduleName": "Antigua and Barbuda",
		"Date": "FriFri/JunJun/2016201620162016",
		"Time": 1699,
		"ProjectID": "T9V 9E1",
		"Batch": "CED97887-43C7-B0C2-B95C-9F9F8614524D",
		"Language": "Ontario",
		"Status": "Not-Started"
	},
	{
		"ID": 37,
		"ScheduleName": "Dominica",
		"Date": "WedWed/JanJan/2014201420142014",
		"Time": 246,
		"ProjectID": "Z4Y 8F2",
		"Batch": "10BF7D6D-3B55-F7C2-984A-71ADA4B7866A",
		"Language": "SN",
		"Status": "Not-Started"
	},
	{
		"ID": 38,
		"ScheduleName": "Indonesia",
		"Date": "SunSun/DecDec/2014201420142014",
		"Time": 1957,
		"ProjectID": "V5C 4K5",
		"Batch": "21BC52E3-58BC-5A55-5EAB-5A15F6546B2E",
		"Language": "WP",
		"Status": "Started"
	},
	{
		"ID": 39,
		"ScheduleName": "Jersey",
		"Date": "ThuThu/OctOct/2015201520152015",
		"Time": 2131,
		"ProjectID": "A2E 8F8",
		"Batch": "B9949CA7-DC5D-EE6F-6FA0-77A143FADA4E",
		"Language": "Euskadi",
		"Status": "Not-Started"
	},
	{
		"ID": 40,
		"ScheduleName": "Croatia",
		"Date": "SunSun/MarMar/2015201520152015",
		"Time": 1419,
		"ProjectID": "H3M 5I3",
		"Batch": "6FE1B4C5-EB32-1827-D2BD-4953645FB3DB",
		"Language": "Rio de Janeiro",
		"Status": "Started"
	},
	{
		"ID": 41,
		"ScheduleName": "Burkina Faso",
		"Date": "TueTue/AprApr/2016201620162016",
		"Time": 1395,
		"ProjectID": "R5A 7J2",
		"Batch": "30BE95F7-1A09-2A6B-0A1A-D5CEA470CEFB",
		"Language": "SJ",
		"Status": "Started"
	},
	{
		"ID": 42,
		"ScheduleName": "Isle of Man",
		"Date": "ThuThu/JunJun/2016201620162016",
		"Time": 848,
		"ProjectID": "Z4H 4F4",
		"Batch": "67DC6CD6-7447-F401-D438-C6D96F846BBD",
		"Language": "South Island",
		"Status": "Started"
	},
	{
		"ID": 43,
		"ScheduleName": "Benin",
		"Date": "ThuThu/AugAug/2016201620162016",
		"Time": 689,
		"ProjectID": "V1G 5R5",
		"Batch": "74E60245-9179-4ADD-910D-D31EFDAE5239",
		"Language": "PI",
		"Status": "Started"
	},
	{
		"ID": 44,
		"ScheduleName": "Peru",
		"Date": "TueTue/DecDec/2015201520152015",
		"Time": 942,
		"ProjectID": "Q8K 6J2",
		"Batch": "F516084D-87BB-653D-7BBB-2BEC71DF0A68",
		"Language": "Georgia",
		"Status": "Not-Started"
	},
	{
		"ID": 45,
		"ScheduleName": "Algeria",
		"Date": "TueTue/JunJun/2014201420142014",
		"Time": 1996,
		"ProjectID": "S7M 6H5",
		"Batch": "EDBA749C-73A3-72BB-B989-BC327ADCB32E",
		"Language": "MN",
		"Status": "Not-Started"
	},
	{
		"ID": 46,
		"ScheduleName": "Denmark",
		"Date": "FriFri/MarMar/2015201520152015",
		"Time": 181,
		"ProjectID": "G6X 1U8",
		"Batch": "45B2639C-89AB-16A0-B889-615245485D60",
		"Language": "Andalucía",
		"Status": "Not-Started"
	},
	{
		"ID": 47,
		"ScheduleName": "Malawi",
		"Date": "SatSat/FebFeb/2015201520152015",
		"Time": 677,
		"ProjectID": "G7S 5G9",
		"Batch": "39845678-939E-9ECE-D417-4F1AC4D1CCA0",
		"Language": "JI",
		"Status": "Started"
	},
	{
		"ID": 48,
		"ScheduleName": "Indonesia",
		"Date": "ThuThu/MarMar/2015201520152015",
		"Time": 1714,
		"ProjectID": "Z6U 5O4",
		"Batch": "C845AD55-62D1-0AC0-F5E9-F2F73277F089",
		"Language": "Wi",
		"Status": "Not-Started"
	},
	{
		"ID": 49,
		"ScheduleName": "Egypt",
		"Date": "TueTue/JulJul/2014201420142014",
		"Time": 1687,
		"ProjectID": "P5X 0B7",
		"Batch": "C7AF952B-A3AB-B039-D640-B23B9490C89C",
		"Language": "Alabama",
		"Status": "Started"
	},
	{
		"ID": 50,
		"ScheduleName": "Haiti",
		"Date": "ThuThu/DecDec/2015201520152015",
		"Time": 1882,
		"ProjectID": "Y1J 8E1",
		"Batch": "4BE60025-78F9-591D-19A4-14875933E724",
		"Language": "Madrid",
		"Status": "Started"
	},
	{
		"ID": 51,
		"ScheduleName": "Georgia",
		"Date": "SatSat/MarMar/2016201620162016",
		"Time": 946,
		"ProjectID": "D0W 8Y7",
		"Batch": "90095C24-6C1D-4964-6AD2-F16C978D0BCA",
		"Language": "Vienna",
		"Status": "Not-Started"
	},
	{
		"ID": 52,
		"ScheduleName": "El Salvador",
		"Date": "ThuThu/DecDec/2015201520152015",
		"Time": 1664,
		"ProjectID": "O3G 5N5",
		"Batch": "A6E726AE-F08F-7D59-F793-609FE4761BB5",
		"Language": "West-Vlaanderen",
		"Status": "Not-Started"
	},
	{
		"ID": 53,
		"ScheduleName": "Saudi Arabia",
		"Date": "TueTue/MayMay/2016201620162016",
		"Time": 2322,
		"ProjectID": "P7M 7I8",
		"Batch": "E82E2F89-3937-8BF4-8283-593484B807AD",
		"Language": "Picardie",
		"Status": "Started"
	},
	{
		"ID": 54,
		"ScheduleName": "Samoa",
		"Date": "FriFri/DecDec/2015201520152015",
		"Time": 2186,
		"ProjectID": "Y4K 4X7",
		"Batch": "403C139E-C62A-2412-FC9A-CF418198069B",
		"Language": "OV",
		"Status": "Started"
	},
	{
		"ID": 55,
		"ScheduleName": "Gambia",
		"Date": "TueTue/JulJul/2014201420142014",
		"Time": 457,
		"ProjectID": "E9Y 5D1",
		"Batch": "EC91228B-6E73-3694-B3F2-083706D0C087",
		"Language": "LA",
		"Status": "Not-Started"
	},
	{
		"ID": 56,
		"ScheduleName": "Virgin Islands, United States",
		"Date": "MonMon/MarMar/2016201620162016",
		"Time": 1505,
		"ProjectID": "P5E 6H7",
		"Batch": "2659C7CF-5283-F796-E86F-4C9AFFF3DCC5",
		"Language": "MP",
		"Status": "Started"
	},
	{
		"ID": 57,
		"ScheduleName": "Congo, the Democratic Republic of the",
		"Date": "FriFri/JunJun/2014201420142014",
		"Time": 1823,
		"ProjectID": "Z7X 4H6",
		"Batch": "59B3C61C-763B-9AEC-6AC2-ACEBF8AFDC84",
		"Language": "Zeeland",
		"Status": "Not-Started"
	},
	{
		"ID": 58,
		"ScheduleName": "Croatia",
		"Date": "SatSat/AprApr/2015201520152015",
		"Time": 1262,
		"ProjectID": "J0J 0Q2",
		"Batch": "4F7C8B03-40F7-68BC-0CF9-EC9A71D49F4C",
		"Language": "Lombardia",
		"Status": "Not-Started"
	},
	{
		"ID": 59,
		"ScheduleName": "Kenya",
		"Date": "TueTue/NovNov/2015201520152015",
		"Time": 1791,
		"ProjectID": "N0Z 9X5",
		"Batch": "9D800108-507F-6ED2-6838-312145EAFD19",
		"Language": "Vienna",
		"Status": "Not-Started"
	},
	{
		"ID": 60,
		"ScheduleName": "United Kingdom (Great Britain)",
		"Date": "MonMon/JulJul/2015201520152015",
		"Time": 809,
		"ProjectID": "M9E 8O3",
		"Batch": "3161EC91-86F0-B430-8255-4B8E5C3D1F3D",
		"Language": "WV",
		"Status": "Started"
	},
	{
		"ID": 61,
		"ScheduleName": "Cayman Islands",
		"Date": "MonMon/OctOct/2015201520152015",
		"Time": 674,
		"ProjectID": "J0X 8I0",
		"Batch": "67224E38-494D-0ADD-C70E-2F054431413A",
		"Language": "VI",
		"Status": "Not-Started"
	},
	{
		"ID": 62,
		"ScheduleName": "Oman",
		"Date": "MonMon/NovNov/2015201520152015",
		"Time": 427,
		"ProjectID": "G1A 7N6",
		"Batch": "D7A0409A-7002-7A61-6EB5-37DA06894FBD",
		"Language": "Pomorskie",
		"Status": "Not-Started"
	},
	{
		"ID": 63,
		"ScheduleName": "Brazil",
		"Date": "SatSat/AugAug/2014201420142014",
		"Time": 1385,
		"ProjectID": "F0C 2M1",
		"Batch": "C7C1CC91-029F-9DEA-7B4A-4D5115815FC5",
		"Language": "Karnataka",
		"Status": "Not-Started"
	},
	{
		"ID": 64,
		"ScheduleName": "Timor-Leste",
		"Date": "WedWed/FebFeb/2016201620162016",
		"Time": 990,
		"ProjectID": "X4U 7P8",
		"Batch": "07541D95-AEB5-9449-6C75-7A46767D65CE",
		"Language": "NO",
		"Status": "Started"
	},
	{
		"ID": 65,
		"ScheduleName": "Germany",
		"Date": "MonMon/OctOct/2016201620162016",
		"Time": 1892,
		"ProjectID": "F6Q 1A8",
		"Batch": "B8C288FE-1E75-1712-16FB-03E446172490",
		"Language": "ON",
		"Status": "Started"
	},
	{
		"ID": 66,
		"ScheduleName": "Niger",
		"Date": "FriFri/AugAug/2014201420142014",
		"Time": 623,
		"ProjectID": "S5I 8J7",
		"Batch": "9BBD6956-EDA4-4B1E-841C-95FC59D48654",
		"Language": "Vienna",
		"Status": "Not-Started"
	},
	{
		"ID": 67,
		"ScheduleName": "Iran",
		"Date": "ThuThu/OctOct/2016201620162016",
		"Time": 866,
		"ProjectID": "W9O 7Q4",
		"Batch": "A99EDFF3-4657-98DC-24B6-4D14708D3203",
		"Language": "Bretagne",
		"Status": "Started"
	},
	{
		"ID": 68,
		"ScheduleName": "Virgin Islands, British",
		"Date": "TueTue/SepSep/2014201420142014",
		"Time": 543,
		"ProjectID": "I8K 6Y3",
		"Batch": "ECEC86D3-E603-692F-A98C-B4BF19A7D6E6",
		"Language": "AN",
		"Status": "Started"
	},
	{
		"ID": 69,
		"ScheduleName": "Niger",
		"Date": "FriFri/JanJan/2015201520152015",
		"Time": 1175,
		"ProjectID": "T1O 8B2",
		"Batch": "FFFB3B2A-AD46-DF8C-23E8-4BB7EA09D326",
		"Language": "VE",
		"Status": "Started"
	},
	{
		"ID": 70,
		"ScheduleName": "Morocco",
		"Date": "SunSun/NovNov/2013201320132013",
		"Time": 645,
		"ProjectID": "U1C 3N7",
		"Batch": "38C41EA4-267D-A357-7785-3BC5554120CA",
		"Language": "Hesse",
		"Status": "Not-Started"
	},
	{
		"ID": 71,
		"ScheduleName": "Iraq",
		"Date": "MonMon/MarMar/2014201420142014",
		"Time": 1038,
		"ProjectID": "G9F 0L2",
		"Batch": "3DCB0E74-C290-DA49-BDFF-39A0C96BD4CD",
		"Language": "San José",
		"Status": "Not-Started"
	},
	{
		"ID": 72,
		"ScheduleName": "Lithuania",
		"Date": "WedWed/AprApr/2014201420142014",
		"Time": 1982,
		"ProjectID": "A0V 4I7",
		"Batch": "38617BDE-BE2E-9088-20DB-CD1E11965F59",
		"Language": "ON",
		"Status": "Not-Started"
	},
	{
		"ID": 73,
		"ScheduleName": "Namibia",
		"Date": "FriFri/MayMay/2016201620162016",
		"Time": 233,
		"ProjectID": "M6S 4I7",
		"Batch": "C53776B1-DE71-D243-EED8-1B45333872CD",
		"Language": "Quebec",
		"Status": "Not-Started"
	},
	{
		"ID": 74,
		"ScheduleName": "Cook Islands",
		"Date": "FriFri/JunJun/2015201520152015",
		"Time": 1391,
		"ProjectID": "W1D 6Z1",
		"Batch": "674D4330-662B-A24C-7C3A-7DD815454845",
		"Language": "Alberta",
		"Status": "Started"
	},
	{
		"ID": 75,
		"ScheduleName": "Norfolk Island",
		"Date": "SatSat/JulJul/2015201520152015",
		"Time": 1514,
		"ProjectID": "O7F 7X2",
		"Batch": "21E3A28F-508F-4572-43D2-EEDF0B1E5717",
		"Language": "Quebec",
		"Status": "Started"
	},
	{
		"ID": 76,
		"ScheduleName": "Mongolia",
		"Date": "MonMon/SepSep/2014201420142014",
		"Time": 1807,
		"ProjectID": "E7S 7H9",
		"Batch": "E6A82F33-C5DA-DBB1-8545-C8717CDB0595",
		"Language": "New South Wales",
		"Status": "Started"
	},
	{
		"ID": 77,
		"ScheduleName": "Hungary",
		"Date": "WedWed/DecDec/2013201320132013",
		"Time": 196,
		"ProjectID": "B7J 1M3",
		"Batch": "F49454EB-B16E-BE92-6C21-F42764CA142F",
		"Language": "Basse-Normandie",
		"Status": "Not-Started"
	},
	{
		"ID": 78,
		"ScheduleName": "Montserrat",
		"Date": "WedWed/OctOct/2014201420142014",
		"Time": 1751,
		"ProjectID": "C8Y 0Y6",
		"Batch": "CD36EBA2-8228-3604-4DCB-BCAB19380E05",
		"Language": "CV",
		"Status": "Started"
	},
	{
		"ID": 79,
		"ScheduleName": "Puerto Rico",
		"Date": "FriFri/MarMar/2016201620162016",
		"Time": 920,
		"ProjectID": "R5K 4R7",
		"Batch": "29617964-89B7-FB4D-7FFC-6B9706F785CD",
		"Language": "NI",
		"Status": "Not-Started"
	},
	{
		"ID": 80,
		"ScheduleName": "Maldives",
		"Date": "MonMon/MarMar/2015201520152015",
		"Time": 1364,
		"ProjectID": "P6W 6A1",
		"Batch": "A5FF5540-53C9-6B52-86A5-6207EB0011A4",
		"Language": "NI",
		"Status": "Not-Started"
	},
	{
		"ID": 81,
		"ScheduleName": "Cuba",
		"Date": "SunSun/DecDec/2015201520152015",
		"Time": 1009,
		"ProjectID": "X0P 5N2",
		"Batch": "F4CFEF2C-AC08-968D-AA85-EDF0C09FD13A",
		"Language": "Ontario",
		"Status": "Not-Started"
	},
	{
		"ID": 82,
		"ScheduleName": "Liberia",
		"Date": "WedWed/NovNov/2013201320132013",
		"Time": 1895,
		"ProjectID": "T7H 3N4",
		"Batch": "605637D1-FB71-AB3E-EA21-E8159B9681C2",
		"Language": "Alajuela",
		"Status": "Not-Started"
	},
	{
		"ID": 83,
		"ScheduleName": "Ireland",
		"Date": "FriFri/MayMay/2015201520152015",
		"Time": 173,
		"ProjectID": "A8P 1F2",
		"Batch": "FD764C25-B457-7EAB-461D-9362397064D3",
		"Language": "Wi",
		"Status": "Not-Started"
	},
	{
		"ID": 84,
		"ScheduleName": "French Southern Territories",
		"Date": "ThuThu/SepSep/2014201420142014",
		"Time": 2285,
		"ProjectID": "D8N 7E4",
		"Batch": "9BA663C1-474C-7BDB-ADBB-AAC4DD2E6001",
		"Language": "BR",
		"Status": "Not-Started"
	},
	{
		"ID": 85,
		"ScheduleName": "Northern Mariana Islands",
		"Date": "SatSat/AprApr/2014201420142014",
		"Time": 810,
		"ProjectID": "B5Y 0Q8",
		"Batch": "8186322C-7670-B802-5805-34DC5A51DC46",
		"Language": "São Paulo",
		"Status": "Started"
	},
	{
		"ID": 86,
		"ScheduleName": "Switzerland",
		"Date": "SatSat/AugAug/2014201420142014",
		"Time": 872,
		"ProjectID": "J2S 8Z0",
		"Batch": "E33D48F9-3750-47EE-7B72-FD45F39DCDA2",
		"Language": "Antwerpen",
		"Status": "Started"
	},
	{
		"ID": 87,
		"ScheduleName": "Martinique",
		"Date": "ThuThu/JanJan/2014201420142014",
		"Time": 1883,
		"ProjectID": "Q5X 5C3",
		"Batch": "D6F5B4E9-BBB6-B27C-F09D-A6B9139A1A45",
		"Language": "Veneto",
		"Status": "Not-Started"
	},
	{
		"ID": 88,
		"ScheduleName": "Burundi",
		"Date": "SunSun/OctOct/2014201420142014",
		"Time": 651,
		"ProjectID": "L4P 2S2",
		"Batch": "A49ED308-2EF6-41C5-D16D-9D84FC5B8CE6",
		"Language": "Bihar",
		"Status": "Started"
	},
	{
		"ID": 89,
		"ScheduleName": "Tokelau",
		"Date": "SunSun/MarMar/2016201620162016",
		"Time": 262,
		"ProjectID": "G3D 8S7",
		"Batch": "0B2A8C97-4A3D-DAFD-7557-32704AD817EE",
		"Language": "VI",
		"Status": "Not-Started"
	},
	{
		"ID": 90,
		"ScheduleName": "Burundi",
		"Date": "MonMon/OctOct/2015201520152015",
		"Time": 1506,
		"ProjectID": "Q0P 9Y6",
		"Batch": "6D85E4C3-EB8F-DC8D-13AF-FCB5074E47EE",
		"Language": "Vienna",
		"Status": "Not-Started"
	},
	{
		"ID": 91,
		"ScheduleName": "Gambia",
		"Date": "ThuThu/JanJan/2014201420142014",
		"Time": 2310,
		"ProjectID": "X8P 8U4",
		"Batch": "D36C74B0-7E9E-E62F-CBF5-6FDE7EF92207",
		"Language": "Imo",
		"Status": "Not-Started"
	},
	{
		"ID": 92,
		"ScheduleName": "Venezuela",
		"Date": "WedWed/NovNov/2015201520152015",
		"Time": 673,
		"ProjectID": "D6H 7G7",
		"Batch": "CC0917D6-6A36-012C-D778-369A95C83FC0",
		"Language": "ON",
		"Status": "Not-Started"
	},
	{
		"ID": 93,
		"ScheduleName": "Korea, North",
		"Date": "WedWed/OctOct/2013201320132013",
		"Time": 1288,
		"ProjectID": "P3K 0B8",
		"Batch": "243B4093-A90A-FACF-9620-1116D7B64CE7",
		"Language": "CA",
		"Status": "Started"
	},
	{
		"ID": 94,
		"ScheduleName": "Gabon",
		"Date": "SatSat/JunJun/2016201620162016",
		"Time": 1846,
		"ProjectID": "Z1E 8D9",
		"Batch": "F4D3EA40-BE4C-A9EA-E2F7-E5662486697A",
		"Language": "Uttar Pradesh",
		"Status": "Not-Started"
	},
	{
		"ID": 95,
		"ScheduleName": "Guam",
		"Date": "FriFri/SepSep/2016201620162016",
		"Time": 760,
		"ProjectID": "G1C 1H4",
		"Batch": "5BE2CB15-273C-474E-65DF-C8FEA9252C22",
		"Language": "Ontario",
		"Status": "Not-Started"
	},
	{
		"ID": 96,
		"ScheduleName": "Greenland",
		"Date": "SatSat/MayMay/2016201620162016",
		"Time": 881,
		"ProjectID": "I9M 6O5",
		"Batch": "9A349D21-442E-3933-73EF-D9E2880B295F",
		"Language": "Saarland",
		"Status": "Not-Started"
	},
	{
		"ID": 97,
		"ScheduleName": "South Georgia and The South Sandwich Islands",
		"Date": "TueTue/OctOct/2015201520152015",
		"Time": 430,
		"ProjectID": "R7W 6F2",
		"Batch": "8A49D863-FCE7-FB4E-A59C-3A1BE7C53B9D",
		"Language": "MA",
		"Status": "Not-Started"
	},
	{
		"ID": 98,
		"ScheduleName": "Eritrea",
		"Date": "SatSat/OctOct/2013201320132013",
		"Time": 44,
		"ProjectID": "K5N 5U9",
		"Batch": "CB47D5A7-F556-96D2-9209-B9EDE68A9EB1",
		"Language": "Uttar Pradesh",
		"Status": "Not-Started"
	},
	{
		"ID": 99,
		"ScheduleName": "Serbia",
		"Date": "ThuThu/OctOct/2013201320132013",
		"Time": 1493,
		"ProjectID": "T4O 4P0",
		"Batch": "5CAF2A75-2C03-D7AE-AD97-AC735F31479D",
		"Language": "Zl",
		"Status": "Not-Started"
	},
	{
		"ID": 100,
		"ScheduleName": "Korea, South",
		"Date": "SunSun/JunJun/2015201520152015",
		"Time": 2168,
		"ProjectID": "N0B 2A4",
		"Batch": "13BDD1CA-3DC5-25FE-14B1-8862D5C7211C",
		"Language": "Hamburg",
		"Status": "Started"
	}
]
	};
}]);

surveyApp.config(function($routeProvider,$locationProvider) {
	$routeProvider
		.when('/', {	
			templateUrl : 'pages/profile.html',
			controller  : 'profileController'
		})

		.when('/profile', {	
			templateUrl : 'pages/profile.html',
			controller  : 'profileController'
		})

		.when('/surveys', {
			templateUrl : 'pages/surveys.html',
			controller  : 'surveysController'
		})

		.when('/researchers', {
			templateUrl : 'pages/researchers.html',
			controller  : 'researchersController'
		})

		.when('/survey', {
			templateUrl : 'pages/survey.html',
			controller  : 'surveyController'
		})

		.when('/data', {
			templateUrl : 'pages/data.html',
			controller  : 'dataController'
		})

		.when('/settings', {	
			templateUrl : 'pages/settings.html',
			controller  : 'settingsController'
		})

		.when('/sms', {	
			templateUrl : 'pages/sms.html',
			controller  : 'smsController'
		})

		.when('/manager', {	
			templateUrl : 'pages/manager.html',
			controller  : 'managerController'
		})

		.when('/entrepreneur', {	
			templateUrl : 'pages/entrepreneur.html',
			controller  : 'entreController'
		})
	$locationProvider.html5Mode(true);
});

surveyApp.controller('appController', function($scope,surveyFactory) {
	$scope.user = surveyFactory.user;
	$scope.surveys = surveyFactory.surveys;
	$scope.researchers = surveyFactory.researchers;
});

surveyApp.controller('profileController', function($scope,surveyFactory) {
	$scope.user = surveyFactory.user;
});

surveyApp.controller('surveysController', function($scope,surveyFactory) {
	$scope.surveys = surveyFactory.surveys;
});

surveyApp.controller('researchersController', function($scope,surveyFactory) {
	$scope.researchers = surveyFactory.researchers;
});

surveyApp.controller('settingsController', function($scope,surveyFactory) {
	$scope.User = surveyFactory.user;
});

surveyApp.controller('surveyController', function($scope,surveyFactory) {
	$scope.Type = surveyFactory.surveys[0].Type;
	$scope.survey = surveyFactory.surveys[0].Sections;
	$scope.questions = surveyFactory.surveys[0].Sections[0].Question;
});

surveyApp.controller('mainController', function($scope,surveyFactory) {
	$scope.message = 'This is the main page';
});

surveyApp.controller('entreController', function($scope,surveyFactory) {
	$scope.user = surveyFactory.user;
});

surveyApp.controller('smsController', function($scope,surveyFactory) {
	$('.btn-group').button();
});

surveyApp.controller('managerController', function($scope,surveyFactory) {
	$scope.managers = surveyFactory.managers;
	$scope.projects = surveyFactory.projects;
});

surveyApp.controller('dataController', function($scope, $filter, ngTableParams, surveyFactory) {
	 	var data = surveyFactory.data2;
            $scope.columns = [
                { title: 'ID', field: 'ID', visible: true },
                { title: 'Schedule Name', field: 'ScheduleName', visible: true },
                { title: 'Date', field: 'Date', visible: true },
                { title: 'Time', field: 'Time', visible: true },
                { title: 'Project ID', field: 'ProjectID', visible: true },
                { title: 'Batch', field: 'Batch', visible: true },
                { title: 'Language', field: 'Language', visible: true },
                { title: 'Status', field: 'Status', visible: true }
            ];
            $scope.tableParams = new ngTableParams({
                page: 1,            // show first page
                count: 10,          // count per page
                filter: {
                    name: 'M'       // initial filter
                }
            }, {
                total: data.length, // length of data
                getData: function($defer, params) {
                    // use build-in angular filter
                    var orderedData = params.sorting() ?
                            $filter('orderBy')(data, params.orderBy()) :
                            data;

                    $defer.resolve(orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                }
            });
});