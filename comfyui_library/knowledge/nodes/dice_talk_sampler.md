# Dice_Talk_Sampler

## 节点类型

`Dice_Talk_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL_DICETALK`（2 次）
- `data_dict:DICETALK_PREDATA`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `fps:FLOAT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2079434005, "randomize", 25, 1, 0.5, 25]`（1 次）
- `[914439295, "randomize", 25, 1, 1, 25]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
