def restore_documents(originals: tuple[str, ...], backups: tuple[str, ...]) -> set[str]:
    ## single line version:##
    return set(filter(lambda x: not x.isdigit(), map(lambda x: x.upper() , (originals + backups))))

    ## Original version ##
    #combined = originals + backups
    #lower = map(lambda x: x.upper() , combined)
    #clean = sef(filter(lambda x: not x.isdigit()))
    #return clean