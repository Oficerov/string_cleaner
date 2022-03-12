def entity_map(new_rule={}):
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
    } | new_rule
