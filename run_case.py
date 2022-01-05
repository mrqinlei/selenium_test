#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import subprocess
import os

WIN = sys.platform.startswith('win')


def main():
    """主函数"""
    steps = [
        "pytest --alluredir allure-results --clean-alluredir",
        "allure generate allure-results -c -o allure-report",
        # "allure open allure-report"
    ]
    for step in steps:
        subprocess.run("call " + step, shell=True)


if __name__ == "__main__":
    main()
