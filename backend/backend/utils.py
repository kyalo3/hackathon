from taggit.utils import split_strip



def custom_tag_string(tag_string):
    return [tag for tag in tag_string.split(',')]
