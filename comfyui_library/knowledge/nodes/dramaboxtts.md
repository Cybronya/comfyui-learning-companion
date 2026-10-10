# DramaBoxTTS

## 节点类型

`DramaBoxTTS`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:DRAMABOX_MODEL`（1 次）
- `voice_embedding:DRAMABOX_VOICE_EMBEDDING`（1 次）
- `prompt:STRING`（1 次）
- `cfg_scale:FLOAT`（1 次）
- `stg_scale:FLOAT`（1 次）
- `steps:INT`（1 次）
- `duration_multiplier:FLOAT`（1 次）
- `seed:INT`（1 次）
- `watermark:BOOLEAN`（1 次）
- `voice_sample:AUDIO`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["A woman speaks with warm curiosity, \"Oh my, what do you have there, Christine?\"\nShe pauses softly, \"A snowflake? I`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
