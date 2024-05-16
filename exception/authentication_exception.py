class AuthenticationException(Exception):
    def __init__(self):
        super().__init__(" Exception: Only Authorized User can enter")
