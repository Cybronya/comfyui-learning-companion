# easy promptAwait

## 节点类型

`easy promptAwait`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `now:*`（1 次）
- `prev:*`（1 次）
- `prompt:STRING`（1 次）
- `toolbar:EASY_PROMPT_AWAIT_BAR`（1 次）

## 输出

- `output:*`（1 次）
- `prompt:STRING`（1 次）
- `continue:BOOLEAN`（1 次）
- `seed:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", {"select": "prev", "unlock": true, "seed": 0, "last_seed": 0}]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
