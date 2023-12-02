import argparse
import datetime
import os
import subprocess
from typing import List, Optional, Tuple

TODAY = datetime.datetime.today()
SCRIPT_PATH = os.path.dirname(__file__)
INPUT_PATH = SCRIPT_PATH.replace('scripts', 'inputs')
TS_DIR = SCRIPT_PATH.replace('scripts', 'js')
GO_DIR = SCRIPT_PATH.replace('scripts', 'go')
PY_DIR = SCRIPT_PATH.replace('scripts', 'python')

VALID_LANGS = ('all', 'py', 'ts', 'go')

def ts_run_cmd(day: int, input_path: str, year: int = 0, test: bool = False) -> List[str]:
    code_path = os.path.join(TS_DIR, f'day{str(day).zfill(2)}', 'main.ts')
    return ['bun', 'run', code_path, ]


def go_run_cmd(day: int, input_path: str, year: int = 0, test: bool = False) -> List[str]:
    code_path = os.path.join(GO_DIR, 'cmd', f'day{str(day).zfill(2)}', 'main.go')
    if input_path is None:
        input_path = get_input_path(day=day, test=test)
    return ['go', 'run', code_path,]


def py_run_cmd(day: int, input_path: str, year: int = 0, test: bool = False) -> List[str]:
    code_path = os.path.join(PY_DIR, f'day{str(day).zfill(2)}', 'main.py')
    input_path = get_input_path(day=day, test=test)
    return ['python', code_path, ]


def get_input_path(day: int, year: int = 0, test: bool = False) -> str:
    return os.path.join(os.path.dirname(__file__).replace('scripts', 'inputs'), f'day{str(day).zfill(2)}{"_test" if test else ""}.txt')


def get_all_commands(lang: str, version: str, day: int) -> List[Tuple[List[str], str]]:
    commands = []

    if day == 0:
        days = tuple(range(1, TODAY.day + 1))
    else: 
        days = (day,)

    if lang == 'all':
        langs = ('py', 'ts', 'go')
    else:
        langs = (lang,)

    if version == 'all':
        tests = (True, False)
    else:
        tests = (version == 'test',)
    
    for d in days:
        for l in langs: 
            day_lang = f'Day: {d} - {l}'
            title = '=' * int((80 - len(day_lang) - 4) / 2) + f'  {day_lang}  ' + '=' * int((80 - len(day_lang) - 4) / 2)
            match l:
                case 'py':
                    for t in tests:
                        input_path = get_input_path(d, test=t)
                        commands.append((['echo', title], ''))
                        if t:
                            commands.append((['echo', 'TEST'], ''))
                        commands.append((py_run_cmd(day=d, test=t, input_path=input_path), input_path))
                case 'ts':
                    for t in tests:
                        input_path = get_input_path(d, test=t)
                        commands.append((['echo', title], ''))
                        if t:
                            commands.append((['echo', 'TEST'], ''))
                        commands.append((ts_run_cmd(day=d, test=t, input_path=input_path), input_path))
                case 'go':
                    for t in tests:
                        input_path = get_input_path(d, test=t)
                        commands.append((['echo', title], ''))
                        if t:
                            commands.append((['echo', 'TEST'], ''))
                        commands.append((go_run_cmd(day=d, test=t, input_path=input_path), input_path))
                case _:
                    continue
    return commands



def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', action='store', default='all')
    ap.add_argument('--year', action='store', type=int, default=TODAY.year)
    ap.add_argument('--day', action='store', type=int, default=TODAY.day)
    ap.add_argument('--version', action='store', default='all')
    ap.add_argument('--input', action='store', required=False)
    args = ap.parse_args()

    if args.lang not in VALID_LANGS:
        raise ValueError(f'invalid language! expected {VALID_LANGS}, got="{args.lang}"')
    
    all_commands = get_all_commands(args.lang, args.version, args.day)
    for command, input_path in all_commands:
        if input_path == '':

            subprocess.run(command)
        else:
            with open(input_path) as input_file:
                subprocess.run(command, stdin=input_file)





if __name__ == '__main__':
    raise(SystemExit(main()))