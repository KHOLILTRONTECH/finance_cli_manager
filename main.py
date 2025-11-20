import argparse
from db import init_db
from commands.add import register_add
from commands.list_data import register_list_command
from commands.filter_data import register_filter_command
from commands.summary import register_summary_command
from commands.export_import import register_export_import_commands
from commands.delete import register_delete_command
from commands.update import register_update_command
from commands.graph import register_graph_command
from utils.backup import auto_backup
from utils.dashboard import display_dashboard
from commands.report import register_report_command



def main():
    init_db()
    auto_backup()

    # tampilkan dashboard setiap kali program dijalankan
    display_dashboard()

    parser = argparse.ArgumentParser(
        description="Aplikasi Pengelola Keuangan Harian (SQLite + CLI)"
    )
    subparsers = parser.add_subparsers(dest="command")
    subparsers.required = True

    # register command
    register_add(subparsers)
    register_list_command(subparsers)
    register_filter_command(subparsers)
    register_summary_command(subparsers)
    register_export_import_commands(subparsers)
    register_delete_command(subparsers)
    register_update_command(subparsers)
    register_graph_command(subparsers)
    register_report_command(subparsers)


    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
