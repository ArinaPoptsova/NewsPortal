class AuthorDoesNotExist(Exception):
    def __str__(self):
        return 'You don\'t have permissions to post'


class RequestOver(Exception):
    def __str__(self):
        return 'Today you can no longer post new articles'
