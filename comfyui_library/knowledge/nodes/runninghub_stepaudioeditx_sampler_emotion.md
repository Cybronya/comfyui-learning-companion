# RunningHub StepAudioEditX Sampler(Emotion)

## 节点类型

`RunningHub StepAudioEditX Sampler(Emotion)`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:RHSAEditXModel`（2 次）
- `prompt_audio:AUDIO`（2 次）
- `prompt_text:STRING`（2 次）
- `edit_info:COMBO`（2 次）
- `n_edit_iter:INT`（2 次）
- `seed:INT`（2 次）

## 输出

- `audio:AUDIO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["原音频内容", "sad", 2, 679697255803103, "randomize"]`（1 次）
- `["原音频内容", "sad", 2, 11694615514105, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
