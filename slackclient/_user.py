class User(object):
    def __init__(self, server, user):
        self.id = user['id']
        self.team_id = user['team_id']
        self.name = user['name']
        self.deleted = user['deleted']
        self.status = user['status']
        self.color = user['color']
        self.real_name = user['real_name']
        self.tz = user['tz']
        self.tz_label = user['tz_label']
        self.tz_offset = user['tz_offset']
        self.is_admin = user['is_admin']
        self.is_owner = user['is_owner']
        self.has_2fa = user['has_2fa']
        self.profile = user['profile']

        self.server = server

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
