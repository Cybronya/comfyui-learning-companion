# MegaStyleTextEncode

## 节点类型

`MegaStyleTextEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `pipe:MEGASTYLE_PIPE`（5 次）
- `prompt:STRING`（5 次）
- `t5_sequence_length:INT`（5 次）
- `positive:BOOLEAN`（5 次）

## 输出

- `conditioning:MEGASTYLE_COND`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["A woman is play basketball", 512, true]`（3 次）
- `["A  dog", 512, true]`（1 次）
- `["a cat", 512, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
