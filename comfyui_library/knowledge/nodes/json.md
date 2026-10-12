# JSON取值节点

## 节点类型

`JSON取值节点`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `JSON路径或文本:STRING`（7 次）
- `键:STRING`（7 次）
- `节点开关:BOOLEAN`（7 次）

## 输出

- `状态:BOOLEAN`（7 次）
- `值:STRING`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "role_list", true]`（2 次）
- `["", "script_lines", true]`（2 次）
- `["", "global_prompt", true]`（1 次）
- `["", "local_prompts", true]`（1 次）
- `["", "segment_lengths", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
