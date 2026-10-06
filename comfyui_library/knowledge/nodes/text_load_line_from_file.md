# Text Load Line From File

## 节点类型

`Text Load Line From File`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `multiline_text:STRING`（3 次）
- `file_path:STRING`（3 次）
- `dictionary_name:STRING`（3 次）
- `label:STRING`（3 次）
- `mode:COMBO`（3 次）
- `index:INT`（3 次）

## 输出

- `line_text:STRING`（3 次）
- `dictionary:DICT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "[filename]", "TextBatch", "index", 6]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
