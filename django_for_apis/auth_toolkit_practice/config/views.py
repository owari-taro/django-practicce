from oauth2_provider.views import TokenView
import json
from oauth2_provider.models import get_access_token_model
from oauth2_provider.signals import app_authorized
from django.http import HttpResponse, JsonResponse


class SmartScopesTokenView(TokenView):
    """ A view to assign scopes to the OAuth2 token according to
    the passed credentials.

    Right now, the `read` scope is granted to any registered user
    but the `write` scope requires the `is_staff` or `is_superuser`
    flag to be `True` in their profile.

    See: https://github.com/jazzband/django-oauth-toolkit/issues/731#issuecomment-601379927

    """

    def post(self, request, *args, **kwargs):
        url, headers, body, status = self.create_token_response(request)
        if status == 200:
            json_body = json.loads(body)
            access_token = json_body.get('access_token')
            if access_token is not None:
                token = get_access_token_model().objects.get(
                    token=access_token)

                # --- customization starts here

                WRITE_SCOPE = 'write'
                print("#############################")
                user = token.user
                print(token.user)
                print(type(token.user))
                scopes = json_body.get('scope').split()
                print(user.__dict__)
                if (
                    WRITE_SCOPE in scopes
                    and not (
                        user.is_staff

                    )
                ):
                    scopes.remove(WRITE_SCOPE)
                    scope = ' '.join(scopes)

                    token.scope = scope
                    token.save()

                    json_body['scope'] = scope
                    body = json.dumps(json_body)

                # --- customization ends here

                app_authorized.send(
                    sender=self, request=request,
                    token=token)
        response = HttpResponse(content=body, status=status)

        for k, v in headers.items():
            response[k] = v
        return response
