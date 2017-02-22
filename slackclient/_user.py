class User(object):
    def __init__(self, server, user):
        self.server = server
        self.id = user['id']
        try:
            self.team_id = user['team_id']
            self.name = user['name']
            self.deleted = user['deleted']
            self.status = user.get('status')
            self.color = user.get('color')
            self.real_name = user.get('real_name')
            self.tz = user.get('tz')
            self.tz_label = user.get('tz_label')
            self.tz_offset = user.get('tz_offset')
            self.is_admin = user.get('is_admin')
            self.is_owner = user.get('is_owner')
            self.has_2fa = user.get('has_2fa')
            self.profile = user.get('profile')
        except Exception as ex:
            print(ex)

    def __eq__(self, compare_str):
        return compare_str in (self.id, self.name)

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        data = ""
        for key in list(self.__dict__.keys()):
            if key != "server":
                data += "{0} : {1}\n".format(key, str(self.__dict__[key])[:40])
        return data

    def __repr__(self):
        return self.__str__()
