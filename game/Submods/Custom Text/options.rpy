init -990 python:
    store.mas_submod_utils.Submod(
        author="SteveeWasTaken",
        name="Custom Text",
        description=(
            "A simple submod in which you can ask Monika to say whatever you want.\n"
            "If you wish to use the Custom expression, just ask Monika!\n"
            "There's a prompt for it in the \"Monika\" category."
        ),
        version="1.3.0",
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