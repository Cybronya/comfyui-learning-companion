# RunningHubControlFoleyGenerator

## 节点类型

`RunningHubControlFoleyGenerator`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipe:CONTROLFOLEY_PIPE`（1 次）
- `video:VIDEO`（1 次）
- `ref_audio:AUDIO`（1 次）
- `prompt:STRING`（1 次）
- `negative_prompt:STRING`（1 次）
- `duration:FLOAT`（1 次）
- `num_steps:INT`（1 次）
- `cfg_strength:FLOAT`（1 次）
- `seed:INT`（1 次）
- `mask_away_clip:BOOLEAN`（1 次）

## 输出

- `audio:AUDIO`（1 次）
- `video:VIDEO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", 8, 25, 4.5, 62034651164364, "randomize", false, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
