# LongCatAvatarWhisperEmbeds

## 节点类型

`LongCatAvatarWhisperEmbeds`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `whisper_model:WHISPERMODEL`（1 次）
- `audio_1:AUDIO`（1 次）
- `audio_2:AUDIO`（1 次）
- `audio_3:AUDIO`（1 次）
- `audio_4:AUDIO`（1 次）
- `ref_target_masks:MASK`（1 次）
- `normalize_loudness:BOOLEAN`（1 次）
- `num_frames:INT`（1 次）
- `fps:FLOAT`（1 次）
- `audio_scale:FLOAT`（1 次）

## 输出

- `multitalk_embeds:MULTITALK_EMBEDS`（1 次）
- `audio:AUDIO`（1 次）
- `num_frames:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 93, 25, 1, 1, "para"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
