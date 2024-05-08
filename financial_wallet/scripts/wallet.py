#!/usr/bin/env python3
import argparse
from financial_wallet import command_handler


def get_args() -> str:
    parser = argparse.ArgumentParser(description='''
    Задай команду из предложенных, следуй инструкции и получи результат''')
    parser.add_argument('-i', '--instruction', metavar='INSTRUCTION',
                        default='balance', help='set instruction of output',
                        choices=[
                            'balance',
                            'income',
                            'consumption',
                            'add_entry',
                            'change_entry',
                            'delete_entry',
                            'find_entry',
                        ])
    return parser.parse_args()


def main() -> None:
    args: str = get_args()
    print(command_handler(command=args.instruction))


if __name__ == '__main__':
    main()
