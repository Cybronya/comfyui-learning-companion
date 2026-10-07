# FramePackTimestampedTextEncode

## 节点类型

`FramePackTimestampedTextEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `text:STRING`（1 次）
- `total_second_length:FLOAT`（1 次）

## 输出

- `positive_timed_data:TIMED_CONDITIONING_WITH_METADATA`（1 次）
- `negative:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["[0s-5s: Beautiful korea girl is playing the piano and sticks out her tongue] ", "ugly", 5, 9, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
