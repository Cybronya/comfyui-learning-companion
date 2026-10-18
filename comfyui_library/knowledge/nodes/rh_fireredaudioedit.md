# RH_FireRedAudioEdit

## 节点类型

`RH_FireRedAudioEdit`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 14 个 workflow 中。

## 输入

- `model:FIREREDAUDIO_MODEL`（23 次）
- `audio:AUDIO`（23 次）
- `instruction:STRING`（22 次）
- `edit_type:COMBO`（21 次）
- `operation:COMBO`（21 次）
- `value:FLOAT`（21 次）
- `seed:INT`（21 次）
- `n_timesteps:INT`（21 次）
- `inference_cfg:FLOAT`（21 次）
- `max_new_audio_steps:INT`（21 次）

## 输出

- `audio:AUDIO`（23 次）
- `rewritten_text:STRING`（23 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["semantic", "delete '夜色那么美'", "pitch", 3, 0, "fixed", 10, 2, 60, 6, 512]`（6 次）
- `["semantic", "", "volume", 0.30000000000000004, 0, "fixed", 10, 2, 180, 6, 512]`（4 次）
- `["acoustic", "shift the pitch by 3 steps\nadjust the speed to 0.8\nadjust the volume to 1.3", "pitch", 3, 1, "fixed", 10`（3 次）
- `["acoustic", "", "pitch", 3, 1, "fixed", 10, 2, 60, 6, 512]`（3 次）
- `["acoustic", "", "speed", 2, 1, "fixed", 10, 2, 180, 6, 512]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
