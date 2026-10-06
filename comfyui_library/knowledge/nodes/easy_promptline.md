# easy promptLine

## 节点类型

`easy promptLine`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 21 个 workflow 中。

## 输入

- `prompt:STRING`（36 次）
- `start_index:INT`（36 次）
- `max_rows:INT`（36 次）

## 输出

- `STRING:STRING`（36 次）
- `COMBO:*`（36 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["text", 0, 1000, ""]`（15 次）
- `["text", 0, 1, true]`（5 次）
- `["text", 0, 9999, true]`（5 次）
- `["A full-body portrait of a beautiful East Asian woman with an elegant low bun, sitting cross-legged on a dark wooden ch`（4 次）
- `["A full-body portrait of a beautiful East Asian woman with an elegant low bun, sitting cross-legged on a dark wooden ch`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
