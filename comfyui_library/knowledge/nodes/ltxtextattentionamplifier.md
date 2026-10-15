# LTXTextAttentionAmplifier

## 节点类型

`LTXTextAttentionAmplifier`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `text_amplification:FLOAT`（1 次）
- `spatial_focus:FLOAT`（1 次）
- `block_index_filter:STRING`（1 次）
- `bypass:BOOLEAN`（1 次）
- `debug:BOOLEAN`（1 次）

## 输出

- `model:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1.3, 0.15000000000000002, "36-48", false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
