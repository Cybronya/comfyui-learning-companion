"""
python -m engine — ComfyUI Learning Companion 命令行入口

子命令：
    ask     问一个问题（可带 workflow），直接打印中文回答（无需 LLM）

用法（仓库根目录）：
    python -m engine ask "为什么图很僵硬"
    python -m engine ask "这个流程用了什么 LoRA" --workflow path/to/wf.json
    python -m engine ask "CFG 多少合适" --limit 5
    python -m engine ask "讲讲这个流程" --workflow wf.json --no-graph
"""

import argparse
import sys

from . import create_agent


def main(argv=None) -> int:
    # Windows 控制台默认 GBK，回答里的特殊字符可能炸输出；
    # 进程内重配 UTF-8（失败不影响主流程，比如已被重定向）
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    parser = argparse.ArgumentParser(
        prog="python -m engine",
        description="ComfyUI Learning Companion 引擎命令行",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_ask = sub.add_parser(
        "ask",
        help="提问并打印中文回答（无需 LLM，规则拼装）",
    )
    p_ask.add_argument("question", help="你的问题")
    p_ask.add_argument(
        "-w", "--workflow",
        default=None,
        help="workflow JSON 路径（可省略）",
    )
    p_ask.add_argument(
        "-n", "--limit",
        type=int, default=None,
        help="本次最多召回几条知识",
    )
    p_ask.add_argument(
        "--no-graph",
        action="store_true",
        help="本次不加载知识图谱（跳过跨条目事实）",
    )

    args = parser.parse_args(argv)

    if args.command == "ask":
        config = {"enable_graph": False} if args.no_graph else None
        agent = create_agent(config=config)
        print(agent.ask_text(args.question, args.workflow, limit=args.limit))
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
