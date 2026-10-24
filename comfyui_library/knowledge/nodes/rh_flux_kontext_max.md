# RH_Flux_Kontext_Max

## 节点类型

`RH_Flux_Kontext_Max`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `prompt:STRING`（2 次）
- `guidance_scale:FLOAT`（2 次）
- `aspect_ratio:COMBO`（2 次）
- `seed:INT`（2 次）

## 输出

- `image:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 2.6, "1:1", 755171042, "randomize"]`（1 次）
- `["把2026换成 \"happy\"", 3.5, "3:4", 196632103, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
