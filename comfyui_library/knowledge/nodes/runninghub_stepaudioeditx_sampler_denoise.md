# RunningHub StepAudioEditX Sampler(Denoise)

## 节点类型

`RunningHub StepAudioEditX Sampler(Denoise)`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `model:RHSAEditXModel`（6 次）
- `prompt_audio:AUDIO`（6 次）
- `prompt_text:STRING`（6 次）
- `n_edit_iter:INT`（6 次）
- `seed:INT`（6 次）

## 输出

- `audio:AUDIO`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["原音频内容", 2, 966377666656295, "randomize"]`（1 次）
- `["原音频内容", 2, 1115849592930108, "randomize"]`（1 次）
- `["原音频内容", 2, 1013735413580036, "randomize"]`（1 次）
- `["原音频内容", 2, 483517096640676, "randomize"]`（1 次）
- `["原音频内容", 2, 235845476121654, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
