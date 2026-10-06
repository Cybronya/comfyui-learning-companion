# YuE2GenerateMusic

## 节点类型

`YuE2GenerateMusic`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `clip:CLIP`（3 次）
- `style:STRING`（3 次）
- `lyrics:STRING`（3 次）
- `abc:STRING`（3 次）
- `seed:INT`（3 次）
- `mode:COMBO`（3 次）
- `max_duration:FLOAT`（3 次）
- `temperature:FLOAT`（3 次）
- `top_p:FLOAT`（3 次）
- `top_k:INT`（3 次）

## 输出

- `CONDITIONING:CONDITIONING`（3 次）
- `seconds:FLOAT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["violin with girl singing jpop anime", "[verse]\nfluff the fluffy tail\nfluff the fluffy tail\nfluff the fluffy tail\nf`（1 次）
- `["Mandarin Chinese, Chinese opera-xibo fusion pop, female voice switching between ethereal soft pop verses and piercing `（1 次）
- `["New Orleans brass-funk, second-line drums, sousaphone, honky-tonk piano, trombone and baritone sax, playful Mandarin d`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
