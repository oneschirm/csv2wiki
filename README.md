#csv2wiki : about

csv2wiki converts CSV files to mediawiki-formatted tables. 

#features

* csv2wiki uses **zero** non-standard modules -- only csv
* converts unsafe characters to their html entity equivalents
* output as a string or file

#usage

**convert a table with headers, output as string**

<pre>
from csv2wiki import csv2wiki
wiki_table = csv2wiki.convert_csv_table('test.csv', True)
output_string = wiki_table.get_string()
</pre>

the script will produce a string that can printed, redirected, etc. 

**convert a table without headers, output as a file**

<pre>
from csv2wiki import csv2wiki
wiki_table = csv2wiki.convert_csv_table('test2.csv', False)
wiki_table.get_file('test2_wiki_output.txt')
</pre>

the script will output the content to a file named `test2_wiki_output.txt`

#notes

this module outputs the mediawiki table enhanced with `class="wikitable sortable"`

you can contact me on github or at oneschirm@gmail.com
