class AuthorDoesNotExist(Exception):
    def __str__(self):
        return 'You don\'t have permissions to post'
