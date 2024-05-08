#!/usr/bin/env python3
import argparse
from financial_wallet import command_handler


def get_args():
    parser = argparse.ArgumentParser(description='''
    Задай команду из предложенных, следуй инструкции и получи результат''')
    parser.add_argument('-i', '--instruction', metavar='INSTRUCTION',
                        default='balance', help='set instruction of output',
                        choices=[
                            'balance',
                            'income',
                            'consumption',
                            'add_note',
                            'change_entry',
                            'delete_entry',
                            'search_record',
                        ]
    )
    return parser.parse_args()


def main():
    args = get_args()
    print(command_handler(command=args.instruction))

if __name__ == '__main__':
    main()
