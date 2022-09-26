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
            ("Default", "1eua", False, False),
            ("Default (Open Mouth)", "1eub", False, False),
            ("Worried", "1ekc", False, False),
            ("Worried (Open Mouth)", "1ekb", False, False),
            ("Surprised", "1euc", False, False),
            ("Surprised (Sad Open Mouth)", "1eud", False, False),
            ("Surprised (Happy Open Mouth)", "1eub", False, False),
            ("Confused", "1etc", False, False),
            ("Confused (Sad Open Mouth)", "1etd", False, False),
            ("Confused (Happy Open Mouth)", "1etb", False, False),
            ("Angry", "1efc", False, False),
            ("Angry (Sad Open Mouth)", "1efd", False, False),
            ("Angry (Happy Open Mouth)", "1efb", False, False),
            ("Happy", "1hua", False, False),
            ("Happy (Open Mouth)", "1hub", False, False),
            ("Smug", "1tua", False, False),
            ("Smug (Open Mouth)", "1tub", False, False),
            ("Smug (Left)", "1mua", False, False),
            ("Smug (Left / Open Mouth)", "1mub", False, False),
            ("Smug (Right)", "1gua", False, False),
            ("Smug (Right / Open Mouth", "1gub", False, False),
            ("Sparkling", "1sub", False, False),
            ("Sparkling (Open Mouth)", "1sub", False, False),
            ("Wink (Left)", "1nua", False, False),
            ("Wink (Left / Open Mouth)", "1nub", False, False),
            ("Wink (Right)", "1kua", False, False),
            ("Wink (Right / Open Mouth", "1kub", False, False),
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
