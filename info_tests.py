import mock


class Foo(object):

    """ New changes!!!!!!!!!!!!!!!!!!!!!!!!!!!!!111111111111111
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    """

    registry = mock.Mock()
    registry.auth_api = mock.Mock()


    def __init__(self):
        self.registry.auth_api.get_access_info.return_value = dict(res_limits=['a', 'b'], full='true')
        self.registry.full_access = False


f = Foo()
print f.registry.auth_api.get_access_info({'a': 123, 'b': 3426})
print f.registry.full_access
print getattr(f.registry, 'auth_api')

