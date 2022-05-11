class Account:
    def __init__(self, site, login, password):
        self.site     = site
        self.login    = login
        self.password = password

    def __str__(self):
        return "site: {site} \n login: {login} \n password: {password}".format(site     = self.site,
                                                                               login    = self.login,
                                                                               password = self.password)

    
