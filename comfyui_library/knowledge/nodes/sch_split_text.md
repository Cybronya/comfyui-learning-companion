# sch_split_text

## 节点类型

`sch_split_text`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `text:STRING`（6 次）
- `current_frame:INT`（6 次）
- `preset:COMBO`（6 次）
- `delimiter:STRING`（6 次）

## 输出

- `i_text:*`（6 次）
- `length:INT`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["a b c", 0, "Line", " "]`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
