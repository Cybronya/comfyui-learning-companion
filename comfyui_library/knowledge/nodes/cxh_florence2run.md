# CXH_Florence2Run

## 节点类型

`CXH_Florence2Run`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `florence2_model:FL2MODEL`（1 次）
- `text_input:STRING`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `caption:STRING`（1 次）
- `data:JSON`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "referring_expression_segmentation", true, false, 1024, 3, true, "", 252937, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
