print("hello Odoo 13");

import odoolib

#informations to edite *************************************************************************************************
hostname="edu-odoo13en.odoo.com" #server url
database="edu-odoo13en" #domaine name
login="mirko.muller@he-arc.ch" # administrator login (create the object)
password='606c6c'
########################################################################################################################

#connection
connection = odoolib.get_connection(
	hostname = hostname,
	database = database,
	login = login,
	password = password,
	port= 443,
	protocol="jsonrpcs"
   )


#ask for country_id
country_model = connection.get_model('res.country')
ch_id = country_model.search([('name', '=', 'Switzerland')])[0]

print(ch_id);

## works create user
#partner_model = connection.get_model('res.partner')
#a_turner = partner_model.create({
# 	'name': 'okok okok',
# 	'street': 'Avenue du Peyrou 8',
# 	'zip': '2000',
#   'city': 'Neuchâtle',
#   'country_id' : ch_id,
#   'phone': '032 456 78 58',
#   'email': 'ok.0k0k@uweb.ch'
#     })

##end works create user

#partner_model = connection.get_model('base.automation')

#sudoenv['mail.message'].sudo().create({
# env = partner_model.create({
#     'email_from': env.user.partner_id.email,  ### add the sender email
#     'author_id': env.user.partner_id.id,  ### add the creator id
#     'model': 'mail.channel',  ### model should be mail.channel
#     'type': 'comment',
#     'subtype_id': env.ref('mail.mt_comment').id,  ### Leave this as it is
#     'body': "Body of the message",  ### here add the message body
#     'channel_ids': [(1, env.ref(
#         'inventory_notifications_mhr.mail.channel_all_employees').id)],
#     ## This is the channel where you want to send the message and all the users of this channel will receive message
#     'res_id': env.ref('modulename.mail.channel_all_employees').id, ### here add the channel you created.
# })
#
# env['mail.message'].create({'message_type': "notification",
#                                  "subtype": env.ref("mail.mt_comment").id,
#                                  'body': "Message body",
#                                  'subject': "Message subject",
#                                  'needaction_partner_ids': [(2, 2)], #
#                                  'res_id': 1, # id du mail.channel
#                                  })


partner_model = connection.get_model('mail.channel')
a_turner = partner_model.message_post({
	'message_type': 'comment',
	'subtype': 'mail.mt_comment',
	'body': 'Hello Word and my messages',
	'partner_ids': 49
})
