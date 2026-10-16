# MiniMaxMusic3TextEncode

## 节点类型

`MiniMaxMusic3TextEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `caption:STRING`（1 次）
- `lyrics:STRING`（1 次）
- `seed:INT`（1 次）
- `max_duration:FLOAT`（1 次）
- `cfg_scale:FLOAT`（1 次）
- `top_k:INT`（1 次）

## 输出

- `CONDITIONING:CONDITIONING`（1 次）
- `seconds:FLOAT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", 222, "fixed", 60, 1.7, 50]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
