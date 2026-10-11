# SONIC_PreData

## 节点类型

`SONIC_PreData`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `clip_vision:CLIP_VISION`（9 次）
- `vae:VAE`（9 次）
- `audio:AUDIO`（9 次）
- `image:IMAGE`（9 次）
- `weight_dtype:DTYPE`（9 次）
- `duration:FLOAT`（3 次）

## 输出

- `data_dict:SONIC_PREDATA`（9 次）
- `bbox:BBOX`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[576, 10, 1]`（3 次）
- `[512, 10, 0.5]`（2 次）
- `[512, 30, 0.5]`（1 次）
- `[512, 99999, 1]`（1 次）
- `[512, 11, 0.5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
