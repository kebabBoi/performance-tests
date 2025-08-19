import xml.etree.ElementTree as El

xml_data = '''
<user>
    <id>1</id>
    <first_name>Michael</first_name>
    <last_name>Jordan</last_name>
    <email>mj@mail.ru</email>
    <address>
        <street>Gold St.</street>
        <city>California</city>
        <zip>100100</zip>
    </address>
</user>
'''

root = El.fromstring(xml_data)

print("User ID:", root.find('id').text)
print("User name:", root.find('first_name').text, root.find('last_name').text)
print("User email:", root.find('email').text)