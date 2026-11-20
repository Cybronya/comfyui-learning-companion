# TextBoxConcatenate

## 节点类型

`TextBoxConcatenate`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `text_external:STRING`（5 次）
- `text:STRING`（5 次）
- `separator:STRING`（5 次）
- `mode:COMBO`（5 次）

## 输出

- `text:STRING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["西施", ". ", "append_external_input"]`（3 次）
- `["", "", "append_external_input"]`（1 次）
- `["请按以下要求生成“portrait”的视频。\n\n", "", "append_external_input"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
