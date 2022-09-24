init -990 python:
    store.mas_submod_utils.Submod(
        author="SteveeWasTaken",
        name="Custom Text",
        description=(
            "A simple submod in which you can ask Monika to say whatever you want.\n\n"
            "If you wish to use the Custom expression, then open the Expression Previewer,"
            " make your own expression, and copy the expression code. After that, open your"
            " submods folder, the \"Custom Text\" folder, then \"main.rpy\".\n"
            "Go to line 63 and replace \"1eud\" with the expression code you copied before.\n"
            "Tell Monika that you'll restart your game, then write your text and choose \"Custom\"!"
        ),
        version="1.2.0",
        version_updates={}
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Custom Text",
            user_name="SteveeWasTaken",
            repository_name="mas-custom-text",
            update_dir=""
        )