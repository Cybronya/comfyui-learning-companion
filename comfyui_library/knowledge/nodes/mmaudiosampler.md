# MMAudioSampler

## 节点类型

`MMAudioSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `mmaudio_model:MMAUDIO_MODEL`（1 次）
- `feature_utils:MMAUDIO_FEATUREUTILS`（1 次）
- `images:IMAGE`（1 次）
- `duration:FLOAT`（1 次）
- `steps:INT`（1 次）
- `cfg:FLOAT`（1 次）
- `seed:INT`（1 次）
- `prompt:STRING`（1 次）
- `negative_prompt:STRING`（1 次）
- `mask_away_clip:BOOLEAN`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[35.06000000000001, 25, 4.5, 7, "fixed", "A girl is masturbating,", "", false, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
