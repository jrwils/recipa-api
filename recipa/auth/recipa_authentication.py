from tastypie.authentication import SessionAuthentication

class RecipaAuthentication(SessionAuthentication):
    '''
    Allow read-only access for GET requests. Otherwise, enforce default SessionAuthentication.
    '''
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True
        return super(RecipaAuthentication, self).is_authenticated(self, request, **kwargs)
