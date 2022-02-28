#Assignment1#
#Anasua Das#
#120220427
#24.02.2022#
################################################################################################

import re
from pprint import pprint
def find_couple(bride,groom):
   regex = re.compile(r'(\s*Marriage\sof\s(?P<Name>([A-Z]*\s[A-Z]*)*)\n)'
                    r'(\s*in\s*(?P<Year>\d*)\n)'
                    r'(\s*Group\sRegistration\sID\t(?P<ID>N\/R)\n)'
                    r'(\s*SR\sDistrict\/Reg\sArea\t(?P<DIST>[A-Z][a-z]*|[A-Za-z]*\s[A-Za-z]*))'
                    r'(\s*Returns\sYear\t(?P<ReturnYear>\d*)\n)'
                    r'(\s*Returns\sQuarter\t(?P<Quarter>\d*)\n)'
                    r'(\s*Returns\sVolume\sNo\t(?P<Volume>\d*)\n)'
                    r'(\s*Returns\sPage\sNo\t(?P<Page>\d*)\n)'
)
    
   bridedetails=[]
   count=0
   bridedata=bride.read()
   for m in regex.finditer(bridedata):
       bridedetails.append(m.groupdict())
   groomdetails=[]
   groomdata=groom.read()
   for n in regex.finditer(groomdata):
       groomdetails.append(n.groupdict())
   for items1 in bridedetails:
       dict1=items1
       Name_b=dict1.get('Name')
       ReturnYear_b=dict1.get('ReturnYear')
       ID_b=dict1.get('ID')
       DIST_b=dict1.get('DIST')
       Quarter_b=dict1.get('Quarter')
       Volume_b=dict1.get('Volume')
       Page_b=dict1.get('Page')
       for items2 in groomdetails:
         dict2=items2
         Name_g=dict2.get('Name')
         ReturnYear_g=dict2.get('ReturnYear')
         ID_g=dict2.get('ID')
         DIST_g=dict2.get('DIST')
         Quarter_g=dict2.get('Quarter')
         Volume_g=dict2.get('Volume')
         Page_g=dict2.get('Page')
         if(ReturnYear_b==ReturnYear_g and DIST_b==DIST_g and Quarter_b==Quarter_g and Volume_b==Volume_g and Page_b==Page_g):
           print("Possible Match")
           print(Name_g," and ",Name_b," in ",DIST_g," in ",ReturnYear_g,"\nQuarter = ",Quarter_g,"volume =",Volume_g,"page = ",Page_g)
            
#maryRoche=open('mary_roche.txt','r')
#nicholas=open('nicholas.txt','r')
#find_couple(maryRoche,nicholas)