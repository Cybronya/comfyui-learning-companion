# T8_IndexTTS25_EmotionControl

## 节点类型

`T8_IndexTTS25_EmotionControl`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `mode:COMFY_DYNAMICCOMBO_V3`（1 次）
- `mode.happy:FLOAT`（1 次）
- `mode.angry:FLOAT`（1 次）
- `mode.sad:FLOAT`（1 次）
- `mode.afraid:FLOAT`（1 次）
- `mode.disgusted:FLOAT`（1 次）
- `mode.melancholic:FLOAT`（1 次）
- `mode.surprised:FLOAT`（1 次）
- `mode.calm:FLOAT`（1 次）
- `mode.strength:FLOAT`（1 次）

## 输出

- `情感控制:T8_INDEXTTS25_EMOTION`（1 次）
- `情感信息:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["vector", 0.4000000000000001, 0.05000000000000001, 0.10000000000000002, 0.10000000000000002, 0, 0, 0.20000000000000004,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
