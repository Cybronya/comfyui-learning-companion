# FL_CosyVoice3_Dialog

## 节点类型

`FL_CosyVoice3_Dialog`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:COSYVOICE_MODEL`（1 次）
- `speaker_A_Audio:AUDIO`（1 次）
- `speaker_B_Audio:AUDIO`（1 次）
- `speaker_C_Audio:AUDIO`（1 次）
- `speaker_D_Audio:AUDIO`（1 次）
- `dialog_text:STRING`（1 次）
- `speed:FLOAT`（1 次）
- `seed:INT`（1 次）

## 输出

- `dialog_audio:AUDIO`（1 次）
- `speaker_a_audio:AUDIO`（1 次）
- `speaker_b_audio:AUDIO`（1 次）
- `speaker_c_audio:AUDIO`（1 次）
- `speaker_d_audio:AUDIO`（1 次）
- `message:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["SPEAKER A: Hello, how are you?\nSPEAKER B: I'm doing great, thanks for asking!", 1, 1219482711, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
