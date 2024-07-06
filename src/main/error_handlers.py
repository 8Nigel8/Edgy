import traceback


class NotFoundException(Exception):
    ...


class WrongPasswordException(Exception):
    ...


def add_error_handlers(app, env):
    if env in ['production', 'test']:
        @app.errorhandler(Exception)
        def handle_exception(e: Exception):
            return {
                'status': 'failure',
                'exception': e.__class__.__name__
            }

        return

    # Developing handling
    @app.errorhandler(Exception)
    def handle_exception(e: Exception):
        return {
            'status': 'failure',
            'error': 'InternalServerError',
            'message': str(e),
            'traceback': traceback.format_exc()
        }, 500

    @app.errorhandler(NotFoundException)
    def handle_not_found(e: NotFoundException):
        return {
            'status': 'Not found',
            'error': 'Not Found',
            'message': str(e),
            'traceback': traceback.format_exc()
        }, 404

    @app.errorhandler(WrongPasswordException)
    def handle_password_error(e: WrongPasswordException):
        return {
            'status': 'failure',
            'error': 'Wrong password',
            'message': str(e),
            'traceback': traceback.format_exc()
        }, 401
