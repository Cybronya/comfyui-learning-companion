# Miaoshouai_Flux_CLIPTextEncode

## 节点类型

`Miaoshouai_Flux_CLIPTextEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `caption:STRING`（1 次）
- `guidance:FLOAT`（1 次）

## 输出

- `CONDITIONING:CONDITIONING`（1 次）
- `EMPTY CONDITIONING:CONDITIONING`（1 次）
- `t5xxl:STRING`（1 次）
- `clip_l:STRING`（1 次）
- `analyze:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[3.5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
