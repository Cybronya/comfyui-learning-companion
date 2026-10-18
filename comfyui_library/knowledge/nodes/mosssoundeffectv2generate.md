# MossSoundEffectV2Generate

## 节点类型

`MossSoundEffectV2Generate`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `moss_pipe:MOSS_TTS_PIPE`（4 次）
- `prompt:STRING`（4 次）
- `seconds:FLOAT`（4 次）
- `seed:INT`（4 次）
- `num_inference_steps:INT`（4 次）
- `cfg_scale:FLOAT`（4 次）
- `sigma_shift:FLOAT`（4 次）
- `negative_prompt:STRING`（4 次）
- `append_duration_suffix:BOOLEAN`（4 次）

## 输出

- `audio:AUDIO`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 5, 603284427500735, "randomize", 100, 4, 5, "", true]`（1 次）
- `["", 5, 1030770910140610, "randomize", 100, 4, 5, "", true]`（1 次）
- `["", 5, 831853889407201, "randomize", 100, 4, 5, "", true]`（1 次）
- `["", 5, 319607871925023, "randomize", 100, 4, 5, "", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
