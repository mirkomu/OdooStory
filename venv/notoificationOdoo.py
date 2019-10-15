class name:
    _inherit = 'mail.thread'


#code:
self.env['mail.message'].create({'message_type': "notification",
                                 "subtype": self.env.ref("mail.mt_comment").id,
                                 'body': "Message body",
                                 'subject': "Message subject",
                                 'needaction_partner_ids': [(4, self.user_id.partner_id.id)],
                                 'model': self._name,
                                 'res_id': self.id,
                                 })


def action_send_notification(self):
    self.env['mail.message'].create({
        'email_from': self.env.user.partner_id.email,  ### add the sender email
        'author_id': self.env.user.partner_id.id,  ### add the creator id
        'model': 'mail.channel',  ### model should be mail.channel
        'type': 'comment',
        'subtype_id': self.env.ref('mail.mt_comment').id, ### Leave this as it is
        'body': "Body of the message",  ### here add the message body
    'channel_ids': [(1, self.env.ref(
        'inventory_notifications_mhr.mail.channel_all_employees').id)],  ## This is the channel where you want to send the message and all the users of this channel will receive message
    'res_id': self.env.ref('modulename.mail.channel_all_employees').id,  ### here add the channel you created.
    })
