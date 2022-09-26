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
    if _return == "cus":
        # logic for custom expression, pass it further on to mas_quipExp
    elif _return == "nvm":
        # logic for nevermind
    else:
        $ mas_quipExp(_return)
        m "[moniText]"
    return
