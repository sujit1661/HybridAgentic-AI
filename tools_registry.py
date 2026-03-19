from tools.file_tool import *
from tools.coding_shell_tools import *
from tools.System_tools import *
from tools.general_tools import *
from tools.github_tools import *
from tools.general_github_api_tools import *

def load_all_tools():
    tools = [
        get_current_time,
        get_weather,
        create_folder,
        create_empty_file,
        rename_file,
        read_file,
        create_file_with_content,
        remove_file,
        remove_folder,
        copy_file,
        move_file,
        write_file,
        list_files,
        search_file,
        get_file_size,
        append_doc,
        summarize_current_project_folder,
        create_zip_folder,
        run_js_script,
        run_python_script,
        install_python_packages,
        install_node_packages,
        search_web,
        print_project_hierarchy,
        execute_terminal_command,
        get_os_info,
        list_processes,
        get_cpu_RAM_usage,
        search_github,
        list_repo_files,
        download_github_repo,
        get_repo_readme,
        download_random_image_by_name,
        create_github_repo,
        delete_github_repo,
        list_github_repos,
        create_github_file,
        delete_github_file,
        add_folder_and_files_to_github,
    ]

    for t in tools:
        if not t.__doc__:
            raise ValueError(f"{t.__name__} ❌ missing docstring")

    return tools