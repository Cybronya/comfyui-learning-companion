# FishS2VoiceCloneTTS

## 节点类型

`FishS2VoiceCloneTTS`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `reference_audio:AUDIO`（1 次）
- `model_path:COMBO`（1 次）
- `text:STRING`（1 次）
- `language:COMBO`（1 次）
- `device:COMBO`（1 次）
- `precision:COMBO`（1 次）
- `attention:COMBO`（1 次）
- `max_new_tokens:INT`（1 次）
- `chunk_length:INT`（1 次）
- `temperature:FLOAT`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["s2-pro-fp8", "", "zh", "auto", "auto", "auto", 0, 200, 0.8, 0.8, 1.1, 1717652958, "randomize", true, false, false, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
