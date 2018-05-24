# Local Django
from core.api_views import LoginView
from core.serializers import LoginSerializerV1


class LoginViewV1(LoginView):
    serializer_class = LoginSerializerV1

    def _action(self, serializer):
        action = super(LoginViewV1, self)._action(serializer)

        action.data.update({
            'user_id': serializer.user.id,
        })

        return action
