# Dice_Talk_PreData

## 节点类型

`Dice_Talk_PreData`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip_vision:CLIP_VISION`（2 次）
- `vae:VAE`（2 次）
- `audio:AUDIO`（2 次）
- `image:IMAGE`（2 次）
- `weight_dtype:DTYPE`（2 次）

## 输出

- `data_dict:DICETALK_PREDATA`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["happy.npy", 512, 5, 0.5, true]`（1 次）
- `["happy.npy", 384, 10, 0.5, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
