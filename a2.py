########### Name: Anasua Das  #############
########### Student Id:120220427 ##########
########### Python Assignment 2 ###########
########### Year: 2021-22 #################
########### Counting Word Frequency of a document and writing each word and it's corresponding frequency of occurence in an excel worksheet.################################### 
##########################################################################################################################################################################
import docx
from docx import Document
import re
import os
import pyexcel as p
def analyze(docfile):
   newlist=[]
   dict={}
   dict_frequency={}
   name = os.path.basename('C:\\Users\\Abc\\Desktop\\PythonAss2\\pride_and_prejudice.docx')
   fname= os.path.splitext(name)[0]+"_word_stats.xlsx"
   for para in docfile.paragraphs:
    paratext=para.text
    paratext=paratext.lower() #converting text to lower case
    my_punc = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '.',
           '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', 
           '`', '{', '|', '}', '~', '»', '«', '“', '”']
    punc_pattern = re.compile("[" + re.escape("".join(my_punc)) + "]")
    paratext=re.sub(punc_pattern, "", paratext)
    #print(paratext)
    words=paratext.split()
    #print(words)
    for word in words:
       newlist.append(word) # extracting words from the text
       if word not in dict: #counting each word in the dictionary
          dict[word]=1
       else:
          dict[word]+=1
   #print(dict)
   total_words=len(newlist)
   for key,val in dict.items(): #calculating frequency of each  word in dictionary
      frequency=val/total_words
      if frequency>=0.001:
         dict_frequency.update({key:frequency}) #new dictionary updated with word and the calculated frequency
   dict_frequency = sorted(dict_frequency.items(),key=lambda x:x[1], reverse=True) #sorted in descending order
   #print(dict_frequency)
   
   p.save_as(array=dict_frequency, dest_file_name=fname,sheet_name = 'Word Frequency Stats') #write worksheet with word and its corresponding frequency 
   
   
#docfile=docx.Document('C:\\Users\\Abc\\Desktop\\PythonAss2\\pride_and_prejudice.docx')
#analyze(docfile)