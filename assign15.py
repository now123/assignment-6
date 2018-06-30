#Q.1- Extract the user id, domain name and suffix from the following email addresses.
#emails = "zuck26@facebook.com" "page33@google.com"
"#jeff42@amazon.com"
#desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]

import re
email="zuck26@facebook.com page33@google.com jeff42@amazon.com "
y=re.findall(r'[\w_$+=]{1,20}',email)
print (y)

#Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
#text = "Betty bought a bit of butter, But the butter was so bitter,
# So she bought some better butter, To make the bitter butter better."
import re
text = "Betty bought a bit of butter, But the butter was so bitter,  So she bought some better butter, To make the bitter butter better."
m = re.findall(r'[b]\w+', text)
n = re.findall(r'[B]\w+', text)
print(m,n)

#Q.3- Split the following irregular sentence into words
#sentence = "A, very very; irregular_sentence"
#desired_output = "A very very irregular sentence"
import re
sentence = "A, very very; irregular_sentence"
d=sentence.replace("_"," ")
desired_output=re.sub('[^\w\s]',' ',d)
print(desired_output)



