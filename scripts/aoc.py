import argparse
import datetime
import os
import requests
import subprocess
import time
from typing import List, Tuple

TODAY = datetime.datetime.today()
SCRIPT_PATH = os.path.dirname(__file__)
INPUT_PATH = SCRIPT_PATH.replace('scripts', 'inputs')
TS_DIR = SCRIPT_PATH.replace('scripts', 'js')
GO_DIR = SCRIPT_PATH.replace('scripts', 'go')
PY_DIR = SCRIPT_PATH.replace('scripts', 'python')

VALID_LANGS = ('all', 'py', 'ts', 'go')

TOO_RECENT_KEY = 'You gave an answer too recently'
BAD_ANSWER_KEYS = [
    "That's not the right answer",
    "You don't seem to be solving the right level"
]
GOOD_ANSWER_KEY = "That's the right answer!"

PY_CODE_TEMPLATE = '''\
import re


def main():
    input_text = open(0).read()
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')

def solve_part_one(input_text: str) -> int:
    total = 0
	return total


def solve_part_two(input_text: str) -> int:
    total = 0

    return total

if __name__ == '__main__':
    raise SystemExit(main())

'''
TS_CODE_TEMPLATE = '''\
import fs from 'fs'

function solve_day_one(input: string): number {
    let total = 0
    return total
}

function solve_day_two(input: string): number {
    let total = 0
    return total
}

function main() {
    const data = fs.readFileSync(0, 'utf-8')
    const part_one_result = solve_day_one(String(data))
    const part_two_result = solve_day_two(String(data))
    console.log(`part one: ${part_one_result}`)
    console.log(`part two: ${part_two_result}`)
}

main()'''
GO_CODE_TEMPLATE = r'''package main

import (
    "fmt"
    "io"
    "os"
    "regexp"
    "strconv"
    "strings"
)

func solve_part_one(input_text string) int {
    total := 0

    return total
}

func solve_part_two(input_text string) int {
    total := 0

    return total
}


func main() {
    stdin, err := io.ReadAll(os.Stdin)
    if err != nil {
        panic(err)
    }

    input := string(stdin)

    part_one_result := solve_part_one(input)
    part_two_result := solve_part_two(input)
    fmt.Printf("part one: %d\n", part_one_result)
    fmt.Printf("part two: %d\n", part_two_result)
}'''


def ts_run_cmd(day: int, year: int = 0, test: bool = False) -> List[str]:
    code_path = os.path.join(TS_DIR, f'day{str(day).zfill(2)}', 'main.ts')
    return ['bun', 'run', code_path]


def go_run_cmd(day: int, year: int = 0, test: bool = False) -> List[str]:
    code_path = os.path.join(GO_DIR, 'cmd', f'day{str(day).zfill(2)}', 'main.go')
    return ['go', 'run', code_path]


def py_run_cmd(day: int, year: int = 0, test: bool = False) -> List[str]:
    code_path = os.path.join(PY_DIR, f'day{str(day).zfill(2)}', 'main.py')
    return ['python', code_path]


def get_input_path(day: int, year: int = 0, test: bool = False) -> str:
    return os.path.join(os.path.dirname(__file__).replace('scripts', 'inputs'),
                        f'day{str(day).zfill(2)}{"_test" if test else ""}.txt')


def get_all_commands(lang: str, test: bool, day: int, actual: bool) -> List[Tuple[List[str], str]]:
    commands = []

    if not test and not actual:
        return commands

    if day == 0:
        days = tuple(range(1, TODAY.day + 1))
    else:
        days = (day,)

    if lang == 'all':
        langs = ('py', 'ts', 'go')
    else:
        langs = (lang,)

    for d in days:
        for _lang in langs:
            day_lang = f'Day: {d} - {_lang}'
            title = '=' * int((80 - len(day_lang) - 4) / 2) + f'  {day_lang}  ' + '=' * int(
                (80 - len(day_lang) - 4) / 2)
            match _lang:
                case 'py':
                    commands.append((['echo', title], ''))
                    if test:
                        commands.append((['echo', '<<TEST>>'], ''))
                        input_path = get_input_path(d, test=True)
                        commands.append((py_run_cmd(day=d), input_path))
                    if actual:
                        commands.append((['echo', '<<ACTUAL>>'], ''))
                        input_path = get_input_path(d, test=False)
                        commands.append((py_run_cmd(day=d), input_path))

                case 'ts':
                    commands.append((['echo', title], ''))
                    if test:
                        input_path = get_input_path(d, test=True)
                        commands.append((['echo', '<<TEST>>'], ''))
                        commands.append((ts_run_cmd(day=d), input_path))
                    if actual:
                        commands.append((['echo', '<<ACTUAL>>'], ''))
                        input_path = get_input_path(d, test=False)
                        commands.append((ts_run_cmd(day=d), input_path))
                case 'go':
                    commands.append((['echo', title], ''))
                    if test:
                        input_path = get_input_path(d, test=True)
                        commands.append((['echo', '<<TEST>>'], ''))
                        commands.append((go_run_cmd(day=d), input_path))
                    if actual:
                        commands.append((['echo', '<<ACTUAL>>'], ''))
                        input_path = get_input_path(d, test=False)
                        commands.append((go_run_cmd(day=d), input_path))
                case _:
                    continue
    return commands


