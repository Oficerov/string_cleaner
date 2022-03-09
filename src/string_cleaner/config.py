def entity_map():
    """Return map special symbols -> html-entity"""
    return {
        "'": "&apos;",
        "\"": "&quot;",
        "«": "&laquo;",
        "»": "&raquo;",
        "‘": "&lsquo;",
        "’": "&rsquo;",
        "‚": "&sbquo;",
        "“": "&ldquo;",
        "”": "&rdquo;",
        "„": "&bdquo;",
        "‹": "&lsaquo;",
        "›": "&rsaquo;",
        "<": "&lt;",
        ">": "&gt;"
    }
