# YC_FiveTextCombineNode

## 节点类型

`YC_FiveTextCombineNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `text1:STRING`（1 次）
- `text2:STRING`（1 次）
- `text3:STRING`（1 次）
- `text4:STRING`（1 次）
- `text5:STRING`（1 次）
- `separator:STRING`（1 次）

## 输出

- `text1_out:STRING`（1 次）
- `text2_out:STRING`（1 次）
- `text3_out:STRING`（1 次）
- `text4_out:STRING`（1 次）
- `text5_out:STRING`（1 次）
- `combined_text:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["text1", "text2", "text3", "text4", "text5", ","]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
