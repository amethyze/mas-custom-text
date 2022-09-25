init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_text",
            prompt="Custom Text",
            category=["Custom Text"],
            pool=True,
            unlocked=True
        )
    )

label monika_text:
    m "What do you want me to say, [player]?{nw}"
    $ moniText = mas_input(
            "What do you want me to say, [player]?"
        )
    m "What expression should I do?"
    python:
        exp_prompt_list = [
            ("Default", "def", False, False),
            ("Default (Open Mouth)", "defb", False, False),
            ("Worried", "wor", False, False),
            ("Worried (Open Mouth)", "worb", False, False),
            ("Surprised", "surp", False, False),
            ("Surprised (Sad Open Mouth)", "surpb", False, False),
            ("Surprised (Happy Open Mouth)", "surpc", False, False),
            ("Confused", "conf", False, False),
            ("Confused (Sad Open Mouth)", "confb", False, False),
            ("Confused (Happy Open Mouth)", "confc", False, False),
            ("Angry", "ang", False, False),
            ("Angry (Sad Open Mouth)", "angb", False, False),
            ("Angry (Happy Open Mouth)", "angc", False, False),
            ("Happy", "hap", False, False),
            ("Happy (Open Mouth)", "hapb", False, False),
            ("Smug", "smug", False, False),
            ("Smug (Open Mouth)", "smugb", False, False),
            ("Smug (Left)", "smugl", False, False),
            ("Smug (Left / Open Mouth)", "smuglb", False, False),
            ("Smug (Right)", "smugr", False, False),
            ("Smug (Right / Open Mouth", "smugrb", False, False),
            ("Sparkling", "spark", False, False),
            ("Sparkling (Open Mouth)", "sparkb", False, False),
            ("Wink (Left)", "winkl", False, False),
            ("Wink (Left / Open Mouth)", "winklb", False, False),
            ("Wink (Right)", "winkr", False, False),
            ("Wink (Right / Open Mouth", "winkrb", False, False),
            ("Custom", "cus", True, False)
            ]
        final_items = [
                (_("Nevermind."), "nvm", False, False, 0)
            ]

    call screen mas_gen_scrollable_menu(exp_prompt_list, mas_ui.SCROLLABLE_MENU_MEDIUM_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, *final_items)
    if _return == "def":
        m 1eua "[moniText]"
    elif _return == "defb":
        m 1eub "[moniText]"
    elif _return == "wor":
        m 1ekc "[moniText]"
    elif _return == "worb":
        m 1ekd "[moniText]"
    elif _return == "surp":
        m 1euc "[moniText]"
    elif _return == "surpb":
        m 1eud "[moniText]"
    elif _return == "surpc":
        m 1eub "[moniText]"
    elif _return == "conf":
        m 1etc "[moniText]"
    elif _return == "confb":
        m 1etd "[moniText]" 
    elif _return == "confc":
        m 1etb "[moniText]" 
    elif _return == "ang":
        m 1efc "[moniText]"
    elif _return == "angb":
        m 1etd "[moniText]" 
    elif _return == "angc":
        m 1etb "[moniText]"
    elif _return == "hap":
        m 1hua "[moniText]" 
    elif _return == "hapb":
        m 1hub "[moniText]"
    elif _return == "smug":
        m 1tua "[moniText]"
    elif _return == "smugb":
        m 1tub "[moniText]" 
    elif _return == "smugr":
        m 1mua "[moniText]" 
    elif _return == "smugrb":
        m 1mub "[moniText]" 
    elif _return == "smugl":
        m 1gua "[moniText]"
    elif _return == "smuglb":
        m 1gub "[moniText]" 
    elif _return == "spark":
        m 1sua "[moniText]" 
    elif _return == "sparkb":
        m 1sub "[moniText]" 
    elif _return == "winkl":
        m 1nua "[moniText]" 
    elif _return == "winklb":
        m 1nub "[moniText]" 
    elif _return == "winkr":
        m 1kua "[moniText]" 
    elif _return == "winkl":
        m 1kub "[moniText]" 
    elif _return == "cus":
        m 1eud "[moniText]"
    return