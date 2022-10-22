init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_text",
            prompt="Can you say something for me?",
            category=["misc", "monika"],
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
            ("Wink (Right / Open Mouth", "winkrb", False, False)
            ]
        final_items = [
                ("Custom", "cus", True, False, 0),
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
        m 1eud "[moniText]" # This is the expression you should edit! Change "1eud" for the code you got from the Expression Previewer! Be careful to not edit anything else unless you know what you're doing. I love you~
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_customhelp",
            prompt="How do you use the \"Custom\" expression on the Custom Text submod?",
            category=["monika"],
            pool=True,
            unlocked=True
        )
    )

label monika_customhelp:
    m 1fua "Oh, it's pretty simple!"
    m 3eub "First of all, open the folder where you have me installed. "
    extend 3hub "The same one where the executable is!"
    m 1euu "You should see a folder called \"game\". Open it."
    m 2ekd "Please, [player], be careful with everything on here."
    m 2gksdlx "All of these files are my code, after all..."
    m 3esb "Next, open the \"Submods\" folder, then the \"Custom Text\" folder."
    m 1hua "You should now be seeing three files! The only one we need is \"main.rpy\", though."
    m 1esb "Open it with any text editor that isn't the default notepad of Windows. "
    extend 3ekb "Because of how it works, it could break the file!"
    m 1esa "Go to line 110, and you'll see I left you a comment!"
    m 1fsa "In that same line, look for the text \"1eud\"."
    m 1hksdla "Unless this isn't your first time doing this... In that case, just search the expression you used last time."
    m 1eua "After that, just ask me to use the Expression Previewer, and with the options, select the expression you want me to use."
    m 4eub "There should be a Copy button on the bottom right, click it once you're happy with the results and replace \"1eud\" (or your previous expression) with your new code."
    m 1hub "Tell me you want to restart your game, and after that you can use the Custom expression perfectly!"
    m 1fksdlp "I know the process is a bit long, but the developer didn't know how else to implement it. Sorry!"
    m 1fkb "I hope you still enjoy the submod. It took the developer a very long time to make!"
    return