def run(args: argparse.Namespace) -> None:
    if args.lang not in VALID_LANGS:
        raise ValueError(f'invalid language! expected {VALID_LANGS}, got="{args.lang}"')

    all_commands = get_all_commands(args.lang, args.test, args.day, args.actual)
    for command, input_path in all_commands:
        if input_path == '':
            subprocess.run(command)
        else:
            with open(input_path) as input_file:
                start_time = time.perf_counter()
                subprocess.run(command, stdin=input_file)
                end_time = time.perf_counter()
                if args.time:
                    elapsed = end_time - start_time
                    print(f'took {elapsed}ms')


def setup(args: argparse.Namespace) -> None:

    if args.year == TODAY.year and args.day > TODAY.day + 2:
        raise ValueError('looking too far ahead there, bro')

    if args.year == TODAY.year and args.day == TODAY.day + 1:
        time_to_wait = (
                datetime.datetime(args.year, 12, args.day, 5, 0, 10, 0, datetime.timezone.utc)
                - datetime.datetime.now(datetime.timezone.utc)
        )
        print(f'waiting {str(time_to_wait)}')
        time.sleep(time_to_wait.seconds)

    input_path = os.path.join(INPUT_PATH, f'day{str(args.day).zfill(2)}.txt')
    test_input_path = os.path.join(INPUT_PATH, f'day{str(args.day).zfill(2)}_test.txt')

    for lang_path in (PY_DIR, TS_DIR, os.path.join(GO_DIR, 'cmd')):
        lang_day_path = os.path.join(lang_path, f'day{str(args.day).zfill(2)}')
        if not os.path.exists(lang_day_path):
            os.mkdir(lang_day_path)

    for lang_path, file_ext, template in (
            (PY_DIR, 'py', PY_CODE_TEMPLATE),
            (TS_DIR, 'ts', TS_CODE_TEMPLATE),
            (os.path.join(GO_DIR, 'cmd'), 'go', GO_CODE_TEMPLATE)
    ):
        code_path = os.path.join(lang_path, f'day{str(args.day).zfill(2)}', f'main.{file_ext}')
        if not os.path.exists(code_path) or not open(code_path).read():
            with open(code_path, 'w') as file:
                file.write(template)

    r = requests.get(f'https://adventofcode.com/{args.year}/day/{args.day}/input', cookies={
        'session': os.getenv('AOC_COOKIE')
    })

    if r.status_code != 200:
        raise requests.RequestException('Could not get input')

    with open(input_path, 'w') as file:
        file.write(r.text.rstrip())

    with open(test_input_path, 'w') as file:
        file.write('')


def submit(args: argparse.Namespace) -> None:
    url = f'https://adventofcode.com/{args.year}/day/{args.day}/answer'
    r = requests.post(
        url,
        cookies={'session': os.getenv('AOC_COOKIE')},
        data={'level': args.part, 'answer': args.answer}
    )

    for line in r.text.splitlines():
        if GOOD_ANSWER_KEY in line:
            print(GOOD_ANSWER_KEY)
            return
        if TOO_RECENT_KEY in line:
            print(TOO_RECENT_KEY)
            assert False
        for k in BAD_ANSWER_KEYS:
            if k in line:
                print(k)
                return

    print('Bad request!')
    assert False


def main() -> None:
    ap = argparse.ArgumentParser()
    subparser = ap.add_subparsers(dest='subcommand')

    run_ap = subparser.add_parser('run')

    run_ap.add_argument('--lang', action='store', default='all')
    run_ap.add_argument('--year', action='store', type=int, default=TODAY.year)
    run_ap.add_argument('--day', action='store', type=int, default=TODAY.day)
    run_ap.add_argument('--test', action='store_true')
    run_ap.add_argument('--actual', action='store_true')
    run_ap.add_argument('--input', action='store', required=False)
    run_ap.add_argument('--time', action='store_true')

    setup_ap = subparser.add_parser('setup')
    setup_ap.add_argument('--day', action='store', type=int, default=TODAY.day)
    setup_ap.add_argument('--year', action='store', type=int, default=TODAY.year)

    setup_ap = subparser.add_parser('submit')
    setup_ap.add_argument('--day', action='store', type=int, default=TODAY.day)
    setup_ap.add_argument('--year', action='store', type=int, default=TODAY.year)
    setup_ap.add_argument('--part', action='store', type=int, default=1)
    setup_ap.add_argument('--answer', action='store')
    args = ap.parse_args()

    match args.subcommand:
        case 'run':
            run(args)
        case 'setup':
            setup(args)
        case 'submit':
            submit(args)
        case _:
            raise ValueError('unexpected subcommand')


if __name__ == '__main__':
    raise SystemExit(main())
