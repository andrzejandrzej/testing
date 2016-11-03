import web

urls = (
    '/stage2', 'ins',
    '/console_log', 'ind',
    '/internal/api_call/', 'index',
    '/csp', 'csp',
    '/stage1', 'stage1'
)

lols = []

class ins:
    def POST(self):
        pass

    def GET(self):
        # print "O: {}".format(o)
        # print "T: {}".format(t)
        # print "H: {}".format(h)

        print web.input()

class index:
    def GET(self):
        print web.ctx.items()


    def POST(self):
        print web.capturestdout
        # print web.whereami
        print web.data()
        print web.ctx.items()
        return web.data()

class ind:
    def POST(self):
        data = web.data()
        if data:
            print "##########"
            print data[:20]
            print "##########"


class csp:
    def POST(self):
        print web.ctx.items()
        return web.data()

    def GET(self):
        print web.ctx.items()


class stage1:
    def POST(self):
        print web.ctx.items()


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()