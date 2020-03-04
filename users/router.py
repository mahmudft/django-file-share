class UsersRouter:
    def db_for_read(self, model, **hints):
        """
        Attempts to read logs models go to logs.
        """
        if model._meta.app_label == 'users':
            return 'logs'

        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write user models go to logs.
        """
        if model._meta.app_label == 'users':
            return 'logs'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label == 'users' or \
                obj2._meta.app_label == 'users':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'users_db'
        database.
        """
        if app_label == 'users':
            return db == 'logs'
        return 'default'
