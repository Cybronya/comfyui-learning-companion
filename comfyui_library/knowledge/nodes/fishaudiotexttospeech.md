# FishAudioTextToSpeech

## 节点类型

`FishAudioTextToSpeech`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model.voices.voice0:FISHAUDIO_VOICE`（2 次）
- `model.voices.voice1:FISHAUDIO_VOICE`（2 次）

## 输出

- `AUDIO:AUDIO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["[sigh] Yes, this voice is AI generated. \n[excited] Now in ComfyUI. Type text, add tags like this, and boom. Instant v`（1 次）
- `["[curious] Want a voice that sounds exactly like you?\n[calm] Record a short clip, clone it with Fish Audio, and type y`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
