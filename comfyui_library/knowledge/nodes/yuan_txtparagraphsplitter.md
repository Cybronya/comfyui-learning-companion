# YUAN_TXTParagraphSplitter

## 节点类型

`YUAN_TXTParagraphSplitter`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `any_1:*`（26 次）
- `text:STRING`（26 次）
- `输出模式:BOOLEAN`（26 次）
- `段落优化:BOOLEAN`（26 次）
- `分段方式:COMBO`（26 次）
- `输出段落:INT`（26 次）
- `输入端口:INT`（26 次）
- `选取段落:STRING`（26 次）
- `any_2:*`（19 次）
- `any_3:*`（9 次）

## 输出

- `数::INT`（26 次）
- `总段::STRING`（26 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", false, true, "端口", 0, 2, "-1", null]`（10 次）
- `["", true, true, "段落", 0, 1, "", null]`（7 次）
- `["", false, true, "端口", 0, 3, "0", null]`（5 次）
- `["", false, true, "端口", 0, 3, "-1", null]`（3 次）
- `["", true, true, "端口", 0, 4, "", null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
