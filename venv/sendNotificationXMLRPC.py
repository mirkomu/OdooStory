import xmlrpc.client

url = "https://edu-odoo13en.odoo.com"
db = "edu-odoo13en"
username = "mirko.muller@he-arc.ch"
password = "606c6c"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print("la version de Odoo: ", common.version())

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
print("test si nous avons les droits d'acces")
# print (models.execute_kw(db, uid, password,
#    'res.partner', 'check_access_rights',
#    ['read'], {'raise_exception': False}))

#print("create record: ")
#id=models.execute_kw(db, uid, password, 'res.partner', 'create', [{
#    'name': "New Partner XML not customer spec 2",
#    'phone' : "0329432323",
#}])

#print (id)

#print("search a record")
#models.execute_kw(db, uid, password,
#    print('res.partner', 'search',
#    ['name', '=', "Müller Mirko"])) #non marche pas


print("create notification")
id = models.execute_kw(db, uid, password, 'mail.channel', 'message_post', [{
#id=models.execute_kw(db, uid, password, 'mail.channel', 'create', [{
    'subtype': "mail.mt_comment",
    'body': "my notification to you",
    # partner to whom you send notification, 49 = res.partner from testUser, res.users =>6, 1=> res.partner (Müller Mirko)
    #'partner_ids': [(49,1)]
    # 'subject': "Message subject",
    # 'model': "mail.channel",
}])


# print ("create record")

# models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "New Partner",}])

## for odoo automatisation
'''env['mail.channel'].message_post({'message_type': "comment",
                                  "subtype": "mail.mt_comment",  # subject type
                                  'body': "My message",
                                  'needaction_partner_ids': [(49, 1)],  # partner to whom you send notification
                                  'res_id': 1,  # id de User Müller Mirko
                                  })

env['res.partner'].create({
    "name": "my new automated user",
})
'''