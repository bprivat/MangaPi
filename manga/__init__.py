from tasks.tasks import updateManga

def startup():
    """Tasks to run on server startup."""
    
    #Search for new chapters
    updateManga()