# -*- coding:utf-8 -*-
#convert to wikitable
import csv

class convert_csv_table(object):

    def __init__(self,file_name, headers):
        self.file_name = file_name
        self.headers = headers
        self.convert()
        
    # defines unsafe characters and attempts to convert them to
    #html entities (which can be safely parsed by mediawiki)
    def sanitize(self,string):
        special_characters = {"’":"&#8216;",
"’":"&#8217;",
"[":"&#91;",
"]":"&#93;",
"{":"&#123;",
"}":"&#125;",
" ":"&nbsp;",
"&":"&amp;",
"|":"&#124;",
"!":"&#33;",
"=":"&#61;",
"*":"&#42;",
"#":"&#35;",
"<":"&#60;",
">":"&#62;",
"/":"&#47;",
"-":"&#45;",
"+":"&#43;",
"\"":"&#8220;",
"'":"&#39;"}

        try:
            if any(character in string for character in special_characters.keys()):
                string = special_characters[string]
            elif string == None:
                string = ''
            return string
        except KeyError, e:
            return string

    #main method to create a mediawiki table from csv input
    def convert(self):
        with open(self.file_name, 'rU') as raw_file:
            input_file = csv.reader(raw_file)
            if self.headers:
                content = '{|! class="wikitable sortable"\n!%s\n' % '\n!'.join(input_file.next())
            else: 
                content = '{|! class="wikitable sortable"\n'
            for line in input_file:
                content += '|-\n'
                for column in line:
                    content += '|%s\n' % self.sanitize(column)
            content += '|}'
            
            self.content = content                
            
    #call after conversion -- returns a string        
    def get_string(self):
        return self.content
        
    #call after conversion -- writes to a file    
    def get_file(self, output_name):
        output_file = open(output_name, 'wb')
        output_file.write(self.content)
        output_file.close()