# CR Simple Prompt Scheduler

## 节点类型

`CR Simple Prompt Scheduler`

## 分类

Sampling

## 作用

调度器：控制去噪步长序列（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `current_frame:INT`（1 次）

## 输出

- `current_prompt:STRING`（1 次）
- `next_prompt:STRING`（1 次）
- `weight:FLOAT`（1 次）
- `show_help:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["0, blue\n15, yellow\n40, red\n66, olive\n80, pink", 0, "CR"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
