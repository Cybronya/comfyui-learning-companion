# IndexTTS2_Basic

## 节点类型

`IndexTTS2_Basic`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `speaker_audio:AUDIO`（2 次）
- `model_manager:INDEXTTS2_MODEL`（2 次）
- `text:STRING`（2 次）
- `output_filename:STRING`（2 次）
- `language:COMBO`（2 次）
- `speed:FLOAT`（2 次）
- `temperature:FLOAT`（2 次）
- `top_p:FLOAT`（2 次）
- `use_fp16:BOOLEAN`（2 次）
- `use_cuda_kernel:BOOLEAN`（2 次）

## 输出

- `audio:AUDIO`（2 次）
- `output_path:STRING`（2 次）
- `info:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "female_voice_01.wav", "auto", 0.5, 0.4, 0.57, 0.7, 0.9, false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
