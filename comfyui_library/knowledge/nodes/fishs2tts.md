# FishS2TTS

## 节点类型

`FishS2TTS`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_path:COMBO`（1 次）
- `text:STRING`（1 次）
- `language:COMBO`（1 次）
- `device:COMBO`（1 次）
- `precision:COMBO`（1 次）
- `attention:COMBO`（1 次）
- `max_new_tokens:INT`（1 次）
- `chunk_length:INT`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["s2-pro-bnb-nf4", "大家好！[excited] 我是 Fish Audio S2，今天先不讲道理，先秀一下声音表现力！ [pause] 你以为我只会普通说话？ [whisper] 那你可能低估我了。 [pause] 我可`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
