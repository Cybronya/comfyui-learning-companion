# VibeVoiceTTS

## 节点类型

`VibeVoiceTTS`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `speaker_1_voice:AUDIO`（1 次）
- `speaker_2_voice:AUDIO`（1 次）
- `speaker_3_voice:AUDIO`（1 次）
- `speaker_4_voice:AUDIO`（1 次）
- `model_name:COMBO`（1 次）
- `text:STRING`（1 次）
- `attention_mode:COMBO`（1 次）
- `cfg_scale:FLOAT`（1 次）
- `inference_steps:INT`（1 次）
- `seed:INT`（1 次）

## 输出

- `AUDIO:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["VibeVoice-Large-pt", "", "flash_attention_2", 1.3, 30, 280963734375904, "randomize", true, 0.95, 0.95, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
