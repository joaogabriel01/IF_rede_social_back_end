class routes:

    def init_app(app):

        @app.route('/teste')
        def teste():
            return 'RotaTeste'

        @app.route('/teste2')
        def teste2():
            return 'RotaTeste2'