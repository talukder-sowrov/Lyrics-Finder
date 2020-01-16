class RegularExpressions:
    def __init__(self, startComment, endComment):
        self.startComment = startComment
        self.endComment = endComment

    def changeCommentStyle(self, newStartComment, newEndComment):
        self.startComment = newStartComment
        self.endComment = newEndComment